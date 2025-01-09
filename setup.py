from setuptools import find_packages, setup

with open("src/README.md", "r") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    description="A package for multiple linear regression by gradient descent.",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DrSolidDevil/mlr-gd/",
    author="DrSolidDevil",
    license="TO BE DETERMINED",
    classifiers=[
        "License :: OSI Approved :: TO BE DETERMINED",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    install_requires=["numpy >= 2.2.1"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],  # To be determined if necessary to include
    },
    python_requires=">=3.11",
)
