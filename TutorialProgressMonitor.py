import watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Tm(FileSystemEventHandler):
    def __init__(self, bt, filename) -> None:
        """
        :param bt: blender tutorial
        :type bt: BlenderTutorial
        """
        super().__init__()
        self.bt = bt
        
        last_index = filename.rindex('/')
        self.folder = "."
        self.filename = filename
        if (last_index != -1):
            self.filename = filename[last_index+1:]
            foldername = filename[0:last_index]
            self.folder = foldername
            last_index = foldername.rindex('/')
            if (last_index != -1):
                self.folder = foldername[0:last_index]

        self.file_observer = Observer()
        self.file_observer.schedule(self, path=self.folder, recursive=True)

    def startObserving(self):
        self.file_observer.start()
    
    def stopObserving(self):
        self.file_observer.stop()

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(self.filename):
            print("Progress file modified")
            self.bt.onProgressChange()