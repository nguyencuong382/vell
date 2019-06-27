# Vell

A tool for spell checking multiple files in a folder. Sometimes when you write a document for your project but you get misspelled words you don't know

## Getting Started

### Installing

```
pip install --upgrade vell
```

### Check spell

1. Create `vell.ini` config file based on [vell.sample.ini](https://github.com/nguyencuong382/vell/vell.sample.ini)
2. Run the bello command to check spell:

```
vell
```

### Custom `vell.ini` config file

Some misspelled words like 'my_var' are your definition and they appear many time, you can ignore them by theirs frequency of appearance
In this case. I tell to vell if a word appear more than 5 times, they will be ignored

```
[spell]
level_ignore = 5
...
```

Vell checks multiple files with specific extensions. To add more type of files:

```
[spell]
...
extensions =
	    .html,
        .rst,
	    README.md,
...
```

Some misspelled words like _html, env_ are keywords, you can ignore them when checking

```
[spell]
...
ignore_words =
        ; code
        html

        ; environment
        env
...
```

To exclude paths you don't want vell to check spell:

```
...
[path]
exclude =
	    .env,
	    .vscode,
        __pycache__,
...
```
