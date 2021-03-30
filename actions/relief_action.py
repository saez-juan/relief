from file_drivers import info
from utils import colors

def run ():
    current_version = info.get ("version")
    HEADER = colors.paint ("Relief", "magenta") + " " + current_version + "\n  By " + colors.paint ("Juan Saez", "yellow")

    print (HEADER)