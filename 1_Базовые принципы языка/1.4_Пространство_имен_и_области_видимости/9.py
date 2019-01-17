def create(namespace, parent):


def add(namespace, var):


def get(namespace, var):


n = int(input())

for i in range(n):
    cmd, namespace, argument = input().split()

    if cmd == "create":
        create(namespace, argument)

    elif cmd == "add":
        add(namespace, argument)

    elif cmd == "get":
        get(namespace, argument)

    

print(command)