#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import argparse

# Dictionary of states with their information
states_info = {
    "Alabama": {"abbreviation": "AL", "capital": "Montgomery"},
    "Alaska": {"abbreviation": "AK", "capital": "Juneau"},
    "Arizona": {"abbreviation": "AZ", "capital": "Phoenix"},
    "Arkansas": {"abbreviation": "AR", "capital": "Little Rock"},
    "California": {"abbreviation": "CA", "capital": "Sacramento"},
    # ... Add more states here ...
}

def search_by_name(name):
    if name in states_info:
        return states_info[name]
    else:
        return None

def search_by_abbreviation(abbreviation):
    for state, info in states_info.items():
        if info["abbreviation"] == abbreviation:
            return info
    return None

def search_by_capital(capital):
    for state, info in states_info.items():
        if info["capital"] == capital:
            return info
    return None

def main():
    parser = argparse.ArgumentParser(description="Search for information about states in America.")
    parser.add_argument("-n", "--name", help="Search by state name.")
    parser.add_argument("-a", "--abbreviation", help="Search by state abbreviation.")
    parser.add_argument("-c", "--capital", help="Search by capital city.")
    args = parser.parse_args()

    if args.name:
        result = search_by_name(args.name)
    elif args.abbreviation:
        result = search_by_abbreviation(args.abbreviation)
    elif args.capital:
        result = search_by_capital(args.capital)
    else:
        parser.print_help()
        return

    if result:
        print(f"Name: {result['abbreviation']}")
        print(f"Abbreviation: {result['abbreviation']}")
        print(f"Capital: {result['capital']}")
    else:
        print("No matching state found.")

if __name__ == "__main__":
    main()

