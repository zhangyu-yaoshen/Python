
from random import randint

class Stu:

    def __init__(self, num, name, address):
        self.num = num
        self.name = name
        self.address = address
        self.course_list = []

    def add_course(self, course):
        self.course_list.append(course)

    def show(self):
        print("学生姓名:%s" % self.name)
        for c in self.course_list:
            print("选的课程是:%s" % c.name)
            if c.teacher:
                print("授课老师的电话:%s" % (c.teacher.tel))
            else:
                print("该课程还没有老师")

    def check(self):
        # 1.显示所有课程.
        # 2.选课
        # 3.添加到列表中
        pass

class Course:

    def __init__(self, num, name, teacher=None):
        # if teacher != None and isinstance(teacher, Teacher):
            self.num = num
            self.name = name
            self.teacher = teacher
        # else:
        #     raise Exception()

    def set_teacher(self, teacher):
        self.teacher = teacher

    def show(self):
        if self.teacher:
            print("课程的名称是:%s, 授课老师是:%s" % (self.name, self.teacher.name))
        else:
            print("课程的名称是:%s, 授课老师是:%s" % (self.name, "无"))

class Teacher(object):

    def __init__(self, id, name, tel):
        self.id = id
        self.name = name
        self.tel = tel



c1 = Course(1, "体育课")
c2 = Course(2, "生物课")
c3 = Course(3, "历史课")
c4 = Course(4, "思想品德课")
c5 = Course(5, "电子竞技课")
c6 = Course(6, "python课")

t1 = Teacher(1, "周杰伦", 11111)
t2 = Teacher(2, "彭于晏", 11112)
t3 = Teacher(3, "林更新", 11113)
t4 = Teacher(4, "吴彦祖", 11114)
t5 = Teacher(5, "周星驰", 11115)
t6 = Teacher(6, "alex", 11116)

c1.set_teacher(t1)
c2.set_teacher(t2)
c3.set_teacher(t3)
c4.set_teacher(t4)
c5.set_teacher(t5)
c6.set_teacher(t6)

c_lst = [c1, c2, c3, c4, c5, c6]

stu_lst = []

for i in range(30):
    stu = Stu(i,"Stu%s" % i,"美丽富饶的沙河")

    s = set()
    while len(s) < 3:
        s.add(randint(0, 5))
    for index in s:
        stu.add_course(c_lst[index]) # 你选的课

    stu_lst.append(stu)

for stu in stu_lst:
    stu.show()
