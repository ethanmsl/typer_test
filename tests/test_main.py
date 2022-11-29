from typer_test import main

# a pytest test for the run() function in main
def test_run():
    assert main.run() == 0
