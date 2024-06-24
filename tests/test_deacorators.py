from src.decorators import log


def test_log(capsys):
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert "my_function ok" in captured.out

    try:
        my_function(0, "2")
    except TypeError:
        captured = capsys.readouterr()
        assert (
            "my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs:(1, '2'), {}"
            in captured.out
        )
