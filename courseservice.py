from display import Display
from courserepository import CourseRepository


class CourseService:
    def __init__(self):
        self.course_repository = CourseRepository()
        self.display = Display()

    def showing_all_courses(self):
        self.display.clear()
        all_courses = self.course_repository.get_all_courses()
        course_info = [
            (str(info.id),
             str(info.subject.title),
             str(info.professor.first_name),
             str(info.professor.last_name))
            for info in all_courses]
        self.display.print_table(
            table_title="List of all courses",
            column_titles=[
                "ID",
                "Subject Title",
                "Professor First Name",
                "Professor Last Name",
                ],
            row_values=course_info
        )
        next_step = input("Do you want to return to the course menu? (y): ").lower()
        return next_step

    def adding_course(self):
        self.display.clear()
        print("Please add the details of the new course.")
        professor_id = input("Professor ID: ")
        subject_id = input("Subject ID: ")
        self.course_repository.add_course(professor_id, subject_id)
        self.display.clear()
        print(f"Successfully added new course.")
        next_step = input("Do you want to return to the course menu, press '1'.\n"
                          "If you want to add another course, press '2'.\n->  ")
        return next_step

    def editing_course(self):
        self.display.clear()
        print("Please provide the course ID of the course you want to edit and the new details.")
        course_id = int(input("course ID: "))
        edit_prof = input("Do you want to edit the professor ID? (y/n): ").lower()
        if edit_prof == "y":
            new_professor_id = input("Professor ID: ")
        else:
            new_professor_id = None
        edit_subj = input("Do you want to edit the subject ID? (y/n): ").lower()
        if edit_subj == "y":
            new_subject_id = input("Subject ID: ")
        else:
            new_subject_id = None
        self.course_repository.edit_course(course_id, new_professor_id, new_subject_id)
        self.display.clear()
        print(f"Successfully changed course with ID '{course_id}'.")
        next_step = input("Do you want to return to the course menu, press '1'.\n"
                          "If you want to edit another course, press '2'.\n->  ")
        return next_step

    def deleting_course(self):
        self.display.clear()
        print("Please provide the course ID of the course you want to delete from the database.")
        course_id = int(input("course ID: "))
        self.course_repository.delete_course(course_id)
        self.display.clear()
        print(f"Successfully deleted the course from the database.")
        next_step = input("Do you want to return to the course menu, press '1'.\n"
                          "If you want to delete another course from the database, press '2'.\n->  ")
        return next_step
