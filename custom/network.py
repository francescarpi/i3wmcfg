#!/usr/bin/env python
# encoding: utf-8
# --------------------------------------------------------------------------

from i3pystatus.network import Network

from subprocess import Popen


class CustomNetwork(Network):
    def on_leftclick(self):
        Popen(["gnome-control-center", "network"])
        

