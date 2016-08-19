import win32gui
import win32con
import ctypes
user32 = ctypes.windll.user32

# Functions Used By Classes; Might be Useful to Someone
def close_hwnd(hwnd):
    return win32gui.PostMessage(hwnd,win32con.WM_CLOSE,0,0)

def get_hwnd_title(hwnd):
    return win32gui.GetWindowText(hwnd)

def get_hwnd_rect(hwnd):
    return win32gui.GetWindowRect(hwnd)

def get_hwnd_visible(hwnd):
    return win32gui.IsWindowVisible(hwnd)

# Classes
class WindowRect:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    @property
    def rect(self):
        return self.__x1, self.__y1, self.__x2, self.__y2

    @property
    def width(self):
        return self.__x2 - self.__x1
    
    @property
    def height(self):
        return self.__y2 - self.__y1
    
    @property
    def x(self):
        return self.__x1
    
    @property
    def y(self):
        return self.__y1

    @property
    def coords(self):
        return self.x, self.y

class Window:
    def __init__(self, hwnd):
        self.hwnd = hwnd
    
    @property
    def title(self):
        return get_hwnd_title(self.hwnd)
    
    @property
    def visible(self):
        return get_hwnd_visible(self.hwnd)

    @property
    def rect(self):
        return get_hwnd_rect(self.hwnd)

    @property
    def WindowRect(self):
        return WindowRect(*self.rect)

    @property
    def x(self):
        return self.WindowRect.x
    
    @property
    def y(self):
        return self.WindowRect.y
    
    @property
    def width(self):
        return self.WindowRect.width
    
    @property
    def height(self):
        return self.WindowRect.height
    
    @property
    def coords(self):
        return self.WindowRect.coords
    
    def close(self):
        close_hwnd(self.hwnd)
    
    def move(self, newX, newY):
        return win32gui.MoveWindow(self.hwnd, newX, newY, self.width, self.height, True)
    
    def resize(self, newWidth, newHeight):
        return win32gui.MoveWindow(self.hwnd, self.x, self.y, newWidth, newHeight, True)

# Functions Used to Accumulate Window Information from OS
def get_hwnds(handles=[]):
    """Returns a list of current hwnds"""

    def window_enum_handler(hwnd, resultList=[]):
        """Helper Function for Window_Enum_Handler"""
        resultList.append(hwnd)
        return hwnd

    hwnds = []
    # calls window_enum_handler with handles when each window found
    win32gui.EnumWindows(window_enum_handler, hwnds)
    return hwnds

def get_windows(handles=[]):
    """Returns a list of current Windows"""
    hwnds = get_hwnds()
    windows = [Window(hwnd) for hwnd in hwnds]
    return windows

def get_screen_width():
    return user32.GetSystemMetrics(0)

def get_screen_height():
    return user32.GetSystemMetrics(1)