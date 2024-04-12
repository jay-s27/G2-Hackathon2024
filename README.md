# G2 HACKATHON 2024 - Problem Statement 1

**Statement Summary:** To identify products that have not been listed on G2 platform   

## Approach
- To collect data from various sources from the net requires web scraping
- This code scrapes sites like producthunt.com for the *Upcoming Releases*
- Web scraping script is implemented using Python.
- The name of the to-be released apps are stored into a csv file
- An API is used to retrieve data from the G2 website and is compared with the products scraped from other sites.
- In case the product is not available in G2, the product name is printed.
  

## Web Scraping   
- BeautifulSoup, requests library in Python are used to scrape the site
- `find()`, `find_all()` functions are used to access the elements(or tags) in the web page
- The class names of the tag are used to narrow down to the exact tag that is required, this can be used as an arguement in the `find()` function. 
- The `find_all()` function is used to retirieve all the tags mentioned as the arguement.
- Tags are navigated till the required data is found
- `.text` is then used to retrieve the name of the product
