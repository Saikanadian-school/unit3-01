
import ui

randomnumber = 5

def number_button(sender):
    
    number = int(view['number'].text)
    
    if number == randomnumber:
        
        view['correct_answer'].text = "correct"

view = ui.load_view()
view.present('sheet')
