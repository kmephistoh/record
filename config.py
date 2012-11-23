from libqtile.manager import Key, Screen, Group
from libqtile.command import lazy
from libqtile import layout, bar, widget,hook
@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == 'dialog'
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True

mod="mod4"
keys = [
    # Switch between windows in current stack pane
    Key( [], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 -q set Master 2dB+")),
    Key( [], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 -q set Master 2dB-")),
    Key( [], "XF86AudioMute", lazy.spawn("amixer -c 0 -q set Master toggle")),
    Key(["mod1"], "k", lazy.layout.down()),
    Key(["mod1"], "j", lazy.layout.up()),
    Key(["mod1"], "h", lazy.layout.previous()),
    Key(["mod1"], "l", lazy.layout.previous()),
    # Move windows up or down in current stack
    Key( ["mod1", "control"], "k", lazy.layout.shuffle_down()),
    Key( ["mod1", "control"], "j", lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key( ["mod1"], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key( ["mod1", "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with multiple stack panes
    Key( [mod, "shift"], "Return", lazy.layout.toggle_split()),
    # Application launchers
    Key([mod], "t", lazy.spawn("terminator")),
    Key([mod], "c", lazy.spawn("chromium")),
    Key([mod], "f", lazy.spawn("firefox")),
    Key([mod], "m", lazy.spawn("clementine")),
    Key([mod], "e", lazy.spawn("nautilus")),
    Key([mod], "o", lazy.spawn("opera")),

    # Toggle between different layouts as defined below
    Key(["mod1"], "Tab",    lazy.nextlayout()),
    Key([mod], "x",      lazy.window.kill()),
    Key(["mod1", "control"], "r", lazy.restart()),
]

groups = [
    Group("t"),
    Group("n"),
    Group("a"),
    Group("o"),
]
for i in groups:
    # mod1 + letter of group = switch to group
    keys.append( Key(["mod1"], i.name, lazy.group[i.name].toscreen()))

    # mod1 + shift + letter of group = switch to & move focused window to group
    keys.append( Key(["mod1", "shift"], i.name, lazy.window.togroup(i.name)))

layouts = [ layout.Max(), layout.Stack(stacks=2) ]

screens = [ Screen( bottom = bar.Bar(
                    [   widget.GroupBox(margin_y=1,fontsize=18,padding=int(0.5)),
                        widget.WindowName(foreground="404040"),
                        widget.Volume(foreground="404040"),
                        widget.Systray(),
                        widget.Clock('%Y/%m/%d %a %H:%M',foreground="215578"),
                    ], 25,),
                  ),
]

main = None
follow_mouse_focus = True
cursor_warp = False
floating_layout = layout.Floating()
mouse =() 

