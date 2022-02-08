#!/usr/bin/bash
#xautolock -time 5 -locker 'gnome-screensaver-command -l' &
variety &
compton &
dunst &
gnome-screensaver &
#pulseeffects --gapplication-service &
#sudo chmod 666 /sys/class/backlight/intel_backlight/brightness
xinput set-prop 'Elan Touchpad' 'libinput Tapping Enabled' 1
xinput set-prop 'Elan Touchpad' 'libinput Natural Scrolling Enabled' 1
numlockx on
/home/roshan/.myscripts/automatic_royalroad_update_checker &
