from vell import spell


def test_import():
    assert 'check' in spell.__dict__.keys()


def test_check():
    spell.check()
