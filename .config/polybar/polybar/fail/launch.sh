#!/usr/bin/env bash

# Terminate already running bar instances
killall polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch polybar
polybar time -c $HOME/.config/polybar/fail/config.ini &
polybar workspaces -c $HOME/.config/polybar/fail/config.ini &

if [[ $(xrandr -q | grep 'HDMI1 connected') ]]; then
	polybar external -c $(dirname $0)/config.ini &
fi
