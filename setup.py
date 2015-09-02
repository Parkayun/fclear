"""
fclear
------
Clear compiled files.
"""

from os import path
from setuptools import setup

long_description = open(
    path.join(
        path.dirname(__file__),
        'README.rst'
    )
).read()


setup(
    name='fclear',
    version='0.0.1',
    url='https://github.com/Parkayun/fclear',
    license='MIT',
    author='Ayun Park',
    author_email='iamparkayun@gmail.com',
    description='Clear compiled files.',
    long_description=long_description,
    packages=['fclear'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    entry_points={
        'console_scripts': [
            'fclear=fclear.cli:run',
        ],
    },
)
