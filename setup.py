from setuptools import setup
import sys


# def forbid_publish():
#     argv = sys.argv
#     blacklist = ["register", "upload"]

#     for command in blacklist:
#         if command in argv:
#             values = {"command": command}
#             print('Command "%(command)s" has been blacklisted, exiting...' % values)
#             sys.exit(2)


#forbid_publish()

setup(
    name="raster_analysis",
    version="0.1.0",
    description="A package to extract values from raster files.",
    url="https://github.com/lhuddleston16/pachama_test",
    author="Levi Huddleston",
    author_email="levilhuddleston@gmail.com",
    license="MIT",
    packages=["raster_analysis"],
    install_requires=[
        "affine==2.3.1",
        "aiohttp==3.8.1",
        "aiosignal==1.2.0",
        "argcomplete==2.0.0",
        "async-timeout==4.0.2",
        "attrs==21.4.0",
        "black==22.6.0",
        "boto==2.49.0",
        "cachetools==5.2.0",
        "certifi==2022.6.15",
        "cffi==1.15.1",
        "charset-normalizer==2.1.0",
        "click==8.1.3",
        "click-plugins==1.1.1",
        "cligj==0.7.2",
        "coverage==6.4.1",
        "crcmod==1.7",
        "cryptography==37.0.2",
        "fasteners==0.17.3",
        "frozenlist==1.3.0",
        "gcs-oauth2-boto-plugin==3.0",
        "google-apitools==0.5.32",
        "google-auth==2.9.0",
        "google-reauth==0.1.1",
        "gsutil==5.10",
        "httplib2==0.20.4",
        "idna==3.3",
        "iniconfig==1.1.1",
        "monotonic==1.6",
        "multidict==6.0.2",
        "mypy-extensions==0.4.3",
        "numpy==1.23.0",
        "oauth2client==4.1.3",
        "packaging==21.3",
        "pathlib==1.0.1",
        "pathspec==0.9.0",
        "platformdirs==2.5.2",
        "pluggy==1.0.0",
        "py==1.11.0",
        "pyasn1==0.4.8",
        "pyasn1-modules==0.2.8",
        "pycparser==2.21",
        "pyOpenSSL==22.0.0",
        "pyparsing==3.0.9",
        "pytest==7.1.2",
        "pyu2f==0.1.5",
        "rasterio==1.2.10",
        "requests==2.28.1",
        "retry-decorator==1.1.1",
        "rsa==4.7.2",
        "six==1.16.0",
        "snuggs==1.4.7",
        "tomli==2.0.1",
        "typing_extensions==4.2.0",
        "urllib3==1.26.9",
        "yarl==1.7.2",
    ],
)
