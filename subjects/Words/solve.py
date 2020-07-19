def words():
    st = input()
    lst = st.split()

    dic = {}
    for s in lst:
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1

    n = 0
    m = ""
    for j in dic:
        if (dic[j] > n):
            n = dic[j]
            m = j
    print(m)

if __name__ == "__main__":
    words()
