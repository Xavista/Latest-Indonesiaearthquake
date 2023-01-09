import setuptools

with open('README.md', 'r',  encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='latestearthquake-indonesia',
    version='0.0.1',
    description='This is package will get the latest earthquake from BMKG|Meteorological Climatological and Geophysical Agency',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ilham sapista ',
    author_email='ilham.sapista@gmail.com',
    url='https://github.com/Xavista/Latest-Indonesiaearthquake',

    classifiers = [
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)e',
    'Operating System :: OS Independent',
    ],

    packages=setuptools.find_packages(),
    python_requires='>=3.6'
)
