dic = {'global':{'parent' : 'None', 'vars':[]}}

def create(_namespace, _parent):
    dic[_namespace] = {'parent': _parent, 'vars': []}

def add(_namespace,_var):
    dic[_namespace]['vars'].append(_var)

def get(_namespace, _var):
    for i in dic[_namespace]['vars']:
        if _var in dic[_namespace]['vars']:
            return _namespace
    else:
        if dic[_namespace]['parent'] == 'None':
            return dic[_namespace]['parent']
        _namespace = dic[_namespace]['parent']
        return get(_namespace, _var)  

n = int(input())
while n !=0:
    x = input().split()
    if(x[0] == 'create'): create(x[1],x[2])
    if(x[0] == 'add'): add(x[1],x[2])
    if(x[0] == 'get'): print(get(x[1],x[2]))
    n-=1
