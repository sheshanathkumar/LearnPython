from plyer import notification
import os
import psutil

def cpuNotify (title, message):
    notification.notify (
        title = title,
        message = message,
        app_icon = None,
        timeout = 5
    )


if __name__ == '__main__':

    stats = f" \nAvailable Memory: {psutil.virtual_memory()[0]//(1024*1024*1000)}GB" \
            f"\nUsed Memory: {psutil.virtual_memory()[3]//(1024*1024*1000)}GB" \
            f"\nTotal Memory: {psutil.virtual_memory()[0]//(1024*1024*1000)}GB " \
            f"\nFree Memory: {psutil.virtual_memory()[4]//(1024*1024*1000)}GB"

    cpuNotify("Stats", stats)



    # print('total cpu:', os.cpu_count())
    #
    # print('Total Memory', psutil.virtual_memory()[0]//(1024*1024*1000) , ' GB')
    # print('Available Memory', psutil.virtual_memory()[1]//(1024*1024*1000), ' GB')
    # print('Used Memory', psutil.virtual_memory()[3]//(1024*1024*1000), ' GB', psutil.virtual_memory()[2], '%')
    # print('Free Memory', psutil.virtual_memory()[4]//(1024*1024*1000), ' GB')