import os

def generate_app(app_type: str, graph: dict, output_base_dir: str = "project_11_app_generator/generated_apps") -> str:
    """
    Generates Aayu source files based on the architecture graph.
    Returns the path to the main.aayu file.
    """
    app_dir = os.path.join(output_base_dir, app_type)
    os.makedirs(app_dir, exist_ok=True)
    
    # Generate Entities
    for entity in graph["entities"]:
        entity_name = entity["name"]
        filename = f"{entity_name.lower()}.aayu"
        filepath = os.path.join(app_dir, filename)
        
        with open(filepath, "w") as f:
            f.write(f"record {entity_name}.\n")
            for field in entity["fields"]:
                f.write(f"    {field}\n")
            f.write("end.\n")
            
    # Generate Tasks
    for task_name in graph["tasks"]:
        filename = f"{task_name.lower()}.aayu"
        filepath = os.path.join(app_dir, filename)
        
        with open(filepath, "w") as f:
            f.write(f"task {task_name}.\n")
            f.write(f"    show \"Executing {task_name}...\".\n")
            f.write("end.\n")
            
    # Generate Main
    main_filepath = os.path.join(app_dir, "main.aayu")
    with open(main_filepath, "w") as f:
        # Use import statements so the whole app connects together
        for entity in graph["entities"]:
            f.write(f"use {entity['name'].lower()}.\n")
        for task_name in graph["tasks"]:
            f.write(f"use {task_name.lower()}.\n")
        
        f.write(f"\nshow \"{app_type.replace('_', ' ').title()} Generated\".\n")
        
    return main_filepath
