from wumpus.types.location import Location, Direction
from wumpus.agent.KnowledgeBase import KnowledgeBase


class Agent:
    loc: Location
    dir: Direction
    KB: KnowledgeBase

    arrows: int
    has_gold: bool
