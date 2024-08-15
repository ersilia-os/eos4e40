import sys
import os
import csv
import tempfile
import subprocess

root = os.path.dirname(os.path.abspath(__file__))

CHECKPOINTS_BASEDIR = os.path.abspath(os.path.join(root, "..", "..", "checkpoints", "final_model"))
FRAMEWORK_BASEDIR = os.path.abspath(os.path.join(root, ".."))

input_file = sys.argv[1]
output_file = sys.argv[2]


class ChempropModel(object):
    def __init__(self):
        self.DATA_FILE = "data.csv"
        self.FEAT_FILE = "features.npz"
        self.PRED_FILE = "pred.csv"
        self.RUN_FILE = "_run.sh"
        self.framework_dir = FRAMEWORK_BASEDIR
        self.checkpoints_dir = CHECKPOINTS_BASEDIR

    def predict(self, smiles_list):
        tmp_folder = tempfile.mkdtemp()
        #tmp_folder = self.framework_dir # TODO remove
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
                "python {0}/code/save_features.py --data_path {1} --save_path {2} --features_generator rdkit_2d_normalized".format(
                    self.framework_dir, data_file, feat_file
                )
            ]
            lines += [
                "python {0}/code/predict.py --test_path {1} --checkpoint_dir {2} --preds_path {3} --features_path {4} --no_features_scaling".format(
                    self.framework_dir,
                    data_file,
                    self.checkpoints_dir,
                    pred_file,
                    feat_file,
                )
            ]
            print(lines)
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


print("Reading file", input_file)
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)
    smiles_list = []
    for r in reader:
        smiles_list += [r[0]]

print(len(smiles_list), "molecules read!")

print("Running model!"),
print(f"content after reading the file: {smiles_list}")
model = ChempropModel()
result = model.predict(smiles_list)
print("Calculations done")

values = []
header = None
print(f"this is the result: {result}")
for item in result: 
    print(f"each item is:{item}")
    if header is None:
        print(f"header is none: so it is {item.keys()}")
        header = list(item.keys())
        print(f"appending header: {item.values()}")
        values.append(header) 
    values.append(list(item.values()))  

with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(values)  
