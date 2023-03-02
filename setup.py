from setuptools import setup, find_packages


with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='derogationstool',
    version='0.1.0',
    author = 'Dilara Ercan',
    description= 'Birds and Habitats Directive Derogations Tool',
    long_description= long_description,
    long_description_content_type='text/markdown',
    url = 'https://github.com/edilara/derogationstool',
    classifiers=
    [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages= find_packages(),
    include_package_data=True,
    install_requires=[
        'chardet>=4.0.0',
        'charset-normalizer>=2.0.4',
        'click>=8.0.4',
        'colorama>=0.4.6',
        'cookiecutter>=1.7.3',
        'cryptography>=38.0.4',
        'elementpath>=3.0.2',
        'idna>=3.4',
        'Jinja2>=3.1.2',
        'jinja2-time>=0.2.0',
        'MarkupSafe>=2.1.1',
        'mkl-fft>=1.3.1',
        'mkl-random>=1.2.2',
        'mkl-service>=2.4.0',
        'numexpr>=2.8.4',
        'numpy>=1.23.5',
        'packaging>=22.0',
        'pandas>=1.5.2',
        'pip>=22.3.1',
        'poyo>=0.5.0',
        'pycparser>=2.21',
        'pyOpenSSL>=22.0.0',
        'PySocks>=1.7.1',
        'python-dateutil>=2.8.2',
        'python-slugify>=5.0.2',
        'pytz>=2022.7',
        'requests>=2.28.1',
        'setuptools>=65.6.3',
        'six>=1.16.0',
        'text-unidecode>=1.3',
        'Unidecode>=1.2.0',
        'urllib3>=1.26.14',
        'wheel>=0.37.1',
        'win-inet-pton>=1.1.0',
        'wincertstore>=0.2',
        'xmlschema>=2.1.1'
    ],
    entry_points={
        'console_scripts': [
            'derogationstool = derogationstool.src.derogationstool:main',
        ],
    },
)