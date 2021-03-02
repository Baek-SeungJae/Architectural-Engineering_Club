class Studio:

    # Studio 객체를 생성할시 Secon(2지망), Third(3지망), Confirm(유력 후보) 멤버를 만든다.
    def __init__(self):
        self.Second = {}
        self.Third = {}

        self.Confirm = {}


    # 1지망 및 유력 후보들을 Confirm 멤버에 저장한다.
    def setConfirm(self, Student_Id, Student_Name):
        self.Confirm[Student_Id] = Student_Name

    # 2지망에 지원한 학생들을 Second 멤버에 저장한다.
    def setSecond(self, Student_Id, Student_Name):
        self.Second[Student_Id] = Student_Name

    # 3지망에 지원한 학생들을 Third 멤버에 저장한다.
    def setThird(self, Student_Id, Student_Name):
        self.Third[Student_Id] = Student_Name

    # 유력 후보에서 지운다
    def delStudent(self, Student_Id):
        del self.Confirm[Student_Id]

    # 2지망에서 지운다
    def delSecond(self, Student_Id):
        del self.Second[Student_Id]

    # 3지망에서 지운다
    def delThird(self, Student_Id):
        del self.Third[Student_Id]