# Python's `requests` Library

This repository is a practical learning guide to mastering the `requests` library in Python. It includes conceptual explanations, step-by-step code examples, and practical projects to solidify understanding of HTTP requests, web APIs, and web interactions.

The goal is to build a solid foundation by moving from core concepts to real-world applications.

### Why `requests`?

The `requests` library is the de facto standard for making HTTP requests in Python. It's incredibly user-friendly and handles much of the complexity of web communication, allowing developers to focus on building powerful applications without getting bogged down by low-level details.

### Repository Structure

This repository is organized to help you learn progressively:

  - [`concepts/`](./concepts): Contains small, focused Python scripts that demonstrate specific features of the `requests` library, like making `GET` and `POST` requests, handling headers, and managing errors.
  - [`projects/`](./projects): Contains larger, more practical applications that combine multiple concepts into a single, functional tool, such as a basic web scraper or an API client.
  - [`requirements.txt`](./requirements.txt): Lists all the necessary libraries for this project, including `requests`.
  - [`.gitignore`](./.gitignore): Specifies files and folders that should be ignored by Git (e.g., virtual environments, cache files).

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

### Contributing

This is a personal learning project, but if you have suggestions for new projects or improvements to the documentation, feel free to open an issue or pull request.