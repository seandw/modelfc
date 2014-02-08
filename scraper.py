"""
A scraping script to get results from (specific) HTML pages into a
leaner format.
"""
import sys
import json
from bs4 import BeautifulSoup

def scrape(html):
    """
    Generates JSON output with the meaningful bits of the HTML input.
    """
    soup = BeautifulSoup(html)

    home_teams = soup.find_all("div", class_="field-home-team")
    away_teams = soup.find_all("div", class_="field-away-team")
    scores = soup.find_all("div", class_="field-score")

    results = [{"home": home.string,
                "away": away.string,
                "score": score.string.strip()}
               for (home, away, score) in zip(home_teams, away_teams, scores)]

    return json.dumps(results, indent=2)

if __name__ == "__main__":
    for name in sys.argv[1:]:
        output = open(name.replace("html", "json"), "w")
        output.write(scrape(open(name).read()))
