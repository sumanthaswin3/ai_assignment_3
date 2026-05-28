UGV Navigation with Static Obstacles

Name: Sumanth Aswin
Roll Number: SE24UCSE016
Course: Artificial Intelligence

Objective

To design an algorithm that enables an Unmanned Ground Vehicle (UGV) to navigate through a battlefield grid while avoiding obstacles and reaching the goal using the shortest path.

Description

The battlefield is represented as a 70x70 grid. Some cells contain obstacles which the vehicle cannot pass through. The obstacle density can be generated randomly at three levels: low, medium, and high.

The program uses the A* search algorithm to find the shortest path from the start node to the goal node while avoiding obstacles.

Algorithm Used

A* Search Algorithm

Evaluation Function:

f(n) = g(n) + h(n)

where

g(n) = cost from start node
h(n) = heuristic estimate to goal

Measures of Effectiveness

Path length
Nodes expanded
Obstacle density impact

Run

python3 ugv_static.py
