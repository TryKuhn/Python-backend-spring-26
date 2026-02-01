import pathlib

import pytest
from advanced.seminars.materials.task2_sem1 import User, Item, Health


def test_user_update_health():
    user = User(nickname="try_kuhn", strength=3, agility=7, intelligence=8, luck=1, health=20, experience=0)
    assert user.health == 20

    user.health = 15
    assert user.health == 15

def test_health_remove_count():
    item = Health(id=1, count=10, path_to_image=pathlib.Path("path/to/image"), health_points=5)

    assert item.count == 10

    item.remove_count(3)
    assert item.count == 7

    with pytest.raises(ValueError):
        item.remove_count(8)

    with pytest.raises(ValueError):
        item.remove_count(-2)
