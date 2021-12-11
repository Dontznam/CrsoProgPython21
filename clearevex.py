import pyfiglet
from termcolored import colored

result = pyfiglet.figlet_format("Esperimetno", font="slant")
print(colored(result, "red"))