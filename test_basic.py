
from src.main import run
def test_run(tmp_path, capsys):
    # run and capture output (function writes file in CWD)
    # use tmp_path as CWD
    import os
    cwd = os.getcwd()
    try:
        os.chdir(tmp_path)
        run("TestUser")
        captured = capsys.readouterr()
        assert "Hello, TestUser!" in captured.out
        assert (tmp_path / "output.txt").exists()
    finally:
        os.chdir(cwd)
