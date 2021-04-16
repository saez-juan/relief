import env
from utils.gcli import RELIEF, println
from utils.colors import paint

def run ():
    println (env.VERSION + " | Desarrollado por " + paint ("Juan Saez", "yellow"))
