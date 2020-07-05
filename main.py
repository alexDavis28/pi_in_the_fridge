import sys
import thermometer as t

def check():
    pass


def log():
    pass


def graph():
    pass


def test():
    pass


if __name__ == '__main__':
    try:
        behaviour = sys.argv[1]
        if behaviour not in ["check", "log", "graph", "test"]:
            raise IndexError
    except IndexError:
        behaviour = "test"

    if behaviour == "check":
        check()
    elif behaviour == "log":
        log()
    elif behaviour == "graph":
        graph()
    elif behaviour == "test":
        test()
    else:
        print("Huh, the behaviour wasn't found, sorry")
