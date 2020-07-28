- The deliverable is to implement a data scraper using https://git.nomics.world/explore/groups and https://db.nomics.world library

- The target provider is https://www.paj.gr.jp/english/statis/  (это один из примеров сайта)

The goal is to write a “fetcher” in python3 using Dbnomics (aka DBN, an open-source library with tools to write fetchers and a very precise data model) for a given data provider.

- Your goal is to
   - Deliver the code to fetch (i.e., download.py and convert.py) the data from a specific provider into DBN data model
   - Ensure that the produced data is properly validated (using the data validator)
   - Make sure that the code is formatted and has no lints, using the provided linter.py

- Your goal is not to:
   - Run the fetchers in production
   - Maintain infrastructure and operate the fetchers