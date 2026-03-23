import pytest
from game import Platformer, WIDTH, HEIGHT
from PySide6.QtCore import Qt, QRect


class FakeEvent:
    def __init__(self, key):
        self._key = key

    def key(self):
        return self._key


@pytest.fixture
def game(qtbot):
    g = Platformer()
    qtbot.addWidget(g)
    return g


def test_initial_state(game):
    assert game.score == 0
    assert game.game_over is False
    assert game.on_ground is True
    assert len(game.obstacles) >= 1


def test_spawn_obstacle(game):
    initial_count = len(game.obstacles)
    game.spawn_obstacle()
    assert len(game.obstacles) == initial_count + 1


def test_jump_sets_velocity(game):
    event = FakeEvent(Qt.Key_Space)
    game.keyPressEvent(event)

    assert game.velocity_y < 0
    assert game.on_ground is False
    assert game.holding_jump is True


def test_release_space_stops_holding(game):
    press = FakeEvent(Qt.Key_Space)
    release = FakeEvent(Qt.Key_Space)

    game.keyPressEvent(press)
    game.keyReleaseEvent(release)

    assert game.holding_jump is False


def test_gravity_applies(game):
    game.velocity_y = 0
    game.game_loop()

    assert game.velocity_y > 0


def test_player_lands_on_ground(game):
    game.player.moveBottom(HEIGHT + 100)
    game.velocity_y = 10

    game.game_loop()

    assert game.on_ground is True
    assert game.velocity_y == 0


def test_collision_sets_game_over(game):
    game.obstacles = [QRect(game.player.x(), game.player.y(), 30, 50)]

    game.game_loop()

    assert game.game_over is True


def test_score_increases(game):
    score_before = game.score
    game.game_loop()

    assert game.score == score_before + 1


def test_restart_after_game_over(game):
    game.game_over = True
    game.score = 100

    event = FakeEvent(Qt.Key_R)
    game.keyPressEvent(event)

    assert game.game_over is False
    assert game.score == 0
