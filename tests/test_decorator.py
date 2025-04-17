import pytest

from src.decorator import log


@log()
def successful_function():
    return "Success"


@log()
def failing_function():
    raise ValueError("Test error")


# Проверяем на возрат нужного значения
def test_successful_execution(capsys):
    result = successful_function()
    captured = capsys.readouterr()

    assert result == "Success"
    assert captured.out == "successful_function ok\n"


# Проверяем ошибку
def test_failing_execution(capsys):
    with pytest.raises(ValueError):
        failing_function()

    captured = capsys.readouterr()
    assert "failing_function, Test error: <<ValueError>> Inputs: (), {}" in captured.out


# Туст на то, что  функция правильно возращает имя
def test_function_name_preserved():
    assert successful_function.__name__ == "successful_function"
    assert failing_function.__name__ == "failing_function"


# Проверяем, что строка втретилась ровно три раза
def test_multiple_calls_logging(capsys):
    for i in range(3):
        successful_function()

    captured = capsys.readouterr()
    assert captured.out.count("successful_function ok")
