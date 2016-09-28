# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 Petter Reinholdtsen
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

streamurl = 'http://video.nuug.no/frikanalen.webm'

import sys
import xbmcgui
import xbmcplugin
import routing

from xbmcplugin import addDirectoryItem
from xbmcplugin import addDirectoryItems
from xbmcplugin import endOfDirectory
from xbmcgui import ListItem

plugin = routing.Plugin()

@plugin.route('/')
def root():
    items = [
        (plugin.url_for(live), ListItem("Direkte"), True),
        (plugin.url_for(schedule), ListItem("Sendeplan"), True),
    ]
    addDirectoryItems(plugin.handle, items)
    endOfDirectory(plugin.handle)

@plugin.route('/live')
def live():
    addon_handle = plugin.handle

    xbmcplugin.setContent(addon_handle, 'videos')

    li = ListItem('Live streaming', iconImage='DefaultVideo.png')
    li.setProperty('IsPlayable', 'true')
    li.setInfo('videos', {'mediatype' : 'video'})

    addDirectoryItem(handle=addon_handle, url=streamurl, listitem=li)

    endOfDirectory(addon_handle)

@plugin.route('/schedule')
def schedule():
    raise Exception("to be implemented")

def run():
    plugin.run()
