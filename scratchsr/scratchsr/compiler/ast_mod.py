import ast
from pathlib import Path
import shutil

from scratchsr.util.registry import registries
from scratchsr.util.random_function import random_function


class AstMod(ast.NodeTransformer):
    def visit_ClassDef(self, node):
        for stmt in node.body:
            if isinstance(stmt, ast.FunctionDef):
                if stmt.name.startswith("on_"):
                    stmt.name += f"__{random_function()}"

        return node

    def visit_Assign(self, node):
        print(ast.dump(node))
        node = ast.Expr(ast.Call(
            func=ast.Name(
                id="scratchsr.user.essential.variable", ctx=ast.Load()
            ),
            args=[ast.Constant(node.targets[0].id), node.value],
        ))
        return node


def modify_ast(filename):
    path = Path(filename).absolute()
    with open(filename) as file:
        program = file.read()

    cwd = Path.cwd()

    scsrfile_path = cwd / ".scsrfiles" / path.relative_to(cwd)
    scsrfile_path.parent.mkdir(parents=True, exist_ok=True)

    registries.add("events", [])

    tree = ast.parse(program, filename)
    tree.body.insert(0, ast.Import([
        ast.alias("scratchsr.user.essential")
    ]))

    tree = AstMod().visit(tree)

    with open(scsrfile_path, "w") as outfile:
        outfile.write(ast.unparse(tree))

    return str(scsrfile_path)


def del_scsrfiles():
    shutil.rmtree(Path.cwd() / ".scsrfiles", ignore_errors=True)


def modify_class(node: ast.ClassDef):
    for stmt in node.body:
        if isinstance(stmt, ast.FunctionDef):
            if stmt.name.startswith("on_"):
                stmt.name += f"__{random_function()}"


def modify_var(node: ast.Assign):
    node = ast.Expr(ast.Call(
        func=ast.Name(
            id="scratchsr.user.essential.variable", ctx=ast.Load()
        ),
        args=[ast.Constant(node.targets[0].id), node.value],
    ))
    return node
