# Closure & Decorators

# Closure
1. What is it?
 - access to variables/functions/classes from out of actual scope

2. How to create?
 - we need to have min 2 function, outer and inner
 - outer function have to return declaration of inner function
 - inner function have to use something from outer function like variables, functions, classes

3. Pros:
 - persistence

4. Cons:
 - leak of memory

## Scope - access/visibility to variable/function declaration, class definition
- LEGB

1. L - local, created by function body
2. E - enclosing, function object '__closure__'
3. G - global, created by module (python file)
4. B - built-in, example: sum, max, print, len

## 2 ways of finding identifier:
1. lhs - left-hand side assignment - check if variable exist locally if not create
2. rhs - right-hand side assignment - search through the scopes (LEGB)

## 2 basic data structure
1. Stack - FILO - first in, last out
2. Queue - FIFO - first in, first out


## List indexing

"a" | "b" | "c"
--- | --- | ---
0 | 1 | 2 
-3 | -2 | -1 