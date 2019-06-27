# Contribute

I wrote Vell for first time uploading to [Pypi](https://pypi.org/) and it is opensource, let's become a Vell contributor

## Upload Vell to Pypi

### Main structure project

```
.
├── vell
│   ├── __init__.py
│   └── spell.py
├── test
├── LICENSE
├── MANIFEST.in
├── README.md
└── setup.py
```

### Create virtual environment

```
virtualenv .env -p python3.6
source .env/bin/activate
```

### Install `twine`

```
pip install twine
```

### Register Pypi

If you don't want type your username and password for each time uploading package, let's create `.pypirc` file

```
vim $HOME/.pypirc
```

Edit file

```
[pypi]
username = <your username>
password = <your password>
```

### Build package

```
python setup.py sdist bdist_wheel
```

### Testing

You can install your package locally to ensure everything is work fine

```
pip install -e .
```

### Upload package py twine

```
twine upload dist/*
```
