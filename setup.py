from setuptools import setup

setup(
  name='fasth',
  version='0.0.1',
  license='LICENSE',
  description='',
  packages=setuptools.find_packages(),
  long_description=open('README.md').read(),
  long_description_content_type="text/markdown",
  python_requires=">=3.6",
  install_requires=[
      "torch>=1.3.1",
      "numpy",
      "ninja",
  ],
)
