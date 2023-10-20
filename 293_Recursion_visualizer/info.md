# Visualize Recursion

The only dependency for recursion visualiser is Graphviz

```cmd
pip install recursion-visualiser
```

Recursion visualiser is a python tool that visualizes recursion tree with animation and draws recursion tree for recursive function. It works with almost any type of recursive function. Just add the recursion-visualiser decorator to your function and let it do the rest of the work.

```python
# Decorator accepts optional arguments: ignore_args , show_argument_name, show_return_value and node_properties_kwargs
@vs(node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
```