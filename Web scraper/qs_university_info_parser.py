from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd


# University Details Extraction Function 
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
def error_func():
    contents = {}
    contents["Total students count"] = 0
    contents["UG student % (Domestic)"] = '0%'
    contents["PG student % (Domestic)"] = '0%'
    contents["International students count"] = 0
    contents["UG student % (International)"] = '0%'
    contents["PG student % (International)"] = '0%'
    contents["Total faculty staff count"] = 0
    contents["Domestic staff %"] = '0%'
    contents["International staff %"] = '0%'
    return contents

# Page button clicking and elements locating function
def page_items(df, driver, i):
    link_contents = list(df[df.columns[1]])
    page_contents = []
    for j, lnk_url in enumerate(link_contents):
        driver.maximize_window()
        driver.get(lnk_url)
        time.sleep(3)

        try:
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
                page_contents.append(error_func())
                continue
            else:
                page_contents.append(university_details(student_info[0]))
        except Exception:
            page_contents.append(error_func())
            continue
      
        
            
    df = pd.DataFrame(page_contents)
    df.to_csv(f"Data\Data_new{i}.csv")
    # driver.close()
    return

def main():
    webdriver_path = "C:\Program Files (x86)\WebDriver\chromedriver.exe"
    driver = webdriver.Chrome(webdriver_path)
    df = pd.read_csv("Data\Link.csv")
    
    
    df_1 = df.iloc[:250,:]
    page_items(df_1, driver, 1)
    
    df_2 = df.iloc[250:450,:]
    page_items(df_2, driver, 2)

    df_3 = df.iloc[450:650,:]
    page_items(df_3, driver, 3)

    df_4 = df.iloc[650:850,:]
    page_items(df_4, driver, 4)

    df_5 = df.iloc[850:1050,:]
    page_items(df_5, driver, 5)

    df_6 = df.iloc[1050:1250,:]
    page_items(df_6, driver, 6)

    df_7 = df.iloc[1250:,:]
    page_items(df_7, driver, 7)

    driver.close()
    return
if __name__ == "__main__":
    main()