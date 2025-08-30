import requests


class Req:
    """A simple class to handle HTTP requests."""
    def __init__(self) -> None:
        pass

    def get(self, url: str = None) -> requests.Response | None:
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
            requests.exceptions.InvalidURL
        ) as error:
            # Handle URL-related exceptions
            print(f"Request failed due to a URL error: {error}")
            return None


if __name__ == "__main__":
    # Instance of Req class.
    req = Req()

    # Define the target URL for our API request.
    target_url = "https://api.github.com/events"

    # Make the GET request and store the response object in a variable.
    target_response = req.get(target_url)

    # Check if the request was successful
    if target_response and target_response.status_code == 200:

        # Print the raw text content of the response.
        print("--- Response Text ---")
        print(target_response.text)
        
        # Then, print the structured JSON content.
        print("\n--- Response JSON ---")
        print(target_response.json())
    else:
        # If the request failed, let me know gang.
        print(f"Request failed with status code: {target_response.status_code}")