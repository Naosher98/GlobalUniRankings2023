from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
columns = ['World Rank','University Name', 'State', 'Country', 'Overall Score', 'Academic Reputation', 'Employer Reputation', 'Citations per Faculty', 'Faculty Students Ratio', 'International Students Ratio', 'International Faculty Ratio', 'International Research Network', 'Employment Outcomes', 'Page url', 'GMAT', 'IELTS', 'TOEFL', 'SAT', 'TOEFL']

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
    
def university_details(info):
    details = info.text.split('\n')
    contents = {}
    contents["Total students count"] = details[1]
    contents["UG student % (Domestic)"] = details[3]
    contents["PG student % (Domestic)"] = details[5]
    contents["International students count"] = details[7]
    contents["UG student % (International)"] = details[9]
    contents["PG student % (International)"] = details[11]
    contents["Total faculty staff count"] = details[13]
    contents["Domestic staff %"] = details[15]
    contents["International staff %"] = details[17]
    # print(contents)
    return contents

def main():
    url = "https://www.topuniversities.com/university-rankings/world-university-rankings/2023"
    webdriver_path = "C:\Program Files (x86)\WebDriver\chromedriver.exe"
    driver = webdriver.Chrome(webdriver_path)
    driver.maximize_window()
    time.sleep(3)
    driver.get(url)

     
    button_loc = driver.find_element(By.XPATH, '//div[contains(@class,"layout") and contains(@class,"layout--qsonecol")]')
    element_ind = button_loc.find_element(By.XPATH, '//*[@id="block-tu-d8-content"]/div/article/div/div/div[3]/div/div[1]/div/div[1]/div/div/ul/li[2]')
    actions = ActionChains(driver)
    actions.click(element_ind).perform()

    time.sleep(5)

    row_contents = []
    link_contents = []
    page_contents = []

    for i in range(144):
        indicator_tab = driver.find_element(By.ID, 'indicator-tab')
        ranking_data_load_ind = indicator_tab.find_element(By.ID, 'ranking-data-load_ind')
        rows = ranking_data_load_ind.find_elements(By.XPATH, '//div[contains(@class,"row") and contains(@class,"ind-row")]')
        for row in rows:
            if row.text == '':
                continue
            else:
                mem = get_text_details(row) 
                row_contents.append(mem)
                lnk = row.find_element(By.TAG_NAME, 'a')
                link_contents.append(lnk.get_attribute('href'))
        location = driver.find_element(By.CLASS_NAME, 'tab-content') 
        element = location.find_element(By.CSS_SELECTOR, 'a.page-link.next')
        
        if element != None:
            actions = ActionChains(driver)
            actions.click(element).perform()
        else:
            continue
        time.sleep(5)
    
    for j, lnk_url in enumerate(link_contents):
        driver.maximize_window()
        driver.get(lnk_url)
        time.sleep(3)
        # print('=======================')
        # print(j)
        location_new = driver.find_element(By.XPATH, '//div[contains(@class,"block") and contains(@class,"block-qs-profiles") and contains(@class,"block-university-information-profile2")]') 
        element_new = location_new.find_element(By.ID, 'studStaff_Tab')
        
        if element_new != None:
            actions = ActionChains(driver)
            actions.click(element_new).perform()
        else:
            continue
        time.sleep(5)
        student_class = driver.find_element(By.XPATH, '//div[contains(@class,"studstaff-subsection-parent")]')
        student_info = student_class.find_elements(By.XPATH, '//div[contains(@class,"studstaff-subsection")]')
        if student_info[0].text == '':
            continue
        else:
            page_contents.append(university_details(student_info[0]))
            # print(student_info[0].text)
    # print(page_contents)
    df_1 = pd.DataFrame(row_contents)
    df_2 = pd.DataFrame(page_contents)
    frames = [df_1, df_2]
    result = pd.concat(frames, axis=1)
    result.to_csv("data_3.csv")
    driver.close()
    return
if __name__ == "__main__":
    main()