from modules import main_function
from modules import utils


mensage = str(input('Type the message to be sent: '))
number_of_mensages = utils.check_if_it_is_number(
    'Enter the number of times this message will be sent: ')

print("Press F2 to start the 'flood'!")
print("(Press ESC to stop)")

main_function.flood(mensage, number_of_mensages)
