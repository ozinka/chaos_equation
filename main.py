brkts = ["{}", "[]", "()", "<>"]


def clean(st):
    res = ""
    for i in st:
        if i in ''.join(brkts):
            res = res + i
    return res


def rm(st_in: str):
    replaced = True
    st = st_in
    while replaced:
        replaced = False
        for i in brkts:
            if st != st.replace(i, ''):
                st = st.replace(i, '')
                replaced = True
    return st


def chk(st_in):
    return str(int(not bool(rm(clean(st_in)))))


st_lst = []
cnt = int(input('input data:\n'))
while cnt:
    st_lst.append(input())
    cnt -= 1

print('answer:')
ans = []
for i in st_lst:
    ans.append(chk(i))

print(' '.join(ans))
