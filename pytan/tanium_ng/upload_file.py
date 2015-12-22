"""Object Serializer/Deserializer for Tanium SOAP XML tag: ``upload_file``

* License: MIT
* Copyright: Copyright Tanium Inc. 2015
* Generated from ``console.wsdl`` by ``build_tanium_ng.py`` on D2015-12-22T00-06-10Z-0400
* Version of ``console.wsdl``: 0.0.1
* Tanium Server version of ``console.wsdl``: 6.5.314.3400
* Version of PyTan: 4.0.0

"""
from .base import BaseType


class UploadFile(BaseType):

    _soap_tag = 'upload_file'

    def __init__(self):
        BaseType.__init__(
            self,
            simple_properties=SIMPLE_ARGS,
            complex_properties=COMPLEX_ARGS,
            list_properties=LIST_ARGS,
        )
        self.id = None
        self.key = None
        self.destination_file = None
        self.hash = None
        self.force_overwrite = None
        self.file_size = None
        self.start_pos = None
        self.bytes = None
        self.file_cached = None
        self.part_size = None
        self.percent_complete = None
        # no complex_properties defined
        # no list_properties defined


# no extra imports used

SIMPLE_ARGS = {}
SIMPLE_ARGS['id'] = int
SIMPLE_ARGS['key'] = str
SIMPLE_ARGS['destination_file'] = str
SIMPLE_ARGS['hash'] = str
SIMPLE_ARGS['force_overwrite'] = int
SIMPLE_ARGS['file_size'] = int
SIMPLE_ARGS['start_pos'] = int
SIMPLE_ARGS['bytes'] = str
SIMPLE_ARGS['file_cached'] = int
SIMPLE_ARGS['part_size'] = int
SIMPLE_ARGS['percent_complete'] = int

COMPLEX_ARGS = {}
# no COMPLEX_ARGS defined

LIST_ARGS = {}
# no LIST_ARGS defined
