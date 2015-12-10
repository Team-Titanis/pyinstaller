hiddenimports = ['PySide.QtGui']

from PyInstaller.hooks.hookutils import pyside_plugins_binaries

def hook(mod):
    mod.binaries.extend(pyside_plugins_binaries('phonon_backend'))
    return mod
