from display import Display
from professorrepository import ProfessorRepository
from textvalidator import TextValidator


class ProfessorService:
    def __init__(self):
        self.professor_repository = ProfessorRepository()
        self.display = Display()
        self.text_validator = TextValidator()

    def showing_all_professors(self):
        self.display.clear()
        all_professors = self.professor_repository.get_all_professors()
        professor_info = [(str(info.id), info.first_name, info.last_name) for info in all_professors]
        self.display.print_table(
            table_title="List of all professors",
            column_titles=["ID", "First Name", "Last Name"],
            row_values=professor_info
        )
        next_step = input("Do you want to return to the professor menu? (y): ").lower()
        return next_step

    def adding_professor(self):
        self.display.clear()
        print("Please add the first and last name of the new professor.")
        firstname = input("Firstname: ")
        lastname = input("Lastname: ")
        if not self.text_validator.validate_text(firstname):
            print("Invalid input. Try again.")
            self.adding_professor()
        elif not self.text_validator.validate_text(lastname):
            print("Invalid input. Try again.")
            self.adding_professor()
        self.professor_repository.add_professor(firstname, lastname)
        self.display.clear()
        print(f"Successfully added professor '{firstname} {lastname}'")
        next_step = input("Do you want to return to the professor menu, press '1'.\n"
                          "If you want to add another professor, press '2'.\n->  ")
        return next_step

    def editing_professor(self):
        self.display.clear()
        print("Please provide the professor ID of the professor you want to edit and the new details.")
        professor_id = int(input("Professor ID: "))
        firstname = input("First name: ")
        lastname = input("Last name:")
        if not self.text_validator.validate_text(firstname):
            print("Invalid input. Try again.")
            self.editing_professor()
        elif not self.text_validator.validate_text(lastname):
            print("Invalid input. Try again.")
            self.editing_professor()
        self.professor_repository.edit_professor(professor_id, firstname, lastname)
        self.display.clear()
        print(f"Successfully changed professor with ID '{professor_id}' to '{firstname} {lastname}'.")
        next_step = input("Do you want to return to the professor menu, press '1'.\n"
                          "If you want to edit another professor, press '2'.\n->  ")
        return next_step

    def deleting_professor(self):
        self.display.clear()
        print("Please provide the professor ID of the professor you want to delete from the database.")
        professor_id = int(input("Professor ID: "))
        self.professor_repository.delete_professor(professor_id)
        self.display.clear()
        print(f"Successfully deleted the professor from the database.")
        next_step = input("Do you want to return to the professor menu, press '1'.\n"
                          "If you want to delete another professor from the database, press '2'.\n->  ")
        return next_step
