###Imports###
from typing import List  # noqa: F401
import os, subprocess
from functools import partial

from libqtile import bar, layout, widget, hook, qtile, extension
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen, EzKey, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.log_utils import logger
from plasma import Plasma

from scripts.floating_window_snapping import move_snap_window
from myWidget.cmus import Cmus as myCmus
from myWidget.my_volume_widget import MyVolumeWidget

mod = "mod4"
#terminal = guess_terminal()
terminal = '/usr/bin/kitty'

############my functions#############
def command_run(qtile,command):
    os.system(command)
######################################

###Key Bindings###
keys = [
    # Spawn
    Key([mod],'Return',             lazy.spawn(terminal),                                           desc='Launch terminal'),
    Key([mod],'r',                  lazy.spawncmd(),                                                desc='Run command using prompt widget'),
    Key([mod],'v',                  lazy.spawn("vivaldi-stable"),                                   desc='Launch vivaldi'),
    Key([mod],'c',                  lazy.spawn("galculator"),                                       desc='Launch galculator'),
    Key([mod],'q',                  lazy.window.kill(),                                             desc='Kill focused window'),
    Key([mod],'w',                  lazy.function(command_run,'rofi -show drun'),                   desc='Launch rofi'),
    Key([mod],'e',                  lazy.function(command_run,'emojicherrypick -c'),              desc='Runs emoji picker and copies to clipboard'),
    
    # Window focus
    Key([mod],'h',                  lazy.layout.left(),                                             desc='Move focus to the left'),
    Key([mod],'Left',               lazy.layout.left(),                                             desc='Move focus to the left'),
    Key([mod],'l',                  lazy.layout.right(),                                            desc='Move focus to the right'),
    Key([mod],'Right',              lazy.layout.right(),                                            desc='Move focus to the right'),
    Key([mod],'k',                  lazy.layout.up(),                                               desc='Move focus up'),
    Key([mod],'Up',                 lazy.layout.up(),                                               desc='Move focus up'),
    Key([mod],'j',                  lazy.layout.down(),                                             desc='Move focus down'),
    Key([mod],'Down',               lazy.layout.down(),                                             desc='Move focus down'),
    Key([mod],'space',              lazy.layout.next(),                                             desc='Move focus to the next window'),
    Key([mod],'o',                  lazy.next_screen()),

    # Window position
    Key([mod,'shift'],'h',          lazy.layout.shuffle_left().when(layout='columns'),              desc='Move window to the left'),
    Key([mod,'shift'],'Left',       lazy.layout.shuffle_left().when(layout='columns'),              desc='Move window to the left'),
    Key([mod,'shift'],'l',          lazy.layout.shuffle_right().when(layout='columns'),             desc='Move window to the right'),
    Key([mod,'shift'],'Right',      lazy.layout.shuffle_right().when(layout='columns'),             desc='Move window to the right'),
    Key([mod,'shift'],'k',          lazy.layout.shuffle_up().when(layout='columns'),                desc='Move window up'),
    Key([mod,'shift'],'Up',         lazy.layout.shuffle_up().when(layout='columns'),                desc='Move window up'),
    Key([mod,'shift'],'j',          lazy.layout.shuffle_down().when(layout='columns'),              desc='Move window down'),
    Key([mod,'shift'],'Down',       lazy.layout.shuffle_down().when(layout='columns'),              desc='Move window down'),
    Key([mod,'shift'],'m',          lazy.group.unminimize_all(),                                    desc='Unminimize all the window in a group'),
    Key([mod],'m',                  lazy.window.toggle_minimize(),                                  desc='Minimize window'),
    Key([mod],'f',                  lazy.window.toggle_floating(),                                  desc='Toggle floating'),

    # Window size
    Key([mod,'control'],'h',        lazy.layout.grow_left(),                                        desc='Grow window to the left'),
    Key([mod,'control'],'Left',     lazy.layout.grow_left(),                                        desc='Grow window to the left'),
    Key([mod,'control'],'l',        lazy.layout.grow_right(),                                       desc='Grow window to the right'),
    Key([mod,'control'],'Right',    lazy.layout.grow_right(),                                       desc='Grow window to the right'),
    Key([mod,'control'],'k',        lazy.layout.grow_up(),                                          desc='Grow window to the up'),
    Key([mod,'control'],'Up',       lazy.layout.grow_up(),                                          desc='Grow window to the up'),
    Key([mod,'control'],'j',        lazy.layout.grow_down(),                                        desc='Grow window to the down'),
    Key([mod,'control'],'Down',     lazy.layout.grow_down(),                                        desc='Grow window to the down'),
    Key([mod,'control'],'equal',    lazy.layout.normalize(),                                        desc='Reset all window sizes'),
    Key([mod,'control'],'f',        lazy.window.toggle_fullscreen(),                                desc='Toggle fullscreen'),

    # Layout control
    Key([mod,'shift'],'Return',     lazy.layout.toggle_split(),                                     desc='Toggle stack mode'),
    Key([mod],'Tab',                lazy.next_layout(),                                             desc='Cycle layouts'),

    # Plasma layout
    Key([mod,'shift'],'h',          lazy.layout.move_left().when(layout='plasma'),                  desc='Move window to the left'),
    Key([mod,'shift'],'Left',       lazy.layout.move_left().when(layout='plasma'),                  desc='Move window to the left'),
    Key([mod,'shift'],'l',          lazy.layout.move_right().when(layout='plasma'),                 desc='Move window to the right'),
    Key([mod,'shift'],'Right',      lazy.layout.move_right().when(layout='plasma'),                 desc='Move window to the right'),
    Key([mod,'shift'],'k',          lazy.layout.move_up().when(layout='plasma'),                    desc='Move window up'),
    Key([mod,'shift'],'Up',         lazy.layout.move_up().when(layout='plasma'),                    desc='Move window up'),
    Key([mod,'shift'],'j',          lazy.layout.move_down().when(layout='plasma'),                  desc='Move window down'),
    Key([mod,'shift'],'Down',       lazy.layout.move_down().when(layout='plasma'),                  desc='Move window down'),

    Key([mod,'control'],'h',        lazy.layout.grow_width(-10).when(layout='plasma'),              desc='Shrink window width by 10px'),
    Key([mod,'control'],'Left',     lazy.layout.grow_width(-10).when(layout='plasma'),              desc='Shrink window width by 10px'),
    Key([mod,'control'],'l',        lazy.layout.grow_width(10).when(layout='plasma'),               desc='Grow window width by 10px'),
    Key([mod,'control'],'Right',    lazy.layout.grow_width(10).when(layout='plasma'),               desc='Grow window width by 10px'),
    Key([mod,'control'],'k',        lazy.layout.grow_height(10).when(layout='plasma'),              desc='Grow window height by 10px'),
    Key([mod,'control'],'Up',       lazy.layout.grow_height(10).when(layout='plasma'),              desc='Grow window height by 10px'),
    Key([mod,'control'],'j',        lazy.layout.grow_height(-10).when(layout='plasma'),             desc='Shrink window height by 10px'),
    Key([mod,'control'],'Down',     lazy.layout.grow_height(-10).when(layout='plasma'),             desc='Shrink window height by 10px'),
    Key([mod,'control'],'equal',    lazy.layout.reset_size().when(layout='plasma'),                 desc='Reset sizes of windows in plasma'),

    # XF86 commands
    Key([],'XF86AudioLowerVolume',  lazy.function(command_run,'pulsemixer --change-volume -2'),         desc='Lower pulseaudio volume by 2%'),
    Key([],'XF86AudioRaiseVolume',  lazy.function(command_run,'pulsemixer --change-volume +2'),         desc='Raise pulseaudio volume by 2%'),
    Key([],'XF86AudioMute',         lazy.function(command_run,'pulsemixer --toggle-mute'),              desc='Toggle pulseaudio mute'),
    Key([],'XF86MonBrightnessDown', lazy.function(command_run,'brightnessctl -d "intel_backlight" set 2%-'),    desc='Decrease monitor brightness by 2%'),
    Key([],'XF86MonBrightnessUp',   lazy.function(command_run,'brightnessctl -d "intel_backlight" set +2%'),    desc='Increase monitor brightness by 2%'),
    Key([],'XF86AudioPlay',         lazy.function(command_run,'cmus-remote --pause'),                   desc='Cmus pause'),
    Key([],'XF86AudioNext',         lazy.function(command_run,'cmus-remote --next'),                    desc='Cmus next'),
    Key([],'XF86AudioPrev',         lazy.function(command_run,'cmus-remote --prev'),                    desc='Cmus prev'),
    Key([],'Print',                 lazy.function(command_run,'flameshot full'),                        desc='Take a whole desktop screenshot'),
    
    # Notification
    Key(['control'],'space',        lazy.function(command_run,'dunstctl close'),                        desc='Close notification'),

    # System
    KeyChord([mod,'shift'],'q',[
        Key([mod],'n',              lazy.function(command_run,'shutdown now'),lazy.ungrab_all_chords(),                     desc='Shut down system'),
        Key([mod],'s',              lazy.function(command_run,'systemctl hybrid-sleep'),lazy.ungrab_all_chords(),           desc='Hybrid sleep system'),
        Key([mod],'h',              lazy.function(command_run,'systemctl hibernate'),lazy.ungrab_all_chords(),              desc='Hibernate system'),
        ],
        mode='System'),

    # Qtile
    KeyChord([mod],'z',[
        Key([],'q',                 lazy.shutdown(),lazy.ungrab_all_chords(),                                               desc='Kill qtile'),
        Key([],'r',                 lazy.reload_config(),lazy.ungrab_all_chords(),                                          desc='Reload config'),
        Key([],'l',                 lazy.function(command_run,'betterlockscreen --off 15 -l dim -- -e &'),lazy.ungrab_all_chords(), desc='lock screen'),
        ],
        mode='Qtile'),

    # Dunst
    KeyChord([mod],'d',[
        Key([],'h',                 lazy.function(command_run,'dunstctl history-pop'),lazy.ungrab_all_chords(),             desc='Show last notification'),
        Key([],'a',                 lazy.function(command_run,'dunstctl context'),lazy.ungrab_all_chords(),                 desc='Show context menu'),
        Key([],'c',                 lazy.function(command_run,'dunstctl close-all'),lazy.ungrab_all_chords(),               desc='Close all notifications'),
        ],
        mode='Notification'),

    # ScratchPad
    KeyChord([mod,'shift'],'s',[
        Key([],'c',                 lazy.group['scratchpad'].dropdown_toggle('calculator'),lazy.ungrab_all_chords(),       desc='Toggle calculator scratchpad'),
        Key([],'k',                 lazy.group['scratchpad'].dropdown_toggle('terminal'),lazy.ungrab_all_chords(),         desc='Toggle terminal scratchpad'),
        Key([],'n',                 lazy.group['scratchpad'].dropdown_toggle('notepad'),lazy.ungrab_all_chords(),          desc='Toggle notepad scratchpad'),
        ],
        mode='Scratchpad'),

    # Plasma
    KeyChord([mod],'s',[
        Key([],'h',                 lazy.layout.mode_horizontal(),lazy.ungrab_all_chords(),              desc='Horizontal mode for plasma layout'),
        Key([],'v',                 lazy.layout.mode_vertical(),lazy.ungrab_all_chords(),                desc='Vertical mode for plasma layout'),
        KeyChord([],'s',[
            Key([],'h',             lazy.layout.mode_horizontal_split(),lazy.ungrab_all_chords(),        desc='Horizontal split mode for plasma'),
            Key([],'v',             lazy.layout.mode_vertical_split(),lazy.ungrab_all_chords(),          desc='Vertical split mode for plasma'),
            ],
            mode='split'),
        ],
        mode='Set mode'),

    KeyChord([mod],'i',[
        Key([],'h',                 lazy.layout.integrate_left(),lazy.ungrab_all_chords(),               desc='Integrate left for plasma layout'),
        Key([],'Left',              lazy.layout.integrate_left(),lazy.ungrab_all_chords(),               desc='Integrate left for plasma layout'),
        Key([],'l',                 lazy.layout.integrate_right(),lazy.ungrab_all_chords(),              desc='Integrate right plasma layout'),
        Key([],'Right',             lazy.layout.integrate_right(),lazy.ungrab_all_chords(),              desc='Integrate right plasma layout'),
        Key([],'k',                 lazy.layout.integrate_up(),lazy.ungrab_all_chords(),                 desc='Integrate up plasma layout'),
        Key([],'Up',                lazy.layout.integrate_up(),lazy.ungrab_all_chords(),                 desc='Integrate up plasma layout'),
        Key([],'j',                 lazy.layout.integrate_down(),lazy.ungrab_all_chords(),               desc='Integrate down plasma layout'),
        Key([],'Down',              lazy.layout.integrate_down(),lazy.ungrab_all_chords(),               desc='Integrate down plasma layout'),
        ],
        mode='Integrate'),
    ]

