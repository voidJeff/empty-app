from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

red = Color(0xff0000, 1.0)
redT = Color(0xff0000, 0.5)
green = Color(0x00ff00, 1.0)
greenT = Color(0x00ff00, 0.4)
blue = Color(0x0000ff, 1.0)
blueT = Color(0x0000ff, 0.3)
black = Color(0x000000, 1.0)

thinline = LineStyle(0, black)

shape1 = CircleAsset(100, thinline, redT)
shape2 = CircleAsset(100, thinline, greenT)
shape3 = CircleAsset(100, thinline, blueT)


Sprite(shape1, (650,300))
Sprite(shape2, (575,430))
Sprite(shape3, (725,430))

myapp = App()
myapp.run()