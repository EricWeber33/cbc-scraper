from bs4 import BeautifulSoup
import requests


# scrapes cbc and appends to file
def scrape():
    # download html content of CBC
    cbc_page = requests.get("https://www.cbc.ca/")

    if cbc_page.status_code != 200:
        print("web page could not be reached")
        return 1

    # create soup object
    soup = BeautifulSoup(cbc_page.content, 'html.parser')

    # get all headlines from featured article section
    featured_section = soup.find("section", class_="featuredArea sclt-featuredarea")
    headlines = featured_section.find_all("h3")

    # append to history file and write to recent file
    history_file = open("scrape_history.txt", "a")
    recent_file = open("last_scrape.txt", "w")

    history_file.write("\n\n")
    history_file.write("FEATURED NEWS\n")
    recent_file.write("FEATURED NEWS\n")

    for x in headlines:
        history_file.write(str(x).split('>')[1][:-4] + "\n")
        recent_file.write(str(x).split('>')[1][:-4] + "\n")

    more_stories_section = soup.find("section", class_="moreStoriesList")
    headlines = more_stories_section.find_all("h3")

    history_file.write("OTHER NEWS\n")
    recent_file.write("OTHER NEWS\n")

    for x in headlines:
        history_file.write(str(x).split('>')[1][:-4] + "\n")
        recent_file.write(str(x).split('>')[1][:-4] + "\n")

    history_file.close()
    recent_file.close()


def main():
    while True:
        user_choice = input("'s' to scrape cbc\n'q' to quit\n")
        if user_choice == "q":
            break
        elif user_choice == "s":
            scrape()


if __name__ == '__main__':
    main()
