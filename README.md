# Antibiotic activity of small molecules

Based on a simple _E.coli_ growth inhibition assay, the authors trained a model capable of identifying antibiotic potential in compounds structurally divergent from conventional antibacterial drugs. One of the predicted active molecules, Halicin, was experimentally validated _in vitro_ and _in vivo_. Halicin is a drug under development as treatment for diabetes.

## Summary

* Predicts **antibiotic activity**
* Takes **compound structures** as input
* Trained with **experimental** bioactivity data against _E.coli_
* Based on a dataset of **>2,000** experiments
* Results **validated experimentally**
* Used for **drug repurposing**
* Identified a **novel broad-spectrum** antibiotic
* Published in *Stokes et al., Cell, 2020*: [](10.1016/j.cell.2020.01.021)

## History

1. Model was downloaded on 28/04/2021 from [](http://chemprop.csail.mit.edu/checkpoints) following the direct link.
2. We opened an issue on GitHub [#128](https://github.com/chemprop/chemprop/issues/108#issuecomment-802245616) to be sure about feature scaling.
3. We duplicated `predict.py` and `scripts/save_features.py` scripts from chemprop GitHub repository.
4. Model was incorporated to Ersilia on 28/04/2021.
