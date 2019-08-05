#!/usr/bin/env bash
flameshot gui --raw | ./shadow.py --iterations=75 --border=40 --offset-x=0 --offset-y=25 --background="#ffffff" --shadow="#858585" | xclip -selection clipboard -t image/png
