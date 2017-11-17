# created by Jenny Trac
# created on Nov 16 2017
# program accepts an array and finds the minumum value

import ui

def minimum(quantity, the_array):
    # function finds the minimum value
    
    minimum_value = the_array[0]
    
    for every_number in the_array:
        if every_number < minimum_value:
            minimum_value = every_number
        else:
            minimum_value = minimum_value
    
    return minimum_value
def get_minimum_touch_up_inside(sender):
    # button to get minimum
    
    quantity_input = int(view['number_textfield'].text)
    array_input = (view['array_textfield'].text).split(' ')
    converted_array = [int(number) for number in array_input]
    
    array_minimum = minimum(quantity_input, converted_array)
    
    view['answer_label'].text = str(array_minimum)

view = ui.load_view()
view.present('sheet')
