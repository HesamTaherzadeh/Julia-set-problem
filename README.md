# Julia-set-problem# Julia-set-problem
## In the context of complex dynamics, a topic of mathematics, the Julia set and the Fatou set are two complementary sets (Julia "laces" and Fatou "dusts") defined from a function. Informally, the Fatou set of the function consists of values with the property that all nearby values behave similarly under repeated iteration of the function, and the Julia set consists of values such that an arbitrarily small perturbation can cause drastic changes in the sequence of iterated function values. Thus the behavior of the function on the Fatou set is "regular", while on the Julia set its behavior is "chaotic". credit : wikipedia

## in this particular implementation of Julia set the equation is z = z^2 + c 

## the main objective of this program here is to show that how vectorazation can help you write more efficent alghorithms 
## so in this program i managed to reduce the computation time expense from 14.168912410736084 seconds to 4.78585 seconds by using numpy vectorazation rather than pure python loops

## I found this exercise really intuitive so i recommend you to rewrite it from scratch and line profile it to see the noticable difference of time in these programs is due to lines that are carrying out vectorazation

## the line by line profiling and cprofiling are also included in this repository
