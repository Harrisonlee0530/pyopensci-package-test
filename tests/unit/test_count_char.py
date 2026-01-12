import pytest
from pyospackage_hli76_test.countchar.count_char import count_char


def test_count_char():

    string = "hello"
    expected = 5
    actual = count_char(string)
    assert actual == expected

    string = ""
    expected = 0
    actual = count_char(string)
    assert actual == expected

    string = "Python is cool"
    expected = 14
    actual = count_char(string)
    assert actual == expected


def test_count_char_wrong_input():
    with pytest.raises(TypeError):
        count_char(123)


@pytest.fixture
def text_data():
    file_path = "tests/unit/text.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines


# def test_line_1(text_data):
#     string = text_data[0].strip()
#     assert count_char(string) == 34


# def test_line_2(text_data):
#     string = text_data[1].strip()
#     assert count_char(string) == 10


# def test_line_3(text_data):
#     string = text_data[2].strip()
#     assert count_char(string) == 7


@pytest.mark.parametrize(
    "test_data_line_number, expected_count",
    [
        (0, 34),
        (1, 10),
        (2, 7)
    ]
)
def test_line_n(text_data, test_data_line_number, expected_count):
    string = text_data[test_data_line_number].strip()
    assert count_char(string) == expected_count