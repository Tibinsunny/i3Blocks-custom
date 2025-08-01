#!/usr/bin/env python3

import subprocess
import sys
import os


block_button = os.environ.get("BLOCK_BUTTON")

def set_gpu_mode(choice):
    command_map = {
        "External GPU": ["system76-power", "graphics", "nvidia"],
        "Integrated GPU": ["system76-power", "graphics", "integrated"],
        "Hybrid": ["system76-power", "graphics", "hybrid"]
    }

    command = command_map.get(choice)
    if not command:
        return

    # Show progress dialog in background
    progress = subprocess.Popen([
        "zenity", "--progress",
        "--pulsate",
        "--auto-close",
        "--no-cancel",
        "--title=Switching GPU",
        f"--text=Switching to {choice}..."
    ])

    # Run the system76-power command (blocking)
    try:
        subprocess.run(command, check=True)
        subprocess.Popen(["notify-send", f"GPU mode switched to: {choice}"])
    except subprocess.CalledProcessError:
        subprocess.Popen(["notify-send", f"Failed to switch to: {choice}"])
    finally:
        progress.terminate()

def show_zenity_list():
    try:
        choice = subprocess.check_output([
            "zenity", "--list",
            "--title=Choose Graphics Mode",
            "--column=Select GPU",
            "External GPU", "Integrated GPU", "Hybrid"
        ], stderr=subprocess.DEVNULL).decode().strip()

        if choice:
            set_gpu_mode(choice)

    except subprocess.CalledProcessError:
        pass  # User cancelled

if block_button == "1":
    show_zenity_list()
print("🎮")
