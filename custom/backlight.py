#!/usr/bin/env python
# encoding: utf-8
# --------------------------------------------------------------------------

from i3pystatus.backlight import Backlight

from subprocess import Popen, PIPE


class CustomBacklight(Backlight):

    @property
    def current_backlight(self):
        process = Popen(["xbacklight"], stdout=PIPE)
        (output, error) = process.communicate()
        exit_code = process.wait()
        return round(float(output[:-1]))
        
    def on_leftclick(self):
        current = self.current_backlight
        if current == 100.0:
            setback = 15
        elif current == 15.0:
            setback = 30
        else:
            setback = 100
        
        Popen(["xbacklight", "-set", str(setback)])
                         
