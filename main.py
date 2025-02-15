def find_council(postcode):
    print(f"Finding the local authority for {postcode}...")
    
    # Most postcodes begin with two letters followed by a number (e.g. "AB1") 
    # but some begin with only one (e.g. "B1"). This if-statement checks for 
    # this and adjusts the search term accordingly.
    if postcode[1].isnumeric:
        filename_search = postcode[0]
    else:
        filename_search = postcode[:1]


if __name__ == "__main__":
    postcode = input("Please enter your postcode: ")
    find_council(postcode)