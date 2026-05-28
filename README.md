# This is a set of mini projects using LangGraph

The first thing I want to do is define a couple of python
type annotations for the future:

## Typed Dictionary

Created like so:

```python

from typing import TypedDict

class Movie(TypedDict):
  name: str
  year: int

movie = Movie(name="Avengers Endgame", year=2019)
```

The point of this is that we want to make sure that data
is a particular structure or format (especially LangGraph).
Specifically, it's used quite a bit to define "states" in
LangGraph. It's basically there to encourage type safety,
because we explicitly define what the types are of all of
the Class properties.

## Union

Created like so (again :D):

```python
from typing import Union

def square(x: Union[int, float]) -> float:
  return x * x

x = 5 # will work because its an int
x = 1.234 # will work because its a float
x = "some rando string" # won't work because its not an int or a float
```

Unions are basically OR operators, and allow you to define multiple
types for one variable while still maintaining good type safety.

## Optional

```python
from typing import Optional

def nice_message(name: Optional[str]) -> None:
  if name is None:
    print("Hey rando")
  else:
    print(f"Hey {name}!")
```

This one is pretty self explanatory, but it makes it so that
a parameter can either be a type or None (not any type, specifically none)

## Any

```python
from typing import Any

def print_value(x: Any):
  print(x)

print_value("Something cool here")
```

This one is also self explanatory, x can be literally anything.

## Lambda

```python
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, nums))
```

Basically allows you to write mini functions in a single line.
The code above runs a for loop and squares each number.
