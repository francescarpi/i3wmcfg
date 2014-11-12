#!/usr/bin/env python
# encoding: utf-8
# --------------------------------------------------------------------------

from i3pystatus.pulseaudio import PulseAudio

from subprocess import Popen, PIPE


class CustomPulseAudio(PulseAudio):
    def on_leftclick(self):
        Popen(["amixer", "set", "Master", "toggle"], stdout=PIPE)

    def on_rightclick(self):
        Popen(["gnome-control-center", "sound"])
    
