# win_manage
Wrapper around win32gui, win32con for Window Management on Windows

## Why
win32gui and win32con have a really weird set of methods; I was looking for some convenience in a project of mine that was managing windows.

## Install
Haven't made this into a pip installable module yet (primarily because I have no idea how), so just drop win_manage.py into your project and make sure win32con+win32gui is installed.

## Usage (command-line demo)
```bash
> python
>>> from win_manage import get_windows
>>>
>>> # get all currently open windows
... get_windows()
[<win_manage.Window instance at 0x031A4E68>, <win_manage.Window instance at 0x031A44B8>,...]
>>>
>>> # get the window I'm writing this README with
... github_window = [x for x in get_windows() if x.title.startswith('Editing win_manage/READM')][0]
>>> github_window
<win_manage.Window instance at 0x032625A8>
>>>
>>> # get window coordinates, then move to top-left corner
... github_window.coords
(2552, -8)
>>> github_window.move(0,0)
>>>
>>> # get window size, then adjust height and width
... (github_window.width, github_window.height)
(1280, 1040)
>>> github_window.resize(400,400)
>>>
>>> # check if window is visible (not hidden), and then close
... github_window.visible
1
>>> github_window.close()
```
