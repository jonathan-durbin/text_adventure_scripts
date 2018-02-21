from cx_Freeze import setup, Executable

base = None
executables = [Executable("game.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "A_Journey",
    options = options,
    version = "1.0",
    description = 'A text-based adventure describing the journey of a concerned individual. He just wants to right some wrongs. Written by Jon Durbin.',
    executables = executables
)