# Trained Chemprop Antibiotics Model

Code: https://github.com/swansonk14/chemprop

This directory contains an ensemble of 20 trained antibiotics models. To make predictions using this ensemble, download and install Chemprop (use the link above), then run:

```
python predict.py --test_path /path/to/molecules.csv --preds_path /path/to/predictions.csv --checkpoint_dir /path/to/this/directory --config_path /path/to/this/directory/0406_inhibition_hyperopt.json --features_generator rdkit_2d_normalized --no_features_scaling
```
