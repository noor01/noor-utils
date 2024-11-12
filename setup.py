from setuptools import setup, find_packages

setup(
    name='noor-utils',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'napari',
        'numpy',
        'pandas',
        'dask',
        'zarr',
        'tifffile',
        'scikit-image',
        'scikit-learn',
        'Pillow', 
    ],
    python_requires='>3.9',
    author='Noorsher Ahmed',
    author_email='noor01@stanford.edu',
    description='A utility package for various data processing tasks',
    url='https://github.com/yourusername/noor-utils',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)