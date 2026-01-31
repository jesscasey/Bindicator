import csv
import os
from pathlib import Path
import requests
from ckanapi import RemoteCKAN

COUNCIL_DATA_FILE = "dataset/council_bin_collection_websites.csv"

def get_council_data(refresh):
    """
    Retrieve council bin collection websites using the data.gov.uk API, then 
    cache the data for future use.
    
    Args:
        refresh (bool): If True, force-refetch from data.gov.uk. Otherwise, 
        use the cached file.
    
    Returns:
        str: CSV data as a string, or None if fetch fails.
    """
    if not refresh and os.path.exists(COUNCIL_DATA_FILE):
        # Retrieve cached data
        print(f"Loading council data from {COUNCIL_DATA_FILE}...")
        try:
            with open(COUNCIL_DATA_FILE, 'r') as f:
                return f.read()
        except Exception as e:
            print(f"Warning: could not read cached council data: {e}")
            return None

    try:
        # Fetch council website data
        ckan = RemoteCKAN('https://data.gov.uk/')
        council_websites = ckan.action.package_show(id='local-authority-services')
        csv_url = council_websites['resources'][0]['url']
        csv_data = requests.get(csv_url).content.decode('utf-8')
        
        # Cache the data
        os.makedirs(Path(COUNCIL_DATA_FILE).parent, exist_ok=True)
        with open(COUNCIL_DATA_FILE, 'w') as f:
            f.write(csv_data)
        
        print(f"Council data has been cached to {COUNCIL_DATA_FILE}")
        return csv_data
    
    except Exception as e:
        print(f"Error: could not fetch council data: {e}")
        return None
