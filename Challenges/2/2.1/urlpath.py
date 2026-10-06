from urllib.parse import urlparse

def getpath(url: str) -> str:
    return urlparse(url)[2]

def main():
    print(getpath("https://example.com/"))
    print(getpath("https://example.com/foo"))
    print(getpath("https://example.com/bar.txt"))
    print(getpath("https://example.com/baz/foo/bar.git"))

if __name__ == "__main__":
    main()