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

import os
import tempfile
import platform
import subprocess
import webbrowser

from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import QApplication, QMessageBox

from qgis.core import *
from qgis.gui import *

from .compat import get_file_dir, PY3
from .qgis23 import QgsCoordinateTransform


class Send2WIWtool(QgsMapTool):
  def __init__(self, iface):
    QgsMapTool.__init__(self, iface.mapCanvas())

    self.canvas = iface.mapCanvas()
    self.iface = iface

    self.plugin_dir = get_file_dir(__file__)

    self.cursor = QCursor(
        QPixmap('%s/icons/cursor.png' % self.plugin_dir),
        1, 1
    )

  def activate(self):
    self.canvas.setCursor(self.cursor)

  def canvasReleaseEvent(self, event):

    QApplication.setOverrideCursor(Qt.WaitCursor)
    x = event.pos().x()
    y = event.pos().y()
    point = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)
    QApplication.restoreOverrideCursor()

    crsSrc = self.canvas.mapSettings().destinationCrs()
    crsWGS = QgsCoordinateReferenceSystem(4326)

    if crsSrc.authid() != "4326":
        xform = QgsCoordinateTransform(crsSrc, crsWGS)
        point = xform.transform(point)
    
    webbrowser.open('https://livingatlas.arcgis.com/wayback/#localChangesOnly=true&ext='+str(point.x()-0.0005)+','+str(point.y()-0.0005)+','+str(point.x()+0.0005)+','+str(point.y()+0.0005))
