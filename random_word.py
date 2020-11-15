#!/usr/bin/env python3

# Import necessary modules for python
import time
from string import digits
import secrets

# Import the necessary modules for kivy
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# Ensure kivy compatibility
kivy.require("1.9.1")


# Class in which we are creating the button 
class Random_Word_GeneratorApp(App): 
      
    def build(self):
        
        # Define kivy window (box) layout.
        superBox = BoxLayout(orientation ='horizontal')
        
        # Define Horizonal Box orientation
        HB = BoxLayout(orientation ='vertical')
        
        # Create Parent button for operating child buttons
        self.btn0 = Button(text ="Push This Button To Generate Six Random " +
            "Words \n(Or push Any Single Button To The Right \nTo Change " + 
            "Only That Single Word.)",
            background_color = [0, 0, 1, 1],
            halign ='center',
            valign ='center')
        self.btn0.bind(on_press = self.callback1)
        self.btn0.bind(on_press = self.callback2)
        self.btn0.bind(on_press = self.callback3)
        self.btn0.bind(on_press = self.callback4)
        self.btn0.bind(on_press = self.callback5)
        self.btn0.bind(on_press = self.callback6)
        
        
        # Creat  button for printing text from child buttons
        self.btn7 = Button(text ="Push This Button To Print List " +
        "Of Current Words \nTo The Text File: 'new_pword_list.txt' " +
        "\nIn the directory this program is located in. ",
            background_color = [1, 0, 1, 1],
            halign ='center',
            valign ='center')
        self.btn7.bind(on_press = self.callback7)
        
        # Add button widgets to the box layout
        HB.add_widget(self.btn0)
        HB.add_widget(self.btn7)
        
        # Define Vertical Box orientation
        VB = BoxLayout(orientation ='vertical')
        
        # Create child buttons, default text, styling and function
        self.btn1 = Button(text ="Push to Generate A Random Word", 
        background_color = [0, 1, 0, 1],
        halign ='center',
        valign ='center')
        self.btn1.bind(on_press = self.callback1)
        
        self.btn2 = Button(text ="Push to Generate A Random Word", 
        background_color = [0, 1, 0, 1],
        halign ='center', 
        valign ='center')
        self.btn2.bind(on_press = self.callback2)
        
        self.btn3 = Button(text ="Push to Generate A Random Word", 
        background_color = [0, 1, 0, 1],
        halign ='center', 
        valign ='center')
        self.btn3.bind(on_press = self.callback3)
        
        self.btn4 = Button(text ="Push to Generate A Random Word", 
        background_color = [0, 1, 0, 1],
        halign ='center', 
        valign ='center')
        self.btn4.bind(on_press = self.callback4)
        
        self.btn5 = Button(text ="Push to Generate A Random Word", 
        background_color = [0, 1, 0, 1],
        halign ='center', 
        valign ='center')
        self.btn5.bind(on_press = self.callback5)
        
        self.btn6 = Button(text ="Push to Generate A Random Word", 
        background_color = [0, 1, 0, 1],
        halign ='center', 
        valign ='center')
        self.btn6.bind(on_press = self.callback6)
        
        # Add Vertical Box Buttons to the box layout
        VB.add_widget(self.btn1)
        VB.add_widget(self.btn2)
        VB.add_widget(self.btn3)
        VB.add_widget(self.btn4)
        VB.add_widget(self.btn5)
        VB.add_widget(self.btn6)
        
                
        # Complete build of box
        superBox.add_widget(HB)
        superBox.add_widget(VB)
        
        return superBox
          
    # Add a function for each button in the Box Layout
    
    # callback function tells when button 1 pressed 
    def callback1(self, event):
        
        # File path and name for 7,000 word list to pull random words from
        filename = 'only_words.txt'
        
        # Create lists for storing text file words and random words       
        words = []
        pword = []
        
        # Open and read text file and store each line in list 'words'        
        with open(filename) as file_object:
            for line in file_object:
                words.append(line)
        
        # Extract random word from list 'words' and store in list 'pword'
        pword.append(secrets.choice(words))
        
        # Send generated password candidate back to corresponding button text
        self.btn1.text = str(pword[0].strip('\t'))

    # callback function tells when button 2 pressed 
    def callback2(self, event):
    
        filename = 'only_words.txt'
               
        words = []
        pword = []
                
        with open(filename) as file_object:
            for line in file_object:
                words.append(line)
        
        pword.append(secrets.choice(words))
            
        def converttostr(input_seq, seperator):
            final_str = ''.join(input_seq)
            return final_str
                
        seperator = ''
                
        self.btn2.text = str(pword[0].strip('\t'))


    # callback function tells when button 3 pressed 
    def callback3(self, event):
    
        filename = 'only_words.txt'
               
        words = []
        pword = []
                
        with open(filename) as file_object:
            for line in file_object:
                words.append(line)
        
        pword.append(secrets.choice(words))
                
        self.btn3.text = str(pword[0].strip('\t'))

        # callback function tells when button 4 pressed 
    def callback4(self, event):
    
        filename = 'only_words.txt'
               
        words = []
        pword = []
                
        with open(filename) as file_object:
            for line in file_object:
                words.append(line)
        
        pword.append(secrets.choice(words))
                
        self.btn4.text = str(pword[0].strip('\t'))

    # callback function tells when button 5 pressed 
    def callback5(self, event):
    
        filename = 'only_words.txt'
               
        words = []
        pword = []
                
        with open(filename) as file_object:
            for line in file_object:
                words.append(line)
        
        pword.append(secrets.choice(words))
                
        self.btn5.text = str(pword[0].strip('\t'))

    # callback function tells when button 6 pressed 
    def callback6(self, event):
    
        filename = 'only_words.txt'
               
        words = []
        pword = []
                
        with open(filename) as file_object:
            for line in file_object:
                words.append(line)
        
        pword.append(secrets.choice(words))
                
        self.btn6.text = str(pword[0].strip('\t'))

    def callback7(self, event):
    
        # Define file path and name for new password list        
        new_file = str('new_pword_list.txt')
        
        # Create string from text stored in each button to print to file
        new_string = str(self.btn1.text + self.btn2.text + self.btn3.text +
            self.btn4.text + self.btn5.text + self.btn6.text)
        
        # Write button text to new text file 'new_pword_list.txt'
        with open(new_file, 'w') as file_object:
            file_object.write(new_string)

        
# creating the object root for ButtonApp() class  
root = Random_Word_GeneratorApp() 
  
# run function runs the whole program 
# i.e run() method which calls the target 
# function passed to the constructor. 
root.run()

