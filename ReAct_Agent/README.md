# Specifications for ReAct

The point of ReAct is to reason then act (hence the name)
and its graph looks like this:
START -> Agent -> Loop (for tool calling) -> END

## Goals

1. Learn how to create Tools in LangGraph
2. How to create a ReAct graph
3. Work with different types of messages (such as ToolMessages)
4. Test out the robustness of the graph

Goal: Create a robust ReAct agent

## Notes

### Annotation

These add additional context to a variable (like metadata) without actually
changing the type of the variable. Like so:

```python
email = Annotation[str, "This has to be a valid email format (like abc@gmail.com)"]
# And to see this, you would do:
print(email.__metadata__)
# Outputs ("This has to be a valid email format (like abc@gmail.com)")
```

### Sequence
This one is here for safe list manipulation, it automatically handles state manipulation
for lists. It's also a type annotation and prevents manipulation graph nodes.

### Reducer Function
A reducer function defines a rule that controls how updates from nodes are
applied to the existing state (basically how do we merge new data into the
current state?). Without a reducer function, we never "update" the state,
we just overwrite the old values. We're going to be using the `add_messages`
reducer to add any new message as a list.
