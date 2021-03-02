import random


# 각 작업실에 할당된 유력 후보들이 최소 인원보다 많은지 검사
# 하나의 작업실이라도 최소 인원보다 적으면, True값을 리턴한다.
def Check_Min(Studio, Min_Member):
    if len(Studio[0]) < Min_Member or len(Studio[1]) < Min_Member or len(Studio[2]) < Min_Member or len(Studio[3]) < Min_Member or len(Studio[4]) < Min_Member or len(Studio[5]) < Min_Member:
        return True
    else:
        return False


# 2지망으로 최소인원을 보유한 작업실에 지원한 학생들과, 최대 인원을 보유한 작업실의 학생들의 정보를 비교
def Check_Second_Studio(Max_Studio_Confirm_Info, Min_Studio_Second_Info):
    temp = []

    choice = []

    ch = False

    for i in Min_Studio_Second_Info:

        for j in Max_Studio_Confirm_Info:

            if i == j:
                # 2지망을 조사하여, 최대 인원수를 가진 작업실의 유력후보와 같은 정보를 가졌다면, ch를 True로 변환하고, 그 정보를 temp에 추가한다.
                ch = True
                temp.append([i, Min_Studio_Second_Info.get(i)])

    if ch == True:

        # 2지망을 조사하여, 최대 인원수를 가진 작업실의 유력후보와 같은 정보를 가진 사람이 1명을 초과할 경우 랜덤으로 고른다.
        if len(temp) > 1:
            choice = random.choice(temp)

        # 2지망을 조사하여, 최대 인원수를 가진 작업실의 유력후보와 같은 정보를 가진 사람이 1명일 경우 그대로 반환한다.
        else:
            choice = temp[0]

        return choice

    # 2지망을 조사하여, 최대 인원수를 가진 작업실의 유력후보와 같은 정보를 가진사람이 한명도 없다면, False를 반환하라.
    else:
        return False


# 2지망으로 최소인원을 보유한 작업실에 지원한 학생들과, 최대 인원을 보유한 작업실의 학생들의 정보를 비교
def Check_Third_Studio(Max_Studio_Confirm_Info, Min_Studio_Third_Info):
    temp = []

    choice = []

    ch = False

    for i in Min_Studio_Third_Info:

        for j in Max_Studio_Confirm_Info:

            if i == j:
                # 3지망을 조사하여, 최대 인원수를 가진 작업실의 유력후보와 같은 정보를 가졌다면, ch를 True로 변환하고, 그 정보를 temp에 추가한다.
                ch = True
                temp.append([i, Min_Studio_Third_Info.get(i)])

    if ch == True:

        # 3지망을 조사하여, 최대 인원수를 가진 작업실의 유력후보와 같은 정보를 가진 사람이 1명을 초과할 경우 랜덤으로 고른다.
        if len(temp) > 1:
            choice = random.choice(temp)

        # 3지망을 조사하여, 최대 인원수를 가진 작업실의 유력후보와 같은 정보를 가진 사람이 1명일 경우 그대로 반환한다.
        else:
            choice = temp[0]

        return choice

    # 3지망을 조사하여, 최대 인원수를 가진 작업실의 유력후보와 같은 정보를 가진사람이 한명도 없다면, False를 반환하라.
    else:
        return False