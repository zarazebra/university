from display import Display
from studentrecordrepository import StudentRecordRepository


class StudentRecordService:
    def __init__(self):
        self.studentrecord_repository = StudentRecordRepository()
        self.display = Display()

    def showing_all_studentrecords(self):
        self.display.clear()
        all_studentrecords = self.studentrecord_repository.get_all_studentrecords()
        studentrecord_info = [
            (str(info.id),
             str(info.student.first_name),
             str(info.student.last_name),
             str(info.course.subject.title),
             str(info.course.professor.first_name),
             str(info.course.professor.last_name),
             str(info.grade))
            for info in all_studentrecords
        ]
        self.display.print_table(
            table_title="List of all studentrecords",
            column_titles=[
                "ID",
                "Student First Name",
                "Student Last Name",
                "Subject Title",
                "Professor First Name",
                "Professor Last Name",
                "Grade"],
            row_values=studentrecord_info
        )
        next_step = input("Do you want to return to the studentrecord menu? (y): ").lower()
        return next_step

    def adding_studentrecord(self):
        self.display.clear()
        print("Please add the details of the new studentrecord.")
        course_id = int(input("Course ID: "))
        student_id = int(input("Student ID: "))
        self.studentrecord_repository.add_studentrecord(student_id=student_id, course_id=course_id)
        self.display.clear()
        print(f"Successfully added studentrecord.")
        next_step = input("Do you want to return to the studentrecord menu, press '1'.\n"
                          "If you want to add another studentrecord, press '2'.\n->  ")
        return next_step

    def submitting_grade(self):
        self.display.clear()
        print("Please provide the studentrecord ID of the studentrecord where you want to submit a grade.")
        studentrecord_id = int(input("studentrecord ID: "))
        grade = input("Grade: ")
        self.studentrecord_repository.submit_grade(studentrecord_id, grade)
        self.display.clear()
        print(f"Successfully submitted grade.")
        next_step = input("Do you want to return to the studentrecord menu, press '1'.\n"
                          "If you want to submit another grade, press '2'.\n->  ")
        return next_step

    def deleting_studentrecord(self):
        self.display.clear()
        print("Please provide the studentrecord ID of the studentrecord you want to delete from the database.")
        studentrecord_id = int(input("studentrecord ID: "))
        self.studentrecord_repository.delete_studentrecord(studentrecord_id)
        self.display.clear()
        print(f"Successfully deleted the studentrecord from the database.")
        next_step = input("Do you want to return to the studentrecord menu, press '1'.\n"
                          "If you want to delete another studentrecord from the database, press '2'.\n->  ")
        return next_step
