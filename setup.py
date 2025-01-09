from setuptools import find_packages, setup

with open("app/README.md", "r") as f:
    long_description = f.read()

setup(
    name="mlr-gd",
    version="0.0",
    description="A package for multiple linear regression by gradient descent.",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DrSolidDevil/mlr-gd/",
    author="DrSolidDevil",
    license="TO BE DETERMINED",
    classifiers=[
        "License :: OSI Approved :: TO BE DETERMINED",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    install_requires=["numpy >= 2.2.1"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],  # To be determined
    },
    python_requires=">=3.11",
)
