from setuptools import setup, find_packages

setup(
    name="Nruta_Mini_Project_7",
    version="0.1",
    author="Nruta Choudhari",
    description="A CLI for biopics database management",
    packages=find_packages(where="mylib"),
    entry_points={
        "console_scripts": [
            "biopics-cli=cli_tool:main",
        ],
    },
    install_requires=[
        "requests",
        "pandas",
        "click",
        "pytest",
        "pytest-cov",
        "ruff",
        "databricks-sql-connector",
        "python-dotenv",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
