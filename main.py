import csv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

# Return the local authority for the entered postcode.
def find_council(postcode):
    print(f"Finding the local authority for {postcode}...")
    
    # Most postcodes begin with two letters followed by a number (e.g. "AB1") 
    # but some begin with only one (e.g. "B1"). This if-statement checks for 
    # this and adjusts the search term accordingly.
    if postcode[1].isnumeric == True:
        filename_search = postcode[0]
    else:
        filename_search = postcode[:2]

    # Search the appropriate dataset for the postcode.
    with open(f"dataset/pcd_lad_aug_2023_{filename_search}.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == postcode:
                print(f"The local authority for {postcode} is {row[2]}.")
                next_bin_day(postcode, row[2])
        print("Postcode not found.")


# Return the next bin collection day for the entered postcode.
def next_bin_day(postcode, council):
    print(f"Finding the next bin collection day for {postcode}...")

    # Get the web page containing the council's bin collection information.
    with open("dataset/council_bin_collection_websites.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if council in row[0]:
                driver.get(row[3])

                # Enter the postcode into the appropriate field.
                postcode_input = driver.find_element(By.ID, row[1])
                postcode_input.send_keys(postcode)
                postcode_input.submit()

                # At this point the page should return a dropdown menu
                # containing all addresses associated with the postcode.
                # The user's house name/number is required to proceed.
                house_no = input("Please enter your house name or number: ")

                # Search the dropdown menu using the house name/number.
                house_no_input = Select(driver.find_element(By.ID, row[2]))
                for option in house_no_input.options:
                    if house_no in option.text:
                        house_no_input.select_by_visible_text(option.text)
                        house_no_input.submit()

                        # Find the household waste collection date.
                        household_element = driver.find_element(By.XPATH, 
                                                                "//*[contains(text(), 'household')]")
                        household_date = household_element.find_element(
                            By.XPATH, 
                            f"following::td[contains(text(), {datetime.now().year})][1]").text
                        
                        # Find the recycling collection date.
                        recycling_element = driver.find_element(By.XPATH, 
                                                                "//*[contains(text(), 'recycling')]")
                        recycling_date = recycling_element.find_element(
                            By.XPATH, 
                            f"following::td[contains(text(), {datetime.now().year})][1]").text
                        
                        # Print the collection dates.
                        print(f"The next household waste collection date for {postcode} is: {household_date}")
                        print(f"The next recycling bin collection date for {postcode} is: {recycling_date}")
                        print(f"For more information, check the council's website: {row[1]}")
                        return
                print(f"Bin collection information for {house_no} could not be found.")
        print(f"Bin collection information for {council} could not be found.")


if __name__ == "__main__":
    postcode = input("Please enter your postcode: ")
    find_council(postcode)