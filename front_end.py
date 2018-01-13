from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import cv2

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='input',width='100px',height='100px'))
        self.input = TextInput(multiline=False,height='100px')
        self.add_widget(self.input)
        self.add_widget(Label(text='output',width='100px',height='100px'))
        self.output = TextInput(multiline=False,height='100px')
        self.add_widget(self.output)
        self.btn=Button(text='submit')
        self.btn.bind(on_press=self.func)
        self.add_widget(self.btn)
    
    def func(self,text):
                
        #read image
        image = cv2.imread("C:\\Users\\vijay\\Pictures\\saltandpeppernoise.jpg")
        cv2.imshow("image",image)

        # apply the 3x3 median filter on the image
        processed_image = cv2.medianBlur(image, 3)
        processed_image = cv2.medianBlur(processed_image, 3)

        # display image
        cv2.imshow('Median Filter Processing', processed_image)

        # save image to disk
        cv2.imwrite('processed_image.png', processed_image)


class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()