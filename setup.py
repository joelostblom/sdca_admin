from setuptools import setup, find_packages


setup(
    name='sdca_admin',
    version='0.1',
    description='A tool to validate CPRs and other things',
    # Uncomment if you have a README.md file
    # long_description=open('README.md').read(),
    # long_description_content_type='text/markdown',

    author='Joel Ostblom',
    author_email='joelostblom@proton.me',
    url='https://github.com/joelostblom/check_cpr',

    python_requires='>=3.8',
    packages=find_packages(),
    install_requires=[
        'pandas>=2.0',
        'openpyxl',
        'xlrd',
    ],
    entry_points={
        'console_scripts': [
            'filter_cpr = sdca_admin:filter_cpr',
        ],
    },
)
