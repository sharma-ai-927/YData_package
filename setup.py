from setuptools import setup, find_packages

setup(
    name='YData',
    version='0.1.0002',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A package to download YData files',
    # long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/sharma-ai-927/YData',
    author='Ethan Meyers',
    author_email='ethan.meyers@yale.edu'
)
