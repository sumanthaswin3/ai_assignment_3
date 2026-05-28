# Dijkstra Algorithm for Indian Cities

**Name:** Sumanth Aswin  
**Roll Number:** SE24UCSE016 
**Course:** Artificial Intelligence  

---

## Objective

To implement Dijkstra’s Algorithm, also known in AI as Uniform-Cost Search, for finding the shortest path between Indian cities based on road distances.

---

## Description

This program models Indian cities as nodes in a weighted graph and road distances as edge costs.  
The user enters a start city and a goal city, and the program computes:

- Shortest path
- Total road distance
- Number of visited nodes

The graph is built from a CSV file containing city-to-city distances.

---

## Files

- `dijkstra_india.py` — Python implementation of Dijkstra’s algorithm
- `cities_distances.csv` — Dataset of Indian cities and road distances
- `README.md` — Documentation

---

## Algorithm Used

Dijkstra’s Algorithm / Uniform-Cost Search

Evaluation function:

f(n) = g(n)

Where g(n) is the path cost from the start node to node n.

---

## How to Run

```bash
python3 dijkstra_india.py
