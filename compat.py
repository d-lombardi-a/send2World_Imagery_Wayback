# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Send2World_Imagery_Wayback
                                 A QGIS plugin
 Collection of internet map services
                              -------------------
        begin                : 2023-05-05
        git sha              : $Format:%H$
        copyright            : (C) 2023 by ARPA Lombardia
        email                : d.lombardi@arpalombardia.it
 ***************************************************************************/
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import os
import sys


PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY2:
    import urlparse
    from urllib2 import urlopen, URLError
else:
    from urllib import parse
    urlparse = parse
    from urllib.request import urlopen, URLError

if PY3:
    import configparser
else:
    import ConfigParser as configparser


def get_file_dir(filename):
    if PY2:
        return os.path.dirname(filename).decode(sys.getfilesystemencoding())
    else:
        return os.path.dirname(filename)
