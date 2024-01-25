"""
File: webcrawler.py
Name: Tina
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        header = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)"}
        response = requests.get(url, headers=header)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        tbody = soup.find('tbody')
        tags = tbody.find_all('tr')
        male_count = 0
        female_count = 0
        for tag in tags[:-1]:
            target = tag.find_all('td')
            male_count += int(target[2].text.replace(',', ''))
            female_count += int(target[4].text.replace(',', ''))
        print('Male Number: ' + str(male_count))
        print('Female Number: ' + str(female_count))



if __name__ == '__main__':
    main()
