# Vehicle-Routing-Optimization
Overview

In the Vehicle Routing Problem (VRP), the goal is to find optimal routes for multiple vehicles visiting a set of locations. (When there's only one vehicle, it reduces to the Traveling Salesman Problem.)

But what do we mean by "optimal routes" for a VRP? One answer is the routes with the least total distance. However, if there are no other constraints, the optimal solution is to assign just one vehicle to visit all locations, and find a shortest route for that vehicle. This is essentially the same problem as the TSP.

A better way to define optimal routes is to minimize the length of the longest single route among all vehicles. This is the right definition if the goal is to complete all deliveries as soon as possible. The VRP example below finds optimal routes defined this way.

[![1](https://github.com/user-attachments/assets/0b071ad6-a6fa-447f-9e62-fd2d397ec2ff)](https://camo.githubusercontent.com/ccd03d565e06250024de561efdf149a0708dd5a04f5a18a38aaf6b3d3fb4da42/68747470733a2f2f646576656c6f706572732e676f6f676c652e636f6d2f6f7074696d697a6174696f6e2f696d616765732f726f7574696e672f7672702e737667)

![2](https://github.com/user-attachments/assets/546886aa-320a-4ddb-8d22-9cf5e878ea39)
