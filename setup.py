"""Colaboratory Tools

This package provides a collection of useful tools for working with
Colaboratory notebooks.

**Source:**
  https://bitbucket.org/mforbes/colaboratory-tools
**Issues:**
  https://bitbucket.org/mforbes/colaboratory-tools/issues
"""
import sys

from setuptools import setup, find_packages

NAME = "colaboratory_tools"

setup_requires = [
]

install_requires = [
]

test_requires = [
]

extras_require = dict(
)


setup(name=NAME,
      version='0.1.0dev',
      packages=find_packages(exclude=['tests']),

      setup_requires=setup_requires,
      install_requires=install_requires,
      tests_require=test_requires,
      extras_require=extras_require,

      # Metadata
      author='Michael McNeil Forbes',
      author_email='michael.forbes+bitbucket@gmail.com',
      url='https://bitbucket.org/mforbes/colaboratory-tools',
      description="Colaboratory Tools.",
      long_description=__doc__,
      license='BSD',

      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 3 - Alpha',

          # Indicate who your project is intended for
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities',

          # Pick your license as you wish (should match "license" above)
          'License :: OSI Approved :: BSD License',

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],
      )
