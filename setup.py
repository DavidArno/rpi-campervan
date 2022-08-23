from distutils.core import setup

setup(
    name='rpi_campervan',
    version='0.1dev0',
    author='David Arno', 
    author_email='david@davidarno.org',
    packages=["rpi_campervan/data_sources"],
    long_description=open('README.md').read()
)