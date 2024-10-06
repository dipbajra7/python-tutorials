import converter_module
from converter_module import convert_kph_to_mph
from utils_module import find_max

from ecompackage.shipping import calc_shipping
from ecompackage import tax

import random



print(converter_module.convert_kg_to_lbs(60))
print(converter_module.convert_lbs_to_kg(140))
print(convert_kph_to_mph(100))

print(find_max([1,2,3,55,6,7]))



calc_shipping()
tax.calulate_state_tax()



print('--------------------------------------------------------------')
numbers = [1,2,3,4,5,6]
print(f'({random.choice(numbers)}, {random.choice(numbers)})')

