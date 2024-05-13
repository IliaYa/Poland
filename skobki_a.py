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