###Groups###
groups = [
    Group('1', position=1, label='', matches=[Match(wm_class=['Vivaldi-stable'])]),
    Group('2', position=2, label='', matches=[Match(wm_class=['kitty'])]),
    Group('3', position=3, label='', matches=[Match(wm_class=['Write'])]),
    Group('4', position=4, label='', matches=[Match(wm_class=['Evince']), Match(wm_class=['llpp'])]),
    Group('5', position=5),
    Group('6', position=6),
    Group('7', position=7),
    Group('8', position=8, label='♫', matches=[Match(wm_class=['Rhythmbox'])]),
    Group('9', position=9, label='', spawn=["kitty --class 'ranger' -e ranger"], layout='max'),
    Group('p'),
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

groups.append(ScratchPad('scratchpad', [DropDown('calculator', 'galculator'),
    DropDown('terminal', 'kitty', opacity=0.95),
    DropDown('notepad', '/home/roshan/repos/Write/Write', opacity=0.8, height=0.5),]))

###Layouts###
layouts = [
    Plasma(border_normal='#220000', border_focus='#881111', border_normal_fixed='#220000', border_focus_fixed='#881111',border_width=2,border_width_single=0),
    layout.Max(),
    #layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=2, margin=0, margin_on_single=0),
    #layout.MonadWide(border_focus='#881111',single_border_width=0),
    ]

###Widgets###
widget_defaults = dict(
    font='FreeSans',
    fontsize=13,
    padding=3,
    )
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar([
            widget.GroupBox(fontsize=18, highlight_method='line', visible_groups=['1','2','3','4','5','6','7','8','9']),
            widget.Prompt(),
            widget.Chord(),
            widget.Spacer(mouse_callbacks={'Button1':partial(os.system,'flameshot gui')}),
            widget.Clock(format='%d/%m %a %I:%M %p', mouse_callbacks={'Button1':partial(os.system,'zenity --calendar &')}),
            widget.Spacer(mouse_callbacks={'Button1':lazy.group['scratchpad'].dropdown_toggle('notepad')}),
            widget.WidgetBox(widgets=[
                                widget.NetGraph(),
                                widget.Systray(),
                                ],
                            close_button_location='right',
                            text_closed='',
                            text_open='',
                            fontsize=16,
                            ),
            widget.Sep(),
            myCmus(),
            widget.Sep(),
            #widget.PulseVolume(fmt='{}'),
            MyVolumeWidget(),
            widget.Sep(),
            widget.Battery(format='{char}{percent:2.2%}',notify_below=10,charge_char=' ', discharge_char='', foreground='ffffff'),
            widget.Sep(),
            ],
            24,
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
cursor_warp = True
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(wm_class='pinentry'),  # GPG key password entry
    Match(wm_class='Pinentry-gtk-2'),  # GPG key password entry
    Match(wm_class='galculator'),   # Calculator
    ])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "qtile"

@hook.subscribe.startup_once
def autostart():
    path = '/home/roshan/.config/qtile/scripts/autostart.sh'
    subprocess.call([path])

@hook.subscribe.client_managed
def move_to_group(client):
    if client.window.get_wm_class()[0] != 'ranger':
        client.group.cmd_toscreen()
