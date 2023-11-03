from main import append


def test_append():
    assert append(1) == [1]
    assert append(2, [3, 4]) == [3, 4, 2]
    assert append(3) == [3]
