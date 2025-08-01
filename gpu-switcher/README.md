
# GPU Switcher for System76 (i3blocks)

A simple i3blocks module to display and switch between GPU modes (Integrated, Hybrid, NVIDIA) on System76 laptops using `system76-power`.

---

## Features

- Shows current GPU mode in the i3 status bar.
- **Clickable:**
    - **Left-click:** Cycles between GPU modes (Integrated → Hybrid → NVIDIA → Integrated).
    - **Right-click:** Opens a selection menu (e.g., using `zenity` or `yad`) to choose the desired GPU mode.
- Designed for System76 hybrid graphics laptops.
- Lightweight and non-intrusive.

---

## Setup

1.  **Place the script:**
    Copy `gpu-switcher.py` to:
    ```
    ~/.config/i3blocks/gpu-switcher/
    ```

2.  **Make it executable:**
    ```bash
    chmod +x ~/.config/i3blocks/gpu-switcher/gpu-switcher.py
    ```

3.  **Add to i3blocks config:**
    Add the following block to your `~/.config/i3blocks/config` file:
    ```ini
    [gpu-switcher]
    command=~/.config/i3blocks/gpu-switcher/gpu-switcher.py
    interval=600
    # Add optional click actions if your script supports them:
    # BUTTON=1 for left-click, BUTTON=3 for right-click
    # min_width=50 # Optional: Adjust if text/emoji are cut off
    ```

---

## Usage

- The i3bar block will display the current GPU mode, typically indicated by a 🎮 emoji or text like "Integrated", "Hybrid", or "NVIDIA".
- **To switch modes:**
    - **Left-click** on the block to quickly cycle through the modes (Integrated → Hybrid → NVIDIA → Integrated).
    - **Right-click** on the block to open a selection dialog where you can choose your desired GPU mode.
- After selecting a new GPU mode, the system will initiate the transition. This may take a moment.
- **Important:** A manual system reboot is required for the new GPU mode to take full effect.

---



## Tested On

-   System76 Lemur Pro (Intel + NVIDIA Hybrid Graphics)
-   Pop!\_OS 22.04
-   i3 with i3blocks

---

## License

MIT License

---

## Contributing

Feel free to fork, submit pull requests, or open issues to improve this tool.
