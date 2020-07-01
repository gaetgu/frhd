from setuptools import *

versionFile = "VERSION"
setup(name="frhd-python",
    version=5.1,
    description="Library to edit FRHD tracks",
    long_description=open('README.rst').read(),
    url="https://github.com/gaetgu/frhd",
    download_url="https://github.com/gaetgu/frhd/archive/v_5.1.tar.gz",
    install_requires=[
        'json',
        'requests',
        'decode'
      ],
    author="Gaetgu",
    author_email="gabriel.ethan.phantom@gmail.com",
    license="MIT License",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Code Generators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only"
    ],
    keywords="development freeriderhd freerider frhd code track tracks",
    packages=find_packages(exclude=["images"]),
)
