# Chemprop antibiotic

## Model identiifers
- Slug: chemprop-antibiotic
- Ersilia ID: eos4e40
- Tags: E. coli. IC50, antibiotic

## Model Description 
Prediction of the E.coli in vitro growth inhibition potential of small molecules
- Input: SMILES 
- Output: IC50 
- Model type: Regression
- Mode of training: Pretrained
- Training data: 2335 compounds (https://github.com/chemprop/chemprop/blob/master/data.tar.gz)
- Experimentally validated: Yes 

## Source Code
This model has been published by Stokes JM, Yang K, Swanson K, Jin W, Cubillos-Ruiz A, Donghia NM, MacNair CR, French S, Carfrae LA, Bloom-Ackermann Z, Tran VM, Chiappino-Pepe A, Badran AH, Andrews IW, Chory EJ, Church GM, Brown ED, Jaakkola TS, Barzilay R, Collins JJ. A Deep Learning Approach to Antibiotic Discovery. Cell. 2020 Feb 20;180(4):688-702.e13. doi: [10.1016/j.cell.2020.01.021.](https://www.sciencedirect.com/science/article/pii/S0092867420301021) Erratum in: Cell. 2020 Apr 16;181(2):475-483. PMID: 32084340; PMCID: PMC8349178.

* Code: https://github.com/chemprop/chemprop
* Checkpoints: http://chemprop.csail.mit.edu/checkpoints

## License and copyright notice
The GPL-v3 license applies to all parts of the repository that are not externally maintained libraries. 
This repository uses the externally maintained library "Chemprop", located at /model and licensed under an [MIT License](https://github.com/ersilia-os/eos4e40/blob/main/model/LICENSE.md)

## History
1. Model was downloaded on 28/04/2021 from [Chemprop](http://chemprop.csail.mit.edu/checkpoints) following the direct link.
2. We opened an issue on GitHub [#128](https://github.com/chemprop/chemprop/issues/108#issuecomment-802245616) to be sure about feature scaling.
3. We duplicated `predict.py` and `scripts/save_features.py` scripts from chemprop GitHub repository.
4. Model was incorporated to Ersilia on 28/04/2021.
