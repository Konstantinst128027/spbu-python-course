import typing

def print_in_txt(message: str, log_file: str = "project/Task4/examples/example_game.txt") -> None:
    """
    Prints message to terminal and writes to log file
    """
    print(message)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(message + "\n")