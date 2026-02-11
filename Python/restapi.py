import requests # makes HTTP calls (GET, POST, etc.), install requests using command "py -m pip install requests"
from requests.adapters import HTTPAdapter # plugs retry behavior into requests
from urllib3.util.retry import Retry # defines how retries should work

def create_session_with_retries(
    retries=3, # Retries failed requests for 3 times
    backoff_factor=0.5, # Waits longer after each failure
    status_forcelist=(500, 502, 503, 504) # Retries only for specific server errors
):
    """
    Create a requests session with retry logic.
    """
    session = requests.Session() # Session is browser-like object that remembers how to make requests, Reuses TCP connections (faster), Shares headers, cookies, timeouts and Applies adapters (like retry logic)

    # Call the Retry class (which was defined in 'urllib3.util.retry') object to create an instance or calling the constructor
    retry = Retry(
        total=retries, # total=3 as retries=3 → max 3 retry attempts
        read=retries, # retry if reading response fails
        connect=retries, # retry if connection fails
        backoff_factor=backoff_factor, # wait time between retries 0.5s → 1s → 2s
        status_forcelist=status_forcelist, # retry only for server errors as we mentioned in function arguments
        allowed_methods=["GET"]
    ) 

    adapter = HTTPAdapter(max_retries=retry) # Use the above retry logic for all HTTP and HTTPS requests
    # Adapter = “rulebook for how requests are sent”. An HTTPAdapter controls: How connections are created, Whether retries happen, How errors are handled
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    return session


def fetch_github_repos(username):
    url = f"https://api.github.com/users/{username}/repos" # f is formated string, it will replace the value of username with the given value
    session = create_session_with_retries()

    try:
        response = session.get(url, timeout=5, verify=False) # making the request, timeout=5 → fail fast if server is slow, Prevents hanging forever, verify=False: Do NOT verify the server’s SSL certificate
        response.raise_for_status()  # Raises HTTPError for 4xx/5xx automatically

        repos = response.json()
        return repos # API returns JSON → parsed into: List of dictionaries

    except requests.exceptions.Timeout: # Server didn’t respond in time
        print("❌ Request timed out")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
    except ValueError:
        print("❌ Failed to parse JSON response")

    return None


def parse_and_display(repos):
    if not repos:
        print("No data to display.")
        return

    print("\n📦 Public Repositories:\n")
    for repo in repos:
        name = repo.get("name")
        stars = repo.get("stargazers_count")
        language = repo.get("language")
        url = repo.get("html_url")

        print(f"- {name}")
        print(f"  ⭐ Stars: {stars}")
        print(f"  🧠 Language: {language}")
        print(f"  🔗 URL: {url}\n")


# Run this code only if this file is executed directly, not when it’s imported
if __name__ == "__main__":
    username = "manaswini3103"  # change to any GitHub username
    repos = fetch_github_repos(username)
    parse_and_display(repos)

# output
# C:\Users\chennasa\AppData\Roaming\Python\Python312\site-packages\urllib3\connectionpool.py:1097: InsecureRequestWarning: Unverified HTTPS request is being made to host 'api.github.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
#   warnings.warn(
# 
# 📦 Public Repositories:
# 
# - devops-learning
#   ⭐ Stars: 0
#   🧠 Language: Python
#   🔗 URL: https://github.com/manaswini3103/devops-learning
# 
# - MavenHelloWorld
#   ⭐ Stars: 0
#   🧠 Language: Java
#   🔗 URL: https://github.com/manaswini3103/MavenHelloWorld
# 
# - Testing-Repo
#   ⭐ Stars: 0
#   🧠 Language: None
#   🔗 URL: https://github.com/manaswini3103/Testing-Repo
