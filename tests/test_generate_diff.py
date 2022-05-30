import pytest
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize("first_file, second_file", [("./tests/fixtures/sample_json1.json",
                                                      "./tests/fixtures/sample_json2.json")])
def test_sample_json(first_file, second_file):
    with open('./tests/fixtures/sample_json_result.txt') as f:
        expected = f.read()

    actual = generate_diff(first_file, second_file, 'json')

    assert actual == expected


@pytest.mark.parametrize("first_file, second_file", [("./tests/fixtures/sample_yaml1.yaml",
                                                      "./tests/fixtures/sample_yaml2.yml")])
def test_yaml(first_file, second_file):
    with open('./tests/fixtures/sample_yaml_result.txt') as f:
        expected = f.read()

    actual = generate_diff(first_file, second_file)
    print(actual)

    assert actual == expected


@pytest.mark.parametrize("first_file, second_file", [("./tests/fixtures/inner_json1.json",
                                                      "./tests/fixtures/inner_json2.json")])
def test_stylish(first_file, second_file):
    with open('./tests/fixtures/inner_json_result.txt') as f:
        expected = f.read()

    actual = generate_diff(first_file, second_file)

    assert actual == expected


@pytest.mark.parametrize("first_file, second_file", [("./tests/fixtures/inner_json1.json",
                                                      "./tests/fixtures/inner_json2.json")])
def test_plain(first_file, second_file):
    with open('./tests/fixtures/inner_plain_result.txt') as f:
        expected = f.read()

    actual = generate_diff(first_file, second_file, 'plain')
    print(actual)

    assert actual == expected
