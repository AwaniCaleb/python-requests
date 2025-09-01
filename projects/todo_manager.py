import requests


class TodoManager():
    def __init__(self) -> None:
        self.request_session = requests.Session()
        pass

    def get_all_todos(self) -> dict:
        all_todos = self.request_session.get("https://jsonplaceholder.typicode.com/todos")

        try:
            all_todos.raise_for_status()

            return all_todos.json()

        except Exception as e:
            print(f"Oops! Something went wrong: {e}")


if __name__ == "__main__":
    mgt = TodoManager()

    print(mgt.get_all_todos())