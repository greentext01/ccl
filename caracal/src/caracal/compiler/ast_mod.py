import ast

from caracal.core.registry import registries
from caracal.util.random import random


def modify_ast(filename):
    out = []
    with open(filename) as file:
        program = file.read()
    
    tree = ast.parse(program, filename)
    registries.add("events")
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            for stmt in node.body:
                if isinstance(stmt, ast.FunctionDef):
                    if stmt.name.startswith("on_"):
                        stmt.name += f"_{random()}"
                        out.append(stmt.name)
