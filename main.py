import sys
import tasks

if __name__ == '__main__':
    try:
        behaviour = sys.argv[1]
        if behaviour not in ["check", "log", "graph", "test", "ping"]:
            raise IndexError
    except IndexError:
        behaviour = "test"

    if behaviour == "check":
        tasks.check()
    elif behaviour == "log":
        tasks.log()
    elif behaviour == "graph":
        tasks.graph()
    elif behaviour == "test":
        tasks.test()
    elif behaviour == "ping":
        tasks.ping()
    else:
        print("Huh, the behaviour wasn't found, sorry")
