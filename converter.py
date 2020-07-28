#! /usr/bin/env python3


# {{ cookiecutter.provider_slug }}-fetcher -- Download and convert data from {{ cookiecutter.provider_code }}
# By: {{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>
#
# Copyright (C) {% now 'utc', '%Y' %} Cepremap
# https://git.nomics.world/dbnomics-fetchers/{{ cookiecutter.provider_slug }}-fetcher
#
# {{ cookiecutter.provider_slug }}-fetcher is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# {{ cookiecutter.provider_slug }}-fetcher is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


"""Convert data from {{ cookiecutter.provider_code }} to DBnomics data model (see https://git.nomics.world/dbnomics/dbnomics-data-model/).

Read source data from a source directory, write converted data to a target directory.

See also `.gitlab-ci.yml` in which data is committed to a Git repository of converted data.
"""

import argparse
import json
import logging
import sys
import os
from pathlib import Path
import shutil

# from dbnomics_json_errors import ErrorsArtifact

PROVIDER_DATA = {
    "code": 'paj-tojson',
    "name": 'paj-tojson',
    "region": "jp",
    "terms_of_use": "",
    "website": "https://www.paj.gr.jp/",
}

log = logging.getLogger(__name__)


def make_folder(folder):
    try:
        os.mkdir(folder)
    except FileExistsError:
        try:
            os.rmdir(folder)
            os.mkdir(folder)
        except OSError:
            import shutil
            shutil.rmtree(folder)
            os.mkdir(folder)

def get_files(folder) -> list:
    if os.path.exists(folder):
        files = os.listdir(folder)
    return files


def write_json_file(file_path: Path, data):
    """Writes data the JSON way to file_path"""

    with file_path.open('w', encoding='utf-8') as json_fd:
        json.dump(data, json_fd, ensure_ascii=False, indent=2, sort_keys=True)


def convert_data():
    pass



def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('source_dir', type=Path, help='path of source directory')
    parser.add_argument('target_dir', type=Path, help='path of target directory')
    parser.add_argument('--log', default='WARNING', help='level of logging messages')
    args = parser.parse_args()

    numeric_level = getattr(logging, args.log.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: {}'.format(args.log))
    logging.basicConfig(
        format="%(levelname)s:%(name)s:%(asctime)s:%(message)s",
        level=numeric_level,
        stream=sys.stdout,  # Use stderr if script outputs data to stdout.
    )

    source_dir = args.source_dir
    if not source_dir.exists():
        parser.error("Source dir {!r} not found".format(str(source_dir)))

    target_dir = args.target_dir
    if not target_dir.exists():
        parser.error("Target dir {!r} not found".format(str(target_dir)))

    nb_expected_datasets = 0
    errors_artifact = ErrorsArtifact()

    # =====================================================

    for dataset in iterate_datasets():
        nb_expected_datasets += 1
        try:
            # convert_this_dataset(dataset)
            pass
        except Exception as e:
            if args["--stop-on-exceptions"]:
                raise e
            log.warning("{!r} dataset aborted ! - {}".format(dataset_code, e))
            # Add error to artifacts
            errors_artifact.add_dataset_error(dataset_code, e)
            # Delete dataset dir
            shutil.rmtree(target_dir)
            continue

    # provider.json
    write_json_file(target_dir / 'provider.json', PROVIDER_DATA)

    return 0



if __name__ == '__main__':
    source_dir = "paj-source-data"
    target_dir = "paj-json-data"

    files = get_files(source_dir)
    convert_data(files)


    # sys.exit(main())
