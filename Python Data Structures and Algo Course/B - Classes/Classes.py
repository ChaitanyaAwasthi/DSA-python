class Cookie:

    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color


# why would this change the color ?

    def set_color(self, color):
        self.color = color


object1 = Cookie('Green')
print('hello %s' % object1.get_color())
