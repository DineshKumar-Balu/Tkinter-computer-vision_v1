import cx_Freeze
from cx_Freeze import setup, Executable
import os
import sys

# Define paths to include
ffmpeg_path = os.path.join("ffmpeg", "bin", "ffmpeg.exe")
tesseract_path = os.path.join("Tesseract-OCR", "tesseract.exe")
tessdata_path = os.path.join("Tesseract-OCR", "tessdata")
# config_toml_path = os.path.join(".streamlit", "config.toml")
# python_installer_path = "python-3.12.0-amd64.exe"  # Path to the Python installer

# Ensure paths exist
assert os.path.exists(ffmpeg_path), f"FFmpeg path does not exist: {ffmpeg_path}"
assert os.path.exists(tesseract_path), f"Tesseract path does not exist: {tesseract_path}"
assert os.path.exists(tessdata_path), f"Tessdata path does not exist: {tessdata_path}"
# assert os.path.exists(config_toml_path), f"config.toml path does not exist: {config_toml_path}"
# assert os.path.exists(python_installer_path), f"Python installer path does not exist: {python_installer_path}"

# Build options
build_exe_options = {
    "packages": ["tkinter", "pandas", "cv2", "pytesseract"],
    "excludes": [],
    "include_files": [
        (ffmpeg_path, os.path.join("ffmpeg", "bin", "ffmpeg.exe")),
        (tesseract_path, os.path.join("Tesseract-OCR", "tesseract.exe")),
        (tessdata_path, os.path.join("Tesseract-OCR", "tessdata")),
        # (config_toml_path, os.path.join(".streamlit", "config.toml")),
        # (python_installer_path, python_installer_path)  # Include the Python installer
    ],
}

base = None
if sys.platform == "win32":
     base="Win32GUI"
    # import ctypes
    # ctypes.windll.kernal32.SetConsoleTitle('')

# Define the executable
exe = [Executable("launcher.py",base ="Win32GUI")]

# Setup the build configuration
setup(
    name="TkinterApp",
    version="1.0",
    description="A simple tkinter app",
    options={"build_exe": build_exe_options}, # Add any required packages and files
    executables=exe
)