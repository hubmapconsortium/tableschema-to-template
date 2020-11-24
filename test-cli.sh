#!/usr/bin/env bash
set -o errexit
set -o pipefail

red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

die() { set +v; echo "${red}$*${reset}" 1>&2 ; sleep 1; exit 1; }

# Make tempdir and cleanup afterwards.
OLD=`mktemp -d`
NEW=`mktemp -d`

src/ts2xl.py \
  --input_schema tests/fixtures/schema.yaml \
  --output_dir $NEW
unzip -q $NEW/template.xlsx -d $NEW

cp tests/fixtures/template.xlsx $OLD
unzip -q $OLD/template.xlsx -d $OLD

for UNZIPPED_PATH in 'xl/worksheets/sheet1.xml'; do
  # The XML files in tests/fixtures/output-unzipped/ have been pretty-printed:
  # They should not be directly compared against the command-line output.
  # That is handled in the python test.
  #
  # Instead, here, we just unzip and do a byte-wise comparison of the original XML.
  cmp -s $NEW/$UNZIPPED_PATH \
        $OLD/$UNZIPPED_PATH \
    || die "CLI output ($NEW) output does not match fixture ($OLD) for $UNZIPPED_PATH
Consider: cp $NEW/template.xlsx ./tests/fixtures/"
done
echo 'Newly generated XSLX seems to match fixture'
rm -rf $NEW
rm -rf $OLD
