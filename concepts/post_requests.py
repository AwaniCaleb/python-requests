import requests


class Req:
    """A class to handle different types of HTTP requests."""
    def __init__(self) -> None:
        pass

    def post(self, url: str, payload: dict, is_json: bool = False) -> requests.Response | None:
        """
        Performs a POST request to the specified URL with data.

        Args:
            url (str): The URL for the POST request.
            payload (dict): The dictionary of data to send in the request body.
            is_json (bool): If True, sends the payload as JSON;
                             otherwise, sends as form-encoded data.

        Returns:
            requests.Response: The response object from the POST request.
            None: An error occurred during the request.
        """
        try:
            if is_json:
                response = requests.post(url=url, json=payload)
            else:
                response = requests.post(url=url, data=payload)
            return response
        except (
            requests.exceptions.URLRequired,
            requests.exceptions.MissingSchema,
            requests.exceptions.InvalidSchema,
            requests.exceptions.InvalidURL,
        ) as error:
            # Catch and handle common URL-related exceptions.
            print(f"Request failed due to a URL error: {error}")
            return None


if __name__ == "__main__":
    # Create an instance of the Req class.
    req = Req()

    # Define the target URL and the dictionary of data to be sent.
    target_url = "https://httpbin.org/post"
    payload = {'name': 'Learning Coach', 'skill': 'APIs'}

    # Make the POST request, specifying that we want to send JSON data.
    target_response = req.post(target_url, payload, is_json=True)

    # Check if the response object exists and the request was successful (status code 200).
    if target_response and target_response.status_code == 200:
        # Print the final URL, which remains clean.
        print("--- Final URL ---")
        print(target_response.url)

        # Print the structured JSON content to see the data the server received.
        print("\n--- Response JSON ---")
        print(target_response.json())
    else:
        # Print a helpful message if the request failed.
        status_code = target_response.status_code if target_response else "N/A"
        print(f"Request failed with status code: {status_code}")