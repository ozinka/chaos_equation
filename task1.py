

cnt = int(input('input data:\n'))
lst = input().split()

sm = 0
for i in lst:
    sm += int(i)
    cnt -= 1
    if cnt == 0:
        break

print('answer:')
print(sm)