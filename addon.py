# -*- coding: utf-8 -*-
import sys
import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
from kodibgcommons import utils

reload(sys)  
sys.setdefaultencoding('utf8')

def index():
  li = xbmcgui.ListItem('Directory')
  url = utils.make_url({"id": 0, "action": "show_video"})
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, True)

  li = xbmcgui.ListItem("Playable item")
  url = "http://playable.com/video.mp4"
  li.setInfo( type = "Video", infoLabels = { "Title" : "Playable video"} )
  li.setProperty("IsPlayable", str(True))
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li)
  
params = utils.get_params()
utils.log('Running with params: {0}'.format(params))

action = params.get("action", None)
utils.log("action=%s" % action)

if not action:
  index()

xbmcplugin.endOfDirectory(int(sys.argv[1]))
