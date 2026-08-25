def execute_python(code: str):
    """Execute python code.

    This is a simplified demo tool.
    Production agents need sandboxing.
    """
    namespace = {}
    exec(code, namespace)
    return namespace
