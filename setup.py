#! /usr/bin/env python
"""lgtm_bot install script."""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="lgtm-bot",
    version="0.0.1",
    description="LGTM Gitlab bot",
    long_description=open("README.md").read(),
    author="Stefan Caraiman",
    url="https://github.com/stefan-caraiman/gitlab-lgtm-bot.git",
    packages=["lgtm_bot", "lgtm_bot.server", "lgtm_bot.common"],
    scripts=["scripts/lgtm_bot"],
    requires=open("requirements.txt").readlines(),
)
