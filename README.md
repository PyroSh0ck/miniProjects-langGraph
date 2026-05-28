# This is a set of mini projects using LangGraph

## Notes

### Type Annotations

The first thing I want to do is define a couple of python
type annotations for the future:

#### Typed Dictionary

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

#### Union

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

#### Optional

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

#### Any

```python
from typing import Any

def print_value(x: Any):
  print(x)

print_value("Something cool here")
```

This one is also self explanatory, x can be literally anything.

#### Lambda

```python
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, nums))
```

Basically allows you to write mini functions in a single line.
The code above runs a for loop and squares each number.

### Elements

#### State

A state is a "shared data structure" which holds the information/context
of the entire application. Its basically the memory of the app and it holds
stuff like variables and stuff.

Think about it like a whiteboard in a meeting. Any participant in the room
(a node) can write and read information on the whiteboard (the state) to
stay updated and coordinate actions.

#### Nodes

Nodes are individual functions/operations that perform specific tasks
within the graph. Each node gets an input (which is usually just the
state) and then it gives an output (or updates the state).

An analogy could be an assembly line, where each section is responsible
for one and only one action to the current product until it reaches
its final output.

#### Graph

A graph is the overarching structure that maps out how nodes are connected.
Its by far the most important segment of LangGraph.

#### Edges

Edges are the connections between nodes and are directional (i.e. they
point from one node to another to tell us which node happens first).

You can think of this one like train tracks. The tracks (edges) connect
each individual train station (node) to another train station. The map
of how the train stations are connected would be the graph, and the train
itself would be the state, as it's "updated" as it moves from station (node)
to station (node).

##### Conditional Edges

Conditional edges are just edges that decide the next node to execute based
on some conditional logic on the current state.

For example, a traffic light has 3 different states, red, green, and yellow.
Red would lead to the node for stopping, yellow for slowing down, and green
to keep going straight.

#### Start Node

The start node is effectively the "virtual entry point" for LangGraph (like
a index.ts would be for Node), and it marks where you start the workflow.
It doesn't actually perform any operations.

#### End Node

The end node, like the start node, is just the conclusion of a workflow in
LangGraph. It also doesn't perform any operations, as the graph's execution
just stops once it reaches the end node.

#### Tools

Specialized functions/utilities that nodes can use to perform specific tasks
like fetching data from an API. They also improve the capabilities of nodes by
providing extra functionalities. A node is a PART of the graph structure, while
a tool is just something a node can use.

#### ToolNode

A ToolNode is a special kind of NODE whose main job is to run a tool. It
connects the output of the tool back into the state so that other nodes
can use that information.

For an analogy, think of this one like an operator using a machine. The
operator (ToolNode) controls a machine (a tool), and then sends the results
back to the assembly line.

#### StateGraph

A StateGraph is a class in LangGraph that's used to build and compile the
graph structure, and it manages the nodes, edges, and state.

#### Runnable

A Runnable in LangGraph is the name for any generic component in an AI
workflow that performs a task. They are the building blocks for making
modular systems. The difference between a Runnable and a Node is that
a Runnable can represent various operations, while a Node only performs
an update to the State. It's also very common in LangChain.

#### Messages

There are 5 main types of messages in LangChain and LangGraph:

- Human Message - input from a user
- AI Message - response from the AI model
- System Message - gives context/instructions to a model
- Function Message - gives the result of a function call
- Tool Message - gives the result from a tool call
