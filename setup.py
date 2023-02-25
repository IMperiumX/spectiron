#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.md") as history_file:
    history = history_file.read()

requirements = [
    "Click>=7.0",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Yusuf Adel",
    author_email="yusufadell.dev@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Python library for generating OpenApi 3 specs from Python code",
    entry_points={
        "console_scripts": [
            "openapi_specgen=openapi_specgen.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="openapi_specgen",
    name="openapi_specgen",
    packages=find_packages(include=["openapi_specgen", "openapi_specgen.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/yusufadell/openapi_specgen",
    version="0.1.0",
    zip_safe=False,
)
