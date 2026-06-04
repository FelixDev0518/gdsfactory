import sys
print(sys.version)
print(sys.executable)

import gdsfactory as gf
gf.config.print_version_plugins()

print([name for name in dir(gf) if 'cell' in name])


# def straight(length=10, width: float = 1, layer=(1, 0)): 
#     c = gf.Component()
#     c.add_polygon([(0, 0), (length, 0), (length, width), (0, width)], layer=layer) # This draws the main rectangular body of the waveguide.
#     c.add_port( # This adds two connection points, or ports, which are essential for connecting this component to others.
#         name="o1", center=(0, width / 2), width=width, orientation=180, layer=layer # "o1" is the input port and is facing left due to rotation (orientation=180)
#     )
#     c.add_port(
#         name="o2", center=(length, width / 2), width=width, orientation=0, layer=layer # "o2" is the output port and is facing right.
#     )
#     return c


# c = gf.Component()

# # Three waveguides are created. They have different lengths and sit on different layers, but all have the same width.
# wg1 = c << straight(length=6, width=2.5, layer=(1, 0)) 
# wg2 = c << straight(length=6, width=2.5, layer=(2, 0))
# wg3 = c << straight(length=15, width=2.5, layer=(3, 0))
# wg2.movey(10) # This moves wg2 up by 10 µm.
# wg2.rotate(10) # this rotates wg2 by 10 degrees.

# wg3.movey(20) # This moves wg3 up by 20 µm.
# wg3.rotate(15) # This rotates wg3 by 15 degrees.
# # Let us keep wg1 in place on the bottom, and connect the other straights to it.
# # To do that, on wg2 we will take the "o1" port and connect it to the "o2" on wg1:
# # wg2.connect("o1", wg1.ports["o2"], allow_layer_mismatch=True)

# # Next, on wg3 let us take the "o1" port and connect it to the "o2" on wg2:
# # wg3.connect("o1", wg2.ports["o2"], allow_layer_mismatch=True)

# c.write_gds("photodetector.gds")  
# # c.plot()
# c.show()
