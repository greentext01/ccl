from glob import glob
import importlib
import os
from scratchsr.compiler.ast_mod import modify_ast
from scratchsr.errors.missing_path_error import MissingPathError


def run_sprites():
    if not os.path.exists("sprites"):
        raise MissingPathError("sprites")

    for filename in glob("sprites/**/*.ccl.py"):
        path = modify_ast(filename)

        spec = importlib.util.spec_from_file_location(path, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
