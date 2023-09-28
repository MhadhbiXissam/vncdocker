
try : from ewmh import EWMH
except exception as e  : import os ; os.system('pip install ewmh')


from ewmh import EWMH

def print_window_info(window):
    window_attributes = window.get_attributes()
    print("\t* Window ID:", window.id)
    print("\t\t- Window Title:", window.get_wm_name())
    print("\t\t- Window Class:", window.get_wm_class())
    #print("Window Attributes:", window_attributes)

def print_windows(root, ewmh):
    window_ids = root.getClientList()
    for window_id in window_ids:
        print_window_info(window_id)


if __name__ == "__main__":
    ewmh = EWMH()
    root = ewmh
    print("Windows_Information:")
    print_windows(root, ewmh)
