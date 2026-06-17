import pytest
import gdsfactory as gf

import tests.components.test_components as tc

from layouts.Photomodulator import (
    photonic_cable,
    cold_electrode,
    warm_electrode,
    graphene_under,
    graphene_upper
)



def test_photonic_cable_creation():
    c = photonic_cable(width=5.0, length=20.0)
    
    # Is component empty?
    assert len(c.polygons) > 0
    # Is there polygon?
    assert (1, 0) in c.layers


def test_electrode_ports():
    c = cold_electrode(width=3.0, length=3.0)
    
    assert "junction_graphene" in c.ports

    assert c.ports["junction_graphene"].width == 3.0


def test_gds():
    assert tc.test_gds("output/photo_modulator.gds")
    