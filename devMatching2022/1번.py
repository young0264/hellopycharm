def solution(registered_list, new_id):
    answer = ''
    s = set(registered_list)

    def makeSN(id):
        S, N = '', '0'
        print(id)
        id = list(id)
        for i in id:
            if 97 <= ord(i) <= 122:
                S += i
            else:
                N += i

        N = str(int(N)+1)
        print("N",N)
        n_id = S+N
        return n_id

    while True:
        if new_id in s:
            new_id = makeSN(new_id)

        else:
            return new_id
registered_list = ["bird98","bird99","cow2"]
new_id = "bird98"
print(solution(registered_list, new_id))
