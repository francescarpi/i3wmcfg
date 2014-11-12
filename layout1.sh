#!/bin/bash

i3-msg workspace 1
i3-msg layout tabbed
i3-msg exec terminator

i3-msg workspace 2
i3-msg layout tabbed
i3-msg exec emacs --client
i3-msg exec google-chrome
