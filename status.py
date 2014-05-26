#!/usr/bin/python3
# encoding: utf-8
# --------------------------------------------------------------------------

from i3pystatus import Status

status = Status(standalone=True)

# Fehca y hora
status.register("clock",
                format="%d/%m/%Y %X",)

status.register("load")

status.register("battery",
                format=("{status}/{consumption:.2f}W {percentage:.2f}% "
                        "[{percentage_design:.2f}%] {remaining:%E%hh:%Mm}"),
                path="/sys/class/power_supply/BAT1/uevent",
                alert=True,
                alert_percentage=5,
                status={
                    "DIS": "↓",
                    "CHR": "↑",
                    "FULL": "=",
                },)

status.register("network",
                interface="p8p1",
                format_up="{v4cidr}",)

status.register("wireless",
                interface="wlp2s0",
                format_up="{essid} {quality:03.0f}%",)

status.register("disk",
                path="/",
                format="{used}/{total}G [{avail}G]",)

status.register("pulseaudio",
                format="♪{volume}% {muted}",)

status.run()
