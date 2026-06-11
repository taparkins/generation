from setuptools import setup

setup(
    name='generation',
    version='0.1',
    description='snippets of code intended to build up a collection of procedural generation scripts',
    url='',
    author='taparkins',
    author_email='talia.a.parkinson@gmail.com',
    license='MIT',
    packages=['src', 'tests'],
    install_requires=['Pillow'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    zip_safe=False,
)
