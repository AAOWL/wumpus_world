from __future__ import annotations
from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    NORTH = (-1, 0)
    EAST = (0, +1)
    SOUTH = (+1, 0)
    WEST = (0, -1)


@dataclass(frozen=True)
class Location:
    row: int
    col: int

    def move(self, direction: Direction) -> Location:
        dr, dc = direction.value
        return Location(self.row + dr, self.col + dc)
