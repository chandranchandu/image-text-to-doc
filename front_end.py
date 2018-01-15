from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import cv2
from docx import Document
from docx.shared import Inches
document = Document()
import pytesseract
import os
from PIL import Image

Builder.load_string("""
<LoginScreen>:
    GridLayout:
        cols:3
        rows:5
        Label:
            text:'input'
            font_size:'50sp'
        TextInput:
            id:input      
        Button:
            text:'Browse'
            on_press:root.manager.current='input'
        Label:
            text:'output'
            font_size:'50sp'
        TextInput:
            id:output
        Button:
            text:'Browse'
            on_press:root.manager.current='output'
        Button:
            text:'submit and convert!'
            on_press:root.func(root.manager.get_screen('input').items,root.manager.get_screen('output').items)
<InputScreen>:
    label:display
    BoxLayout:
        Label:
            id:display
        FileChooserIconView:
            id:filechoose
            multiselect:True
            on_selection:root.select(self.selection)
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
<OutputScreen>:
    label:display
    BoxLayout:
        Label:
            id:display
        FileChooserIconView:
            id:filechoose
            multiselect:True
            on_selection:root.select(self.selection)
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
""")
class InputScreen(Screen):
   
    items=[]
    def select(self,selection):
        if selection:
            self.items.append(selection[0])
            self.ids["display"].text=str(self.items)

class OutputScreen(Screen):
   
    items=[]
    def select(self,selection):
        if selection:
            self.items.append(selection[0])
            self.ids["display"].text=str(self.items)

class LoginScreen(Screen):
    
    def func(self,inputs,output):
        self.ids["input"].text=str(inputs)
        for img in inputs:
            #read image
            image = cv2.imread(img)
            cv2.imshow("image",image)

            # apply the 3x3 median filter on the image
            processed_image = cv2.medianBlur(image, 3)
            processed_image = cv2.medianBlur(processed_image, 3)

            # display image
            cv2.imshow('Median Filter Processing', processed_image)
            imname='{}.png'.format(os.getpid())
            cv2.imwrite(imname,processed_image)
            pytesseract.pytesseract.tesseract_cmd = 'F:/tesseract/tesseract.exe'
            result = pytesseract.image_to_string(Image.open("F:/A.I/smartIndia/imtotext/f2.jpg"), lang="tam")
            document.add_paragraph(result)
            document.add_page_break()
            document.save('ex.docx')


            # save image to disk
            #cv2.imwrite('processed_image.png', processed_image)

class SettingsScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(LoginScreen(name='menu'))
sm.add_widget(InputScreen(name='input'))
sm.add_widget(OutputScreen(name='output'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()
    