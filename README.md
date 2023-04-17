﻿# Programming

## Initialize virtual environment on the commmand line
Create virtual envirnoment
```
py -m venv .venv
```
Upgarde pip
```
py -m pip install --upgrade pip
```
Set permission for program
```
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
```
Install packages from requirements.txt
```
pip install -r .\requirements.txt
```
Freeze 
```
python -m pip freeze > requirements.txt
```

## Some errors:
* TypeError: an integer is required (got type list)
```
res = array('i', [[0] * (n + 1) for _ in range(3)])
```
-> Solution: We can not create an array from 2d list, so we create amount of array in a list
```
    res = [array('i', [0] * (n + 1)) for _ in range(3)]
```


## References

array: https://docs.python.org/3/library/array.html
