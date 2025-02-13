from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

version = "0.3.0"

setup(
    name="mlr-gd",
    version=version,
    description="A package for multiple linear regression by gradient descent.",
    packages=find_packages(exclude=['tests']),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DrSolidDevil/mlr-gd/",
    author="DrSolidDevil",
    license="BSD 3-Clause",
    keywords=[
        "linear regression",
        "linear",
        "regression",
        "gradient descent",
        "machine learning",
        "artificial intelligence"
    ],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    install_requires=["numpy >= 2.2.1"],
    extras_require={
        "dev": ["twine>=6.0.1", "pandas>=2.2.3", "pytest>=8.3.4", "setuptools>=75.8.0"],
        "docs": ["pydata-sphinx-theme >= 0.16.1", "Sphinx >= 8.1.3", "myst-parser >= 4.0.0"]
    },
    python_requires=">=3.11",
)
