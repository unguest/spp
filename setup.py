from setuptools import setup, find_packages
setup(
    name="HelloWorld",
    version="0.1",
    packages=find_packages(),
    scripts=["spp.py"],

    # metadata to display on PyPI
    author="unguest",
    author_email="unguestdev@gmail.com",
    description="SPP permits you to generate a password that fits your needs in no time.",
    keywords="password generator secure random",
    url="https://github.com/unguest/spp/README.md",   # project home page, if any
    project_urls={
        "Source Code": "https://github.com/unguest/spp/",
    },
    classifiers=[
        "License :: MIT"
    ]

    # could also include long_description, download_url, etc.
)