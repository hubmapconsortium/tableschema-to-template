#!/usr/bin/env bash
set -o errexit
set -o pipefail

cd `dirname $0`

git diff --quiet || die 'Uncommitted changes: Stash or commit'
git checkout master
git pull

perl -i -pne 's/(\d+)$/$1+1/e' VERSION

rm -rf build/
rm -rf dist/

python3 setup.py sdist bdist_wheel
python3 -m twine upload \
  --config-file .pypirc \
  --non-interactive \
  dist/*

VERSION=`cat VERSION`
git commit -m "Version $VERSION"
git tag $VERSION
git push origin --tags