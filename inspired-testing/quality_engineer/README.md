# Inspired Testing - Technical Challenge (SET)

My solutions to the **Inspired Testing**'s (SET) technical challenge.

For questions **1**, **2** and **4** see the [How To Run The Tests](#how-to-run-the-tests) section.

##### Question 3 (answer)

```python
def print_list(a_list):
    for i in range(1, len(a_list)):
        print('Element {} = {}'.format(str(i),str(a_list[i])))

a_list = [1, 2, 3, 5, 7, 9]
print_list(a_list)

```

###### Why does print_list() not correctly print out the elements a_list?


When passing **1** and **len(a_list)** to the built-in *range(start, stop, [step])* method, 
what we are essentially telling *range(start, stop, [step])* is to start reading the list
from the **2<sup>nd</sup>** element (or the element whose index is 1) 
up to (and not including) the **n<sup>th</sup>** element (or the element that has an index of 6 - *length of the list*).

There are two possible fixes:

```python
def print_list(a_list):
    for i in range(0, len(a_list)):
        print('Element {} = {}'.format(str(i),str(a_list[i])))
```

or simply:
```python
def print_list(a_list):
    for i in range(len(a_list)):
        print('Element {} = {}'.format(str(i),str(a_list[i])))
```

**Note:** Array like List use "zero-based indexing", which is a way of numbering the items in an array such 
that the first item of it has an index of 0.

### How To Run The Tests

You need [python](https://www.python.org/downloads/) and [pipenv](https://pypi.org/project/pipenv/). 
You can read more about pipenv [here](https://pipenv.pypa.io/en/latest/).

```console
$ cd InspiredTesting/SET
$ pipenv install
```

To run the tests,

```console
$ pytest -p no:cacheprovider -s
```
