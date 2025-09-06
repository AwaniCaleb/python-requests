# Python's `requests` Library

This repository is a practical learning guide to mastering the `requests` library in Python. It includes conceptual explanations, step-by-step code examples, and practical projects to solidify understanding of HTTP requests, web APIs, and web interactions.

The goal is to build a solid foundation by moving from core concepts to real-world applications.

### Why `requests`?

The `requests` library is the de facto standard for making HTTP requests in Python. It's incredibly user-friendly and handles much of the complexity of web communication, allowing developers to focus on building powerful applications without getting bogged down by low-level details.

### Repository Structure

This repository is organized to help you learn progressively:

  - [`concepts/`](./concepts/): Contains small, focused Python scripts that demonstrate specific features of the `requests` library, like making `GET` and `POST` requests, handling headers, and managing errors.
  - [`projects/`]: Contains larger, more practical applications that combine multiple concepts into a single, functional tool, such as a basic web scraper or an API client.
  - `requirements.txt`: Lists all the necessary libraries for this project, including `requests`.
  - `.gitignore`: Specifies files and folders that should be ignored by Git (e.g., virtual environments, cache files).

### Learning Plan

I'll follow a structured plan to cover the essential aspects of the library:

1.  **Introduction to `requests`**
2.  **Making `GET` Requests**
3.  **Handling Query Parameters**
4.  **Making `POST` Requests**
5.  **Headers and Authentication**
6.  **Handling Errors and Exceptions**
7.  **Using Session Objects**

Each topic will have its own code example within the `concepts/` directory. Hopefully lol

### Getting Started

To get started, you'll need Python installed on your system. It's highly recommended to use a virtual environment to manage your project's dependencies.

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/awanicaleb/python-requests.git
    cd python-requests
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required libraries:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables**
    
    For the `weather_app.py` project, you will need a free API key from [OpenWeatherMap](https://openweathermap.org/).
    * Sign up for an account to get your API key.
    * Create a file named `.env` in the project's root directory.
    * Add your API key to the file like this:

        ```
        WEATHER_APP_API_KEY="YOUR_API_KEY_HERE"
        ```

### Projects and Concepts Covered

* **`error_handling.py`**: A foundational script demonstrating how to use `try...except` blocks and `response.raise_for_status()` to handle common HTTP errors gracefully.
* **`session_objects.py`**: A script that introduces `requests.Session()` to improve the performance of a series of requests by maintaining a persistent connection and managing cookies.
* **`todo_manager.py`**: A complete CRUD (Create, Read, Update, Delete) application that interacts with the JSONPlaceholder API. It features methods for adding, viewing, updating, and deleting to-do items.
* **`weather_app.py`**: A more advanced project that fetches and displays weather data from the OpenWeatherMap API. This project demonstrates handling API keys securely with environment variables and accepting command-line input from the user.

### Usage

#### `todo_manager.py`

This script is meant to be run directly to perform various API actions. You can uncomment the different sections in the `if __name__ == "__main__":` block to test the `create`, `update`, and `delete` methods.

#### `weather_app.py`

Run this script from your terminal and provide a city name as an argument.

* **Example**: Get the weather for London.
    ```sh
    python weather_app.py "London"
    ```
* **Example**: Get the weather for a city with a space in its name.
    ```sh
    python weather_app.py "New York"
    ```
* **Example**: Without an argument, the script will show an error message.
    ```sh
    python weather_app.py
    ```

### Contributing

This is a personal learning project, but if you have suggestions for new projects or improvements to the documentation, feel free to open an issue or pull request.