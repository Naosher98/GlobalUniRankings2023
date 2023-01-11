# Dependencies
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd

# Informations that are extracted
columns = ['World Rank','University Name', 'State', 'Country', 'Overall Score', 'Academic Reputation', 'Employer Reputation', 'Citations per Faculty', 'Faculty Students Ratio', 'International Students Ratio', 'International Faculty Ratio', 'International Research Network', 'Employment Outcomes', 'Total students count','UG student % (Domestic)','PG student % (Domestic)','International students count','UG student % (International)','PG student % (International)','Domestic staff %', 'International staff %','Total faculty staff count']

# Function that returns extracted information in dictionary format
def get_text_details(row):     
    details = row.text.split('\n')
    contents = {}
    contents["World Rank"] = details[0]
    contents["University Name"] = details[1]
    contents["Country"] = details[2].strip()
    if details[4] == 'QS Stars':
        contents["Overall Score"] = details[5]
        contents["Academic Reputation"] = details[6]
        contents["Employer Reputation"] = details[7]
        contents["Citations per Faculty"] = details[8]
        contents["Faculty Students Ratio"] = details[9]
        contents["International Students Ratio"] = details[10]
        contents["International Faculty Ratio"] = details[11]
        contents["International Research Network"] = details[12]
        contents["Employment Outcomes"] = details[11]
    else:
        contents["Overall Score"] = details[3]
        contents["Academic Reputation"] = details[4]
        contents["Employer Reputation"] = details[5]
        contents["Citations per Faculty"] = details[6]
        contents["Faculty Students Ratio"] = details[7]
        contents["International Students Ratio"] = details[8]
        contents["International Faculty Ratio"] = details[9]
        contents["International Research Network"] = details[10]
        contents["Employment Outcomes"] = details[11]
    return contents
    

def main():
    url = "https://www.topuniversities.com/university-rankings/world-university-rankings/2023"
    webdriver_path = "C:\Program Files (x86)\WebDriver\chromedriver.exe"
    driver = webdriver.Chrome(webdriver_path)
    driver.maximize_window()
    time.sleep(3)
    driver.get(url)

    # Finding and performing clicking operation on the "Ranking Indicator" button
    button_loc = driver.find_element(By.XPATH, '//div[contains(@class,"layout") and contains(@class,"layout--qsonecol")]')
    element_ind = button_loc.find_element(By.XPATH, '//*[@id="block-tu-d8-content"]/div/article/div/div/div[3]/div/div[1]/div/div[1]/div/div/ul/li[2]')
    actions = ActionChains(driver)
    actions.click(element_ind).perform()

    # Setting the window open time to 5 seconds 
    time.sleep(5)

    row_contents = []
    link_contents = []

    # Iterating through all 143 pages of the website
    for i in range(144):
        # Elements that contain university data 
        indicator_tab = driver.find_element(By.ID, 'indicator-tab')
        ranking_data_load_ind = indicator_tab.find_element(By.ID, 'ranking-data-load_ind')
        rows = ranking_data_load_ind.find_elements(By.XPATH, '//div[contains(@class,"row") and contains(@class,"ind-row")]')
        # Iterating through each elements
        for row in rows:
            if row.text == '':
                continue
            else:
                # Extracting information from text
                mem = get_text_details(row) 
                row_contents.append(mem)
                # Extracting links of individual university
                lnk = row.find_element(By.TAG_NAME, 'a')
                link_contents.append(lnk.get_attribute('href'))
        # Finding the next page button
        try:
            location = driver.find_element(By.CLASS_NAME, 'tab-content') 
            element = location.find_element(By.CSS_SELECTOR, 'a.page-link.next')
        except Exception:
            element =None
        # Performing clicking operation on the next page button
        if element != None:
            actions = ActionChains(driver)
            actions.click(element).perform()
        else:
            continue
        time.sleep(5)
    
    
    # Creating dataframes 
    df_1 = pd.DataFrame(row_contents)
    df_2 = pd.DataFrame(link_contents)
    
    # Exporting the dataframes to CSV format
    df_1.to_csv("data.csv")
    df_2.to_csv("data_2.csv")
    driver.close()
    return
if __name__ == "__main__":
    main()