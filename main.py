import sys
# import thermometer as t

# def get_temperature() -> float:
#     return t.read_temp()


if __name__ == '__main__':
    try:
        behaviour = sys.argv[1]
        if behaviour not in ["check", "log", "graph", "test"]:
            raise IndexError
    except IndexError:
        behaviour = "test"
    print(f"Running: {behaviour}")
