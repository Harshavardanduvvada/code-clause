import hashlib

# Dictionary to store the URL mappings
url_mapping = {}

def shorten_url(long_url):
    # Create a hash of the long URL
    hash_object = hashlib.md5(long_url.encode())
    short_url = hash_object.hexdigest()[:6]  # Use first 6 characters of hash
    
    # Store the mapping
    url_mapping[short_url] = long_url
    return short_url

def main():
    print("Welcome to the URL Shortener!")
    
    while True:
        long_url = input("Enter the long URL (or 'exit' to quit): ")
        if long_url.lower() == 'exit':
            break
            
        # Shorten the URL
        short_url = shorten_url(long_url)
        print(f"Shortened URL: http://short.url/{short_url}")

if __name__ == "__main__":
    main()
