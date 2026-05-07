import winreg
import atexit

PROXY_ADDRESS = "127.0.0.1:8085"
REG_PATH = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"

def enable_proxy():
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        REG_PATH,
        0,
        winreg.KEY_SET_VALUE
    )
    try:
        winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(key, "ProxyServer", 0, winreg.REG_SZ, PROXY_ADDRESS)
    finally:
        winreg.CloseKey(key)

def disable_proxy():
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        REG_PATH,
        0,
        winreg.KEY_SET_VALUE
    )
    try:
        winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(key, "ProxyServer", 0, winreg.REG_SZ, "")
    finally:
        winreg.CloseKey(key)

def setup_proxy():
    enable_proxy()
    atexit.register(disable_proxy)
