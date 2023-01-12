# Global University Rankings 2023: A Comparative Analysis

## Project Objective: 
In order to provide a comprehensive and up-to-date understanding of the leading universities in the world, this project aims to collect information on the top-ranked universities in 2023 by utilizing the [QS world university rankings](https://www.topuniversities.com/university-rankings/world-university-rankings/2023) as the primary data source. This will involve web scraping the ranking data to gather information on various indicators of university performance, such as academic reputation, faculty and research achievements, and student success. The gathered data will be used to gain insights into the current state of higher education and to identify key trends and patterns in the field. Additionally, the resulting data will be provided in an easily accessible format to serve as a valuable resource for students, parents, educators, and researchers to make informed decisions about higher education.

## Methodology:
1. Data collection from QS World University Ranking using the Selenium web scraping framework.
2. Data processing, which includes tasks such as data merging, splitting, cleaning, and formatting to ensure consistency and accuracy.
3. Data visualization and analysis using Tableau Software, a powerful tool for creating interactive data visualizations and dashboards.
4. Identification of meaningful insights and patterns from the Tableau Dashboard, utilizing advanced analytical techniques to uncover key findings and trends.

## Visualization [Dashboard](https://public.tableau.com/app/profile/naosher.mustakim/viz/QSWorldUniversityRankings2023/Dashboard1?publish=yes) 

## Build from sources:
1. Clone the repository:
```bash
git clone https://github.com/Naosher98/Global-University-Rankings-2023-A-Comparative-Analysings-2023.git
```
2. Initialize and activate a virtual environment:
```bash
virtualenv --no-site-packages  venv
source venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Download Chrome WebDriver from https://chromedriver.chromium.org/downloads
5. Run the `qs_ranking_scraper` script:
```bash
python Web scraper\qs_ranking_scraper.py --chromedriver_path <path_to_chromedriver>
```
6. Run the `qs_university_info_parser` script:
```bash
python Web scraper\qs_university_info_parser.py --chromedriver_path <path_to_chromedriver>
```
7. Run all cells of the `Data_Processing` notebook. This will generate a file named "QS World University Rankings 2023 modified.csv" containing all the required fields. Alternatively, you can access the scraped data at ["QS World University Rankings 2023 modified.csv"](https://github.com/Naosher98/Global-University-Rankings-2023-A-Comparative-Analysings-2023/blob/main/Data/QS%20World%20University%20Rankings%202023%20modified.csv).

