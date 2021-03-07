import os
import tempfile
import subprocess
import pandas as pd
import csv
import pickle
import shutil

from bentoml import env, artifacts, api, BentoService
from bentoml.adapters import DataframeInput
from bentoml.exceptions import MissingDependencyException
from bentoml.service import BentoServiceArtifact

# Predict parameters
FEATURES_GENERATOR = "rdkit_2d_normalized"
NO_FEATURES_SCALING = True


def _import_chemprop_module():
    try:
        import chemprop
    except ImportError:
        chemprop = None

    if chemprop is None:
        raise MissingDependencyException(
            "chemprop module is required to use ChempropModelArtifact"
        )

    return chemprop


def load_chemprop_model(checkpoints_dir):
    mdl = ChempropModel()
    mdl._load(checkpoints_dir)
    return mdl


class ChempropModel(object):

    def __init__(self):
        self.features_generator = FEATURES_GENERATOR
        self.no_features_scaling = NO_FEATURES_SCALING

    def _load(self, checkpoints_dir):
        self.checkpoints_dir = checkpoints_dir

    def set_checkpoints_dir(self, dest):
        self.checkpoints_dir = os.path.abspath(dest)

    def predict(self, smiles_list):
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_input = os.path.join(tmp_dir, "test.csv")
            tmp_output = os.path.join(tmp_dir, "pred.csv")
            with open(tmp_input, "w") as f:
                f.write("smiles\n")
                for smiles in smiles_list:
                    f.write("%s\n" % smiles)
            cmd = "chemprop_predict --test_path %s --checkpoint_dir %s --preds_path %s" % (tmp_input, self.checkpoints_dir, tmp_output)
            cmd += " --features_generator %s" % self.features_generator
            if self.no_features_scaling:
                cmd += " --no_features_scaling"
            subprocess.Popen(cmd, shell=True).wait()
            with open(tmp_output, "r") as f:
                reader = csv.reader(f)
                header = next(reader)
                R = []
                for r in reader:
                    R += [r]
        return pd.DataFrame(R, columns=header)


class ChempropArtifact(BentoServiceArtifact):
    """Dummy Chemprop artifact to deal with file locations of checkpoints"""

    def __init__(self, name, pickle_extension=".pkl"):
        super(ChempropArtifact, self).__init__(name)
        self._model = None
        self._pickle_extension = pickle_extension

    def _copy_checkpoints(self, base_path):
        src_folder = self._model.checkpoints_dir
        dst_folder = os.path.join(base_path, "checkpoints")
        if os.path.exists(dst_folder):
            os.rmdir(dst_folder)
        shutil.copytree(src_folder, dst_folder)

    def _model_file_path(self, base_path):
        return os.path.join(base_path, self.name + self._pickle_extension)

    def pack(self, chemprop_model):  # pylint:disable=arguments-differ
        self._model = chemprop_model
        return self

    def load(self, path):
        model_file_path = self._model_file_path(path)
        chemprop_model = pickle.load(open(model_file_path, "rb"))
        chemprop_model.set_checkpoints_dir(os.path.join(os.path.dirname(model_file_path), "checkpoints"))
        return self.pack(chemprop_model)

    def get(self):
        return self._model

    def save(self, dst):
        self._copy_checkpoints(dst)
        pickle.dump(self._model, open(self._model_file_path(dst), "wb"))


@env(docker_base_image="ersiliaos/eos4e40:repo")
@artifacts([ChempropArtifact('model')])
class eos4e40(BentoService):

    @api(input=DataframeInput(), batch=True)
    def predict(self, mols: pd.DataFrame):
        mols = pd.DataFrame(mols)
        smiles_list = []
        for r in mols.values:
            smiles_list += [r[0]]
        return self.artifacts.model.predict(smiles_list)
