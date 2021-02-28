from setuptools import setup
from torch.utils import cpp_extension

setup(
  name='fasth',
  version='0.0.1',
  license='LICENSE',
  description='',
  packages=["fasth"],
  long_description=open('README.md').read(),
  long_description_content_type="text/markdown",
  ext_modules=[cpp_extension.CppExtension('fasth', ['fasth/fasth_cuda.cu', 'fasth/fasth.cpp'])],
  cmdclass={'build_ext': cpp_extension.BuildExtension},
  python_requires=">=3.6",
  install_requires=[
      "torch>=1.3.1",
      "numpy",
      "ninja",
  ],
)
