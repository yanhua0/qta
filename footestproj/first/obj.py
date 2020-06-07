import json


class server:
    def __init__(self):
        self.ttt = "123"


class obj:
    def __init__(self):
        self.server = server()
        self.age = None


if __name__ == '__main__':
    dict = {'age': 1233, "server": {"ttt": "test"}}

    for x in dict:
        print(x)

    obj = obj()
    obj.__dict__ = dict
    print(obj.__dict__)

    server = server()
    server.__dict__ = dict["server"]
    obj.server = server
    print(obj.server.ttt)
