# Goals

Make a more complex AgentState
Create a processing node that performs operations on list data
Setup a LangGraph that processes and outputs computed results
Invoke the graph with structured inputs and retrieve outputs

## Notes

If a variable in the state has not been passed in, then it
is treated as type None rather than an empty variable for that
type. Like `result` would not be an empty string, it would just
be None. So you couldn't do something like state['result'] +=
"blah blah", since you cannot concat something with None.
