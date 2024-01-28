from display import Display
from subjectrepository import SubjectRepository


class SubjectService:
    def __init__(self):
        self.subject_repository = SubjectRepository()
        self.display = Display()

    def showing_all_subjects(self):
        self.display.clear()
        all_subjects = self.subject_repository.get_all_subjects()
        subject_info = [(info.id, info.title) for info in all_subjects]
        self.display.print_table(
            table_title="List of all subjects",
            column_titles=["ID", "Title"],
            row_values=subject_info
        )
        next_step = input("Do you want to return to the subject menu? (y): ").lower()
        return next_step

    def adding_subject(self):
        self.display.clear()
        print("Please add the title of the new subject.")
        title = input("Title: ")
        self.subject_repository.add_subject(title)
        self.display.clear()
        print(f"Successfully added subject '{title}'")
        next_step = input("Do you want to return to the subject menu, press '1'.\n"
                          "If you want to add another subject, press '2'.\n->  ")
        return next_step

    def editing_subject(self):
        self.display.clear()
        print("Please provide the subject ID of the subject you want to edit and the new title.")
        subject_id = int(input("subject ID: "))
        title = input("Title: ")
        self.subject_repository.edit_subject(subject_id, title)
        self.display.clear()
        print(f"Successfully changed subject with ID '{subject_id}' to '{title}'.")
        next_step = input("Do you want to return to the subject menu, press '1'.\n"
                          "If you want to edit another subject, press '2'.\n->  ")
        return next_step

    def deleting_subject(self):
        self.display.clear()
        print("Please provide the subject ID of the subject you want to delete from the database.")
        subject_id = int(input("subject ID: "))
        self.subject_repository.delete_subject(subject_id)
        self.display.clear()
        print(f"Successfully deleted the subject from the database.")
        next_step = input("Do you want to return to the subject menu, press '1'.\n"
                          "If you want to delete another subject from the database, press '2'.\n->  ")
        return next_step
