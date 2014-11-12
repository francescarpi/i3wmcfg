#!/usr/bin/python3
# encoding: utf-8
# --------------------------------------------------------------------------

from i3pystatus import Status
    
status = Status(standalone=True)

status.register("custom.clock",
                format="⏰ %d/%m/%Y %H:%M",)

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

status.register("custom.network",
                interface="p8p1",
                format_up="{v4cidr}",)

status.register("custom.wireless",
                interface="wlp2s0",
                format_up="{essid} {quality:.0f}%",)

status.register("disk",
                path="/",
                format="⛁ {used}/{total}G [{avail}G]",)

status.register("mem", format="{avail_mem:.0f} Mb")

status.register("custom.pulseaudio",
                format="♪{volume}% {muted}",)

status.register("custom.backlight",
                format="⛭{percentage:.0f}%",
                backlight="intel_backlight")


status.run()
