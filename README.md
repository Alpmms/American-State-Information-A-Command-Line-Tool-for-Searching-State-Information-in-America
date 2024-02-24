# American-State-Information-A-Command-Line-Tool-for-Searching-State-Information-in-America
American State Information: A Command-Line Tool for Searching State Information in America

This project is a command-line tool that allows users to search for information about states in America. The user can search by state name, abbreviation, or capital city. The tool is implemented using Python and the argparse library for parsing command-line arguments.

The user can run the script from the command line by providing the appropriate argument. For example, to search by state name, the user can run python american_state_information.py -n Alabama. To search by abbreviation, the user can run python american_state_information.py -a AZ. To search by capital city, the user can run Python american_state_information.py -c Phoenix.

The script contains a dictionary called states_info that stores each state's information. The dictionary's keys are the state names, and the values are dictionaries containing each state's abbreviation and capital city.

The script defines three functions: search_by_name, search_by_abbreviation, and search_by_capital. Each function inputs a search term and searches the states_info dictionary for a matching state. If a matching state is found, the function returns the state information. Otherwise, it returns None.

The main function is the entry point of the script. It uses the argparse library to parse the command-line arguments. If the user provides a search term, the script searches for the matching state using the appropriate search function. If no matching state is found, the script prints a message indicating that no matching state was found.

To use this tool, the user must have Python installed on their computer. They can then run the script from the command line by providing the appropriate argument. The script will then search for the matching state and print the state information.

This project is a good starting point for data analysts who want to improve their Python skills and learn how to create command-line tools. It also serves as a useful reference for users searching for information about states in America.
