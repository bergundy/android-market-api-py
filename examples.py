from pprint import pprint
from googleplay_api import PlayStoreSession, playstore_proto
from sys import exit

import getpass


if __name__ == "__main__":
    # Start a new session and login
    email = raw_input("Email: ")
    passwd = getpass.getpass()
    session = PlayStoreSession()
    session.login(email, passwd)

    # Search for "bankdroid" on the market and print the first result
    results = session.searchApp("bankdroid")
    if len(results) == 0:
        print "No results found"
        exit()

    app = results[0]
    pprint(app)

    # Print the last two comments for the app
    results = session.getComments(app["id"])
    pprint(results[:2])

    # Download and save the first screenshot
    data = session.getImage(app["id"])
    with open("screenshot.png", "wb") as f:
        f.write(data)

    # Download and save the app icon
    data = session.getImage(app["id"], imagetype=playstore_proto.GetImageRequest.ICON)
    with open("icon.png", "wb") as f:
        f.write(data)

    # Get all the categories and subcategories
    results = session.getCategories()
    pprint(results)
