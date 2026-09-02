#!/usr/bin/env python3
"""Builds the asciicast for the profile header GIF, with a typing effect."""
import json

SP = "/tmp/claude-1000/-home-mampi/9723eb75-a80e-45be-a96a-ce08c86b35b1/scratchpad"
ESC = "\x1b"
GREEN = ESC + "[1;32m"
CYAN = ESC + "[36m"
DIM = ESC + "[0;90m"
OFF = ESC + "[0m"

ev = []
t = 0.35


def out(s):
    ev.append([round(t, 3), "o", s])


def prompt(cmd):
    global t
    out(GREEN + "$" + OFF + " ")
    for ch in cmd:                      # tecleo carácter a carácter
        t += 0.045
        out(ch)
    t += 0.28
    out("\r\n")


def says(lines, colour="", pause=0.55):
    global t
    for ln in lines:
        t += 0.09
        out(colour + ln + OFF + "\r\n")
    t += pause
    out("\r\n")


prompt("whoami")
says(["Josep Mampel Marqués — Barcelona"])

prompt("cat day-job")
says(["Embedded automotive. Bootloaders, AUTOSAR, diagnostics, secure boot.",
      "You do not redeploy on a Friday when the code ships inside a car."], DIM)

prompt("cat night-job")
says(["Kubernetes controllers in Go.",
      "Signed firmware became signed images. The watchdog became a probe."], DIM)

prompt("ls ~/work")
says(["provenance-gate    webapp-operator    idp-backstage",
      "llm-gateway        birdvision         mampiz.dev"], CYAN)

prompt("echo $LOOKING_FOR")
says(["platform / cloud infrastructure"])

t += 1.8
out(GREEN + "$" + OFF + " ")

header = {"version": 2, "width": 76, "height": 18,
          "env": {"SHELL": "/bin/bash", "TERM": "xterm-256color"}}
with open(SP + "/intro.cast", "w") as fh:
    fh.write(json.dumps(header) + "\n")
    for e in ev:
        fh.write(json.dumps(e) + "\n")
print(f"cast escrito: {len(ev)} eventos, {t:.1f}s de duración")
