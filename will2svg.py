#!/usr/bin/env python3

import os
import sys
import tempfile
from will2yaml import will2yaml, get_page_size, getPages
from yaml2svg import yaml2svg


if len(sys.argv) < 2:
    print("{0} infile.will".format(sys.argv[0]))
    exit()
else:
    _pages = getPages(will_filename= sys.argv[1])
    print('{} contains {} pages...'.format(sys.argv[1], len(_pages)))
    for _page in _pages:
        print(_page)

        temp = tempfile.NamedTemporaryFile(mode='w', delete=False)

        temp.write(will2yaml(will_filename=sys.argv[1], protobufName=_page))


        w, h, mat = get_page_size(sys.argv[1])

        _split = _page.split("/");
        print(_split[len(_split)-1])
        _dotSplit = _split[len(_split)-1].split('.')
        print(_dotSplit[0:len(_dotSplit)-1])
        _svgFileName = os.path.splitext(sys.argv[1])[0] + '_' + '.'.join(_dotSplit[0:len(_dotSplit)-1]) + '.svg'
        print('svg file name: {}'.format(_svgFileName))

        f = open(_svgFileName, 'w')
        f.write(yaml2svg(yaml_filename=temp.name, width=w, height=h, matrix=mat))
        f.close()
        temp.close()
        
    os.unlink(temp.name)
    print('Finished!')
    
