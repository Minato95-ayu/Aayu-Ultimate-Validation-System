def generate_graph(app_type: str) -> dict:
    """
    Generates the architecture graph (entities and tasks) based on app_type.
    """
    if app_type == "library":
        return {
            "entities": [
                {"name": "Student", "fields": ["name", "age"]},
                {"name": "Book", "fields": ["title", "author"]},
                {"name": "Library", "fields": ["name"]}
            ],
            "tasks": ["borrow_book", "return_book"]
        }
    elif app_type == "student_portal":
        return {
            "entities": [
                {"name": "Student", "fields": ["name", "roll_number"]},
                {"name": "Course", "fields": ["title", "credits"]},
                {"name": "Grade", "fields": ["score", "grade_letter"]}
            ],
            "tasks": ["enroll", "assign_grade"]
        }
    elif app_type == "blog_cms":
        return {
            "entities": [
                {"name": "User", "fields": ["username", "email"]},
                {"name": "Post", "fields": ["title", "content"]},
                {"name": "Comment", "fields": ["author", "body"]}
            ],
            "tasks": ["publish", "moderate"]
        }
    else:
        raise ValueError(f"Unknown app_type: {app_type}")
