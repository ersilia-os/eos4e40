# Broad spectrum antibiotic activity

Based on a simple E.coli growth inhibition assay, the authors trained a model capable of identifying antibiotic potential in compounds structurally divergent from conventional antibiotic drugs. One of the predicted active molecules, Halicin (SU3327), was experimentally validated in vitro and in vivo. Halicin is a drug under development as a treatment for diabetes.

## Identifiers

* EOS model ID: `eos4e40`
* Slug: `chemprop-antibiotic`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Probability`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Probability that a compound inhibits E.coli growth. The inhibition threshold was set at 80% growth inhibition in the training set.

## References

* [Publication](https://pubmed.ncbi.nlm.nih.gov/32084340/)
* [Source Code](http://chemprop.csail.mit.edu/checkpoints)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos4e40)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4e40.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos4e40) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://pubmed.ncbi.nlm.nih.gov/32084340/) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a MIT license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!