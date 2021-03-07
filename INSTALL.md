# eos4e40
Antibiotic activity of small molecules from Stokes et al 2020

Checkpoints where downloaded from on 4 November 2020 (Antibiotics file): http://chemprop.csail.mit.edu/checkpoints

```
conda create -n chemprop python=3.8
conda activate chemprop
conda install -c conda-forge rdkit
pip install git+https://github.com/bp-kelley/descriptastorus
pip install chemprop
```



### Vanilla predictions

```
chemprop_predict --test_path data/drugs_100.csv --checkpoint_dir model --preds_path test_preds.csv
``