from colors import paint

__TAB_SIZE = 4

RELIEF = paint ("Relief", "magenta")

def println (txt, tabs=1):
    current_indent = __get_indent (tabs)
    print (current_indent + str (txt))

def print_item (txt, bullet_color="white", tabs=1):
    current_indent = __get_indent (tabs)
    print (current_indent + "  " + paint (chr (0x25AA), bullet_color) + " " + str (txt))

def __get_indent (size):
    global __TAB_SIZE

    return (" " * __TAB_SIZE) * int (size)
