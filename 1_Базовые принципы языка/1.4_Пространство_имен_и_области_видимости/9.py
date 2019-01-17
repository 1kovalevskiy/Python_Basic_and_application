def create(namespace, parent):
    dictionary[parent][2].append(namespace)
    dictionary[namespace] = [[], parent, []]
    return None

def add(namespace, var):
    dictionary[namespace][0].append(var)
    return None

def get(namespace, var):
    flag = 0
    if namespace != 'global':
        flag = dictionary[namespace][0].count(var)
        if flag > 0:
            print(namespace)
        else:
            get(dictionary[namespace][1], var)
    else:
        flag = dictionary[namespace][0].count(var)
        if flag > 0:
            print(namespace)
        else:
            print(None)
    return None

dictionary = {'global':[[], None, []]}
n = int(input())

for i in range(n):
    cmd, namespace, argument = input().split()

    if cmd == "create":
        create(namespace, argument)

    elif cmd == "add":
        add(namespace, argument)

    elif cmd == "get":
        get(namespace, argument)

    print(dictionary)
