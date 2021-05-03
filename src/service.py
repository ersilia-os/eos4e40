from typing import List

from bentoml import BentoService, api, artifacts
from bentoml.adapters import JsonInput
from bentoml.types import JsonSerializable

import shutil
import os
import csv
import tempfile
import subprocess
import pickle

from bentoml.service import BentoServiceArtifact

CHECKPOINTS_BASEDIR = "0405_broad_inhibition_20folds"
FRAMEWORK_BASEDIR = "framework"


def load_chemprop_model(framework_dir, checkpoints_dir):
    mdl = ChempropModel()
    mdl.load(framework_dir, checkpoints_dir)
    return mdl


class ChempropModel(object):
    def __init__(self):
        self.DATA_FILE = "data.csv"
        self.FEAT_FILE = "features.npz"
        self.PRED_FILE = "pred.csv"
        self.RUN_FILE = "run.sh"

    def load(self, framework_dir, checkpoints_dir):
        self.framework_dir = framework_dir
        self.checkpoints_dir = checkpoints_dir

    def set_checkpoints_dir(self, dest):
        self.checkpoints_dir = os.path.abspath(dest)

    def set_framework_dir(self, dest):
        self.framework_dir = os.path.abspath(dest)

    def predict(self, smiles_list):
        tmp_folder = tempfile.mkdtemp()
        data_file = os.path.join(tmp_folder, self.DATA_FILE)
        feat_file = os.path.join(tmp_folder, self.FEAT_FILE)
        pred_file = os.path.join(tmp_folder, self.PRED_FILE)
        with open(data_file, "w") as f:
            f.write("smiles" + os.linesep)
            for smiles in smiles_list:
                f.write(smiles + os.linesep)
        run_file = os.path.join(tmp_folder, self.RUN_FILE)
        with open(run_file, "w") as f:
            lines = []
            lines += [
                "python {0}/save_features.py --data_path {1} --save_path {2} --features_generator rdkit_2d_normalized".format(
                    self.framework_dir, data_file, feat_file
                )
            ]
            lines += [
                "python {0}/predict.py --test_path {1} --checkpoint_dir {2} --preds_path {3} --features_path {4} --no_features_scaling".format(
                    self.framework_dir,
                    data_file,
                    self.checkpoints_dir,
                    pred_file,
                    feat_file,
                )
            ]
            f.write(os.linesep.join(lines))
        cmd = "bash {0}".format(run_file)
        with open(os.devnull, "w") as fp:
            subprocess.Popen(
                cmd, stdout=fp, stderr=fp, shell=True, env=os.environ
            ).wait()
        with open(pred_file, "r") as f:
            reader = csv.reader(f)
            h = next(reader)
            result = []
            for r in reader:
                result += [{h[1]: float(r[1])}]
        return result


class ChempropArtifact(BentoServiceArtifact):
    """Dummy Chemprop artifact to deal with file locations of checkpoints"""

    def __init__(self, name):
        super(ChempropArtifact, self).__init__(name)
        self._model = None
        self._extension = ".pkl"

    def _copy_checkpoints(self, base_path):
        src_folder = self._model.checkpoints_dir
        dst_folder = os.path.join(base_path, "checkpoints")
        if os.path.exists(dst_folder):
            os.rmdir(dst_folder)
        shutil.copytree(src_folder, dst_folder)

    def _copy_framework(self, base_path):
        src_folder = self._model.framework_dir
        dst_folder = os.path.join(base_path, "framework")
        if os.path.exists(dst_folder):
            os.rmdir(dst_folder)
        shutil.copytree(src_folder, dst_folder)

    def _model_file_path(self, base_path):
        return os.path.join(base_path, self.name + self._extension)

    def pack(self, chemprop_model):
        self._model = chemprop_model
        return self

    def load(self, path):
        model_file_path = self._model_file_path(path)
        chemprop_model = pickle.load(open(model_file_path, "rb"))
        chemprop_model.set_checkpoints_dir(
            os.path.join(os.path.dirname(model_file_path), "checkpoints")
        )
        chemprop_model.set_framework_dir(
            os.path.join(os.path.dirname(model_file_path), "framework")
        )
        return self.pack(chemprop_model)

    def get(self):
        return self._model

    def save(self, dst):
        self._copy_checkpoints(dst)
        self._copy_framework(dst)
        pickle.dump(self._model, open(self._model_file_path(dst), "wb"))


@artifacts([ChempropArtifact("model")])
class Service(BentoService):
    @api(input=JsonInput(), batch=True)
    def predict(self, input: List[JsonSerializable]):
        input = input[0]
        smiles_list = [inp["input"] for inp in input]
        output = self.artifacts.model.predict(smiles_list)
        return [output]
