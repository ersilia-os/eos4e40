# imports
import os
import csv
import sys

from chemprop.args import PredictArgs
from chemprop.train import make_predictions
from chemprop.utils import load_args, update_prediction_args
# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]


# current file directory
root = os.path.dirname(os.path.abspath(__file__))
dir_model= os.path.abspath(os.path.join(root,"..", "..","checkpoints", "final_model"))


# my model: CHANGES OCCUR HERE
def my_model(smiles_list):
    
    smiles_list_list= [[smiles] for smiles in smiles_list]  
    arguments = [
    '--test_path', '/dev/null',
    '--preds_path', '/dev/null',
    '--checkpoint_dir', dir_model,
    '--features_generator', 'rdkit_2d_normalized',
    '--no_features_scaling'
    ]

    args = PredictArgs().parse_args(arguments)
    train_args = load_args(args.checkpoint_dir)
    update_prediction_args(predict_args=args, train_args=train_args)
    preds = make_predictions(args=args, smiles=smiles_list_list)
    return preds


# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
outputs = my_model(smiles_list)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["activity"])  # header
    for o in outputs:
        writer.writerow(o)