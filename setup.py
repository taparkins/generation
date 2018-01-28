from setuptools import setup

setup(
    name='generation',
    version='0.1',
    description='snippets of code intended to build up a collection of procedural generation scripts',
    url='',
    author='aparkins',
    author_email='aric.parkinson@gmail.com',
    license='MIT',
    packages=['src', 'tests'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    zip_safe=False,
)
