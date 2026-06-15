def parse_intent(user_input: str) -> str:
    """
    Parses natural language input to determine the app type.
    """
    input_lower = user_input.lower()
    
    if "library" in input_lower:
        return "library"
    elif "student" in input_lower and "portal" in input_lower:
        return "student_portal"
    elif "blog" in input_lower or "cms" in input_lower:
        return "blog_cms"
    
    raise ValueError("Sorry, I only understand intents for: Library Management System, Student Portal, and Blog CMS.")
