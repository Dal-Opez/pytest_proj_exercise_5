from utils import dicts

data = {
    "1": "one",
    "2": "two",
    "3": "three"
}

def test_get_val():
    assert dicts.get_val(data, "1") == "one"
    assert dicts.get_val(data, "4") == "git"
    assert dicts.get_val(data, "5", "error") == "error"

