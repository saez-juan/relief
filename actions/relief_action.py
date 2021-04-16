from utils.colors import paint
from utils.gcli import RELIEF
import env

def run ():
    current_version = env.VERSION

    HEADER = RELIEF + " " + str (current_version) + "\n  por " + paint ("Juan Saez", "yellow")

    print (HEADER)