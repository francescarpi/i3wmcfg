#!/usr/bin/env python
# Install:
#  sudo pacman -S python-pip playerctl python-colour python-netifaces python-dbus otf-font-awesome gsimplecal termite xf86-input-synaptics
#  sudo pip install git+https://github.com/enkore/i3pystatus.git fontawesome i3ipc
# --------------------------------------------------------------------------

import logging
import math

import fontawesome as fa

from i3pystatus import Status, get_module
from i3pystatus.core.command import run_through_shell
from i3pystatus.updates import pacman, cower

from subprocess import Popen, PIPE

from touchpad import Touchpad

logger = logging.getLogger('i3pystatus')

status = Status(logfile='$HOME/.i3pystatus.log')

status.register(
    'text',
    text=fa.icons['power-off'],
    on_leftclick='i3-nagbar -t warning -m "What do you want to do?" -b "Reboot" "reboot" -b "Shutdown" "shutdown -h now"',
)

status.register(
    'clock',
    format=fa.icons['clock'] + ' %H:%M:%S ' + fa.icons['calendar'] + ' %d',
    color='#C678DD',
    interval=1,
    on_leftclick='/usr/bin/gsimplecal',
)


status.register(
    'network',
    interface='enp3s0',
    color_up='#8AE234',
    color_down='#EF2929',
    format_up=fa.icons['project-diagram'] + ' {interface} {network_graph_recv}{bytes_recv}KB/s',
    format_down=fa.icons['project-diagram'],
)


status.register(
    'network',
    interface='wlp4s0',
    color_up='#8AE234',
    color_down='#EF2929',
    format_up=fa.icons['wifi'] + ' {interface} {network_graph_recv}{bytes_recv}KB/s',
    format_down=fa.icons['wifi'],
)


@get_module
def backlight(self):
    levels = [15, 25, 50, 75, 100]

    process = Popen(['xbacklight', '-get'], stdout=PIPE)
    out, err = process.communicate()

    if not err:
        out = math.ceil(float(out))
        try:
            level_index = levels.index(out)
        except ValueError:
            level_index = len(levels) - 2

        try:
            backlight = levels[level_index + 1]
        except IndexError:
            backlight = levels[0]

        process = Popen(['xbacklight', '-set', str(backlight)], stdout=PIPE)
        process.communicate()

status.register(
    'backlight',
    interval=5,
    format=fa.icons['desktop'] + ' {percentage:.0f}%',
    backlight='intel_backlight',
    on_leftclick=backlight,
)


status.register(
    'battery',
    battery_ident='BAT0',
    interval=5,
    format=' {status} {percentage:.0f}%',
    alert=True,
    alert_percentage=15,
    color='#FFFFFF',
    critical_color='#FF1919',
    charging_color='#E5E500',
    full_color='#D19A66',
    status={
        'DIS': fa.icons['battery-full'],
        'CHR': fa.icons['battery-full'],
        'FULL': fa.icons['battery-full'],
    },
)

status.register(
    'temp',
    format=fa.icons['thermometer-full'] + ' {temp} °C',
    color='#78EAF2',
)

status.register(
    'mem',
    color='#999999',
    warn_color='#E5E500',
    alert_color='#FF1919',
    format=fa.icons['microchip'] + ' {avail_mem}/{total_mem} GB',
    divisor=1073741824,
)

status.register(
    'disk',
    color='#56B6C2',
    path='/home',
    on_leftclick='nautilus',
    format=fa.icons['home'] + ' {avail} GB',
)


status.register(
    'keyboard_locks',
    format=fa.icons['keyboard'] + ' {caps}',
    caps_on='Caps Lock',
    caps_off='',
    color='#e60053',
)


status.register(
   'spotify',
   format=fa.icons['spotify'] + ' {title} {status}',
   format_no_player=fa.icons['spotify'] + ' Not running',
)

status.register(
    'cpu_usage',
    on_leftclick='termite --title=htop -e \'htop\'',
    format=fa.icons['heartbeat'] + ' {usage}%',
)


# status.register(
#     Touchpad,
#     format=fa.icons['fingerprint'] + ' {status}',
#     yesno=fa.icons['times'] + ',' + fa.icons['check'],
# )


# status.register(
#     'pomodoro',
#     sound=False,
# )


status.register(
    'pulseaudio',
    color_unmuted='#98C379',
    color_muted='#E06C75',
    format_muted=fa.icons['volume-up'] + ' [muted]',
    format=fa.icons['volume-up'] + ' {volume}%',
)

status.register(
    'window_title',
    format=fa.icons['window-maximize'] + ' {title}'
)


status.run()
