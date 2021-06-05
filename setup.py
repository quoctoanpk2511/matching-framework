import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="matchingframework", # It should be unique name
    version="0.1.1",
    author="Phan Quoc Toan",
    author_email="quoctoanpk2511@gmail.com",
    description="The data matching framework for two dataset",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/quoctoanpk2511/matching-framework",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "base"},
    packages=setuptools.find_packages(where="base"),
    python_requires='>=3.8',
    install_requires=[
        "numpy==1.19.3",
        "pandas==1.1.5",
    ],
    project_urls={
        'Homepage': 'https://github.com/quoctoanpk2511/matching-framework',
    },
    entry_points={
        'console_scripts': [
            'git-tagup=git_tagup.__main__:main',
            'gtu=git_tagup.__main__:main',
        ],
    },
)
