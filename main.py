from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem
from kivy.properties import StringProperty, ListProperty

navigation_helper = '''
Screen:

    NavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Developer"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]

                    Widget:


        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                Image:
                    source:'kolorowe_png_72.png'
                MDLabel:
                    text:"KNGK_Geoinformatyka"
                    font_style:'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]
                    
                MDLabel:
                    text:"kngk@student.agh.edu.pl"
                    font_style:'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                    
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Facebook'
                            IconLeftWidget:
                                icon:"facebook"
                        OneLineIconListItem:
                            text: 'WebSite'
                            IconLeftWidget:
                                icon:"search-web"
                                
                                
                            
'''


class ContentNavigationDrawer(BoxLayout):
    pass

class GPSApp(MDApp):
    def build(self):
        return Builder.load_string(navigation_helper)

if __name__=="__main__":
    GPSApp().run()