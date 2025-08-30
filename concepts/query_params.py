import requests

class Query_Params():
    def __init__(self) -> None:
        super().__init__()
    
    def get(self, url: str = None, params: dict = {}) -> requests.Response | None:
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
            return requests.get(url=url, params=params)
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
    req = Query_Params()
    
    target_url = "https://httpbin.org/get"
    params = {"time": "now"}

    target_response = req.get(target_url, params)

    if target_response.status_code == 200:
        print(target_response.text)