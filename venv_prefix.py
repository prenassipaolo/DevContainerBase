import sys


def in_venv():
    print(
        f"Prefix: {sys.prefix}",
        f"Base prefix: {sys.base_prefix}"
    )

    is_virtual_env = sys.prefix != sys.base_prefix
    if is_virtual_env:
        print("Running inside a virtual environment.")
    else:
        print("Not running inside a virtual environment.")
    return is_virtual_env

if __name__ == "__main__":
    in_venv()