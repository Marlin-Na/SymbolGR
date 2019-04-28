
from setuptools import setup

INSTALL_REQUIRES = [
    "astropy",
    "numpy"
]

EXTRAS_REQUIRE = {
    "dev": [
        "sympy>=1.1",
        "pytest"
    ]
}

setup(
    name = "symbolgr",
    version = "0.0.1",
    description = "Symbolic calculation of various tensors in General Relativity",
    author = "Jialin Ma",
    author_email = "marlin-@gmx.cn",
    packages = ["symbolgr"],
    install_requires = INSTALL_REQUIRES,
    extras_require = EXTRAS_REQUIRE
)

