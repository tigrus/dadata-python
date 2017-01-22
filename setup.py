import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "DaData Client",
    version = "0.0.1",
    author = "Nikolay Fominykh",
    author_email = "nikolayfn@gmail.com",
    description = ("DaData Python Client"),
    license = "BSD",
    keywords = "dadata api-client",
    # url = "http://packages.python.org/an_example_pypi_project",
    packages=['dadata', 'tests'],
    install_requires=[
        'requests',
        # 'nosetests',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    long_description=read('README'),
    # test_suite='pytest',
    tests_require=['pytest', ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
