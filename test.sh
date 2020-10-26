#!/usr/bin/env bash
set -o errexit
set -o pipefail

red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

start() { [[ -z $CI ]] || echo travis_fold':'start:$1; echo ${green}$1${reset}; }
end() { [[ -z $CI ]] || echo travis_fold':'end:$1; }
die() { set +v; echo "${red}$*${reset}" 1>&2 ; sleep 1; exit 1; }

start flake8
flake8 || die "Try: autopep8 --in-place --aggressive -r ."
end flake8

start pytest
PYTHONPATH="${PYTHONPATH}:src" pytest -vv
end pytest

start cli
# Make tempdir and cleanup afterwards.
OLD=`mktemp -d`
NEW=`mktemp -d`

src/ts2xl.py \
  --input_schema tests/fixtures/schema.yaml \
  --output_dir $NEW
unzip -q $NEW/template.xlsx -d $NEW

cp tests/fixtures/template.xlsx $OLD
unzip -q $OLD/template.xlsx -d $OLD

cmp -s $NEW/xl/worksheets/sheet1.xml \
       $OLD/xl/worksheets/sheet1.xml \
  || die "CLI ($NEW) output does not match fixture ($OLD)"
echo 'Newly generated XSLX seems to match fixture'
rm -rf $NEW
rm -rf $OLD
end cli