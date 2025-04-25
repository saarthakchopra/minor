import os
import time
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

def get_chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    # options.add_argument('--headless')
    options.add_argument('--disable-blink-features=AutomationControlled')
    return options

def get_gsid_for_name(name: str, driver: webdriver.Chrome, wait: WebDriverWait) -> str:
    """
    Go to the author‐search results for `name` with 'google scholar jiit' appended.
    If the first result has a 'Verified email at jiit.ac.in' badge,
    extract and return its GSID. Otherwise return "Not Found".
    """
    # Add "google scholar jiit" to the query for better matching
    query = (name + ' jiit').replace(' ', '+')
    search_url = f"https://scholar.google.com/citations?view_op=search_authors&mauthors={query}"
    driver.get(search_url)

    try:
        # 1) Wait for the first author card's name link
        profile_link = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'h3.gs_ai_name a'))
        )

        # 2) Check the little email‐badge on that same card
        try:
            email_badge = driver.find_element(By.CSS_SELECTOR, '.gs_ai_eml').text
            if 'jiit.ac.in' not in email_badge.lower():
                return "Not Found"
        except NoSuchElementException:
            return "Not Found"

        # 3) Extract GSID from the profile URL
        href = profile_link.get_attribute('href')
        return href.split('user=')[1].split('&')[0]

    except Exception:
        return "Not Found"


def main():
    faculty_names = ["Prof. Sandeep Kumar Singh", "Prof. Krishna Asawa", "Prof. Manish Kumar Thakur", "Prof. Shikha Mehta", "Prof. Anuja Arora", "Prof. Lokendra Kumar", "Prof. Bhagwati Prasad Chamola", "Prof. Pato Kumari", "Prof. Devpriya Soni", "Prof. Neetu Sardana", "Prof. Dharmveer Singh Rajpoot", "Prof. Mukesh Saraswat", "Dr. Tribhuwan Kumar Tewari", "Dr. Prakash Kumar", "Dr. K. Rajalakshmi", "Dr. Parmeet Kaur", "Dr. Mukta Goyal", "Dr. Anita Sahoo", "Dr. Himani Bansal", "Dr. Taj Alam", "Dr. Suma Dawn", "Dr. Arti Jain", "Dr. Hema Nagaraja", "Dr. Pawan Kumar Upadhyay", "Dr. Kavita Pandey", "Dr. Indu Chawla", "Dr. Shikha Jain", "Dr. Megha Rathi", "Dr. Dhanalekshmi G", "Dr. Himanshu Agrawal", "Dr. Anubhuti Roda Mohindra", "Dr. Niyati Aggrawal", "Dr. Gaurav Kumar Nigam", "Dr. Amanpreet Kaur", "Dr. Pulkit Mehndiratta", "Dr. Arpita Jadhav Bhatt", "Ms. Anuradha Gupta", "Dr. Shardha Porwal", "Dr. Sakshi Gupta", "Dr. Parul Agarwal", "Dr. Ankita", "Dr. Somya Jain", "Prashant Kaushik", "Dr. Aditi Sharma", "Dr. Varsha Garg", "Dr. Kashav Ajmera", "Dr. Kirti Aggarwal", "Dr. P. Raghu Vamsi", "Dr. Payal Khurana Batra", "Dr. Ankit Vidyarthi", "Dr. Ankita Verma", "Dr. Amarjeet Prajapati", "Dr. Neeraj Jain", "Dr. Rashmi Kushwah", "Dr. Shruti Jaiswal", "Dr. Sonal", "Dr. Vivek Kumar Singh", "Dr. Alka Singhal", "Dr. Ashish Mishra", "Dr. Sulabh Tyagi", "Dr Bhawna Saxena", "Dr. Vikash", "Ashish Kumar", "Dr. Kapil Madan", "Dr. Pratik Shrivastava", "Dr. Amit Mishra", "Dr. Ashish Singh Parihar", "Dr. Asmita Yadav", "Dr. Anil Kumar Mahto", "Dr. Jagriti", "Dr. Meenal Jain", "Dr. Ankita Jaiswal", "Dr. Deepika Varshney", "Akanksha Mehndiratta", "Amarjeet Kaur", "Dr. Sherry Garg", "Dr. Naveen Chauhan", "Dr. Shobhit Tyagi", "Purtee Jethi Kohli", "Prantik Biswas", "Dr. Neeraj Pathak", "Dr. Akash Kumar", "Dr. Tanvi Gautam", "Dr. Jasmin", "Dr. Kedar Nath Singh", "Dr. Sayani Ghosal", "Dr. Aastha Maheshwari", "Dr. Shruti Gupta", "Dr. Tarun Agrawal", "Dr. Diksha Chawla", "Dr. Varun Srivastava", "Dr. Mradula Sharma", "Kirti Jain", "Deepti", "Shariq Murtuza", "Sarishty Gupta", "Amitesh", "Ambalika Sarkar Bachar", "Pushp S. Mathur", "Dr. Lalita Mishra", "Twinkle Tyagi", "Rajiv Kumar Mishra", "Astha Singh", "Anupama Padha", "Aarti Goel", "Janardan Kumar Verma", "Neha", "Akshit Raj Patel", "Sumeshwar Singh", "Ayushi Pandey", "Aditi Priya", "Shivendra Vikram Singh", "Sonal Saurabh", "Satya Prakash Patel", "Mohit Singh", "Pankaj Mishra", "Shweta Rani", "Richa Kushwaha", "Prateek Kumar Soni", "Mr. Megh Singhal", "Niveditta Batra", "Prakhar Mishra", "Anuja Shukla", "Ritika Chaudhary", "Mayuri Gupta"]

    output_path = 'faculty_gsid.csv'
    cols = ['Name', 'GSID']

    # If the file exists, we append; otherwise we'll write header on first write.
    file_exists = os.path.exists(output_path)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=get_chrome_options()
    )
    wait = WebDriverWait(driver, 10)

    for name in faculty_names:
        print(f"Searching GSID for: {name}")
        gsid = get_gsid_for_name(name, driver, wait)
        print(f" → {gsid}\n")

        # Write this single row immediately
        row_df = pd.DataFrame([[name, gsid]], columns=cols)
        row_df.to_csv(
            output_path,
            mode='a',
            header=not file_exists,
            index=False
        )
        file_exists = True  # after first write, always append
        time.sleep(random.uniform(2, 4))

    driver.quit()
    print(f"✅ Done. Results in `{output_path}`")


if __name__ == '__main__':
    main()
