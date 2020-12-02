## Development

From a checkout of the repo, run a demo:
```sh
pip install -r requirements.txt
PYTHONPATH="${PYTHONPATH}:tableschema_to_template" \
  tableschema_to_template/ts2xl.py \
  tests/fixtures/schema.yaml /tmp/template.xlsx
# Open with Excel:
open /tmp/template.xlsx
```

Run the tests:
```sh
pip install -r requirements-dev.txt
./test.sh
```

To build and publish,
- If you haven't already, generate a token on Pypi and create a `.pypirc` in your checkout.
- Increment the version number in setup.py.
- Finally: `./publish.sh`