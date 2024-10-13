import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_department(department_url, department_name):
    response = requests.get(department_url) #for retrieving contents of webpage

    soup = BeautifulSoup(response.content, 'html.parser')
    #allows us to easily search and find elements

    # find all faculty cards on the page
    faculty_cards = soup.select('.card') #retriveing card's info for every card class name

    faculty_data = [] #this will hold faculty info

    for card in faculty_cards:
        # extracting faculty details
        # h5 tag stores faculty member's name
        #text.strip for cleaning any unwanted spaces
        name = card.find('h5').text.strip() if card.find('h5') else "No Name"
        #for getting faculty meme's title
        designation = card.find('p', class_='small text-center font-italic').text.strip() if card.find('p',
                                                                                                       class_='small text-center font-italic') else "No Designation"
        hec_supervisor = "Yes" if "HEC Approved PhD Supervisor" in designation else "No"
        #anchor tag a contains email
        email_tag = card.find('a', href=True)
        email = email_tag.text.strip() if email_tag else "No Email"

        # Append the data to the list
        faculty_data.append(
            [name, designation, hec_supervisor, email, department_name])

    if faculty_data:
        print(f"Scraped {len(faculty_data)} faculty members from {department_name}.")
    else:
        print(f"No faculty data found for {department_name}.")

    return faculty_data


# URLs for each department
departments = {
    'School of Computing': 'http://lhr.nu.edu.pk/faculty',
    'Electrical Engineering': 'http://lhr.nu.edu.pk/ee/faculty/',
    'Civil Engineering': 'http://lhr.nu.edu.pk/cv/faculty/',
    'School of Management': 'http://lhr.nu.edu.pk/fsm/faculty/',
    'Science & Humanities': 'http://lhr.nu.edu.pk/ss/faculty/'
}

all_data = []

# Scraping of data for each department
for department_name, department_url in departments.items():
    faculty_data = scrape_department(department_url, department_name)

    if faculty_data:
        #a pandas dataframe is created and column names are specified
        df = pd.DataFrame(faculty_data,
                          columns=['Name', 'Designation', 'HEC Approved PHD Supervisor', 'Email', 'Department'])
        #generation of a file name by replacing spaces by underscores
        output_csv = f"{department_name.replace(' ', '_').lower()}.csv"
        #saving csv
        df.to_csv(output_csv, index=False)
        all_data.append(df)

# Merge all department DataFrames
if all_data:
    merged_df = pd.concat(all_data, ignore_index=True)
    merged_df.to_csv('fast_lhr_faculty.csv', index=False)
    print("Merged data saved to fast_lhr_faculty.csv.")
else:
    print("No data to merge.")
