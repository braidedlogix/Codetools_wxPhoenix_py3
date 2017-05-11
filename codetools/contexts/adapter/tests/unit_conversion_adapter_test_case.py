# Standard Library Imports
import sys
import unittest

# Numeric Libary imports
from numpy import all

# Enthought Library imports
from traits.testing.api import doctest_for_module
from scimath.units.length import meters, feet, inch

# Geo Library imports
from scimath.units.api import UnitArray
from codetools.contexts.api import UnitConversionAdapter


class UnitConversionAdapterTestCase(unittest.TestCase):
    """ Other tests for UnitConversionContextAdapater
    """

    ############################################################################
    # UnitConversionAdapterTestCase interface
    ############################################################################

    def test_adapt_getitem_converts_correctly(self):
        """ Does getitem convert units correctly?
        """
        context = None
        old_log = UnitArray((1, 2, 3), units=meters)
        getitem_units = {'depth': feet}
        adapter = UnitConversionAdapter(getitem_units=getitem_units)
        name, new_log = adapter.adapt_getitem(context, 'depth', old_log)

        # Did the values get converted correctly?
        self.assertTrue(all(new_log == old_log.as_units(feet)))

        # Are the units assigned correctly?
        self.assertTrue(new_log.units == feet)

        return

    def test_adapt_setitem_converts_correctly(self):
        """ Does setitem convert units correctly?
        """
        context = None
        old_log = UnitArray((1, 2, 3), units=meters)
        setitem_units = {'depth': feet}
        adapter = UnitConversionAdapter(setitem_units=setitem_units)

        # pass the log into the conversion adapter as meters
        name, new_log = adapter.adapt_setitem(context, 'depth', old_log)

        # Did the values get converted correctly?
        self.assertTrue(all(new_log == old_log.as_units(feet)))

        # Are the units assigned correctly?
        self.assertTrue(new_log.units == feet)

        return

    def test_get_set_converts_correctly(self):
        """ Does get/set with different units convert correctly?
        """
        context = None
        meter_log = UnitArray((1, 2, 3), units=meters)
        setitem_units = {'depth': inch}
        getitem_units = {'depth': feet}
        adapter = UnitConversionAdapter(
            getitem_units=getitem_units, setitem_units=setitem_units)
        name, inch_log = adapter.adapt_setitem(context, 'depth', meter_log)
        self.assertTrue(all(inch_log == meter_log.as_units(inch)))

        name, feet_log = adapter.adapt_getitem(context, 'depth', inch_log)
        # Did the values get converted correctly?
        self.assertTrue(all(feet_log == meter_log.as_units(feet)))

        # Are the units assigned correctly?
        self.assertTrue(feet_log.units == feet)

        return


################################################################################
# Test the doctests specified within the module.
################################################################################

# When nosetests is running this test module, it is not necessary to run
# doctests here also.  In fact, the code below causes nosetests to fail.
if 'nose' not in sys.modules:
    from codetools.contexts.adapter import unit_conversion_adapter
    module_test = doctest_for_module(unit_conversion_adapter)

if __name__ == '__main__':
    unittest.main()
