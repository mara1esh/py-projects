'''''
Implement a program that will emulate the work with namespaces. You need to implement support for creating namespaces and adding variables to them.

In this task, each namespace has a unique text identifier - its name.

Your program receives the following queries:

create <namespace> <parent> - create a new namespace named <namespace> inside the space <parent>
add <namespace> <var> - add a variable <var> to the <namespace>
get <namespace> <var> - get the name of the space from which the <var> variable will be taken when requested from the <namespace> space, or None if no such space exists
''''''

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
