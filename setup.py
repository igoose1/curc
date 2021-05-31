from setuptools import setup

import curc

readme = curc.__doc__
version = curc.__version__
with open("requirements.txt", "r") as file:
    requires = [line.strip() for line in file.readlines()]

setup(
    name="curc",
    version=version,
    long_description=readme,
    long_description_content_type="text/plain",
    author="Oskar Sharipov",
    author_email="oskarsh@riseup.net",
    license="Apache License Version 2.0",
    license_files=["license"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Office/Business :: Financial",
    ],
    install_requires=requires,
    python_requires=">=3.7",
)
