# Choosing between OrderedDict and dict

- python dictionaries are unordered
- OrderedDict was added to Python 3.1
- OrderedDict iterates over keys and values in insertion order
- In OrderedDict, new entries are added at end
- dict now retains insertion order (Python 3.6 onwards)

Is  OrderedDict still needed? <br>
- Intent signaling [order of items is necessary]
- control over item order (move_to_end, ...)
- equalitty test behavior
- backwards compatibility
- preserves order of key-value pair insertion
- inherits all methods from dict
