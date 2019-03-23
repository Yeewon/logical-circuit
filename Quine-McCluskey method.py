def solution(input_list):
    var=input_list[0]
    minterms = input_list[1]
    minterm_list = []
    for i in range(2,len(input_list)):
        minterm_list.append(input_list[i])

    # AND함수
    def Combine(var, a, b):  # 곱할 인수를 두개 받는다. var = 몇자리 수인지.
        combine = ''
        for i in range(var):
            if a[i] == b[i] == '1':
                combine += '1'
            elif (a[i] == '1' and b[i] == '0') or (a[i] == '0' and b[i] == '1') or (a[i] == b[i] == '-'):
                combine += '-'
            elif a[i] == b[i] == '0':
                combine += '0'
        return combine

    # 1's 의 갯수대로 나눠서 dictionary에 저장하는 함수 ( 그룹화 )
    def groupage(minterm_list):
        group = {}
        for i in range(len(minterm_list)):
            a = minterm_list[i].count('1')
            if a in group:
                group[a].append(minterm_list[i])
            else:
                group[a] = [minterm_list[i]]
        sorted(group)
        return group

    def solution(bi_list, var):
        for i in range(len(bi_list)):
            bi_list[i] = bi_list[i].replace("-", "2")
            bi_list[i] = int(bi_list[i])
        bi_list.sort()

        for i in range(len(bi_list)):
            bi_list[i] = str(bi_list[i])
            bi_list[i] = bi_list[i].replace("2", "-")

        for i in range(len(bi_list)):
            if len(bi_list[i]) != var:
                bi_list[i] = "0" * (var - len(bi_list[i])) + bi_list[i]

        return bi_list

    # 이진수로 바꾸기
    for i in range(minterms):
        minterm_list[i] = bin(minterm_list[i])

    # print(minterm_list)

    # var 크기로 나타내기
    for i in range(len(minterm_list)):
        minterm_list[i] = minterm_list[i][2:]
        if len(minterm_list[i]) != var:
            minterm_list[i] = '0' * (var - len(minterm_list[i])) + minterm_list[i]

    ##########################################
    # print(minterm_list)
    group = groupage(minterm_list)
    epi_group = groupage(minterm_list)
    # print()
    # print(group)
    ##########################################

    # tabular method algorithm
    i = 1
    cnt = 0
    while True:
        epi = []  # epi를 저장할 list
        key_list = list(group.keys())  # key의 값을 비교하기위해 key list를따로 만듦
        if len(key_list) > 1:
            for j in range(len(key_list) - 1):  # 하나 차이 나는 key의 value들을 비교해서 새로운 list에 저장
                if abs(key_list[j + 1] - key_list[j]) == 1:
                    x = group[key_list[j]]
                    y = group[key_list[j + 1]]
                    for m in x:
                        for n in y:
                            result = Combine(var, m, n)
                            if result.count('-') == i:
                                epi.append(result)
            i = i + 1
            cnt = cnt + 1
            # 중복 정리, 그룹화
            epi = list(set(epi))
            group = groupage(epi)
            # print(group)
        else:
            break

    # print(cnt)
    # print()

    if len(group) == 0:
        # print("epi는 없다.")
        i = 1
        for t in range(cnt - 1):
            epi = []  # epi를 저장할 list
            key_list = list(epi_group.keys())  # key의 값을 비교하기위해 key list를따로 만듦
            if len(key_list) > 1:
                for j in range(len(key_list) - 1):  # 하나 차이 나는 key의 value들을 비교해서 새로운 list에 저장
                    if abs(key_list[j + 1] - key_list[j]) == 1:
                        x = epi_group[key_list[j]]
                        y = epi_group[key_list[j + 1]]
                        for m in x:
                            for n in y:
                                result = Combine(var, m, n)
                                if result.count('-') == i:
                                    epi.append(result)
                i = i + 1
                # 중복 정리, 그룹화
                epi = list(set(epi))
                epi_group = groupage(epi)
                # print(epi_group)

        # key_list = list(epi_group.keys())

        final = list(epi_group.values())
        final_set = []

        # list of list -> list
        for i in range(len(final)):
            for j in range(len(final[i])):
                final_set.append(final[i][j])

        solution(final_set, var)

        print_list = []
        print_list.append("EPI")
        print_list.append("NEPI")
        for i in final_set:
            print_list.append(i)

        return print_list

    else:
        # print("epi는 있다.")
        # print(group)
        final = list(group.values())
        final_set = []

        # list of list -> list
        for i in range(len(final)):
            for j in range(len(final[i])):
                final_set.append(final[i][j])

            solution(final_set, var)

        print_list = []
        print_list.append("EPI")
        for i in final_set:
            print_list.append(i)
        print_list.append("NEPI")

        return print_list
