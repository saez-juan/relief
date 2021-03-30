import info
import colors

def run ():
    current_version = info.get ("version")
    HEADER = colors.paint ("Relief", "magenta") + " " + current_version + "\n  By " + colors.paint ("Juan Saez", "yellow")

    print (HEADER)