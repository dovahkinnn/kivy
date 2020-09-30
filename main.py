from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import requests

class Yazbel(App):

        def build(self):
                self.govde = BoxLayout(orientation = "vertical")

                
                self.buton = Button(text = "Tıkla",size_hint_y = .3)

                self.buton.bind(on_press = self.press)
                

                
                self.govde.add_widget(self.buton)

                return self.govde

        def press(self,nesne):

            url = "https://d7sms.p.rapidapi.com/secure/send"

            payload = "{ \"content\": \"Test Message\", \"from\": \"D7-Rapid\", \"to\": 905051396066}"
            headers = {
                'authorization': "Basic YnB2azYxODQ6Smx0dkFudFE=",
                'x-rapidapi-host': "d7sms.p.rapidapi.com",
                'x-rapidapi-key': "0a58d89bb5mshae95083c431bb71p1efa1ajsn3f974b43a4cd",
                'content-type': "application/json",
                'accept': "application/json"
                }

            response = requests.request("POST", url, data=payload, headers=headers)

            print(response.text)


Yazbel().run()
