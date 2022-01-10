import pathlib
from setuptools import setup, find_packages

# The directory containing this file
root = pathlib.Path(__file__).parent

# The text of the README file
README = (root / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="passax",
    version="1.21",
    description="Retrieve saved passwords. Currenly working for Chrome-based Linux & Windows browsers.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/auax/passax",
    author="Auax",
    author_email="auax.dev@gmail.com",
    license="MIT",
    keywords=["password", "login", "data", "chrome", "brave", "opera", "windows", "linux", "browser", "info"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        'Intended Audience :: Developers',
        "Topic :: Security",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "secretstorage~=3.3.1",
        'pywin32==302; platform_system == "Windows"',
        'pycryptodome==3.12.0'
    ],
    entry_points={
        "console_scripts": [
            "realpython=reader.__main__:main",
        ]
    },
)
