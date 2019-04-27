import openpnm as op
import openpnm.models.geometry.throat_surface_area as tsa
from numpy.testing import assert_allclose
import scipy as sp


class ThroatSurfaceAreaTest:
    def setup_class(self):
        self.net = op.network.Cubic(shape=[5, 5, 5])
        self.geo = op.geometry.GenericGeometry(network=self.net,
                                               pores=self.net.Ps,
                                               throats=self.net.Ts)
        self.geo['throat.diameter'] = sp.ones((self.geo.Nt, ))
        self.geo['throat.length'] = sp.ones((self.geo.Nt, ))
        self.geo['throat.perimeter'] = sp.ones((self.geo.Nt, ))

    def test_cylinder(self):
        self.geo.add_model(propname='throat.surface_area',
                           model=tsa.cylinder, regen_mode="normal")
        assert_allclose(self.geo['throat.surface_area'].mean(), sp.pi)

    def test_cuboid(self):
        self.geo.add_model(propname='throat.surface_area',
                           model=tsa.cuboid, regen_mode="normal")
        assert_allclose(self.geo['throat.surface_area'].mean(), 4)

    def test_rectangle(self):
        self.geo.add_model(propname='throat.surface_area',
                            model=tsa.rectangle, regen_mode="normal")
        assert_allclose(self.geo['throat.surface_area'].mean(), 2)

    def test_extrusion(self):
        self.geo.add_model(propname='throat.surface_area',
                           model=tsa.extrusion, regen_mode="normal")
        assert_allclose(self.geo['throat.surface_area'].mean(), 1)


if __name__ == '__main__':

    t = ThroatSurfaceAreaTest()
    self = t
    t.setup_class()
    for item in t.__dir__():
        if item.startswith('test'):
            print('running test: '+item)
            t.__getattribute__(item)()
