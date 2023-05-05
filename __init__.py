# -*- coding: utf-8 -*-
#******************************************************************************
#
# Send2World_Imagery_Wayback
# ---------------------------------------------------------
# This plugin takes coordinates of a mouse click and sends them to World Imagery Wayback
#
# Copyright (C) 2023 Dario Lombardi (d.lombardi@arpalombardia.it), ARPA Lombardia (https://www.arpalombardia.it/)
#
# This source is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# This code is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# A copy of the GNU General Public License is available on the World Wide Web
# at <http://www.gnu.org/licenses/>. You can also obtain it by writing
# to the Free Software Foundation, 51 Franklin Street, Suite 500 Boston,
# MA 02110-1335 USA.
#
#******************************************************************************


def classFactory(iface):
    # Import class TestPlugin from file testplugin.py
    from .send2World_Imagery_Wayback import Send2WIW
    return Send2WIW(iface)
