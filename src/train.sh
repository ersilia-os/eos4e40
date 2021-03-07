chemprop_hyperopt \
    --data_path ../data/ecoli.csv \
    --dataset_type classification \
    --num_iters 25 \
    --config_save_path ../model/hyperopt \
    --ensemble_size 5 \
    --features_generator rdkit_2d_normalized \
    --no_features_scaling

chemprop_train \
    --data_path ../data/ecoli.csv \
    --save_dir ../model/checkpoints \
    --dataset_type classification \
    --ensemble_size 20 \
    --config_path ../model/hyperopt \
    --features_generator rdkit_2d_normalized \
    --no_features_scaling