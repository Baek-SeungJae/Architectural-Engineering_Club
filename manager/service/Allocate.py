def Allocate_Studio_First(Team_X, Small_Space, Space_Place, Mu, Sof, Arch, Nothing, Club, Student_info):
    # 1지망이 Team_X일 때
    if Student_info[2] == Club[0]:
        Team_X.setConfirm(Student_info[1], Student_info[0])

    # 1지망이 Small_Space일 때
    elif Student_info[2] == Club[1]:
        Small_Space.setConfirm(Student_info[1], Student_info[0])

    # 1지망이 Space_Place일 때
    elif Student_info[2] == Club[2]:
        Space_Place.setConfirm(Student_info[1], Student_info[0])

    # 1지망이 Mu일 때
    elif Student_info[2] == Club[3]:
        Mu.setConfirm(Student_info[1], Student_info[0])

    # 1지망이 Sof일 때
    elif Student_info[2] == Club[4]:
        Sof.setConfirm(Student_info[1], Student_info[0])

    # 1지망이 Arch일 때
    elif Student_info[2] == Club[5]:
        Arch.setConfirm(Student_info[1], Student_info[0])

    # 1지망이 Nothing일 때
    elif Student_info[2] == Club[6]:
        Nothing.setConfirm(Student_info[1], Student_info[0])


def Allocate_Studio_Second_Third(Team_X, Small_Space, Space_Place, Mu, Sof, Arch, Club, Student_info):
    # 2지망이나 3지망이 Team_X일 때
    if Student_info[3] == Club[0] or Student_info[4] == Club[0]:

        if Student_info[3] == Club[0]:
            Team_X.setSecond(Student_info[1], Student_info[0])

        elif Student_info[4] == Club[0]:
            Team_X.setThird(Student_info[1], Student_info[0])

    # 2지망이나 3지망이 Small_Space일 때
    if Student_info[3] == Club[1] or Student_info[4] == Club[1]:

        if Student_info[3] == Club[1]:
            Small_Space.setSecond(Student_info[1], Student_info[0])

        elif Student_info[4] == Club[1]:
            Small_Space.setThird(Student_info[1], Student_info[0])

    # 2지망이나 3지망이 Space_Place일 때
    if Student_info[3] == Club[2] or Student_info[4] == Club[2]:

        if Student_info[3] == Club[2]:
            Space_Place.setSecond(Student_info[1], Student_info[0])

        elif Student_info[4] == Club[2]:
            Space_Place.setThird(Student_info[1], Student_info[0])

    # 2지망이나 3지망이 Mu일 때
    if Student_info[3] == Club[3] or Student_info[4] == Club[3]:

        if Student_info[3] == Club[3]:
            Mu.setSecond(Student_info[1], Student_info[0])

        elif Student_info[4] == Club[3]:
            Mu.setThird(Student_info[1], Student_info[0])

    # 2지망이나 3지망이 Sof일 때
    if Student_info[3] == Club[4] or Student_info[4] == Club[4]:

        if Student_info[3] == Club[4]:
            Sof.setSecond(Student_info[1], Student_info[0])

        elif Student_info[4] == Club[4]:
            Sof.setThird(Student_info[1], Student_info[0])

    # 2지망이나 3지망이 Arch일 때
    if Student_info[3] == Club[5] or Student_info[4] == Club[5]:

        if Student_info[3] == Club[5]:
            Arch.setSecond(Student_info[1], Student_info[0])

        elif Student_info[4] == Club[5]:
            Arch.setThird(Student_info[1], Student_info[0])