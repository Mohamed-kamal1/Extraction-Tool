# URL Extraction Tool

This is a Python script that extracts URLs from a website recursively up to a user-defined depth.

## Explanation 

The code extracts URLs from a website recursively up to a user-defined depth. It uses the `requests` module to send HTTP requests to the website and the `beautifulsoup4` module to parse the HTML content of the website and extract the URLs using the `find_all` method. The extracted URLs are then filtered to remove any URLs that do not start with `http` or `https`. The recursion depth is controlled by a command-line argument. The extracted URLs are printed on the console.


## Dependencies

- Python 3.x
- requests
- beautifulsoup4

## Usage

- `<url>`: The URL to extract.
- `--depth <depth>`: The maximum recursion depth (default: 1).

## Example

(python extract_urls.py https://www.wikipedia.org --depth 2)  
- This command extracts URLs from `https://www.wikipedia.org` recursively up to a depth of `2`.
- The output will be saved in `urls.txt` file .





