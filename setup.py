from setuptools import setup, find_packages

versionFile = "VERSION"
setup(name="frhd-python",
    version=4.3,
    description="Library to edit FRHD tracks",
    long_description=open("README.rst").read(),
    url="https://github.com/gaetgu/frhd",
    download_url="https://github.com/gaetgu/frhd/archive/v_4.3.tar.gz",
    install_requires=[
          'decode',
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
    keywords="development freeriderhd freerider code track tracks",
    packages=find_packages(exclude=["images"]),
)
