from display import Display
from studentservice import StudentService


class Functionality:
    def __init__(self):
        self.student_service = StudentService()
        self.display = Display()

    def adding(self, adding_object):
        self.display.clear()
        if adding_object == "student":
            print("Please add the first and last name of the new student.")
            firstname = input("Firstname: ")
            lastname = input("Lastname: ")
            self.student_service.add_student(firstname, lastname)
            self.display.clear()
            print(f"Successfully added student '{firstname} {lastname}'")
            next_step = input("Do you want to return to the student menu, press '1'.\n"
                              "If you want to add another student, press '2'.\n->  ")
            return next_step
        elif adding_object == "professor":
            print("Please add the first and last name of the new professor.")
            firstname = input("Firstname: ")
            lastname = input("Lastname: ")
            self.student_service.add_student(firstname, lastname)
            self.display.clear()
            print(f"Successfully added professor '{firstname} {lastname}'")
            next_step = input("Do you want to return to the professor menu, press '1'.\n"
                              "If you want to add another professor, press '2'.\n->  ")
            return next_step
        else:
            pass

    def showing_all(self, showing_object):
        self.display.clear()
        if showing_object == "students":
            self.student_service.get_all_students()
            next_step = input("Do you want to return to the student menu? (y): ").lower()
            return next_step
        else:
            pass
