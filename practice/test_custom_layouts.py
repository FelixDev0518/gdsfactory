import os
import pytest
import gdsfactory as gf

from layouts.Photomodulator import (
    photonic_cable,
    cold_electrode,
    warm_electrode,
    graphene_under,
    graphene_upper
)

def test_photonic_cable_creation() -> None:
    c = photonic_cable(width=5.0, length=20.0)
    
    # Is component empty?
    assert len(c.polygons) > 0
    # Is there polygon?
    assert (1, 0) in c.layers


def test_electrode_ports() -> None:
    c = cold_electrode(width=3.0, length=3.0)
    
    assert "junction_graphene" in c.ports

    assert c.ports["junction_graphene"].width == 3.0


def test_gds() -> None:
    gds_path = "output/photo_modulator.gds"
    assert os.path.exists(gds_path), f"GDS file was not generated at {gds_path}"
    
    try: 
        c = gf.import_gds(gds_path)
        assert c is not None
        assert len(c.polygons) > 0, "GDS file is empty"
    except Exception as e:
        pytest.fail(f"Failed to load GDS file.")
    
    