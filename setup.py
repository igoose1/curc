from setuptools import setup

import curc

version = curc.__version__
with open("requirements.txt", "r") as file:
    requires = [line.strip() for line in file.readlines()]
with open("README.rst", "r") as file:
    readme = file.read()

setup(
    name="curc",
    version=version,
    long_description=readme,
    long_description_content_type="text/x-rst",
    author="Oskar Sharipov",
    author_email="oskarsh@riseup.net",
    license="Apache License Version 2.0",
    license_files=["LICENSE"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Office/Business :: Financial",
    ],
    packages=["curc"],
    install_requires=requires,
    python_requires=">=3.7",
    entry_points={"console_scripts": ["curc = curc.__main__:console"]},
)
