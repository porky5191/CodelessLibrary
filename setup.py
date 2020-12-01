from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: End Users/Desktop',
  'Intended Audience :: Developers',
  'Intended Audience :: System Administrators',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='codeless',
  version='0.0.1',
  description='A simple library to perform EDA & Data Engineering quickly without writing any code',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/porky5191/CodelessLibrary',  
  author='Arun Kumar Nath',
  author_email='arunnath792@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='codeless', 
  packages=find_packages(),
  install_requires=['imbalanced-learn==0.7.0', 'matplotlib==3.3.0', 'numpy==1.18.5', 'pandas==1.1.3',
                  'scikit-learn==0.23.2', 'scipy==1.4.1', 'seaborn==0.10.1']
)