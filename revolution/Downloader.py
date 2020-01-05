class Downloader:
    path = ""

    def __init__(self, path):
        print("You attempted to create a Downloader object, but this does nothing.")
        path = path
    
    # Automatically detect and attempt to download Wii video game
    # Download if direct link
    def download(self, url):
        print("Passed url", url)
        print("Will download to path", path)

    # Pass a list of URLs to the downloader to automatically download it
    def multidownload(self, list):
        print("Passed list", list)
        print("Will download to path", path)