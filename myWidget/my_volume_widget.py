import subprocess
from libqtile.widget.base import ThreadPoolText

class MyVolumeWidget(ThreadPoolText):
    """A small widget to show volumes"""

    defaults = [
            ("update_interval", 0.5, "Update time in seconds."),
            ("format", "{char}{vol}%", "Format for the text displayed."),
            ]

    def __init__(self, **config):
        ThreadPoolText.__init__(self, "", **config)
        MyVolumeWidget.defaults.append(("mouse_callbacks", {'Button1': self.toggle_mute, 'Button3' : self.next_display_sink, 'Button4': self.raise_volume, 'Button5': self.lower_volume}, "Sets mouse callbacks."),)
        self.add_defaults(MyVolumeWidget.defaults)

    def toggle_mute(self):
        subprocess.call(f"pulsemixer --id {self.display_sink} --toggle-mute", shell=True)
        self.poll()

    def raise_volume(self):
        subprocess.call(f"pulsemixer --id {self.display_sink} --change-volume +2", shell=True)

    def lower_volume(self):
        subprocess.call(f"pulsemixer --id {self.display_sink} --change-volume -2", shell=True)

    def get_sinks(self):
        pulsemixer_return_values = subprocess.check_output("pulsemixer --list-sinks", shell=True, text=True).split("\n")
        self.sinks = {}
        for sink in pulsemixer_return_values:
            if sink.split("\t")[0] == "Sink:":
                split_string = sink.split('sink-')[1]
                self.sinks[split_string[:split_string.index(',')]] = sink
                if "Default" in sink:
                    self.default_sink = split_string[:split_string.index(',')]

    def get_volume(self, id_):
        sink = self.sinks[id_]
        vol = subprocess.check_output(f"pulsemixer --id {id_} --get-volume",shell=True, text=True)
        mute = subprocess.check_output(f"pulsemixer --id {id_} --get-mute",shell=True, text=True)
        if int(mute):
            return 'M', 'M'
        return vol.split()

    def next_display_sink(self):
        ids = list(self.sinks)
        if (index:= ids.index(self.display_sink)) + 1 < len(ids):
            self.display_sink = ids[index+1]
        else:
            self.display_sink = ids[0]

    def poll(self):
        if hasattr(self, 'default_sink'):
            old_default_sink = self.default_sink
        else:
            old_default_sink = None
        #breakpoint()
        self.get_sinks()
        if old_default_sink != self.default_sink:
            self.display_sink = self.default_sink
        vol_left, vol_right = self.get_volume(self.display_sink)
        if vol_left == vol_right:
            vol = vol_left
        else:
            vol = "L" + vol_left
        if "Built-in" in self.sinks[self.display_sink]:
            char = ''
        else:
            char = ''

        return self.format.format(char=char, vol=vol)
