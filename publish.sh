#!/usr/bin/env bash
set -o errexit
set -o pipefail

cd `dirname $0`
rm -rf dist/
python3 setup.py sdist bdist_wheel
python3 -m twine upload \
  --config-file .pypirc \
  --non-interactive \
  dist/*