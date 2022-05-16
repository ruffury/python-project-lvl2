import pytest
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize("first_file, second_file", [("./tests/fixtures/sample_json1.json",
                                                      "./tests/fixtures/sample_json2.json")])
def test_boolean(first_file, second_file):
    with open('./tests/fixtures/sample_json_result.txt') as f:
        expected = f.read()

    actual = generate_diff(first_file, second_file)

    assert actual == expected


@pytest.mark.parametrize("first_file, second_file", [("./tests/fixtures/sample_yaml1.yaml",
                                                      "./tests/fixtures/sample_yaml2.yml")])
def test_yaml(first_file, second_file):
    with open('./tests/fixtures/sample_yaml_result.txt') as f:
        expected = f.read()

    actual = generate_diff(first_file, second_file)

    assert actual == expected


@pytest.mark.parametrize("first_file, second_file", [("./tests/fixtures/sample_yaml1.yaml",
                                                      "./tests/fixtures/sample_json2.json")])
def test_yaml_json(first_file, second_file):
    with open('./tests/fixtures/sample_yaml_json_result.txt') as f:
        expected = f.read()

    actual = generate_diff(first_file, second_file)

    assert actual == expected