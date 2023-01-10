import os

from setuptools import find_packages, setup


# Inspired by:  https://goodresearch.dev/setup.html
# See https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/
# to work in development mode, e.g.: `python -m pip install -e canstock`

# The two following functions are taken directly from:
# https://github.com/pypa/pip/blob/main/setup.py#L11
# https://packaging.python.org/en/latest/guides/single-sourcing-package-version/#single-sourcing-the-version
def read(rel_path: str) -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with open(os.path.join(here, rel_path)) as fp:
        return fp.read()

def get_version(rel_path: str) -> str:
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            # __version__ = "0.9"
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


long_description = read("README.md")

setup(
    name="ODYM",
    version=get_version("./odym/__init__.py"),
	description="The ODYM model framework is a software library for dynamic material flow analysis (MFA).",
	long_description=long_description,
	long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[  # See https://pypi.org/classifiers/ for full list
                 "License :: OSI Approved :: MIT License",
				 "Programming Language :: Python",
                 "Programming Language :: Python :: 3",
                 "Private :: Do Not Upload",  # Prevents upload to PyPI
    ],
	url="https://github.com/IndEcol/ODYM",
    project_urls={
	    "Documentation": "https://github.com/IndEcol/ODYM",
        "Source": "https://github.com/IndEcol/ODYM",
        "Tracker": "https://github.com/IndEcol/ODYM/issues",
    },
	author="IndEcol",
	# package_dir={"": "src"},  # Apparently, only required if src is in subdirectory under root
    packages=find_packages(
	    where="odym",
		exclude=[""],
	),
	zip_safe=False,
	python_requires=">=3.0",
)
