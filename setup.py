from setuptools import setup

setup(name='mlpipe',
      version='0.1',
      description='A pipe framework for machine learning purposes',
      url='http://github.com/dataroots/mlpipe',
      author='Bart Smeets',
      author_email='bart@dataroots.io',
      license='MIT',
      package_dir={'mlpipe': 'src/mlpipe'},
      packages=['mlpipe'],
      zip_safe=False)