import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

exec(open('dadata/version.py').read())

setup(
    name = "dadata-client",
    version = __version__,
    author = "Nikolay Fominykh",
    author_email = "nikolayfn@gmail.com",
    description = ("DaData Python Client"),
    license = "MIT",
    keywords = "dadata api-client",
    # url = "http://packages.python.org/an_example_pypi_project",
    packages=[
        'dadata',
        'dadata.plugins'
    ],
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
