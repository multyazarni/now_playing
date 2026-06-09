import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import json

APP_DIR = Path(__file__).resolve().parent
CONFIG_FILE = APP_DIR / "config.json"

def default_search_paths():
    home = Path.home()
    appdata = home / "AppData" / "Roaming"
    localappdata = home / "AppData" / "Local"
    return [
        appdata / "AIMP" / "NowPlaying.txt",
        appdata / "AIMP" / "Music" / "NowPlaying.txt",
        localappdata / "AIMP" / "NowPlaying.txt",
        localappdata / "AIMP" / "Music" / "NowPlaying.txt",
        home / "Documents" / "aimp" / "NowPlaying.txt",
        home / "Documents" / "NowPlaying.txt",
    ]

def find_file():
    for p in default_search_paths():
        if p.exists():
            return p
    return None

def load_config():
    if CONFIG_FILE.exists():
        try:
            data = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
            p = data.get("file_path")
            if p:
                path = Path(p)
                if path.exists():
                    return path
        except Exception:
            pass
    return find_file()

def save_config(path):
    CONFIG_FILE.write_text(
        json.dumps({"file_path": str(path)}, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

root = tk.Tk()
root.title("Now Playing")
root.configure(bg="#3b2414")
root.wm_attributes("-topmost", True)
root.state("zoomed")

FILE_PATH = load_config()
last_current = None
last_previous = None

main = tk.Frame(root, bg="#3b2414")
main.pack(expand=True, fill="both")

top_spacer = tk.Frame(main, bg="#3b2414")
top_spacer.pack(expand=True, fill="both")

center_frame = tk.Frame(main, bg="#3b2414")
center_frame.pack()

#path_label = tk.Label(
 #   center_frame,
 #   text=str(FILE_PATH) if FILE_PATH else "No file selected",
 #   font=("Arial", 12),
 #   fg="#d8c8bb",
 #   bg="#3b2414",
 #   wraplength=1100,
 #   justify="center"
#)
#path_label.pack(pady=(0, 12))

current_label = tk.Label(
    center_frame,
    text="Waiting for track...",
    font=("Arial", 58, "bold"),
    fg="#ffffff",
    bg="#3b2414",
    wraplength=1150,
    justify="center"
)
current_label.pack()

tk.Frame(center_frame, height=14, bg="#3b2414").pack()

previous_label = tk.Label(
    center_frame,
    text="",
    font=("Arial", 24),
    fg="#e0d0c5",
    bg="#3b2414",
    wraplength=1100,
    justify="center"
)
previous_label.pack()

bottom_spacer = tk.Frame(main, bg="#3b2414")
bottom_spacer.pack(expand=True, fill="both")

bottom_bar = tk.Frame(main, bg="#3b2414")
bottom_bar.pack(side="bottom", fill="x", pady=10)

def choose_file():
    global FILE_PATH
    filename = filedialog.askopenfilename(
        title="Select NowPlaying.txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if filename:
        FILE_PATH = Path(filename)
        path_label.config(text=str(FILE_PATH))
        save_config(FILE_PATH)

btn = tk.Button(
    bottom_bar,
    text="Select file",
    command=choose_file,
    font=("Arial", 11),
    bg="#4a2d1c",
    fg="#f2e8df",
    activebackground="#5a3621",
    activeforeground="#ffffff",
    relief="flat"
)
btn.pack()

path_label = tk.Label(
    bottom_bar,
    text=str(FILE_PATH) if FILE_PATH else "No file selected",
    font=("Arial", 10),
    fg="#bfaea1",
    bg="#3b2414",
    wraplength=1200,
    justify="center"
)
path_label.pack(pady=(4, 0))

def read_track():
    global last_current, last_previous
    try:
        if not FILE_PATH or not Path(FILE_PATH).exists():
            current_label.config(text="File not found")
            previous_label.config(text="")
            root.after(1000, read_track)
            return

        text = Path(FILE_PATH).read_text(encoding="utf-8", errors="replace")
        lines = [line.strip() for line in text.splitlines() if line.strip()]

        current = lines[0] if len(lines) >= 1 else None
        previous = lines[1] if len(lines) >= 2 else None

        if current != last_current:
            current_label.config(text=current if current else "Waiting for track...")
            last_current = current

        if previous != last_previous:
            previous_label.config(text=f"Previous: {previous}" if previous else "")
            last_previous = previous

    except Exception:
        pass

    root.after(1000, read_track)

read_track()
root.mainloop()