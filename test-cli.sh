#!/usr/bin/env bash
set -o errexit
set -o pipefail

red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

die() { set +v; echo "${red}$*${reset}" 1>&2 ; sleep 1; exit 1; }

function test_good() {
  # Make tempdir and cleanup afterwards.
  OLD_DIR=`mktemp -d`
  NEW_DIR=`mktemp -d`
  NEW_XLSX="$NEW_DIR/template.xlsx"

  PYTHONPATH="${PYTHONPATH}:tableschema_to_template" \
    tableschema_to_template/ts2xl.py \
    tests/fixtures/schema.yaml $NEW_XLSX \
    --sheet_name 'Enter data here' \
    --idempotent
  unzip -q $NEW_XLSX -d $NEW_DIR

  cp tests/fixtures/template.xlsx $OLD_DIR
  unzip -q $OLD_DIR/template.xlsx -d $OLD_DIR

  for UNZIPPED_PATH in `cd tests/fixtures/output-unzipped; find . | grep .xml`; do
    # We look in output-unzipped only to get a list of files:
    # Those have been pretty-printed, and should not be directly compared against the command-line output.
    # Here, we just unzip and do a byte-wise comparison of the XML.
    cmp -s $NEW_DIR/$UNZIPPED_PATH \
          $OLD_DIR/$UNZIPPED_PATH \
      || die "On $UNZIPPED_PATH, CLI output ($NEW_DIR) output does not match fixture ($OLD_DIR). Consider:
  cp $NEW_XLSX ./tests/fixtures/"
    echo "Newly generated XSLX matches XLSX fixture on $UNZIPPED_PATH"
  done
  rm -rf $NEW_DIR
  rm -rf $OLD_DIR
}

function test_bad() {
  ( ! PYTHONPATH="${PYTHONPATH}:tableschema_to_template" \
    tableschema_to_template/ts2xl.py <(echo '{}') /tmp/should-not-exist.xlsx \
    2>&1 ) \
    | grep "Not a valid Table Schema: 'fields' is \(a \)\?required property" \
    || die 'Did not see expected error'
    # The error message changed slightly between versions.
}

function test_docs() {
  PYTHONPATH="${PYTHONPATH}:tableschema_to_template" tableschema_to_template/ts2xl.py --help
  TOOL=
  diff \
        <(perl -ne 'print if /usage:/../```/ and ! /```/' README-cli.md) \
        <(PYTHONPATH="${PYTHONPATH}:tableschema_to_template" tableschema_to_template/ts2xl.py --help) \
      || die 'Update README-cli.md'
}

for TEST in `declare -F | grep test | sed -e 's/declare -f //'`; do
  echo "${green}${TEST}${reset}"
  $TEST
done
