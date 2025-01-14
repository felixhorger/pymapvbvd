#!/usr/bin/env python

import setuptools
import versioneer

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = [
	"numpy",
	"tqdm",
	"dataclasses",
	"scipy",
	"matplotlib",
	"setuptools",
	"pyyaml",
	"pytest",
	"h5py",
	"six"
]

# A horrible hack -  I can't get the requirments.yml to work
# with the dataclass dependency for 3.6
index = install_requires.index('dataclasses')
install_requires[index] += "  ; python_version<'3.7'"

setuptools.setup(
    name='pyMapVBVD',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Python twix file reader',
    author='Will Clarke',
    author_email='william.clarke@ndcn.ox.ac.uk',
    url='https://github.com/wexeee/pymapvbvd',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    license_file='LICENSE',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent", ],
    python_requires='>=3.6')
