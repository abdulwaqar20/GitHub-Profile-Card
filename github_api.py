import requests

BASE_URL = "https://api.github.com"


def get_user_profile(username):
    """Fetch GitHub user profile information."""

    url = f"{BASE_URL}/users/{username}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 404:
            print("Error: GitHub username not found.")

        elif response.status_code == 403:
            print("Error: GitHub API rate limit exceeded.")

        else:
            print(f"API Error: {response.status_code}")

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")

    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")

    return None


def get_user_repositories(username):
    """Fetch public repositories."""

    url = f"{BASE_URL}/users/{username}/repos"

    try:
        response = requests.get(
            url,
            params={"per_page": 100, "sort": "updated"},
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Repository API error: {e}")
        return None