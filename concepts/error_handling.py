import requests


class Req:
    """A simple class to handle HTTP requests."""
    def __init__(self) -> None:
        pass

    def get(self, url: str) -> requests.Response | None:
        """
        Performs a GET request to the specified URL.

        Args:
            url (str): The URL for the GET request.

        Returns:
            requests.Response: The response object from the GET request.
            None: An error occured
        """
        try:
            # Send the GET request to the target URL and return the response object.
            return requests.get(url=url)
        except (
            requests.exceptions.URLRequired,
            requests.exceptions.MissingSchema,
            requests.exceptions.InvalidSchema,
            requests.exceptions.InvalidURL,
        ) as error:
            # Handle URL-related exceptions
            print(f"Request failed due to a URL error: {error}")
            return None


if __name__ == "__main__":
    # Instance of Req class.
    req = Req()

    # Define the target URL for our API request.
    target_url = "https://httpbin.org/status/404"

    # Make the GET request and store the response object in a variable.
    target_response = req.get(target_url)

    try:
        # Raise an exception for bad status codes (4xx or 5xx).
        target_response.raise_for_status()

        # These lines will only run if the request was successful.
        print("--- Response Text ---")
        print(target_response.text)
        print("\n--- Response JSON ---")
        print(target_response.json())

    except requests.exceptions.HTTPError as e:
        # Catch specific HTTP errors raised by raise_for_status().
        print(f"Request failed: {e}")