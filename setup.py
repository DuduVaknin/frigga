from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    readme = fh.read()

with open("version", "r") as fh:
    version = fh.read()

setup(
    author='Meir Gabay',
    author_email='unfor19@gmail.com',
    name='draxprom',
    license='MIT',
    long_description_content_type='text/markdown',
    description='Scrape only relevant metrics in Prometheus.',  # noqa: E501
    long_description=readme,
    version=f'{version}',
    packages=find_packages(),
    keywords='prometheus grafana dashboard metrics',
    include_package_data=True,
    url='https://github.com/unfor19/drax',
    download_url=f'https://github.com/unfor19/drax/archive/v{version}.tar.gz',  # noqa: E501
    install_requires=[
        'Click>=7.1.1',
        'beautifulsoup4>=4.9.1',
        'requests>=2.23.0'
    ],
    entry_points='''
        [console_scripts]
        drax=scripts.drax:cli
    ''',
    setup_requires=[
        'setuptools>=44.1.0',
        'wheel>=0.34.2',
        'twine==3.1.1',
        'docutils>=0.16'
    ],
    classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)