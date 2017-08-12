class Color(object):
    _color = (0,0,0)

    @classmethod
    def value(cls):
        if cls.__name__ == 'Red':
            cls._color = (255,0,0)
        elif cls.__name__ == 'Blue':
            cls._color = (0,255,0)
        return cls._color


class Red(Color):
    pass

class Blue(Color):
    pass

class UnknowColor(Color):
    pass

red = Red()
blue = Blue()
xcolor = UnknowColor()

print 'red = ',red.value()
print 'blue = ',blue.value()
print 'xcolor = ',xcolor.value()            
