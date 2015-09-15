from ggame import App, Color, LineStyle, Sprite
from ggame import CircleAsset

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

thinline = LineStyle(0, black)
mycircle = CircleAsset(5, thinline, blue)
myother = CircleAsset(5, thinline, red)
xcoordinates = range(100, 600, 8)

sprites = [Sprite(mycircle, (x, 15000/x)) for x in xcoordinates]
sprites = [Sprite(myother, (x, x * 2)) for x in xcoordinates]

myapp = App()
myapp.run()
