import os
import csv
import tempfile
import subprocess

from bentoml import BentoService, api, artifacts
from bentoml.adapters import JsonInput
from bentoml.service.artifacts.common import JSONArtifact
from bentoml.types import JsonSerializable


SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))

CHECKPOINTS = os.path.join(SCRIPT_PATH, "../model/0405_broad_inhibition_20folds")

DATA_FILE = "data.csv"
FEAT_FILE = "features.npz"
PRED_FILE = "pred.csv"
RUN_FILE = "run.sh"


@artifacts([JSONArtifact("model")])
class Service(BentoService):
    @api(input=JsonInput())
    def predict(self, input: JsonSerializable):
        tmp_folder = tempfile.mkdtemp()
        data_file = os.path.join(tmp_folder, DATA_FILE)
        feat_file = os.path.join(tmp_folder, FEAT_FILE)
        pred_file = os.path.join(tmp_folder, PRED_FILE)
        with open(data_file, "w") as f:
            f.write("smiles" + os.linesep)
            f.write(input + os.linesep)
        run_file = os.path.join(tmp_folder, RUN_FILE)
        with open(run_file, "w") as f:
            lines = []
            lines += [
                "python {0}/scripts/save_features.py --data_path {1} --save_path {2} --features_generator rdkit_2d_normalized".format(
                    SCRIPT_PATH, data_file, feat_file
                )
            ]
            lines += [
                "python {0}/scripts/predict.py --test_path {1} --checkpoint_dir {2} --preds_path {3} --features_path {4} --no_features_scaling".format(
                    SCRIPT_PATH, data_file, CHECKPOINTS, pred_file, feat_file
                )
            ]
            f.write(os.linesep.join(lines))
        cmd = "bash {0}".format(run_file)
        with open(os.devnull, "w") as fp:
            subprocess.Popen(cmd, stdout=fp, stderr=fp, shell=True, env=os.environ).wait()
        with open(pred_file, "r") as f:
            reader = csv.reader(f)
            h = next(reader)
            result = {
                h[1]: float(next(reader)[1])
            }
        return result


if __name__ == "__main__":
    HALICIN = "C1=C(SC(=N1)SC2=NN=C(S2)N)[N+](=O)[O-]"
    res = Service().predict(HALICIN)
    print(res)
