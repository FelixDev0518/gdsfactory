import gdsfactory as gf
from gdsfactory.gpdk import PDK




gf.gpdk.PDK.activate()
# Create a blank component (essentially an empty GDS cell with some special features).
c = gf.Component()
p1 = c.add_polygon([(-8, -6), (6, 8), (7, 17), (9, 5)], layer=(1, 0))
# Draw text and rectalular
text_hello = gf.components.text("hello!")
rectangle = gf.components.rectangle(size=(5, 10), layer=(2, 0))
rectangle2 = gf.components.rectangle(size=(5, 10), layer=(2, 1))

text1 = c.add_ref(text_hello)
text2 = c << text_hello

rectangle = c.add_ref(rectangle)
rectangle2 = c << rectangle2

text1.movey(25) #unit: nm
text2.move((5,10))
text2.rotate(45)

rectangle.movex(-15)

c.write_gds("demo.gds")  # Write it to a GDS file. You can open it in klayout.

c.show()  # Show it in klayout.
c.plot()  # Plot it in jupyter notebook.
