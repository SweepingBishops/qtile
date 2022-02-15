#!/usr/bin/bash
#xautolock -time 5 -locker 'gnome-screensaver-command -l' &
picom &
nitrogen --restore &
dunst &
gnome-screensaver &
#pulseeffects --gapplication-service &
xinput set-prop 'Elan Touchpad' 'libinput Tapping Enabled' 1 &
xinput set-prop 'Elan Touchpad' 'libinput Natural Scrolling Enabled' 1 &
setxkbmap in,gr -variant eng,simple -option grp:shifts_toggle &
numlockx on &
/home/roshan/.myscripts/automatic_royalroad_update_checker &
qtile cmd-obj -o group 1 -f toscreen &
