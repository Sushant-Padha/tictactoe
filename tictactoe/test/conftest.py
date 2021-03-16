# this file is used to configure options for all other tests (using pytest)
import pytest


def pytest_addoption(parser):
    '''Add --play option to play game (in test_game.py)

    Args:
        parser
    '''
    parser.addoption(
        "--play", action="store_true", help="play sample game (in test_game.py)"
    )


@pytest.fixture
def play_cmdopt(request):
    return request.config.getoption("--play")
