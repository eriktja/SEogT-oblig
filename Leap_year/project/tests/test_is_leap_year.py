from project.leap_year.is_leap_year import is_leap_year, is_one_hundred, is_four_hundred


def test_is_4_leap_year():
    assert is_leap_year(4) == True


def test_is_400_leap_year():
    assert is_leap_year(400) == True


def test_is_2000_leap_year():
    assert is_leap_year(2000) == True


def test_is_100_not_leap_year():
    assert is_one_hundred(300) == True


def test_is_four_hundred_function_return_zero():
    assert is_four_hundred(400) == 0


def test_is_500_hundred_not_leap_year():
    assert is_leap_year(500) == False
