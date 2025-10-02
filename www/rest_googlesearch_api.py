import requests
import json

# As a very simple REST demo, hit the Google Suggestion API endpoint.
SUGGEST_URL = "https://suggestqueries.google.com/complete/search"

def get_google_suggestions(query: str):
    """
    Sends a request to the Google Suggestion service and retrieves autocomplete suggestions.

    Args:
        query (str): The search term to get suggestions for.
    """
    print(f"--- Querying for: '{query}' ---")

    # Define the parameters for the GET request
    params = {
        'client': 'chrome',  # Makes service answer in simple JSON
        'q': query           # The search query
    }

    try:
        # 1. Send the REST request
        response = requests.get(SUGGEST_URL, params=params, timeout=5)

        # Raise an HTTPError for bad responses (4xx or 5xx)
        response.raise_for_status()

        # 2. Parse the JSON result
        # The 'client=chrome' response is typically a list:
        # [
        #   "query",
        #   ["suggestion 1", "suggestion 2", ...],  <- The list of suggestions is here
        #   [0, 0, ...],
        #   ["url1", "url2", ...]
        # ]
        data = response.json()
        # print("Raw Data:", data)
        
        # Check if the expected structure exists and is non-empty
        if isinstance(data, list) and len(data) > 1 and isinstance(data[1], list):
            suggestions = data[1]

            # 3. Print the results
            if suggestions:
                print(f"Found {len(suggestions)} suggestions:")
                for i, suggestion in enumerate(suggestions, 1):
                    print(f"  {i}. {suggestion}")
            else:
                print("No suggestions found for this query.")

        else:
            print("Error: Received unexpected data structure from the API.")
            print(f"Raw data start: {str(data)[:100]}...")


    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error occurred: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON response.")


if __name__ == "__main__":
    search_term = input("Enter query: ")
    if (not search_term):
        search_term = "darwin"

    get_google_suggestions(search_term)

