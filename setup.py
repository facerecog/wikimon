from distutils.core import setup
from setuptools.command.install import install
from setuptools import find_packages
import subprocess


setup(
        name = 'wikimon_bot',
        packages = find_packages(), # this must be the same as the name above
        version = '0.0.9',
        description = 'Wikimon is a Python script which creates an artificial intelligent digital pet that learns through mirroring.',
        author = 'FaceRecog Pte Ltd',
        author_email = 'muhd.amrullah@facerecog.asia',
        url = 'http://facerecog.github.io/wikimon/', # use the URL to the github repo
        download_url = 'https://github.com/facerecog/wikimon/tarball/master',
        keywords = ['bot', 'chat'],
        classifiers = [],
        install_requires=['pytube', 'requests', 'python-Levenshtein', 'flask', 'oauthlib', 'python-axolotl', 'yowsup2'],
        scripts=['wikimon.py'],
        )


