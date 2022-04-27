import sys

from cx_Freeze import Executable, setup

executables = [Executable("main.py", base="Console", target_name="Telegram_chat_word_cloud_generator.exe", shortcutName="Telegram word cloud", shortcutDir="ProgramMenuFolder")]

setup(
    name="Telegram chat word cloud generator",
    version="0.0.1",
    description="Generate word clouds from the Telegram chat backups",
    summary_data={"author": "luke-gto @github"},
    options={},
    executables=executables,
)
