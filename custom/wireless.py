#!/usr/bin/env python
# encoding: utf-8
# --------------------------------------------------------------------------

from i3pystatus.wireless import Wireless

from subprocess import Popen


class CustomWireless(Wireless):
    def on_leftclick(self):
        Popen(["gnome-control-center", "network"])
        
