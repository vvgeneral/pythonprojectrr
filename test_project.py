from project import money, second_guess, slow_print
from unittest.mock import patch


def test_money():
    assert money(10000, 0) == 10000
    assert money(10000, 1) == 15000
    assert money(10000, 2) == 26250
    assert money(10000, 3) == 59062.5
    assert money(10000, 4) == 206718.75
    assert money(10000, 5) == 1033593.75


def test_second_guess():
    with patch('random.randint', return_value=1):
        with patch('builtins.input', side_effect=['y']):
            assert second_guess() == True

        with patch('builtins.input', side_effect=['n']):
            assert second_guess() == False

    with patch('random.randint', return_value=2):
        assert second_guess() == None

def test_slow_print(capfd):
    slow_print("Test message", 0.1, 0.1)
    captured = capfd.readouterr()
    assert captured.out == "Test message \n"
