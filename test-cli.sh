#!/usr/bin/env bash
set -o errexit
set -o pipefail

red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

die() { set +v; echo "${red}$*${reset}" 1>&2 ; sleep 1; exit 1; }

# Make tempdir and cleanup afterwards.
OLD_DIR=`mktemp -d`
NEW_DIR=`mktemp -d`
NEW_XLSX="$NEW_DIR/template.xlsx"

PYTHONPATH="${PYTHONPATH}:tableschema_to_template" \
  tableschema_to_template/ts2xl.py \
  tests/fixtures/schema.yaml $NEW_XLSX
unzip -q $NEW_XLSX -d $NEW_DIR

cp tests/fixtures/template.xlsx $OLD_DIR
unzip -q $OLD_DIR/template.xlsx -d $OLD_DIR

for UNZIPPED_PATH in 'xl/worksheets/sheet1.xml'; do
  # The XML files in tests/fixtures/output-unzipped/ have been pretty-printed:
  # They should not be directly compared against the command-line output.
  # That is handled in the python test.
  #
  # Instead, here, we just unzip and do a byte-wise comparison of the original XML.
  cmp -s $NEW_DIR/$UNZIPPED_PATH \
        $OLD_DIR/$UNZIPPED_PATH \
    || die "On $UNZIPPED_PATH, CLI output ($NEW_DIR) output does not match fixture ($OLD_DIR).
Consider: cp $NEW_XLSX ./tests/fixtures/"
done
echo 'Newly generated XSLX seems to match fixture'
rm -rf $NEW_DIR
rm -rf $OLD_DIR
