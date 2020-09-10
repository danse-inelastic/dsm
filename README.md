[![Build Status](https://travis-ci.com/danse-inelastic/dsm.svg?branch=master)](https://travis-ci.com/danse-inelastic/dsm)

Data stream model helps developers to build "chains" of connected 
computing nodes and run them. 
A computing node has input/ouput sockets, and the "dsm runner"
is responsible to carry "data streams" through the "chains" 
and feed "data streams" to computing nodes.

Usage:

 Please read the main function in Composite.py for an example.

Notes:

Developers are responsible to 

* build computing nodes (with i/o sockets)
    
Developers or Users are responsible to

* specify connections of computing nodes

Hints for developers:

* Read tests in source codes to understand how to use dsm. 
  Start with Composite.py and Runner.py is a good idea

Limitations:

* No loops are allowed.
* Currently only a trivial implementation of "runner" exists. So data streams
  are limited in one physical machine.

