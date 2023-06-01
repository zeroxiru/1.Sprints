def connect_to_db():
    """ Connect to the database.
    Return the DB object, or None in case of an error. """

    try:
        # Connect to databse
        db = get_database_object()
        return db
    except Exception as e:
        print(f"Error connecting to database: {e}")
    return None  # reach here in case of exception


def notify_students(db):
    """ Notify the students about their grades.
    Assume DB is a connect database object. """

    # Means that the database is connected!
    students = db.get_users_from_course()
    students_full_details = get_full_details(students)
    students_full_grades = get_final_grades(students)

    # Contact each student via email to notify them
    students_with_email = communications.get_emails(students)
    for student in students_with_email:
        communications.notify(student)


def main():
    """ Connects to the DB and notifies the students their grades. """
    db = connect_to_db()
    if db is not None:
        notify_students()
    else:
        print("Not connected, nothing to do here!")