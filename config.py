# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook, qtile, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen, EzKey
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os, subprocess #for the autostart
from functools import partial
from scripts.floating_window_snapping import move_snap_window
#import dbus_next #for bluetooth

mod = "mod4"
#terminal = guess_terminal()
terminal = '/usr/bin/kitty'

##########my functions#############
def screenLock(qtile):
    subprocess.call(['/home/roshan/.config/qtile/scripts/screenLock.sh'])

def lowerVolume(qtile):
    subprocess.call(['/home/roshan/.config/qtile/scripts/lowerVolume.sh'])

def raiseVolume(qtile):
    subprocess.call(['/home/roshan/.config/qtile/scripts/raiseVolume.sh'])

def muteUnmute(qtile):
    subprocess.call(['/home/roshan/.config/qtile/scripts/muteUnmute.sh'])

def brightDown(qtile):
    subprocess.call(['/home/roshan/.config/qtile/scripts/brightDown.sh'])

def brightUp(qtile):
    subprocess.call(['/home/roshan/.config/qtile/scripts/brightUp.sh'])

def screenshot(qtile):
    #subprocess.call(['/home/roshan/.config/qtile/scripts/screenshot_full.sh'])
    os.system('flameshot full -p /home/roshan/Pictures/Screenshots/')

def rofi(qtile):
    os.system('rofi -show run')

#def minimize(qtile):
#   subprocess.call(['/home/roshan/.config/qtile/scripts/minimize.sh'])
#
#def unminimize(qtile):
#   subprocess.call(['/home/roshan/.config/qtile/scripts/unminimize.sh'])
####################################



keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    # Switch between windows
    EzKey("M-j", lazy.layout.left(), desc="Move focus to left"),
    Key([mod],"Left", lazy.layout.left(), desc="Move focus to left"),
    EzKey("M-k", lazy.layout.down(), desc="Move focus to down"),
    Key([mod],"Down", lazy.layout.down(), desc="Move focus to down"),
    EzKey("M-l", lazy.layout.up(), desc="Move focus up"),
    Key([mod],"Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod],'semicolon', lazy.layout.right(), desc="Move focus right"),
    Key([mod],'Right', lazy.layout.right(), desc="Move focus right"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    EzKey("M-S-j", lazy.layout.shuffle_left()),
    Key([mod,"shift"],"Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    EzKey("M-S-k", lazy.layout.shuffle_down()),
    Key([mod,"shift"],"Down", lazy.layout.shuffle_down(),
        desc="Move window to the down"),
    EzKey("M-S-l", lazy.layout.shuffle_up()),
    Key([mod,"shift"],"Up", lazy.layout.shuffle_up(),
        desc="Move window up"),
    Key([mod,"shift"],'semicolon', lazy.layout.shuffle_right(), desc="Move focus right"),
    Key([mod,"shift"],'Right', lazy.layout.shuffle_right(), desc="Move focus right"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    EzKey("M-C-j", lazy.layout.grow_left()),
    Key([mod,"control"],"Left", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    EzKey("M-C-k", lazy.layout.grow_down()),
    Key([mod,"control"],"Down", lazy.layout.grow_down(),
        desc="Grow window to the down"),
    EzKey("M-C-l", lazy.layout.grow_up()),
    Key([mod,"control"],"Up", lazy.layout.grow_up(),
        desc="Grow window up"),
    Key([mod,"control"],'semicolon', lazy.layout.grow_right(), desc="Move focus right"),
    Key([mod,"control"],'Right', lazy.layout.grow_right(), desc="Move focus right"),
    Key([mod], "comma", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "period", lazy.layout.grow()),
    Key([mod], "n", lazy.layout.shrink()),
    Key([mod], "m", lazy.layout.maximize()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    EzKey("A-z",lazy.spawn("vivaldi"), lazy.group['2'].toscreen(), desc="Launch Vivaldi and go to group 2."),
    EzKey("A-c",lazy.spawn("gnome-calculator"), desc="Launches Calculator"),
    EzKey("A-l",lazy.function(screenLock),desc="Lock Screen"),
    Key([],'XF86AudioLowerVolume', lazy.function(lowerVolume), desc="Lowers PulseAudio Volume"),
    Key([],'XF86AudioRaiseVolume', lazy.function(raiseVolume), desc="Raises PulseAudio Volume"),
    Key([],'XF86AudioMute', lazy.function(muteUnmute), desc="Toggles audio mute"),
    Key([],'XF86MonBrightnessDown', lazy.function(brightDown), desc="Decreases Monitor Brightness"),
    Key([],'XF86MonBrightnessUp', lazy.function(brightUp), desc="Increases Monitor Brightness"),
    Key([],'Print', lazy.function(screenshot), desc="Takes a screenshot and saves it to ~/Pictures/Screenshots"),
    Key([mod],"w",lazy.function(rofi), desc='Opens rofi run menu'),
    #Key(['mod1', "shift"], "m", lazy.function(unminimize), desc="unminimize window"), 
    #Key(['mod1'], "m", lazy.function(minimize)), 
    ]

#groups = [Group(i) for i in "123456789"]
#
#for i in groups:
#    keys.extend([
#        # mod1 + letter of group = switch to group
#        Key([mod], i.name, lazy.group[i.name].toscreen(),
#            desc="Switch to group {}".format(i.name)),
#
#        # mod1 + shift + letter of group = switch to & move focused window to group
#        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
#            desc="Switch to & move focused window to group {}".format(i.name)),
#        # Or, use below if you prefer not to switch to that group.
#        # # mod1 + shift + letter of group = move focused window to group
#        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#        #     desc="move focused window to group {}".format(i.name)),
#        ])
groups = [
    Group('1', position=1),
    Group('2', matches=[Match(wm_class=['Vivaldi-stable'])], position=2),
    Group('3', position=3),
    Group('4', position=4),
    Group('5', position=5),
    Group('6', position=6),
    Group('7', position=7),
    Group('8', position=8),
    Group('9', spawn=['kitty -e ranger',
        #lazy.window.togroup('9').when(focused=Match(wm_class='kitty'))
        ], position=9),
    ]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),
        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        ])

layouts = [
    layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=2, margin=1, margin_on_single=0),
    layout.Max(),
    #layout.MonadWide(border_focus='#881111',single_border_width=0),
    #layout.Slice(width=683,fallback=layout.MonadWide()),
    #layout.Tile(),
    # Try more layouts by unleashing below layouts.
    #layout.TreeTab(),
    #layout.Stack(num_stacks=2),
    #layout.Bsp(),
    #layout.Matrix(),
    #layout.MonadTall(),
    #layout.RatioTile(),
    #layout.VerticalTile(),
    #layout.Zoomy(),
    #layout.Floating()
    ]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
    )
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [#widget.CurrentLayout(),
            widget.GroupBox(),
            widget.Prompt(),
            widget.Notify(),
            widget.Spacer(mouse_callbacks={'Button1':partial(os.system,'rofi -show run &')}),
            widget.Clock(format='%d/%m %a %I:%M %p', mouse_callbacks={'Button1':partial(os.system,'zenity --calendar &')}),
            widget.Spacer(mouse_callbacks={'Button1':partial(os.system,'flameshot gui -p /home/roshan/Pictures/Screenshots/')}),
            widget.Chord(
                chords_colors={
                    'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                    ),
            #widget.TextBox("default config", name="default"),
            #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
            #widget.Wlan(),
            #widget.Sep(),
            widget.WidgetBox(widgets=[
                widget.Systray(),
            ],
            close_button_location='right',
            text_closed='',
            text_open='',
            fontsize=16,
            ),
            widget.Sep(),
            widget.PulseVolume(fmt='Vol:{}'),
            #widget.Backlight(),
            #widget.Sep(),
            #widget.KeyboardKbdd(),
            #widget.KeyboardLayout(),
            widget.Sep(),
            widget.Battery(format='{char}{percent:2.2%}',notify_below=10,charge_char='', discharge_char='', foreground='ffffff'),
            widget.Sep(),
            #widget.Net(),
            #widget.Bluetooth(max_chars=5,hci='/org/bluez/hci0/dev_41_42_21_10_F2_AA'),
            #widget.TextBox(text='reload config',mouse_callbacks={'Button1': lambda:qtile.lazy.reload_config()}),
            #widget.Sep(),
            #widget.QuickExit(default_text= '[Logout]'),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", move_snap_window(snap_dist=40),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    ])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    path = '/home/roshan/.config/qtile/scripts/autostart.sh'
    subprocess.call([path])