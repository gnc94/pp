class Phone:
    def call(self):
        print('Calling...')

class Mobile(Phone):
    def Camera(self):
        print('Photo Clicked...')

    def WIFI(self):
        print('WIFI Connected')

obj = Mobile()
obj.Camera()
obj.WIFI()
obj.call()
