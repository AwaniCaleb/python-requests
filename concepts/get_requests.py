import requests


class Req:
    def __init__(self) -> None:
        pass
    
    def get(self, url: str = None) -> requests.Response:
        try:
            return requests.get(url=url)
        except (
            requests.exceptions.URLRequired, requests.exceptions.MissingSchema,
            requests.exceptions.InvalidSchema, requests.exceptions.InvalidURL
        ) as error:
            print(f"Request failed due to a URL error: {error}")


if __name__ == "__main__":
    req = Req()
    target_url = "https://api.github.com/events"

    target_response = req.get(target_url)