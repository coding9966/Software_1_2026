import requests

def get_random_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data["value"])  # Only print the joke text
    else:
        print("Failed to fetch joke.")

if __name__ == "__main__":
    get_random_joke()