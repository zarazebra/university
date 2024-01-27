from display import Display
from studentrepository import StudentRepository


class StudentService:  # TODO: class for each entity, e.g. function_student, function_prof
    def __init__(self):
        self.student_repository = StudentRepository()
        self.display = Display()

    def showing_all_students(self):
        self.display.clear()
        all_students = self.student_repository.get_all_students()
        student_info = [(info.id, info.first_name, info.last_name) for info in all_students]
        self.display.print_table(
            table_title="List of all students",
            column_titles=["ID", "First Name", "Last Name"],
            row_values=student_info
        )
        next_step = input("Do you want to return to the student menu? (y): ").lower()
        return next_step

    def adding_student(self):
        self.display.clear()
        print("Please add the first and last name of the new student.")
        firstname = input("Firstname: ")
        lastname = input("Lastname: ")
        self.student_repository.add_student(firstname, lastname)
        self.display.clear()
        print(f"Successfully added student '{firstname} {lastname}'")
        next_step = input("Do you want to return to the student menu, press '1'.\n"
                          "If you want to add another student, press '2'.\n->  ")
        return next_step

    def editing_student(self):
        self.display.clear()
        print("Please provide the student ID of the student you want to edit and the new details.")
        student_id = int(input("Student ID: "))
        firstname = input("First name: ")
        lastname = input("Last name:")
        self.student_repository.edit_student(student_id, firstname, lastname)
        self.display.clear()
        print(f"Successfully changed Student with ID '{student_id}' to '{firstname} {lastname}'.")
        next_step = input("Do you want to return to the student menu, press '1'.\n"
                          "If you want to edit another student, press '2'.\n->  ")
        return next_step

    def deleting_student(self):
        self.display.clear()
        print("Please provide the student ID of the student you want to delete from the database.")
        student_id = int(input("Student ID: "))
        self.student_repository.delete_student(student_id)
        self.display.clear()
        print(f"Successfully deleted the student from the database.")
        next_step = input("Do you want to return to the student menu, press '1'.\n"
                          "If you want to delete another student from the database, press '2'.\n->  ")
        return next_step


