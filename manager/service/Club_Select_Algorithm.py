import random
import pandas as pd

from .Check import Check_Min, Check_Second_Studio, Check_Third_Studio
from .Studio import Studio
from .Allocate import Allocate_Studio_First, Allocate_Studio_Second_Third

class Club_Select_Algorithm:
    def run(self, i):
        Team_X = Studio()
        Small_Space = Studio()
        Space_Place = Studio()
        Mu = Studio()
        Sof = Studio()
        Arch = Studio()
        Nothing = Studio()
        Studio_List = []
        # 작업실 최소 인원
        Min_Member = int(i)

        # 각 작업실별에 특정 키값을 선언해 딕셔너리를 선언
        Club = {0: "Team_X", 1: "Small_Space", 2: "Space_Place",
                3: "Mu", 4: "Sof", 5: "Arch", 6: "Nothing"}

        # 딕셔너리 Club에서 밸류 값만 추출해서 리스트로 저장
        Club_Value = list(Club.values())

        # 신입생들이 지원한 작업실데이터를 불러옴
        New_Students = pd.read_csv(
            'static/csv/result.csv', encoding='CP949')
        New_Students_List = New_Students.values.tolist()
        # 각 신입생을 1지망에 넣기

        for i in New_Students_List:
            Allocate_Studio_First(Team_X, Small_Space, Space_Place, Mu, Sof, Arch, Nothing, Club, i)

        # 작업실들을 List in List 형태로 만들기
        Studio_Confirm_List = [Team_X.Confirm, Small_Space.Confirm, Space_Place.Confirm, Mu.Confirm, Sof.Confirm,
                               Arch.Confirm, Nothing.Confirm]

        Studio_List = [Team_X, Small_Space, Space_Place, Mu, Sof, Arch]
        # 각 신입생을 2지망 및 3지망에 넣기
        for i in New_Students_List:
            Allocate_Studio_Second_Third(Team_X, Small_Space, Space_Place, Mu, Sof, Arch, Club, i)
        # 만약 특정 작업실이 최소인원을 못채웠을 경우 실행
        if Check_Min(Studio_Confirm_List, Min_Member):

            cnt = 0

            # 최소 인원을 채울 때까지 반복한다.
            while Check_Min(Studio_Confirm_List, Min_Member):

                # 무한 루프에 빠지지 않기 위해 카운트를 해준다
                cnt = cnt + 1

                # 최소 인원을 다 채웠을 경우 True로 변환
                ch = False

                # 루프문을 900번을 돌렸는데 정렬이 되지 않았다면, 강제로 멈춘다.
                if cnt == 900:
                    break

                # 각 작업실에 배치된 유력 후보가 몇명인지 리스트 형태로 만들어준다.
                Studio_Number_List = [len(Team_X.Confirm), len(Small_Space.Confirm), len(Space_Place.Confirm),
                                      len(Mu.Confirm), len(Sof.Confirm), len(Arch.Confirm)]

                # 가장 많은 유력 후보를 가진 작업실들을 추출한다.
                max_list = [i for i, j in enumerate(Studio_Number_List) if j == max(Studio_Number_List)]

                # 가장 적은 유력 후보를 가진 작업실들을 추출한다.
                min_list = [i for i, j in enumerate(Studio_Number_List) if j == min(Studio_Number_List)]

                # 최소 인원의 유력 후보를 가진 작업실을 무작위로 추출한다.
                min_Studio = Studio_List[random.choice(min_list)]

                # 최대 인원의 유력 루보를 가진 작업실을 무작위로 추출한다.
                max_Studio = Studio_List[random.choice(max_list)]

                # 최대 인원 수를 가진 작업실의 유력 후보 중에서 2지망으로 최소 인원을 보유한 작업실에 지원한 학생이 있는지 조사.
                random_Choice = Check_Second_Studio(max_Studio.Confirm, min_Studio.Second)

                # 최대 인원 수를 가진 작업실의 유력 후보중 2지망으로 최소 인원을 보유한 작업실에 지원한 학생이 있을 경우 실행
                if random_Choice != False:
                    max_Studio.delStudent(random_Choice[0])
                    min_Studio.setConfirm(random_Choice[0], random_Choice[1])
                    min_Studio.delSecond(random_Choice[0])

                    ch = True

                # 최대 인원 수를 가진 작업실의 유력 후보 중 2지망으로 최소 인원을 보유한 작업실에 지원한 학생이 없을 경우 살행
                elif random_Choice == False:

                    # 최대 인원 수를 가진 작업실의 유력후보 중 3지망으로 최소 인원을 보유한 작업실에 지원한 학생을 조사한다.
                    random_Choice = Check_Third_Studio(max_Studio.Confirm, min_Studio.Third)

                    # 최대 인원 수를 가진 작업실의 유력후보 중 3지망으로 최소 인원을 보유한 작업실에 지원한 학생이 있을 경우 실행
                    if random_Choice != False:
                        max_Studio.delStudent(random_Choice[0])
                        min_Studio.setConfirm(random_Choice[0], random_Choice[1])
                        min_Studio.delThird(random_Choice[0])

                        ch = True

                # 최대 인원 수를 가진 작업실의 유력 후보들을 다 조사했지만, 최소인원을 못채웠을 경우 실행한다.
                if Check_Min(Studio_Confirm_List, Min_Member) and ch == False:

                    # 가장 많은 유력 후보들을 가진 작업실 순서로 재 배치한다.
                    Sorted_Studio = sorted(Studio_List, key=lambda Studio: len(Studio.Confirm), reverse=True)

                    # 재 배치한 자료 순서를 바탕으로 모든 작업실에 대해서
                    # 2지망으로 최소 인원을 보유한 작업실에 지원한 학생과
                    # 3지망으로 최소 인원을 보유한 작업실에 지원한 학생을 조사한다.
                    for Sorted_Studio_Info in Sorted_Studio:
                        ch = False

                        for Confirm_Info in Sorted_Studio_Info.Confirm:

                            # 만약에 2지망으로 최소인원을 보유한 작업실에 지원한 사람이 아직 있을 경우 실행
                            if len(min_Studio.Second) != 0:

                                # 2지망으로 최소 인원을 보유한 작업실에 지원한 사람을 한명씩 조사
                                for Second_Info in min_Studio.Second:

                                    # 일치하는 정보를 찾으면 학생 정보를 이동시킨다.
                                    if Confirm_Info == Second_Info:
                                        min_Studio.setConfirm(Confirm_Info, Sorted_Studio_Info.Confirm[Confirm_Info])

                                        Sorted_Studio_Info.delStudent(Confirm_Info)

                                        min_Studio.delSecond(Confirm_Info)

                                        ch = True

                                        break

                            # 만약에 2지망으로 최소인원을 보유한 작업실에 지원한 사람이 없을 경우 실행
                            elif len(min_Studio.Second) == 0:

                                # 3지망으로 최소 인원을 보유한 작업시레 지원한 사람을 한명씩 조사
                                for Third_Info in min_Studio.Second:

                                    # 일치하는 정보를 찾으면 학생 정보를 이동시킨다.
                                    if Confirm_Info == Third_Info:
                                        min_Studio.setConfirm(Confirm_Info, Sorted_Studio_Info.Confirm[Confirm_Info])

                                        Sorted_Studio_Info.delStudent(Confirm_Info)

                                        min_Studio.delThird(Confirm_Info)

                                        ch = True

                                        break

                            if ch == True:
                                break

                        if ch == True:
                            break
        return {
            "Team_X": Team_X.Confirm,
            "Small_Space": Small_Space.Confirm,
            "Space_Place": Space_Place.Confirm,
            "Mu": Mu.Confirm,
            "Sof": Sof.Confirm,
            "Arch": Arch.Confirm,
            "Nothing": Nothing.Confirm
        }
