# File Name : JSON.py
# Student Name: Ray Happel, Andrew Rozsits, Nate Hoang, Liam Vasey
# email:  happelrc@mail.uc.edu,
# Assignment Number: Assignment 10
# Due Date:   04/10/2025
# Course #/Section:   IS 4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  In this assignment, we are exeuting an API call using a specfic URL that we selected.

# Brief Description of what this module does. We are learning about how to incorporate API files to aggreagate data from JSON files.
# Citations: {"Stack Overflow" is not sufficient. Provide repeatable links, book page #, etc.}

# Anything else that's relevant:

import requests
import json
import csv

class NYCDataFetcher:
    def __init__(self, url: str):  # The constructor
        """
        Initialize with the API URL
        @param url: The API endpoint where we will fetch the data from
        """
        self.url = url
        self.data = {}

    def fetch_data(self) -> dict: # Now we have a data dictionary
        """
        Fetches the data from the API and stores the JSON response
        @return: Parsed JSON data as a Python dictionary
        """
        response = requests.get(self.url) 
        response.raise_for_status() # Raising an exception if the response code is not successful
        self.data = response.json() # Parse the JSON response and store it in the data attribute
        return self.data

