def verify_graph(graph: dict) -> bool:
    """
    Verifies that the generated architecture graph is valid.
    """
    if "entities" not in graph or not isinstance(graph["entities"], list):
        raise ValueError("Graph missing 'entities' list.")
    if "tasks" not in graph or not isinstance(graph["tasks"], list):
        raise ValueError("Graph missing 'tasks' list.")
        
    for entity in graph["entities"]:
        if "name" not in entity:
            raise ValueError("Entity is missing a 'name'.")
        if "fields" not in entity or not isinstance(entity["fields"], list):
            raise ValueError(f"Entity {entity.get('name')} is missing 'fields' list.")
            
    return True
