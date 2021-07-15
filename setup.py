from setuptools import setup

setup(name='DigitalOcean',
      version='0.1',
      description='A Python Interface to Digital Ocean',
      url='N/A',
      author='Tyler McVety',
      author_email='tyler@mcvety.org',
      packages=[
            'DigitalOcean'
      ],
      install_requires=[
          'requests'
      ],
      tests_require=[
          'mock',
          'pytest',
          'pytest-cov',
      ],
      zip_safe=False
)