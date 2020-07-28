#! /usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import sys
import argparse
import http.client
import logging
from pathlib import Path

log = logging.getLogger(__name__)


BASE_URL = "https://www.paj.gr.jp"
URL = BASE_URL + "/english/statis/"

def get_file_urls():
    result = []
    try:
        html_text = requests.get(URL)
    except:
        pass
    if html_text.status_code == 200:
        soup = BeautifulSoup(html_text.text , 'html.parser')
        hrefs = soup.find_all("a")
        for href in hrefs:
            end = href.get('href')
            if end is not None:
                if end[-3:] == "XLS":
                    result.append(end)
    return result

def write_data(urls, folder):
    import os
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

    for url in urls:
        name = url.split('/')[-1]
        file_to_write = requests.get(BASE_URL + url)
        open(folder+ "/" + name, 'wb').write(file_to_write.content)
        file_to_write.close()

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('target_dir', type=Path, help='path of target directory')
    parser.add_argument('--debug-http', action='store_true', help='display http.client debug messages')
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
    logging.getLogger("urllib3").setLevel(logging.DEBUG if args.debug_http else logging.WARNING)
    if args.debug_http:
        http.client.HTTPConnection.debuglevel = 1
        
    urls = get_file_urls()
    target_dir = args.target_dir
    if not target_dir.exists():
        parser.error("Target dir {!r} not found".format(str(target_dir)))

    write_data(urls, target_dir)

    return 0



if __name__ == "__main__":
    import sys
    sys.exit(main())
