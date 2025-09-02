import requests
import random

class TodoManager():
    """
    A class to manage interactions with the `JSONPlaceholder` To-Do API.
    This class handles creating, reading, updating, and deleting to-do items.
    """
    def __init__(self) -> None:
        """Initializes a new requests.Session object for persistent connections."""
        self.request_session = requests.Session()

    def get_all_todos(self) -> dict | None:
        """
        Fetches all to-do items from the `JSONPlaceholder` API.

        Returns:
            dict | None: The JSON data of all to-do items if the request is successful,
                         otherwise returns None.
        """
        try:
            # Use the session to make a GET request to the API.
            response = self.request_session.get("https://jsonplaceholder.typicode.com/todos")
            # Raise an HTTPError for bad status codes (4xx or 5xx).
            response.raise_for_status()

            return response.json()

        except requests.exceptions.HTTPError as e:
            # Catch specific HTTP errors raised by raise_for_status().
            print(f"Oops! Something went wrong: {e}")
            return None
    
    def create_todo(self, todo: dict) -> dict | None:
        """
        Creates a new to-do item on the `JSONPlaceholder` API.

        Args:
            todo (dict): A dictionary containing the data for the new to-do item.
                         e.g., {'title': 'New Task', 'completed': False, 'userId': 1}

        Returns:
            dict | None: The JSON data of the created to-do item with its new ID,
                         or None if the request fails.
        """
        try:
            # Use the session to make a POST request with the to-do data as JSON.
            # The API will return the new to-do item with a unique ID.
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

    def update_todo(self, id: int, todo: dict) -> dict | None:
        """
        Updates an existing to-do item on the `JSONPlaceholder` API.

        Args:
            id (int): The ID of the to-do item to update.
            todo (dict): A dictionary containing the updated data for the to-do item.

        Returns:
            dict | None: The JSON data of the updated to-do item, or None if the
                         request fails.
        """
        try:
            # Use the session to make a PUT request to the specific to-do item URL.
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

    def delete_todo(self, id: int) -> bool:
        """
        Deletes a specific to-do item from the `JSONPlaceholder` API.

        Args:
            id (int): The ID of the to-do item to delete.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        try:
            # Use the session to make a DELETE request to the specific to-do item URL.
            response = self.request_session.delete(
                f"https://jsonplaceholder.typicode.com/todos/{id}"
            )
            response.raise_for_status()

            print("To-do item deleted successfully!")
            return True

        except requests.exceptions.HTTPError as e:
            print(f"Oops! Something went wrong: {e}")
            return False


if __name__ == "__main__":
    # Create an instance of our TodoManager class.
    manager = TodoManager()
    
    # Example 1: Creating a new to-do item
    new_todo = {
        'title': 'Learn about APIs',
        'completed': False,
        'userId': 1
    }
    created_todo = manager.create_todo(new_todo)
    if created_todo:
        print("\n--- New To-do Item ---")
        print(created_todo)
    
    # Example 2: Updating an existing to-do item (using a dummy ID)
    updated_todo = manager.update_todo(200, {'title': 'Learning is fun'})
    if updated_todo:
        print("\n--- Updated To-do Item ---")
        print(updated_todo)
    
    # Example 3: Deleting a to-do item (using a dummy ID)
    delete_todo_id = 1
    if manager.delete_todo(delete_todo_id):
        print("\n--- Deleted To-do Item ---")
        print(f"Todo with ID {delete_todo_id} has been deleted.")