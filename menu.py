from display import Display
from studentservice import StudentService
from professorservice import ProfessorService
from courseservice import CourseService
from subjectservice import SubjectService
from studentrecordsservice import StudentRecordService
from menupage import MenuPage


class Menu:
    def __init__(self):
        self.display = Display()
        self.student_service = StudentService()
        self.professor_service = ProfessorService()
        self.course_service = CourseService()
        self.subject_service = SubjectService()
        self.studentrecord_service = StudentRecordService()

    def show(self):
        while True:
            selected_option = self.show_main_menu()
            match selected_option:
                case "1":
                    self.show_student_menu()
                case "2":
                    self.show_professor_menu()
                case "3":
                    self.show_subject_menu()
                case "4":
                    self.show_course_menu()
                case "5":
                    self.show_studentrecord_menu()
                case "6":
                    self.display.clear()
                    print("Goodbye")
                    break
                case _:
                    self.display.clear()
                    print("Invalid option, please select from the displayed options")
                    self.show_main_menu()

    def show_main_menu(self):
        menu_page = MenuPage(
            title="Main Menu",
            options={
                "1": "Manage Students",
                "2": "Manage Professors",
                "3": "Manage Subjects",
                "4": "Manage Courses",
                "5": "Manage Student Records",
                "6": "Quit Program"
            }
        )
        selected_option = menu_page.select_menu_option()
        return selected_option

    def show_student_menu(self):
        menu_page = MenuPage(
            title="Student Menu",
            options={
                "1": "Show list of students",
                "2": "Add a new student",
                "3": "Edit a student",
                "4": "Delete a student",
                "5": "Return to Main Menu",
                "6": "Quit Program"
            }
        )
        selected_option = menu_page.select_menu_option()
        match selected_option:
            case "1":
                self.show_all_students()
            case "2":
                self.show_add_student()
            case "3":
                self.show_edit_student()
            case "4":
                self.show_delete_student()
            case "5":
                self.show_main_menu()
            case "6":
                self.display.clear()
                print("Goodbye")
                exit()

    def show_professor_menu(self):
        menu_page = MenuPage(
            title="Professor Menu",
            options={
                "1": "Show list of professors",
                "2": "Add a new professor",
                "3": "Edit a professor",
                "4": "Delete a professor",
                "5": "Return to Main Menu",
                "6": "Quit Program"
            }
        )
        selected_option = menu_page.select_menu_option()
        match selected_option:
            case "1":
                self.show_all_professors()
            case "2":
                self.show_add_professor()
            case "3":
                self.show_edit_professor()
            case "4":
                self.show_delete_professor()
            case "5":
                self.show_main_menu()
            case "6":
                self.display.clear()
                print("Goodbye")
                exit()

    def show_course_menu(self):
        menu_page = MenuPage(
            title="Course Menu",
            options={
                "1": "Show list of courses",
                "1.1": "Show list of all students in course",
                "2": "Add a new course",
                "3": "Edit a course",
                "4": "Delete a course",
                "5": "Return to Main Menu",
                "6": "Quit Program"
            }
        )
        selected_option = menu_page.select_menu_option()
        match selected_option:
            case "1":
                self.show_all_courses()
            case "1.1":
                self.show_all_students_of_course()
            case "2":
                self.show_add_course()
            case "3":
                self.show_edit_course()
            case "4":
                self.show_delete_course()
            case "5":
                self.show_main_menu()
            case "6":
                self.display.clear()
                print("Goodbye")
                exit()

    def show_subject_menu(self):
        menu_page = MenuPage(
            title="Subject Menu",
            options={
                "1": "Show list of subjects",
                "2": "Add a new subject",
                "3": "Edit a subject",
                "4": "Delete a subject",
                "5": "Return to Main Menu",
                "6": "Quit Program"
            }
        )
        selected_option = menu_page.select_menu_option()
        match selected_option:
            case "1":
                self.show_all_subjects()
            case "2":
                self.show_add_subject()
            case "3":
                self.show_edit_subject()
            case "4":
                self.show_delete_subject()
            case "5":
                self.show_main_menu()
            case "6":
                self.display.clear()
                print("Goodbye")
                exit()

    def show_studentrecord_menu(self):
        menu_page = MenuPage(
            title="Student Record Menu",
            options={
                "1": "Show list of student records",
                "2": "Add a new student record",
                "3": "Submit a grade",
                "4": "Delete a student record",
                "5": "Return to Main Menu",
                "6": "Quit Program"
            }
        )
        selected_option = menu_page.select_menu_option()
        match selected_option:
            case "1":
                self.show_all_studentrecords()
            case "2":
                self.show_add_studentrecord()
            case "3":
                self.show_submit_grade()
            case "4":
                self.show_delete_studentrecord()
            case "5":
                self.show_main_menu()
            case "6":
                self.display.clear()
                print("Goodbye")
                exit()

    def show_all_students(self):
        next_step = self.student_service.showing_all_students()
        if next_step == "y":
            self.show_student_menu()
        else:
            self.show_all_students()

    def show_add_student(self):
        next_step = self.student_service.adding_student()
        if next_step == "1":
            self.show_student_menu()
        else:
            self.show_add_student()

    def show_edit_student(self):
        next_step = self.student_service.editing_student()
        if next_step == "1":
            self.show_student_menu()
        else:
            self.show_edit_student()

    def show_delete_student(self):
        next_step = self.student_service.deleting_student()
        if next_step == "1":
            self.show_student_menu()
        else:
            self.show_delete_student()

    def show_all_professors(self):
        next_step = self.professor_service.showing_all_professors()
        if next_step == "y":
            self.show_professor_menu()
        else:
            self.show_all_professors()

    def show_add_professor(self):
        next_step = self.professor_service.adding_professor()
        if next_step == "1":
            self.show_professor_menu()
        else:
            self.show_add_professor()

    def show_edit_professor(self):
        next_step = self.professor_service.editing_professor()
        if next_step == "1":
            self.show_professor_menu()
        else:
            self.show_edit_professor()

    def show_delete_professor(self):
        next_step = self.professor_service.deleting_professor()
        if next_step == "1":
            self.show_professor_menu()
        else:
            self.show_delete_professor()

    def show_all_courses(self):
        next_step = self.course_service.showing_all_courses()
        if next_step == "y":
            self.show_course_menu()
        else:
            self.show_all_courses()

    def show_all_students_of_course(self):
        next_step = self.course_service.showing_all_students_of_course()
        if next_step == "y":
            self.show_course_menu()
        else:
            self.show_all_students_of_course()

    def show_add_course(self):
        next_step = self.course_service.adding_course()
        if next_step == "1":
            self.show_course_menu()
        else:
            self.show_add_course()

    def show_edit_course(self):
        next_step = self.course_service.editing_course()
        if next_step == "1":
            self.show_course_menu()
        else:
            self.show_edit_course()

    def show_delete_course(self):
        next_step = self.course_service.deleting_course()
        if next_step == "1":
            self.show_course_menu()
        else:
            self.show_delete_course()

    def show_all_subjects(self):
        next_step = self.subject_service.showing_all_subjects()
        if next_step == "y":
            self.show_subject_menu()
        else:
            self.show_all_subjects()

    def show_add_subject(self):
        next_step = self.subject_service.adding_subject()
        if next_step == "1":
            self.show_subject_menu()
        else:
            self.show_add_subject()

    def show_edit_subject(self):
        next_step = self.subject_service.editing_subject()
        if next_step == "1":
            self.show_subject_menu()
        else:
            self.show_edit_subject()

    def show_delete_subject(self):
        next_step = self.subject_service.deleting_subject()
        if next_step == "1":
            self.show_subject_menu()
        else:
            self.show_delete_subject()

    def show_all_studentrecords(self):
        next_step = self.studentrecord_service.showing_all_studentrecords()
        if next_step == "y":
            self.show_studentrecord_menu()
        else:
            self.show_all_studentrecords()

    def show_add_studentrecord(self):
        next_step = self.studentrecord_service.adding_studentrecord()
        if next_step == "1":
            self.show_studentrecord_menu()
        else:
            self.show_add_studentrecord()

    def show_submit_grade(self):
        next_step = self.studentrecord_service.submitting_grade()
        if next_step == "1":
            self.show_studentrecord_menu()
        else:
            self.show_submit_grade()

    def show_delete_studentrecord(self):
        next_step = self.studentrecord_service.deleting_studentrecord()
        if next_step == "1":
            self.show_studentrecord_menu()
        else:
            self.show_delete_studentrecord()
