from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="melar",
    version="0.0.1",
    description="A package for multiple linear regression by gradient descent.",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DrSolidDevil/mlr-gd/",
    author="DrSolidDevil",
    license="BSD 3-Clause",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    install_requires=["numpy >= 2.2.1"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],  # To be determined if necessary to include
    },
    python_requires=">=3.11",
)
