import numpy as np
from typing import List
import matplotlib.pyplot as plt


#the commented and non commented functions do the same thing. The non commented function is dynamic on which activation function to use is user defined.
#the commented function uses softplus activation function.



def softplus(x):
    return np.log(1 + np.exp(x))


def sigmoid(x):
  return 1 / (1 + np.exp(-x))


def relu(x):
  return max(0, x)


def get_x_activation_function_plots(dose, weight, bias): #adds weights and biases
   return (dose * weight) + bias


def calculate_x_activation_function_plots(dosage, weight, bias): #upper
   xs = []
   for dose in dosage:
    xs.append(get_x_activation_function_plots(dose, weight, bias))
   
   return xs


def calculate_y_activation_function_plots(x_values) -> List[float]:
   ys = []
   for x in x_values:
      ys.append(softplus(x))


   return ys 



def get_scaled_y_values(y_plots, scale): 
   scaled = []
   for y in y_plots:
      scaled.append(y * scale)


   return scaled 



def calculate_y_activation_function_plotsss(func_to_use, x_values) -> List[float]:
   ys = []
   for x in x_values:
      ys.append(func_to_use(x))


   return ys 





def add_two_lists(list1, list2):
   sum_of_lists = []
   for i in range(0, len(list1)):
      sum_of_lists.append(list1[i]+list2[i])
      
   return sum_of_lists   
   


# def test(dosage):

#     upper_initial_y_points = calculate_y_activation_function_plots(calculate_x_activation_function_plots(dosage, -34.4, 2.14), )
#     lower_initial_y_points = calculate_y_activation_function_plots(calculate_x_activation_function_plots(dosage, -2.52, 1.29))

#     scaled_upper_y_value = get_scaled_y_values(upper_initial_y_points, -1.30) # final blue curve
#     scaled_lower_y_value = get_scaled_y_values(lower_initial_y_points, 2.28) # final orange curve

#     squiggle = add_two_lists(scaled_upper_y_value, scaled_lower_y_value)

#     xpoints = dosage
#     ypoints = scaled_lower_y_value

#     y_second_points = scaled_upper_y_value

#     plt.figure(num=0, dpi = 120)
#     #plt.plot(xpoints, ypoints, 'o')
#     plt.plot(xpoints, ypoints)
#     #plt.plot(xpoints, y_second_points, 'x')
#     plt.figure(num=0, dpi = 120)
#     plt.plot(xpoints, y_second_points)

#     plt.figure(num=0, dpi = 120)
#     plt.plot(xpoints, squiggle)
#     plt.show()




# dosage = np.arange(0,1.1,0.1)
# test(dosage)




def run_neural_network_with_provided_activation_function(dosage, func_name):
    func_dict = {'softplus':softplus, 'sigmoid': sigmoid, 'relu': relu}
    func_to_use = func_dict.get(func_name)

    if func_to_use is None:
       return


    upper_initial_y_points = calculate_y_activation_function_plotsss(func_to_use, calculate_x_activation_function_plots(dosage, -34.4, 2.14))
    lower_initial_y_points = calculate_y_activation_function_plotsss(func_to_use, calculate_x_activation_function_plots(dosage, -2.52, 1.29))

    scaled_upper_y_value = get_scaled_y_values(upper_initial_y_points, -1.30) # final blue curve
    scaled_lower_y_value = get_scaled_y_values(lower_initial_y_points, 2.28) # final orange curve

    squiggle = add_two_lists(scaled_upper_y_value, scaled_lower_y_value)

    xpoints = dosage
    ypoints = scaled_lower_y_value

    y_second_points = scaled_upper_y_value

    plt.figure(num=0, dpi = 120)
    #plt.plot(xpoints, ypoints, 'o')
    plt.plot(xpoints, ypoints)
    #plt.plot(xpoints, y_second_points, 'x')
    plt.figure(num=0, dpi = 120)
    plt.plot(xpoints, y_second_points)

    plt.figure(num=0, dpi = 120)
    plt.plot(xpoints, squiggle)
    plt.show()




dosage = list(np.arange(0,1.1,0.1))
run_neural_network_with_provided_activation_function(dosage, 'softplus')
