from wumpus.agent.KnowledgeBase import KnowledgeBase
from wumpus.types.location import Location


def main():
    kb = KnowledgeBase()

    # 예시 데이터
    kb.mark_visit(Location(2, 2))
    kb.possible_wumpus[Location(1, 1)] = 1
    kb.possible_pit[Location(3, 3)] = 3

    for typ in ("visited", "wumpus", "pit"):
        kb.render_map(size=6, map_type=typ)


if __name__ == "__main__":
    main()
