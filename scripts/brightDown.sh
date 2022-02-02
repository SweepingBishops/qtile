#!/usr/bin/fish
set brightness (cat /sys/class/backlight/intel_backlight/brightness)
if test $brightness -gt 1000;
	math $brightness - 500 > /sys/class/backlight/intel_backlight/brightness;
else if test $brightness -gt 200;
	math $brightness - 100 > /sys/class/backlight/intel_backlight/brightness;
else if test $brightness -gt 50;
	math $brightness - 50 > /sys/class/backlight/intel_backlight/brightness;
else if test $brightness -gt 10;
	math $brightness - 10 > /sys/class/backlight/intel_backlight/brightness;
else;
	echo 1 > /sys/class/backlight/intel_backlight/brightness;
end
