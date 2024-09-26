# Bubble Sort

equals = [2, 5, 4, 3]


def swap(x, y):
    equals[x], equals[y] = equals[y], equals[x]
    print(equals)


for i in range(len(equals)):
    for j in range(len(equals)):
        if equals[i] > equals[j]:
            # print(len(self.puzzle[equals[i]]), len(self.puzzle[equals[j]]))
            swap(i, j)

print("-----")

equals = [2, 5, 4, 3]
for i in range(len(equals)):
    for j in range(len(equals) - 1):
        if equals[j] < equals[j + 1]:
            # print(len(self.puzzle[equals[i]]), len(self.puzzle[equals[j]]))
            swap(j, j + 1)

print("-----")


def merge(s1, s2, s):
    print("mergiing for : -", s)
    i = j = 0

    while i + j < len(s):
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            print("less than", s1, s2)
            s[i + j] = s1[i]
            i += 1

        else:
            s[i + j] = s2[j]
            j += 1
            print("adding for j", s1, s2)


def mergeSort(s):
    print("for: ", s)
    n = len(s)
    if n < 2:
        return
    mid = n // 2
    s1 = s[0:mid]
    s2 = s[mid:n]
    print(s1, s2)

    mergeSort(s1)
    mergeSort(s2)

    print("merging", s1, s2, "of: ", s)
    merge(s1, s2, s)
    return s


equals = [2, 5, 4, 3]
print(mergeSort(equals))

x = []


def display(value):

    print(value)
    x.append(value)
    if value == 0:
        print(x)
        return
    display(value - 1)


display(10)
