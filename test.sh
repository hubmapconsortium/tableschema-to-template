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
PYTHONPATH="${PYTHONPATH}:tableschema_to_template" pytest -vv --assert=plain
# "plain" means that instead of a diff, we see the full, untruncated assertion message.
end pytest

start cli
./test-cli.sh || die 'test-cli.sh failed'
end cli