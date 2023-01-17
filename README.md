# Broad spectrum antibiotic activity

Based on a simple E.coli growth inhibition assay, the authors trained a model capable of identifying antibiotic potential in compounds structurally divergent from conventional antibiotic drugs. One of the predicted active molecules, Halicin (SU3327), was experimentally validated in vitro and in vivo. Halicin is a drug under development as a treatment for diabetes.

## Identifiers

* EOS model ID: eos4e40
* Slug: chemprop-antibiotic

## Characteristics

* Input: Compound
* Input shape: Single
* Task: Classification
* Output: Probability
* Interpretation: Probability that a compound inhibits E.coli growth. The classifier was trained using a threshold of 80% growth inhibition 

## References

* [Publication](https://pubmed.ncbi.nlm.nih.gov/32084340/)
* [Source](http://chemprop.csail.mit.edu/checkpoints)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.
[Help us](https://www.ersilia.io/donate) achieve our mission!
