import subprocess


def run_shell(command: str) -> str:
    """Execute a shell command.

    This is a basic implementation for local development.
    Production versions should add sandboxing and permissions.
    """
    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        return result.stderr

    return result.stdout
