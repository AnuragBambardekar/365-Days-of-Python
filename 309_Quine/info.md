# Quine

A quine is a program which prints a copy of its own as the only output. A quine takes no input. Quines are named after the American mathematician and logician Willard Van Orman Quine (1908–2000).

The standard terms for these programs in the computability theory and computer science literature are "self-replicating programs", "self-reproducing programs", and "self-copying programs".

This is indeed the smallest python program that can print its own source code but it is not a quine because a quine should not use open() function to print out its source code.
```
print open(__file__).read() 
```

In general, the method used to create a quine in any programming language is to have, within the program, two pieces: 

(a) code used to do the actual printing and 
(b) data that represents the textual form of the code. 

The code functions by using the data to print the code (which makes sense since the data represents the textual form of the code), but it also uses the data, processed in a simple way, to print the textual representation of the data itself.

## Cheating Quines

In many functional languages, including Scheme and other Lisps, and interactive languages such as APL, numbers are self-evaluating.

```lisp
1
```

## Ouroboros Programs

![Ouroboros](image.png)

Ouroboros programs, also known as self-eating or self-replicating programs, are computer programs that have the ability to generate copies of themselves. The name "Ouroboros" comes from the ancient symbol of a serpent or dragon eating its own tail, symbolizing cyclicality or self-reference. In the context of computer programs, Ouroboros programs essentially "eat" or replicate themselves.

Creating Ouroboros programs can be a complex and fascinating challenge in the field of computer science and programming. Such programs need to possess the capability to generate a complete and accurate copy of their source code, which is a non-trivial task.

The creation of Ouroboros programs can be seen as an exploration of various computer science concepts, including recursion, self-reference, and code generation. These programs are typically not used in practical applications but are developed for educational, artistic, or recreational purposes.

It's worth noting that Ouroboros programs can be considered a subset of quines (self-replicating programs that print their own source code) because they involve self-replication. However, not all quines are Ouroboros programs, as some quines simply print their source code without the ability to generate a full copy of themselves.

Ouroboros programs often raise questions about the nature of computation, recursion, and the limits of what a program can do. They are more of a theoretical and intellectual curiosity rather than a practical programming tool.

