# GENDIFF PROJECT 


[![Actions Status](https://github.com/AniutaP/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/AniutaP/python-project-50/actions)  [![Maintainability](https://api.codeclimate.com/v1/badges/f8ebfd49c1a7ee4eeaf7/maintainability)](https://codeclimate.com/github/AniutaP/Gendiff-project/maintainability)  [![Test Coverage](https://api.codeclimate.com/v1/badges/f8ebfd49c1a7ee4eeaf7/test_coverage)](https://codeclimate.com/github/AniutaP/Gendiff-project/test_coverage)


### Description
Generator of differences is a program that determines the difference between two data structures 
(JSON, YAML files) and displays the differences on the screen in the format of a new data structure. 
The program provides three types of output formats: 
* stylish (by default)
* plain
* json

### System requirements:
* programming Language - Python 3
* operating system - OS Independent


### Installation 
`pip install git+https://github.com/AniutaP/python-project-50.git`


### Usage as library
```
from gendiff import generate_diff

diff = generate_diff(first_file, second_file, formatter)
```


### Usage as utility
```
$ gendiff -h
usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```


### Usage examples
[![asciicast](https://asciinema.org/a/586204.svg)](https://asciinema.org/a/586204)


[![asciicast](https://asciinema.org/a/586205.svg)](https://asciinema.org/a/586205)


[![asciicast](https://asciinema.org/a/589462.svg)](https://asciinema.org/a/589462)


[![asciicast](https://asciinema.org/a/590449.svg)](https://asciinema.org/a/590449)