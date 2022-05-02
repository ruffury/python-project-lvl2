from gendiff import generate_diff
from gendiff.scripts import gendiff_main
import pytest


def test_same_json():
    with open('tests/fixtures/same_json_result.txt') as f:
        result_string = f.read()

    assert generate_diff(
        'tests/fixtures/same_json1.json',
        'tests/fixtures/same_json2.json'
    ) == result_string


def test_different_value():
    with open('tests/fixtures/different_value_result.txt') as f:
        result_string = f.read()

    assert generate_diff(
        'tests/fixtures/different_value1.json',
        'tests/fixtures/different_value2.json'
    ) == result_string


def test_boolean():
    with open('tests/fixtures/boolean_result.txt') as f:
        result_string = f.read()

    assert generate_diff(
        'tests/fixtures/boolean1.json',
        'tests/fixtures/boolean2.json'
    ) == result_string


@pytest.mark.parametrize("first_file, second_file", [("tests/fixtures/same_json1.json", "tests/fixtures/same_json2.json")])
def test_gendiff_cli(capsys, first_file, second_file):
    with open('tests/fixtures/same_json_result_cli.txt') as f:
        result_string = f.read()

    try:
        gendiff_main.main([first_file, second_file])
    except SystemExit:
        pass

    output = capsys.readouterr().out
    assert output == result_string


@pytest.mark.parametrize("option", ("-h", "--help"))
def test_help(capsys, option):
    with open('tests/fixtures/gendiff_help.txt') as f:
        result_string = f.read()

    try:
        gendiff_main.main([option])
    except SystemExit:
        pass

    output = capsys.readouterr().out
    assert output == result_string
