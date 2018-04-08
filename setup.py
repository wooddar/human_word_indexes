from setuptools import setup, find_packages

setup(
    name='human_word_indexes',
    version='1.0',
    python_requires='>=2.7',
    packages=find_packages(),
    url='https://github.com/wooddar/human_word_indexes',
    license='MIT',
    author='hugodarwood',
    author_email='',
    description='A Package to generate human readable indexes for Pandas DataFrames or other data',
    install_requires=['numpy','pandas','nltk']
)
