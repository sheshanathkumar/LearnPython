import win10toast
import os
import psutil

toast = win10toast.ToastNotifier()
stats = f" \nAvailable Memory: {psutil.virtual_memory()[0]//(1024*1024*1000)}GB" \
        f"\nUsed Memory: {psutil.virtual_memory()[3]//(1024*1024*1000)}GB" \
        f"\nTotal Memory: {psutil.virtual_memory()[0]//(1024*1024*1000)}GB " \
        f"\nFree Memory: {psutil.virtual_memory()[4]//(1024*1024*1000)}GB"
toast.show_toast("Notification", stats, None, 4)