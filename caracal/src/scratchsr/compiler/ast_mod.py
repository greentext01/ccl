import ast
from pathlib import Path
import shutil

from scratchsr.core.registry import registries
from scratchsr.util.random_function import random_function


def modify_ast(filename):
    path = Path(filename).absolute()
    with open(filename) as file:
        program = file.read()

    cwd = Path.cwd()

    cclfile_path = cwd / ".cclfiles" / path.relative_to(cwd)
    cclfile_path.parent.mkdir(parents=True, exist_ok=True)
    
    registries.add("events", [])

    with open(cclfile_path, "w") as outfile:
        tree = ast.parse(program, filename)
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                modify_class(node)

        outfile.write(ast.unparse(tree))

    return str(cclfile_path)


def del_cclfiles():
    shutil.rmtree(Path.cwd() / ".cclfiles", ignore_errors=True)


def modify_class(node: ast.ClassDef):
    for stmt in node.body:
        if isinstance(stmt, ast.FunctionDef):
            if stmt.name.startswith("on_"):
                # If you put __CCL__COMPILER__ in the name of a function,
                # it will be ignored in some error messages.
                stmt.name += f"__{random_function()}"
