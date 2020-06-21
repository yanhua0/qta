import json
def t(**json2):

    print(json2)
if __name__ == '__main__':
    d = [1, 2, 3]
    dd = []
    for _ in d:
        dd.append({'s': _})
dic = {'1': '2'}
data = json.dumps(dic)
t(json2=data)

