from dataclasses import dataclass


@dataclass(frozen=True)
class Percept:
    stench: bool = False
    breeze: bool = False
    glitter: bool = False
    scream: bool = False
