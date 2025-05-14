# pylint: disable=unused-import
"""print test"""
import pytest
from wumpus.agent.KnowledgeBase import KnowledgeBase
from wumpus.types.location import Location


def test_render_map_output(capsys):
    kb = KnowledgeBase()
    # 예시 데이터 설정
    kb.mark_visit(Location(2, 2))
    kb.possible_wumpus[Location(1, 1)] = 1
    kb.possible_pit[Location(3, 3)] = 3

    # 맵 출력 호출
    for typ in ("visited", "wumpus", "pit"):
        kb.render_map(size=6, map_type=typ)

    # 출력 캡처
    captured = capsys.readouterr().out

    expected_visited = """Visited Map:
 0  0  0  0  0  0
 0  0  0  0  0  0
 0  0  1  0  0  0
 0  0  0  0  0  0
 0  0  0  0  0  0
 0  0  0  0  0  0
"""
    expected_wumpus = """Possible Wumpus Map:
 0  0  0  0  0  0
 0  1  0  0  0  0
 0  0  0  0  0  0
 0  0  0  0  0  0
 0  0  0  0  0  0
 0  0  0  0  0  0
"""
    expected_pit = """Possible Pit Map:
 0  0  0  0  0  0
 0  0  0  0  0  0
 0  0  0  0  0  0
 0  0  0  3  0  0
 0  0  0  0  0  0
 0  0  0  0  0  0
"""
    assert expected_visited in captured
    assert expected_wumpus in captured
    assert expected_pit in captured
