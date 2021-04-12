from file_drivers import info
from utils.colors import paint

def run ():
    current_version = info.get ("version")

    HEADER = paint ("Relief", "magenta") + " " + current_version + "\n  By " + paint ("Juan Saez", "yellow")

    print (HEADER)