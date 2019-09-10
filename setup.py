from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="understat",
    version="0.1.2",
    packages=find_packages(),
    description="A Python wrapper for https://understat.com/",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amosbastian/understat",
    author="amosbastian",
    author_email="amosbastian@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ],
    keywords="fpl fantasy premier league understat football",
    project_urls={
        "Documentation": "http://fpl.readthedocs.io/en/latest/",
        "Source": "https://github.com/amosbastian/fpl"
    },
    install_requires=[
        "aiohttp",
        "codecov",
        "pytest-aiohttp",
        "pytest-cov",
        "pytest-mock",
        "pytest",
    ],
)
