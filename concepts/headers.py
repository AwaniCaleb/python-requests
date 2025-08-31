import requests


class Req:
    """A class to demonstrate making a GET request with custom header parameters."""
    def __init__(self) -> None:
        pass

    def get(self, url: str, params: dict = {}, headers: dict = {}) -> requests.Response | None:
        """
        Performs a GET request to the specified URL with optional parameters.

        Args:
            url (str): The base URL for the GET request.
            params (dict, optional): A dictionary of query parameters.
                                     Defaults to an empty dictionary.
            headers (dict, optional): A dictionary of header parameters.
                                     Defaults to an empty dictionary.

        Returns:
            requests.Response: The response object from the GET request if successful.
            None: If a URL-related error occurs.
        """
        try:
            # Automatically constructs the URL with the passed parameters.
            response = requests.get(url=url, params=params, headers=headers)
            return response
        except (
            requests.exceptions.URLRequired,
            requests.exceptions.MissingSchema,
            requests.exceptions.InvalidSchema,
            requests.exceptions.InvalidURL,
        ) as error:
            # Handle common URL-related exceptions gracefully.
            print(f"Request failed due to a URL error: {error}")
            return None


if __name__ == "__main__":
    # Instance of class.
    req = Req()

    # Define the base URL and the dictionary of parameters.
    target_url = "https://httpbin.org/headers"
    my_headers = {'User-Agent': 'Learning-Coach-App'}

    # Make the GET request, passing the parameters.
    target_response = req.get(target_url, headers=my_headers)

    # Check if the request was successful
    if target_response and target_response.status_code == 200:
        # Print the final URL
        print("--- Final URL ---")
        print(target_response.url)
        
        # Print the structured JSON content
        print("\n--- Response JSON ---")
        print(target_response.json())
    else:
        # Print a message with the status code if available.
        status_code = target_response.status_code if target_response else "N/A"
        print(f"Request failed with status code: {status_code}")