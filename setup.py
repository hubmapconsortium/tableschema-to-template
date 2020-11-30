import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tableschema-to-template",
    version="0.0.1",
    install_requires=[
        # TODO: Not strict enough.
        'jsonschema',
        'pyyaml',
        'xlsxwriter'
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
    # TODO: May be too strict.
    python_requires='>=3.8',
)
