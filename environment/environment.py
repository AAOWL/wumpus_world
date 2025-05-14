from collections import defaultdict

from wumpus.environment.cell import Cell


class Environment:

    def __init__(self):
        self.cell_map = defaultdict(Cell)
