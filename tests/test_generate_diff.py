import pytest
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize("first_file, second_file", [("./tests/fixtures/different_value1.json",
                                                      "./tests/fixtures/different_value2.json")])
def test_different_value(first_file, second_file):
    with open('./tests/fixtures/different_value_result.txt') as f:
        expected = f.read()

    actual = generate_diff(first_file, second_file)

    assert actual == expected


@pytest.mark.parametrize("first_file, second_file", [("./tests/fixtures/boolean1.json",
                                                      "./tests/fixtures/boolean2.json")])
def test_boolean(first_file, second_file):
    with open('./tests/fixtures/boolean_result.txt') as f:
        expected = f.read()

    actual = generate_diff(first_file, second_file)

    assert actual == expected


@pytest.mark.parametrize("first_file, second_file", [("./tests/fixtures/same_json1.json",
                                                      "./tests/fixtures/same_json2.json")])
def test_same_json(first_file, second_file):
    with open('./tests/fixtures/same_json_result.txt') as f:
        expected = f.read()

    actual = generate_diff(first_file, second_file)

    assert actual == expected
