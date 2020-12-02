import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tableschema-to-template",
    version="0.0.9",
    install_requires=[
        # Keep in sync with requirements-lower-bound.txt:
        'jsonschema>=1.0.0',
        'pyyaml>=3.13',
        'xlsxwriter>=1.2.8'
        # xlsxwriter bound could be loosened:
        # Earlier versions generate slightly different XML, and tests fail here,
        # but that's only because they are too fussy.
    ],
    scripts=[
        'tableschema_to_template/ts2xl.py'
    ],
    author="Chuck McCallum",
    author_email="mccallucc+tableschema@gmail.com",
    description="Given a Frictionless Table Schema, "
    "generates an Excel template with input validation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hubmapconsortium/tableschema-to-template",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # Keep in sync with .travis.yml:
    python_requires='>=3.6',
    # f-strings aren't available in 3.5.
    # pyyaml install fails on 3.4.
)
