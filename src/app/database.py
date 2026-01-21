# Simulated State
tasks_db: list = []


def get_next_id() -> int:
    return len(tasks_db) + 1
