#!/usr/bin/env python
# encoding: utf-8
# --------------------------------------------------------------------------

from i3pystatus.clock import Clock

from subprocess import Popen


class CustomClock(Clock):
    def on_leftclick(self):
        Popen(["gnome-control-center"])
        
    
    
