import gdsfactory as gf

gf.gpdk.PDK.activate()

@gf.cell
def photonic_cable(width: float = 3.0, length: float = 10.0, layer=(1, 0)) -> gf.Component:
    c = gf.Component()
    
    x_left = -(width / 2)
    x_right = width / 2
    y_under = -(length / 2)
    y_upper = length / 2
    
    c.add_polygon([
        (x_left, y_under), 
        (x_right, y_under), 
        (x_right, y_upper), 
        (x_left, y_upper)
        ], layer=layer)
    
    c.add_label(text="Photonic Cable", position=(x_left, y_under))
    
    return c

@gf.cell
def cold_electrode(width: float = 3.0, length: float = 3.0, layer=(2, 1)) -> gf.Component:
    c = gf.Component()
    
    x_left = -(width / 2)
    x_right = width / 2
    y_under = -(length / 2)
    y_upper = length / 2
    
    c.add_polygon([
        (x_left, y_under), 
        (x_right, y_under), 
        (x_right, y_upper), 
        (x_left, y_upper)
        ], layer=layer)
    
    c.add_port(
        name="junction_graphene", center=(x_right, 0), width=length,
        orientation=0, layer=layer)
    
    c.add_label(text="Cold Electrode", position=(x_right, y_upper))
    
    return c

@gf.cell
def warm_electrode(width: float = 3.0, length: float = 3.0, layer=(2, 2)) -> gf.Component:
    c = gf.Component()
    
    x_left = -(width / 2)
    x_right = width / 2
    y_under = -(length / 2)
    y_upper = length / 2
    
    c.add_polygon([
        (x_left, y_under), 
        (x_right, y_under), 
        (x_right, y_upper), 
        (x_left, y_upper)
        ], layer=layer)

    c.add_port(
        name="junction_graphene", center=(x_left, 0), width=length,
        orientation=180, layer=layer)

    c.add_label(text="Warm Electrode", position=(x_right, y_upper))
    
    return c

@gf.cell
def graphene_under(width: float = 3.0, length: float = 5.0, layer=(3, 1), label: str = "") -> gf.Component:
    c = gf.Component()
    
    x_left = -(width / 2)
    x_right = width / 2
    y_under = -(length / 2)
    y_upper = length / 2
    
    c.add_polygon([
        (x_left, y_under), 
        (x_right, y_under), 
        (x_right, y_upper), 
        (x_left, y_upper)
        ], layer=layer)
    
    c.add_port(
        name="junction_pos", center=(x_left, 0), width=length,
        orientation=180, layer=layer)
    
    c.add_port(
        name="junction_neg", center=(x_right, 0), width=length,
        orientation=0, layer=layer)
    
    c.add_label(text=label, position=(x_left, y_under))

    return c

@gf.cell
def graphene_upper(width: float = 3.0, length: float = 5.0, layer=(3, 2), label: str = "") -> gf.Component:
    c = gf.Component()
    
    x_left = -(width / 2)
    x_right = width / 2
    y_under = -(length / 2)
    y_upper = length / 2
    
    c.add_polygon([
        (x_left, y_under), 
        (x_right, y_under), 
        (x_right, y_upper), 
        (x_left, y_upper)
        ], layer=layer)
    
    c.add_port(
        name="junction_pos", center=(x_left, 0), width=length,
        orientation=180, layer=layer)
    
    c.add_port(
        name="junction_neg", center=(x_right, 0), width=length,
        orientation=0, layer=layer)
    
    c.add_label(text=label, position=(x_left, y_under))

    return c

c = gf.Component()

cable = c << photonic_cable(10e-3, 100e-3) # width: 10nm, length: 100nm

graphene_under_ref = c << graphene_under(30e-3, 20e-3, label="Graphene Under")
graphene_upper_ref = c << graphene_upper(30e-3, 20e-3, label="Graphene Upper")

negative_electrode = c << cold_electrode(30e-3, 30e-3)
positive_electrode = c << warm_electrode(30e-3, 30e-3)

graphene_upper_ref.xmin = cable.xmin

graphene_under_ref.xmax = cable.xmax


negative_electrode.connect("junction_graphene", graphene_upper_ref.ports["junction_neg"], allow_layer_mismatch=True,
                            allow_width_mismatch=True)
positive_electrode.connect("junction_graphene", graphene_under_ref.ports["junction_pos"], allow_layer_mismatch=True,
                           allow_width_mismatch=True)

#c.show()
c.write_gds("photo_modulator.gds")