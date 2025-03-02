from setuptools import setup, find_packages

setup(
    name='positionday',
    version='0.1.0',
    packages=find_packages(where='positionday'),  # Specify the directory where the package is located
    package_dir={'': 'positionday'},  # Map the empty package name to the 'positionday' directory
    install_requires=[
        'openai',
        'pocketsphinx',
        'gtts',
        'pygame',
        'pyfiglet',
        'rich',
        'InquirerPy',
    ],
    entry_points={
        'console_scripts': [
            'positionday=positionday.cli:main',
        ],
    },
    license='MIT',  # Add your license information
    description='A package for career coaching and job search',  # Add a description
    long_description=open('README.md').read(),  # Add a long description from README.md
    long_description_content_type='text/markdown',  # Specify the content type of the long description
    author='Your Name',  # Add your name
    author_email='your.email@example.com',  # Add your email
    url='https://github.com/yourusername/positionday',  # Add your project URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Your License',  # Add your license classifier
        'Operating System :: OS Independent',
    ],
)
