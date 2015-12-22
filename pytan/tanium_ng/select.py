"""Object Serializer/Deserializer for Tanium SOAP XML tag: ``select``

* License: MIT
* Copyright: Copyright Tanium Inc. 2015
* Generated from ``console.wsdl`` by ``build_tanium_ng.py`` on D2015-12-22T00-06-10Z-0400
* Version of ``console.wsdl``: 0.0.1
* Tanium Server version of ``console.wsdl``: 6.5.314.3400
* Version of PyTan: 4.0.0

"""
from .base import BaseType


class Select(BaseType):

    _soap_tag = 'select'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties=SIMPLE_ARGS,
            complex_properties=COMPLEX_ARGS,
            list_properties=LIST_ARGS,
        )
        # no simple_properties defined
        self.sensor = None
        self.filter = None
        self.group = None
        # no list_properties defined


from .sensor import Sensor
from .group import Group
from .filter import Filter

SIMPLE_ARGS = {}
# no SIMPLE_ARGS defined

COMPLEX_ARGS = {}
COMPLEX_ARGS['sensor'] = Sensor
COMPLEX_ARGS['filter'] = Filter
COMPLEX_ARGS['group'] = Group

LIST_ARGS = {}
# no LIST_ARGS defined
