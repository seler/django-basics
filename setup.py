import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "basics",
    version = "0.0.0",
    author = u"Rafał Selewońko",
    author_email = "rafal@selewonko.com",
    description = ("Liblary containing always used django apps."),
    license = "GPLv2",
    keywords = "django basic application pages articles galleries photos files",
    url = "http://packages.python.org/django-basics",
    packages=['basics', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
)
