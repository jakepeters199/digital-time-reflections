from main import is_reflectable, is_time_reflectable, is_time_valid, get_reflected_time


def test_is_digit_reflectable():
    assert(is_reflectable('0') is True)
    assert(is_reflectable('1') is False)
    assert(is_reflectable('2') is True)
    assert(is_reflectable('5') is True)


def test_is_time_reflectable():
    assert(is_time_reflectable('0005') is True)
    assert(is_time_reflectable('1005') is False)


def test_is_time_valid():
    assert(is_time_valid('0000') is True)
    assert(is_time_valid('8000') is False)


def test_get_reflected_time():
    assert(get_reflected_time('0000') == '0000')
    assert(get_reflected_time('0250') == '0250')
    assert(get_reflected_time('0500') == '0020')
