from rigging import MODULE_NAME
from utils import build_test_suite
from unittest import main

def test_suite():
    return build_test_suite(MODULE_NAME,[
        'test_encoding',
        'test_mimetypes',
#        'test_rest',
#        'test_pdf',
#        'test_python',
#        'test_lynx',
        ])

if __name__=='__main__':
    main(defaultTest='test_suite')
