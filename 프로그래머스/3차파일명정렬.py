def solution(files):
    answer = []
    arr = []
    for file in files:
        head, number, tail = "", "", ""
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]
                print("number",number)
                for j in range(len(number)):
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break
                arr.append([head, number, tail])
                break

    x = sorted(arr, key=lambda x: (x[0].lower(), int(x[1])))
    print("arr",arr)
    for i in x:
        res = ''.join(i)
        answer.append(res)
    print(answer)
    return answer
solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])