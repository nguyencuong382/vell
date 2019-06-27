# Vell

A tool for spell checking multiple files in a folder. Sometimes when you write a document for your project but you get misspelled words you don't know

## Getting Started

### Installing

```bash
pip install --upgrade vell
```

### Check spell

1. Create `vell.ini` config file based on [vell.sample.ini](vell.sample.ini)
2. Run the bellow command to check spell:

```bash
vell
```

Check spell on a specific folder

```bash
vell ./test
```

### Custom `vell.ini` config file

Some misspelled words like 'my_var' are your definition and they appear many times, you can ignore them by theirs frequency of appearance
In this case. I tell to vell if a word appears more than 5 times, it will be ignored

```ini
[spell]
level_ignore = 5
```

Vell checks multiple files with specific extensions. To add more type of files:

```ini
[spell]
extensions =
    .html,
    .rst,
    README.md,
```

Some misspelled words like _html, env_ are keywords, you can ignore them when checking spell

```ini
[spell]
ignore_words =
    ; code
    html

    ; environment
    env
```

To exclude paths you don't want vell to check spell:

```ini
[path]
exclude =
    .env,
    .vscode,
    __pycache__,
```
