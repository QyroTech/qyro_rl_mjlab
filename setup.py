"""Installation script for the 'Qyro_rl_mjlab' python package."""

from setuptools import setup, find_packages

# Minimum dependencies required prior to installation
INSTALL_REQUIRES = [
    "mujoco",
    "numpy",
    "torch",
    "tyro",
    "tqdm",
]

# Installation operation
setup(
    name="Qyro_rl_mjlab",
    packages=["src"],
    version="0.0.1",
    install_requires=INSTALL_REQUIRES,
)
