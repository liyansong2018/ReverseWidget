import os
import sys
from util.log import *
parent_path = os.path.dirname(sys.path[0])
new_path = parent_path + '/opensource/python_dll_injector'
new_path2 = parent_path + '/ReverseWidget/opensource/python_dll_injector'
# Run this module directly
if new_path not in sys.path:
    sys.path.append(new_path)
# Used by other module
if new_path2 not in sys.path:
    sys.path.append(new_path2)

from opensource.python_dll_injector.main import *

def start_dll_window():
    processes, icons, paths = GetProcessEntries()
    print("Processes found:", len(processes))

    hinstance = GetModuleHandleA(None)

    try:
        icon = LoadImageA(hinstance, b"ui/resources/pictures/syringe.ico", 1,
                          32, 32, 0x00000010 | 0x00000080)
    except:
        icon = LoadIconA(None, LPSTR(32512))

    class_name = b"Hello world!"

    window_class = WNDCLASSA()
    window_class.style = ClassStyle.VREDRAW | ClassStyle.HREDRAW
    window_class.lpfnWndProc = WNDPROC(WindowProc)
    window_class.hInstance = hinstance
    window_class.lpszClassName = class_name
    window_class.hbrBackground = HBRUSH(5)
    window_class.hIcon = icon
    try:
        RegisterClassA(ctypes.byref(window_class))
    except Exception as e:
        Log.error(str(e))

    hwnd_main = CreateWindowExA(
        0,
        class_name,
        b"DLL Injector",
        WindowStyle.OVERLAPPED | WindowStyle.CAPTION
        | WindowStyle.SYSMENU | WindowStyle.MINIMIZEBOX,
        CW_USEDEFAULT, CW_USEDEFAULT, 600, 480,
        None,
        None,
        hinstance,
        None
    )

    client_rect = RECT()
    GetClientRect(hwnd_main, ctypes.byref(client_rect))

    inject_button_width = 100
    inject_button_height = 25
    hwnd_inject_button = CreateButton(hwnd_main, INJECT_BUTTON,
                                      client_rect.right - 10 - inject_button_width,
                                      client_rect.bottom - 10 - inject_button_height,
                                      inject_button_width, b"Inject", height=inject_button_height)

    search_button_width = 100
    search_button_height = 25
    hwnd_search_button = CreateButton(hwnd_main, SEARCH_BUTTON,
                                      client_rect.right - 10 - search_button_width,
                                      client_rect.top + 10,
                                      search_button_width, b'Browse DLL...', height=search_button_height)

    CreateEdit(hwnd_main, FILEPATH_EDIT,
               client_rect.left + 10,
               client_rect.top + 10,
               client_rect.right - 10 - search_button_width - 20,
               25
               )

    hwnd_listview, processes = CreateListView(hwnd_main, PROCESS_LISTVIEW,
                                              client_rect.left + 10,
                                              client_rect.top + 10 + 32,
                                              client_rect.right - client_rect.left - 20,
                                              client_rect.bottom - client_rect.top - 20 - 23 - 10 - 32,
                                              processes, icons, paths
                                              )

    ShowWindow(hwnd_main, 5)

    metrics = NONCLIENTMETRICSA()
    metrics.cbSize = ctypes.sizeof(NONCLIENTMETRICSA)
    # SPI_GETNONCLIENTMETRICS = 0x0029
    SystemParametersInfoA(0x0029, metrics.cbSize, ctypes.byref(metrics), 0)
    font = CreateFontIndirectA(ctypes.byref(metrics.lfMenuFont))

    EnumChildWindows(hwnd_main, WNDENUMPROC(EnumChildProc),
                     LPARAM(ctypes.cast(font, ctypes.c_void_p).value))

    # DeleteObject(font)

    msg = MSG()
    while (bRet := GetMessageA(ctypes.byref(msg), None, 0, 0)) != 0:
        if bRet == -1:
            break
        TranslateMessage(ctypes.byref(msg))
        DispatchMessageA(ctypes.byref(msg))