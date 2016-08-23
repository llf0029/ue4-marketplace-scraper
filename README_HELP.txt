#=============================================================================#
|                     Unreal Engine 4 Marketplace Scraper                     |
#=============================================================================#
| Author:       Lyndon Forsythe                                               |
| Date:         23 August 2016                                                |
|                                                                             |
| Description:  Scrapes the Unreal Engine 4 Marketplace, collating asset      |
|               information including the name, price, URL, and image.        |
|                                                                             |
|               This document will outline the application usage.             |
#=============================================================================#

#=============================== REQUIREMENTS ================================#
Execute the following command in Windows Command Prompt to install all required
dependences: 
    pip install -r requirements.txt

#============================== QUICK RUN MODE ===============================#
To perform a quick query, execute the file "__main__.py" in the Windows Command
Prompt, along with arguments as described below.

Usage:
    __main__.py [-h] [-s QUERY | -c CATEGORY]

Arguments:
    -h, --help                display help documentation
    -s, --search QUERY        search marketplace by keyword
    -c, --category CATEGORY   search marketplace by category

Examples:
    __main__.py --search fire effects
    __main__.py -s fire effects
    __main__.py --category blueprints
    __main__.py -c blueprints

#============================= INTERACTIVE MODE ==============================#
Launching the application in Interactive Mode allows for a much wider range of
options and functionality. To launch Interactive Mode, simply execute the file
"__main__.py" without any arguments.

Usage:
    __main__py

Commands:
    HELP
        Display help documentation for a topic.
        Example: help search

    SEARCH
        Find marketplace items by keyword(s).
        Example: search fire effects

    SEARCH_RESULTS
        Limit the number of search results. Default is 10.
        Example: search_results 50

    CATEGORY
        Find marketplace items by category. There are a specific set of 
        categories that can be viewed by calling the "help category" command.
        Category query will find 25 items at most.
        Example: category blueprints

    VIEW_ASSET_IMAGE
        Displays the image of a selected asset from the previous query.
        Example: view_asset_image 4

    ANALYSE_RESULTS
        Generates and displays a chart comparing asset prices from the previous
        query. Maximum of 60 assets.
        Example: analyse_results

    SAVE
        Stores the results of the previous query for later use. Only one query
        may be stored at a time.
        Example: save

    LOAD
        Loads and displays the previously stored query.
        Example: load

    WISHLIST_ADD
        Adds an item from the previous query to your asset wishlist.
        Example: wishlist_add 4

    WISHLIST_VIEW
        Displays all assets in your wishlist, along with their images.
        Example: wishlist_view

    WISHLIST_CLEAR
        Permanently erases the contents of your wishlist. Use with caution!
        Example: wishlist_clear

    EXIT
        Shuts down the Unreal Engine 4 Marketplace Scraper app.
        Example: exit
