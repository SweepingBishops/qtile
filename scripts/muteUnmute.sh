#!/usr/bin/fish
for i in (pactl list short sinks|awk '{print $1}');
	pactl set-sink-mute $i toggle;
end
