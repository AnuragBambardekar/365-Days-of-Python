# Abstract Syntax Tree

AST stands for Abstract Syntax Tree. It is a hierarchical tree-like data structure that represents the syntactic structure of a Python program. The AST module in Python's standard library provides a way to parse Python source code into an abstract syntax tree.

## Using AST to understand code

At a fairly high level, here’s what happens to your code:

1. The code is parsed into a list of pieces usually called tokens. These tokens are based on a set of rules for things that should be treated differently. For instance, the keyword `if` is a different token than a numeric value like 42.

2. The raw list of tokens is transformed to build an Abstract Syntax Tree, AST. An AST is a collection of nodes which are linked together based on the grammar of the Python language.

3. From an abstract syntax tree, the interpreter can produce a lower level form of instructions called bytecode. These instructions are things like BINARY_ADD and are meant to be very generic so that a computer can run them.

4. With the bytecode instructions available, the interpreter can finally run your code. The bytecode is used to call functions in your operating system which will ultimately interact with a CPU and memory to run the program.

~[MattLayman]

## Motivation for AST

By the time your source code is turned into bytecode, it’s too late to gain much understanding about what you wrote. Bytecode is very primitive and very tuned to making the interpreter fast. In other words, bytecode is designed for computers over people.

On the other hand, abstract syntax trees have enough structured information within them to make them useful for learning about your code. ASTs still aren’t very people friendly, but they are more sensible than the bytecode representation.

## Questions we can answer by analyzing an AST

- How many variables did I use?
- What are the most common function calls in my code?
- Are my modules tightly coupled to each other?
- Which third party libraries show up frequently in different packages?

`The ast module is probably not a tool that you will reach for very often. In those times that you do need ast, its minimal API is quite memorable and you can analyze code quickly.`