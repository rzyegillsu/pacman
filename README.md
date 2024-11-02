This project simulates an agent navigating a grid-like environment using Depth-First Search (DFS) and Iterative Deepening Search (IDS) to reach a target location. The environment and the agent’s starting position are loaded from input.txt, which defines obstacles, open paths, and the target point.

Code Structure:

environment: Simulates the agent’s movement within the environment.

recursive_dfs: Implements recursive DFS to explore paths towards the target.

ids: Uses Iterative Deepening Search for pathfinding with a depth limit.

The program tracks the agent's position and logs each move until it reaches the target.
