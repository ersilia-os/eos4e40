# Broad spectrum antibiotic activity

Based on a simple E.coli growth inhibition assay, the authors trained a model capable of identifying antibiotic potential in compounds structurally divergent from conventional antibiotic drugs. One of the predicted active molecules, Halicin (SU3327), was experimentally validated in vitro and in vivo. Halicin is a drug under development as a treatment for diabetes.

This model was incorporated on 2020-11-04.

## Information
### Identifiers
- **Ersilia Identifier:** `eos4e40`
- **Slug:** `chemprop-antibiotic`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Antimicrobial resistance`
- **Target Organism:** `Escherichia coli`
- **Tags:** `E.coli`, `IC50`, `Antimicrobial activity`, `Chemical graph model`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability that a compound inhibits E.coli growth. The inhibition threshold was set at 80% growth inhibition in the training set.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| inhibition_50um | float | high | Probability of inhibiting the growth (80%) of E.coli at 50 uM |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos4e40](https://hub.docker.com/r/ersiliaos/eos4e40)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4e40.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4e40.zip)

### Resource Consumption
- **Model Size (Mb):** `428`
- **Environment Size (Mb):** `1485`
- **Image Size (Mb):** `2654.67`


### References
- **Source Code**: [http://chemprop.csail.mit.edu/checkpoints](http://chemprop.csail.mit.edu/checkpoints)
- **Publication**: [https://pubmed.ncbi.nlm.nih.gov/32084340/](https://pubmed.ncbi.nlm.nih.gov/32084340/)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2020`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos4e40
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos4e40
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
