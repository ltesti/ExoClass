
#!/usr/bin/env python
# coding=utf-8
from setuptools import setup

# read version number
exec(open("ExoClass/_version.py", "r").read())

# use README as long_description (for PyPI)
try:
    long_description = open("README", "r", encoding="utf-8").read()
except TypeError:
    # under Python 2.7 the `encoding` keyword doesn't exist.
    print(
        "DEPRECATION: Python 2.7 has reached its end-of-life in 2020. "
        "Please upgrade your Python. ExoClass is not meant for python 2 compatibility."
        "This software may not work as intended (or not work at all). "
    )
    long_description = open("README", "r").read()


setup(
    name="ExoClass",
    version=__version__,
    packages=["ExoClass"],
    author="Leonardo Testi",
    author_email="ltesti120a@gmail.com",
    description="Utilities and scripts for the Exoplanets Class at UniBo.",
    long_description=long_description,
    install_requires=["numpy>=1.9", "matplotlib"],
    license="LGPLv3",
    url="https://github.com/ltesti/ExoClass",
    download_url="https://github.com/ltesti/ExoClass/archive/{}.tar.gz".format(
        __version__
    ),
    keywords=["science", "astronomy", "exoplanets", "didattica"],
    classifiers=[
        "Development Status :: 0 - Under Development/Unstable",
        "Intended Audience :: Master Students",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Programming Language :: Python :: 3",
    ],
)
