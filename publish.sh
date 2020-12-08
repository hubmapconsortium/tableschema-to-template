#!/usr/bin/env bash
set -o errexit
set -o pipefail

red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

die() { set +v; echo "${red}$*${reset}" 1>&2 ; sleep 1; exit 1; }

cd `dirname $0`

git diff --quiet || die 'Uncommitted changes: Stash or commit'
git checkout main
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