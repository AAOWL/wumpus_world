from dataclasses import dataclass


@dataclass
class Cell:
    has_wumpus: bool
    has_pit: bool
    has_gold: bool
    has_wall: bool
