from src.new_class import NewClass


def test_new_class():

    instance = NewClass()
    assert instance.a == 1
