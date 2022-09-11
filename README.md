# Uhepp at PyHEP 2022

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sauerburger/pyhep-uhepp/HEAD?labpath=PyHEP_uhepp.ipynb)
[![DOI](https://zenodo.org/badge/535091180.svg)](https://zenodo.org/badge/latestdoi/535091180)

## Additional resources
 - Python package: https://pypi.org/project/uhepp/
 - Package documentation: https://uhepp.readthedocs.io/en/latest/
 - GitLab repsitory: https://gitlab.cern.ch/fsauerbu/uhepp
 - Online plot hub: https://uhepp.org
 - Online hub source code: https://gitlab.sauerburger.com/frank/uhepp.org
 - Feedback and contributions always welcome
       

## How to use this notebook
 - This talk:
 - Go through the notebook
 - Explain as I go
 - Verbose comments and full-text between the cells
 - Go though the notebook at your own pace

## Why and what?

 - Traditionally, histograms in ROOT files: Full information (split by sample, all bins, ...)
 - **But:** Requires custom script to plot
    - Gets out of sync</li>
    - Rednering to PDF/PNG version destroys information
 - **Solution:** Uhepp storage format (JSON/YAML) combines raw data and display settings
     - Allows non-destructive changes</li>
     - Generic plotting code
     - Retreive numeric values
