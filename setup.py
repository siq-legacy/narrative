from distutils.core import setup
from bake.packaging import *

setup(
    name='narrative',
    version='0.0.1',
    packages=enumerate_packages('narrative'),
    package_data={
        'narrative.bindings': ['*.mesh'],
    }
)
