from setuptools import setup

setup(
    name='poems',
    version='1.0.0',
    author='Your Name',
    description='A simple Python program to store favorite and least favorite poems',
    license='MIT',
    py_modules=['poems'],
    entry_points={
        'console_scripts': [
            'poems=poems:main',
        ],
    },
)
