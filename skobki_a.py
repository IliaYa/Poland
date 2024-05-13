'''
def check(expr) :
    arr = []
    for c in expr:
        if c in ["(", "{", "["]:
            arr.append(c)
        else:
            if not arr:
                return 'no'
            cur_c = arr.pop()
            if cur_c == '(':
                if c != ")":
                    return 'no'
            if cur_c == '{':
                if c != "}":
                    return 'no'
            if cur_c == '[':
                if c != "]":
                    return 'no'
    if arr:
        return 'no'
    return 'yes'


print(check(input()))
'''

input()
a = list(input())
b = []
for x in a:
    if len(b) == 0:
        b.append(x)
    else:
        if b[-1] == "(" and x == ")":
            b.pop()
        elif b[-1] == "[" and x == "]":
            b.pop()
        elif b[-1] == "{" and x == "}":
            b.pop()
        else:
            b.append(x)
if len(b) == 0:
    print("Yes")
else:
    print("No")