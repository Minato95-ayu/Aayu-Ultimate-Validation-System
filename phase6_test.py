import sys
import os
import io
from contextlib import redirect_stdout

from intent_engine.parser import parse_intent
from intent_engine.graph import generate_graph
from intent_engine.verifier import verify_graph
from intent_engine.generator import generate_app
from run import run_file

tests = [
    "Create a Library Management System",
    "Create a Student Portal",
    "Create a Blog CMS",
    "Create a Nuclear Reactor Control System"
]

def run_test(intent):
    print(f"Input: {intent}")
    try:
        app_type = parse_intent(intent)
        print("Intent Parsed")
        
        graph = generate_graph(app_type)
        print("Graph Created")
        
        verify_graph(graph)
        print("Verification Passed")
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(base_dir, "generated_apps")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        main_aayu_path = generate_app(app_type, graph, output_base_dir=output_dir)
        print("Code Generated")
        
        # Capture Aayu execution output so test report is clean
        with io.StringIO() as buf, redirect_stdout(buf):
            # run_file caches modules, we might need to reset loaded modules
            run_file(main_aayu_path, loaded_modules=set())
            
        print("Execution Passed")
    except ValueError as e:
        print("Intent Parsed")
        print("\n[FAIL]")
        print("Unknown Application Type")
    except Exception as e:
        print(f"Error: {e}")
    print("-" * 50)

for t in tests:
    run_test(t)
