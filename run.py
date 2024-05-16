from web_flask import app
"""run the application"""

if __name__ == "__main__":
    """ Main Function """
    # debug mode use for not restart your app after each modification
    # after finishing the app you should off debug mode
    app.run(host='0.0.0.0', port=5000)
