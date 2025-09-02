import requests
import random

class TodoManager():
    def __init__(self) -> None:
        self.request_session = requests.Session()
        pass

    def create_todo(self, todo: dict) -> dict:
        try:
            response = self.request_session.post(
                "https://jsonplaceholder.typicode.com/todos",
                json=todo
            )
            response.raise_for_status()

            print("To-do item created successfully!")
            return response.json()

        except requests.exceptions.HTTPError as e:
            print(f"Oops! Something went wrong: {e}")
            return None

    def update_todo(self, id: int, todo: dict) -> dict:
        try:
            response = self.request_session.put(
                f"https://jsonplaceholder.typicode.com/todos/{id}",
                json=todo
            )
            response.raise_for_status()

            print("To-do item updated successfully!")
            return response.json()

        except requests.exceptions.HTTPError as e:
            print(f"Oops! Something went wrong: {e}")
            return None

    def get_all_todos(self):
        all_todos = self.request_session.get("https://jsonplaceholder.typicode.com/todos")

        try:
            all_todos.raise_for_status()

            return all_todos.json()

        except Exception as e:
            print(f"Oops! Something went wrong: {e}")


if __name__ == "__main__":
    mgt = TodoManager()

    new_todo = {
        'title': 'Learn about APIs',
        'completed': False,
        'userId': 1
    }

    created_todo = mgt.create_todo(new_todo)

    if created_todo:
        print("\n--- New To-do Item ---")
        print(created_todo)

    updated_todo = mgt.update_todo(200, {'title': 'Learning is fun'})

    if updated_todo:
        print("\n--- Updated To-do Item ---")
        print(updated_todo)
