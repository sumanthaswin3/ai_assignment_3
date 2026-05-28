UGV Navigation with Dynamic Obstacles

Name: Sumanth Aswin
Roll Number: SE24UCSE016
Course: Artificial Intelligence

Objective

To enable an Unmanned Ground Vehicle (UGV) to navigate through a battlefield grid in the presence of dynamic obstacles that are not fully known in advance.

Description

The battlefield is represented as a 70x70 grid. The UGV starts at a given start node and must reach the goal node by the shortest possible path. Unlike the static obstacle case, new obstacles may appear while the UGV is moving.

The algorithm uses A* search for path planning. Whenever a new obstacle blocks the next step in the current path, the UGV replans from its current position to the goal.

This simulates a real-world scenario where obstacles are dynamic and not completely known a priori.

Algorithm Used

A* Search with Dynamic Replanning

Evaluation Function:
f(n) = g(n) + h(n)

where
g(n) = path cost from start
h(n) = heuristic estimate to goal

Measures of Effectiveness

1. Path length
2. Nodes expanded
3. Number of replans
4. Mission success or failure
5. Obstacle density impact

How It Works

1. Generate a 70x70 grid with random obstacle density.
2. Find a path using A*.
3. Before each movement, add dynamic obstacles.
4. If the next move becomes blocked, run A* again.
5. Continue until goal is reached or no path exists.

Run

python3 ugv_dynamic.py
