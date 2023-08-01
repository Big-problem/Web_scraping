import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # get the HTML
    URL = 'https://realpython.github.io/fake-jobs/'
    page = requests.get(URL)

    # create a Beautiful Soup object
    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(id='ResultsContainer')

    # returns an iterable, can access content using []
    job_elements = results.find_all("div", class_="card-content")

    # for job_element in job_elements:
    # title_element = job_element.find("h2", class_="title")
    # company_element = job_element.find("h3", class_="company")
    # location_element = job_element.find("p", class_="location")
    # print(title_element.text.strip())
    # print(company_element.text.strip())
    # print(location_element.text.strip())
    # print()

    # find tag with specific text
    python_jobs = results.find_all(
        "h2", string=lambda text: "python" in text.lower())
    # access parent elements
    python_job_elements = [
        h2_element.parent.parent.parent for h2_element in python_jobs
    ]

    for job_element in python_job_elements:
        # title_element = job_element.find("h2", class_="title")
        # company_element = job_element.find("h3", class_="company")
        # location_element = job_element.find("p", class_="location")
        # print(title_element.text.strip())
        # print(company_element.text.strip())
        # print(location_element.text.strip())
        # print()

        links = job_element.find_all("a", string='Apply')
        # 印出.text只會顯示實際看到的內容, 但像url是在a tag裡的href, 所以用[]選取
        for link in links:
            link_url = link["href"]
            print(f"Apply here: {link_url}\n")
