import json
from teacher import Teacher


class Teachers:
    def __init__(self):
        try:
            with open("teachers.json") as f:
                teachers_list = json.load(f)

                self.teachers = []
                for teacher_dict in teachers_list:
                    t = Teacher()
                    t.from_dict(teacher_dict)
                    self.teachers += [t]

        except FileNotFoundError:
            self.teachers = []

    def save_teachers_data(self):
        list_to_write = []
        for teacher in self.teachers:
            list_to_write += [teacher.to_dict()]

        with open("teachers.json", "w") as f:
            json.dump(list_to_write, f)

    def next_id(self):
        if self.teachers == []:
            return 1001
        else:
            ids = []
            for t in self.teachers:
                ids.append(t.teacher_id)
            return max(ids) + 1

    def create_teacher(self, first_name, surname):
        for teacher in self.teachers:
            if teacher.first_name == first_name and teacher.surname == surname:
                print("This teacher already exists.")
                return None

        t = Teacher(first_name, surname, self.next_id())
        self.teachers.append(t)
        return t

    def read_teacher_by_id(self, teacher_id):
        for teacher in self.teachers:
            if teacher_id == teacher.teacher_id:
                return teacher
        else:
            return None

    def update_teacher(self, teacher_id):
        for teacher in self.teachers:
            if teacher_id == teacher.teacher_id:
                print(teacher)
                choice = int(input("1-Update first name, 2-Update surname: "))
                if choice == 1:
                    teacher.first_name = input("Give new first name: ")
                elif choice == 2:
                    teacher.surname = input("Give new surname: ")
                return

    def delete_teacher(self, teacher_id, lessons):                    # def delete_teacher(self, teacher_id):
        for i in range(len(self.teachers)):                           #   for teacher in self.teachers:
            if teacher_id == self.teachers[i].teacher_id:             #       if teacher_id == self.teachers.teacher_id:
                self.teachers.pop(i)                                  #           self.teachers.remove(teacher)
                for lesson in lessons.lessons:
                    if teacher_id in lesson.teacher_ids:
                        lesson.teacher_ids.remove(teacher_id)
                return
            else:
                print("No teacher with this id!!!")
