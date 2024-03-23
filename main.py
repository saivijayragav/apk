from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
def flames(nam1, nam2):
    name1 = nam1.lower()
    name2 = nam2.lower()
    for i in name1:
        if i in name2:
            name1 = name1.replace(i, "", 1)
            name2 = name2.replace(i, "", 1)
    suma = len(name1.replace(" ", "")) + len(name2.replace(" ", ""))
    word = "FLAMES"
    ind = 0
    n = len(word)
    ind2 = 1
    li = []
    while len(li)<n-1:
        
        if word[(ind)%6] not in li:
            if ind2 == suma:
                li.append(word[(ind)%6])
                ind2 = 0
            ind2 += 1
            ind += 1
        else:
            ind += 1
    dic = {'F':" Friends", 'L':" Lovers", 'A': " Affectionate", "M":"/will be married", "E":" Enemies","S": " Sister and brother"}       
    for i in word:
        if i not in li:
            return str(nam1+" and "+nam2+" are"+dic[i])


class FLAMES(App):
    def build(self):
        # Layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # Text Inputs for two names
        self.text_input1 = TextInput(hint_text='Enter first name', multiline=False)
        self.text_input2 = TextInput(hint_text='Enter second name', multiline=False)
        
        # Label for displaying the entered names combined
        self.output_label = Label(text='')
        
        # Buttons
        btn_print = Button(text='FLAMES')
        btn_print.bind(on_press=self.print_combined_names)
        
        btn_redo = Button(text='Redo')
        btn_redo.bind(on_press=self.redo)
        
        # Add widgets to layout
        layout_input = BoxLayout(orientation='horizontal', spacing=10)
        layout_input.add_widget(self.text_input1)
        layout_input.add_widget(self.text_input2)
        layout.add_widget(layout_input)
        
        layout_buttons = BoxLayout(orientation='horizontal', spacing=10)
        layout_buttons.add_widget(btn_print)
        layout_buttons.add_widget(btn_redo)
        layout.add_widget(layout_buttons)
        
        layout.add_widget(self.output_label)
        
        return layout
    
    def print_combined_names(self, instance):
        # Retrieve and print the entered names combined
        name1 = self.text_input1.text
        name2 = self.text_input2.text
        combined_names = flames(name1, name2)
        self.output_label.text = combined_names
    
    def redo(self, instance):
        # Clear text input fields and output label
        self.text_input1.text = ''
        self.text_input2.text = ''
        self.output_label.text = ''

if __name__ == '__main__':
    FLAMES().run()
