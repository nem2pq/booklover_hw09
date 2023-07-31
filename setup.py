from setuptools import setup, find_packages

setup(name='booklover',
      version='0.1',
      description='Booklover python packages, my first python package!',
      url='https://github.com/nem2pq/booklover_hw09',
      author='Noah McIntire',
      author_email='nem2pq@virginia.edu',
      license='MIT',
      packages=['booklover'],
      install_requires=['numpy', 'pandas', 'warnings'],
      zip_safe=False)