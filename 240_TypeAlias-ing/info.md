# Type Alias

Type aliases are user-specified types which may be as complex as any type hint, and are specified with a simple variable assignment on a module top level.

Type aliases allow you to quickly define new aliases that can stand in for more complicated type declarations. For example, say that you’re representing a playing card using a tuple of suit and rank strings and a deck of cards by a list of such playing card tuples. A deck of cards is then type hinted as list[tuple[str, str]].

Put simply, the point of using type aliases is twofold:

- to let the user know, in a relatively simple way, what type an argument should have (should, as we’re still talking about type hints), and
- to make static checkers happy.

