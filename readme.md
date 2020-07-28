
Download.py
- Downloads the data from the provider
- Doesn’t change the format
- Unzips the data, if it is zipped

Convert.py
- Convert data into DBN format (i.e., JSON)
An overview of how to write a new fetcher is:
- https://git.nomics.world/dbnomics-fetchers/documentation/-/wikis/write-a-new-fetcher
Understanding the data model
- https://git.nomics.world/dbnomics/dbnomics-data-model/-/blob/master/README.mdResources
External DBN interface

Homepage
- https://db.nomics.world/
Brief description of DBN
- https://db.nomics.world/docs/
List of current DBN providers
- https://db.nomics.world/providers
Example of an implementation of a provider
- https://db.nomics.world/BEA
- Provider fetcher source code
- https://git.nomics.world/dbnomics-fetchers/bea-fetcher
- Provider original data
- https://git.nomics.world/dbnomics-source-data/bea-source-data
- Dataset in JSON format
- https://git.nomics.world/dbnomics-json-data/bea-json-data
Technical documentation

Home of technical documentation
- https://git.nomics.world/dbnomics-fetchers/documentation/-/wikis/home
Data model
DBN data model description
- https://git.nomics.world/dbnomics/dbnomics-data-model/-/blob/master/README.md
Data model cheat sheet
- https://git.nomics.world/dbnomics/dbnomics-data-model/-/blob/master/cheat_sheet.md
Sample output of valid data model
- https://git.nomics.world/dbnomics/dbnomics-data-model/-/tree/master/tests/fixtures
Script to validate the generated data-
https://git.nomics.world/dbnomics/dbnomics-data-model/-/blob/master/dbnomics_data_m
odel/validate_storage.py
DBN fetcher toolbox
Documentation for dbn-fetcher-toolbox
- https://dbnomics-fetcher-toolbox.readthedocs.io/en/latest/index.html
Template with dbn-fetcher-toolbox:
- https://git.nomics.world/dbnomics/dbnomics-fetcher-toolbox/-/blob/master/examples/dow
nload_simple.py
- https://git.nomics.world/dbnomics/dbnomics-fetcher-toolbox/-/blob/master/examples/dow
nload_parts.py
Creating a fetcher using cookie-cutter approach
- https://git.nomics.world/dbnomics/dbnomics-fetcher-cookiecutter/-/tree/master
Template for a downloader without cookie-cutter:
- https://git.nomics.world/dbnomics/dbnomics-fetcher-cookiecutter/-/blob/master/%7B%7B
cookiecutter.project_slug%7D%7D/download.py
Interesting Git repos
Entry point of the Git repo
- https://git.nomics.world/dbnomics
DBN data model
- https://git.nomics.world/dbnomics/dbnomics-data-model
GitLab project containing all the fetcher code
- https://git.nomics.world/dbnomics-fetchers
GitLab project containing all the original data (after download.py) for all providers
- https://git.nomics.world/dbnomics-source-data
GitLab project containing all the JSON data (after convert.py) for all providers
- https://git.nomics.world/dbnomics-json-data
Example of fetcher
- https://git.nomics.world/bduye/dummy-fetcher/
DBN fetcher cookiecutter
- https://git.nomics.world/dbnomics/dbnomics-fetcher-cookiecutterOther useful technologies
JSON schema
- http://json-schema.org/
JSON line format
- http://jsonlines.org/