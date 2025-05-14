from collections import defaultdict

from wumpus.types.location import Location


class KnowledgeBase:
    def __init__(self):
        self.visited = defaultdict(bool)
        self.possible_wumpus = defaultdict(int)
        self.possible_pit = defaultdict(int)

    def mark_visit(self, loc: Location) -> None:
        if not self.visited[loc]:
            self.visited[loc] = True

    def render_map(self, size: int, map_type: str) -> None:
        """
        size x size 크기의 텍스트 맵을 출력.
        map_type: "visited", "wumpus", "pit"
        """

        maps = {
            "visited": self.visited,
            "wumpus": self.possible_wumpus,
            "pit": self.possible_pit,
        }
        titles = {
            "visited": "Visited Map:",
            "wumpus": "Possible Wumpus Map:",
            "pit": "Possible Pit Map:",
        }
        if map_type not in maps:
            raise ValueError(
                f"Unknown map type: {map_type!r}. " f"Choose from {list(maps)}"
            )

        print("\n" + titles[map_type])
        target = maps[map_type]
        for r in range(size):
            row_vals = [f"{target[Location(r, c)]:2}" for c in range(size)]
            print(" ".join(row_vals))
