from display import Display
from studentservice import StudentService
from menupage import MenuPage


class Menu:
    def __init__(self):
        self.display = Display()
        self.student_service = StudentService()

    def show(self):
        while True:
            selected_option = self.show_main_menu()
            match selected_option:
                case "1":
                    self.show_student_menu()
                case "2":
                    self.show_professor_menu()
                case "3":
                    self.show_course_menu()
                case "4":
                    self.show_subject_menu()
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
                "3": "Manage Courses",
                "4": "Manage Subjects",
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
                pass
            case "4":
                pass
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
                "1": "Manage 1",
                "2": "Manage 2"
            }
        )
        selected_option = menu_page.select_menu_option()

    def show_course_menu(self):
        menu_page = MenuPage(
            title="Course Menu",
            options={
                "1": "Manage 1",
                "2": "Manage 2"
            }
        )
        selected_option = menu_page.select_menu_option()

    def show_subject_menu(self):
        menu_page = MenuPage(
            title="Subject Menu",
            options={
                "1": "Manage 1",
                "2": "Manage 2"
            }
        )
        selected_option = menu_page.select_menu_option()

    def show_studentrecord_menu(self):
        menu_page = MenuPage(
            title="Student Record Menu",
            options={
                "1": "Manage 1",
                "2": "Manage 2"
            }
        )
        selected_option = menu_page.select_menu_option()

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
