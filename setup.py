import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="matchingframework", # It should be unique name
    version="0.0.1",
    author="Phan Quoc Toan",
    author_email="author@email.com",
    description="A small title of the package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/quoctoanpk2511/matching-framework",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
install_requires=[
        "numpy==1.19.3",
    ],

    python_requires='>=3.6',


)