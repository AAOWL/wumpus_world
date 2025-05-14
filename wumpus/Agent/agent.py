from wumpus.Types.location import Location, Direction
from wumpus.Agent.KnowledgeBase import KnowledgeBase


class Agent:
    loc: Location
    dir: Direction
    KB: KnowledgeBase

    arrows: int
    has_gold: bool
