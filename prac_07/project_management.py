from project import Project
import datetime

MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n"
        "- (U)pdate project\n- (Q)uit\n>>>")
FILE_NAME = "projects.txt"
LOAD = "l"
SAVE = "s"
DISPLAY = "d"
FILTER = "f"
ADD = "a"
UPDATE = "u"
QUIT = "q"
MAXIMUM_PERCENTAGE = 100
MINIMUM_PERCENTAGE = 0


def main():
    """Call and pass data to the functions below"""
    projects = read_file(FILE_NAME)
    choice = input(MENU).lower()
    while choice != QUIT:
        if choice == LOAD:
            load_file("What file do you want to load?")
        elif choice == SAVE:
            get_file_name(projects)
        elif choice == DISPLAY:
            display_projects(projects)
        elif choice == FILTER:
            filter_projects(projects)
        elif choice == ADD:
            add_project(projects)
        elif choice == UPDATE:
            update_project(projects)
        else:
            print("Invalid input")
        choice = input(MENU).lower()
    save_option = input("Do you want to save your file?(Y/N)").lower()
    if save_option == "y":
        save_projects(projects, FILE_NAME)
    print("Thank you for using custom-built project management software.")


def read_file(file_name):
    """Reads project data from projects CSV file"""
    projects = []
    with open(file_name, "r") as projects_information:
        projects_information.readline()
        for line in projects_information:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))  # use Project class to install project data to the list
            projects.append(project)
        print(f"Loaded {len(projects)} projects from {file_name}")
    return projects


def load_file(input_name):
    """Load specified file or default file"""
    file_name = input(input_name)
    try:
        read_file(file_name)
    except FileNotFoundError:
        print(f"File not found, open default file--{FILE_NAME}")
        read_file(FILE_NAME)


def get_file_name(projects):
    """Get specified file name"""
    user_input_name = input("Input name:")
    if not user_input_name.endswith(".txt"):
        user_input_name += ".txt"
    save_projects(projects, user_input_name)


def save_projects(projects, file_name):
    """Save projects to specified file"""
    with open(file_name, 'w') as new_file:
        print("Name	Start Date	Priority	Cost Estimate	Completion Percentage", file=new_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.percentage}", file = new_file)
    print(f"{len(projects)} projects saved to {file_name}")


def display_projects(projects):
    """Display all projects"""
    incomplete = [project for project in projects if not project.is_completed()]
    complete = [project for project in projects if project.is_completed()]    # uses list comprehension to determine and add complete or incomplete project to different list

    if incomplete:
        print("Incomplete projects:")
        for project in sorted(incomplete):
            print(project)
    else:
        print("No incomplete projects.")

    if complete:
        print("Completed projects:")
        for project in sorted(complete):
            print(project)
    else:
        print("No completed projects.")


def filter_projects(projects):
    """Fileter projects by time"""
    projects_to_filter = projects
    input_date = input("Show projects that start after date (dd/mm/yy):")
    date = datetime.datetime.strptime(input_date, "%d/%m/%Y").date()  # use datetime to input date
    projects_to_filter.sort()
    for project in projects_to_filter:
        date1 = datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()
        if date1 >= date:
            print(project)


def add_project(projects):
    """Add new projects to the list"""
    print("Let's add a new project")
    name = get_valid_string("Name:")
    start_date = input("Start date (dd/mm/yy):")
    priority = int(get_valid_number("Priority:", projects, "priority"))
    cost_estimate = get_valid_number("Cost estimate: $", projects, "cost")
    percentage = int(get_valid_number("Percentage:", projects, "percentage"))
    project = Project(name, start_date, priority, cost_estimate, percentage)
    projects.append(project)


def update_project(projects):
    """Update priority and percentage of project"""
    for index, project in enumerate(projects):
        print(index, project)

    choice = int(get_valid_number("Project choice:", projects, "project_number"))
    print(projects[choice])

    new_percentage = int(get_valid_number("New Percentage:", projects, "percentage"))
    new_priority = int(get_valid_number("New Priority:", projects, "priority"))
    projects[choice].percentage = new_percentage
    projects[choice].priority = new_priority


def get_valid_number(user_input, projects, data_type):
    """Get valid input number"""
    is_valid = False
    while not is_valid:
        try:
            user_input_to_validate = float(input(user_input))
            if user_input_to_validate < MINIMUM_PERCENTAGE:  # determine whether the user input is bigger than 0
                print("Numbers must be > 0")
            else:
                if user_input_to_validate >= len(projects) and data_type == "project_number":
                    print("Invalid project number")
                elif user_input_to_validate > MAXIMUM_PERCENTAGE and data_type == "percentage":
                    print("Invalid percentage")
                else:
                    return user_input_to_validate
        except ValueError:
            print("Invalid input")


def get_valid_string(user_input):
    """Get valid input string"""
    string = input(user_input)
    while string == "":
        print("Invalid input")
        string = input(user_input)
    return string


main()
