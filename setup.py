from setuptools import setup, find_packages

with open("README.md", 'r') as fh:
    long_description = fh.read()

setup(
    name='vell',
    packages=find_packages(),
    version='1.0.5',
    license='MIT',
    description='Check spell for mutiple files in a project',
    author='nguyencuong382',
    author_email='nguyenmanhcuong382@gmail.com',
    url='https://github.com/nguyencuong382/vell',
    keywords=['check', 'spell'],
    install_requires=[
        'pyspellchecker==0.4.0',
        'beautifulsoup4==4.7.1',
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        'console_scripts': ['vell=vell.spell:main'],
    },
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
