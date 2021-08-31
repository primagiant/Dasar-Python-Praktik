if __name__ == '__main__':
    arrList = []
    result = []
    for i in range(int(input())):
        arrList.append([])
        name = input()
        arrList[i].append(name)
        score = float(input())
        arrList[i].append(score)
    arrList = dict(arrList)
    minGrade = min(arrList.keys(), key=(lambda k: arrList[k]))
    # print(minGrade)
    arrList.pop(minGrade)
    minGrade = min(arrList.keys(), key=(lambda k: arrList[k]))
    print(minGrade)
    arrList.pop(minGrade)
    minGrade = min(arrList.keys(), key=(lambda k: arrList[k]))
    print(minGrade)
