import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='kempfolds-dmunn',
    version='0.0.1',
    author='David Munn',
    author_email='dcwmunn@gmail.com',
    description='Grab a Kempfold',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/dmunn/Kempfolds',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Langauge :: Python :: 3",
        "License :: OSI Approved  :: MIT License",
        "Operating System :: OS Independent",
    ],
)
