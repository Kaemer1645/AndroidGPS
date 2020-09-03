from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivy.properties import StringProperty
from plyer import gps
from kivy.utils import platform
from kivy.clock import mainthread




navigation_helper = '''
#:import webbrowser webbrowser
Screen:
    MDRoundFlatIconButton:
        icon: 'crosshairs-gps'
        text: 'Check Your Position'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        size: (dp(200), dp (48))
        on_state:
            app.start(1000, 0) if self.state == 'down' else \
            app.stop()
    MDRoundFlatIconButton:
        icon: 'google-photos'
        text: 'Take Photo Of Your Sign'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        size: (dp(220), dp (48))
        on_press: app.take_photo()
    MDLabel:
        text: app.gps_location
        pos_hint: {'center_x':0.5,'center_y':0.4}
        halign:"center"
    


    NavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "GPS KNGK APP"
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
                    source:'kolorowe_png_150.png'
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
                        MDRectangleFlatIconButton:
                            text: 'Facebook'
                            icon:"facebook"
                            on_press: webbrowser.open('https://www.facebook.com/KNGKAGH/')
                        MDRectangleFlatIconButton:
                            text: 'WebSite'
                            icon:"search-web"
                            on_press: webbrowser.open('http://www.kngk.agh.edu.pl/')

                            

                                
                                
                            
'''


class GPSApp(MDApp):

    gps_location = StringProperty()
    gps_status = StringProperty('Click Start to get GPS location updates')

    class ContentNavigationDrawer(BoxLayout):
        pass

    def request_android_permissions(self):
        """
        Since API 23, Android requires permission to be requested at runtime.
        This function requests permission and handles the response via a
        callback.

        The request will produce a popup if permissions have not already been
        been granted, otherwise it will do nothing.
        """
        from android.permissions import request_permissions, Permission

        def callback(permissions, results):
            """
            Defines the callback to be fired when runtime permission
            has been granted or denied. This is not strictly required,
            but added for the sake of completeness.
            """
            if all([res for res in results]):
                print("callback. All permissions granted.")
            else:
                print("callback. Some permissions refused.")

        request_permissions([Permission.ACCESS_COARSE_LOCATION,
                             Permission.ACCESS_FINE_LOCATION], callback)
        # # To request permissions without a callback, do:
        # request_permissions([Permission.ACCESS_COARSE_LOCATION,
        #                      Permission.ACCESS_FINE_LOCATION])



    def start(self, minTime, minDistance):
        gps.start(minTime, minDistance)

    def stop(self):
        gps.stop()

    @mainthread
    def on_location(self, **kwargs):
        self.gps_location = '\n'.join([
            '{}={}'.format(k, v) for k, v in kwargs.items()])

    @mainthread
    def on_status(self, stype, status):
        self.gps_status = 'type={}\n{}'.format(stype, status)

    def on_pause(self):
        gps.stop()
        return True

    def on_resume(self):
        gps.start(1000, 0)
        pass


    def tester(self):
        self.wyswietl = 'Udalo sie'
    def build(self):
        screen = Screen()
        navigator = Builder.load_string(navigation_helper)
        screen.add_widget(navigator)
        try:
            gps.configure(on_location=self.on_location,
                          on_status=self.on_status)
        except NotImplementedError:
            import traceback
            traceback.print_exc()
            self.gps_status = 'GPS is not implemented for your platform'

        if platform == "android":
            print("gps.py: Android detected. Requesting permissions")
            self.request_android_permissions()
        return screen
    def take_photo(self):
        print('photo taken')
if __name__=="__main__":
    GPSApp().run()