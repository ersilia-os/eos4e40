python /workspaces/eos4e40/model/framework/code/save_features.py --data_path /workspaces/eos4e40/model/framework/data.csv --save_path /workspaces/eos4e40/model/framework/features.npz --features_generator rdkit_2d_normalized
python /workspaces/eos4e40/model/framework/code/predict.py --test_path /workspaces/eos4e40/model/framework/data.csv --checkpoint_dir /workspaces/eos4e40/model/checkpoints/final_model --preds_path /workspaces/eos4e40/model/framework/pred.csv --features_path /workspaces/eos4e40/model/framework/features.npz --no_features_scaling