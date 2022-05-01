import sys

from cx_Freeze import Executable, setup

try:
    from cx_Freeze.hooks import get_qt_plugins_paths
except ImportError:
    include_files = []
else:
    include_files = get_qt_plugins_paths("PyQt5", "platforms")

build_exe_options = {
    "excludes": ["tkinter"],
    "include_files": include_files,
}


executables = [Executable("main.py", base="Win32GUI", icon="ui/icon.ico", target_name="Telegram_chat_word_cloud_generator.exe", shortcutName="Telegram word cloud", shortcutDir="ProgramMenuFolder")]

setup(
    name="Telegram chat word cloud generator",
    version="0.0.1",
    description="Generate word clouds from the Telegram chat backups",
    summary_data={"author": "luke-gto @github"},
    options={},
    executables=executables,
)
