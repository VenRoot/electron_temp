# Watchdog imports
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Vanilla imports
from threading import Thread
from subprocess import run
from pathlib import Path
from os import system
import logging
import time

vividapath = Path().resolve()
vividaxcopy = str(vividapath).replace("/","\\")

def tscthread():
    print("Running the tsc watch")
    #print(path)
    system('tsc -w -p {} >nul'
    .format(vividapath))

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            xcopysource = str(event.src_path).replace("/","\\")
            system('xcopy {} {} /Y /E'.format(
                xcopysource,
                "{}\\out".format(vividaxcopy)
            ))
            print("Added File: - % s." % event.src_path)
        elif event.event_type == 'modified':
            xcopysource = str(event.src_path).replace("/","\\")
            system('xcopy {} {} /Y /E'.format(
                xcopysource,
                "{}\\out".format(vividaxcopy)
            ))
            print("Modified File: - % s." % event.src_path)
        elif event.event_type == 'deleted':
            xcopysource = str(event.src_path).replace("/","\\")
            system('DEL /F {}'.format(
                "{}\\out\\{}".format(
                    vividapath,
                    str(xcopysource).split("\\")[-1]
                )
            ))
            print("Deleted File: % s." % event.src_path)
              
def watchthread():
    print('Running Custom Watcher Thread')
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    event_handler = Handler()
    observer = Observer()
    observer.schedule(event_handler, "{}/src/".format(vividapath), recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

try:
    print("Copying...")
    system("xcopy {}\\src\\*.html {}\\out\\ /Y /E".format(
        vividaxcopy,vividaxcopy
    ))
    system("xcopy {}\\src\\css {}\\out\\css /Y /S".format(
        vividaxcopy,vividaxcopy
    ))

    tsc = Thread(target=tscthread)
    tsc.start()
    wat = Thread(target=watchthread)
    wat.start()
    print("Calling Node start")
    system("npm run start:pythonwindows")
except KeyboardInterrupt:
    exit()