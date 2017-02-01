import os
from setuptools import setup

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
    packages=['dadata'],
    install_requires=[
        'requests',
        # 'nosetests',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    long_description=read('README.md'),
    # test_suite='pytest',
    tests_require=['pytest', 'mock', 'pytest-runner', 'requests-mock' ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
