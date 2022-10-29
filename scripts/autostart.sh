#!/usr/bin/bash
xidlehook \
    --not-when-fullscreen \
    --not-when-audio \
    --timer 180 \
        "betterlockscreen -l dim --off 15 -- -e &" '' \
    --timer 1800 \
        "systemctl suspend" '' &
