#!/usr/bin/fish
set brightness (cat /sys/class/backlight/intel_backlight/brightness)
if test $brightness -eq 1;
echo 10 > /sys/class/backlight/intel_backlight/brightness;
else if test $brightness -lt 50;
	math $brightness + 10 > /sys/class/backlight/intel_backlight/brightness;
else if test $brightness -lt 200;
	math $brightness + 50 > /sys/class/backlight/intel_backlight/brightness;
else if test $brightness -lt 1000;
	math $brightness + 100 > /sys/class/backlight/intel_backlight/brightness;
else;
	math $brightness + 500 > /sys/class/backlight/intel_backlight/brightness;
end
