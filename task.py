from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import shutil
import time

class MyFileHandler(FileSystemEventHandler):
    i = 1

    def on_any_event(self, event):
        # new code start
        wait = True
        while(wait == True):
            time.sleep(1)
            newFileDownload = self.checkFileDownloaded()
            if ('Unconfirmed') in newFileDownload or ('.tmp') in newFileDownload or ('crdownload') in newFileDownload:
                print("{} is downloading ".format(newFileDownload))
            else:
                wait = False

        src = fileFolder + '//' + newFileDownload
        fileExt = os.path.splitext(src)[1][1:]
        self.copyFiles(src, newFileDownload, label=fileExt)
        # new code end

        # 2nd code start
        # wait = True
        # while(wait == True):
        #     for fileName in os.listdir(fileFolder):
        #         if ('Unconfirmed') in fileName or ('.tmp') in fileName or ('crdownload') in fileName:
        #             print("{} is downloading ".format(fileName))
        #             time.sleep(3)
        #         else:
        #             wait = False
        # print("{} File downloaded".format(fileName))
        # src = fileFolder + '//' + fileName
        # fileExt = os.path.splitext(src)[1][1:]
        # self.copyFiles(src,fileName,label=fileExt)

        # 2nd code end

    def checkFileDownloaded(self):
        os.chdir(fileFolder)
        files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
        newestFile = files[-1]
        return newestFile

    def copyFiles(self, src, fileName, label):
        dstNewFolder = fileFolder + '//' + label
        if not os.path.exists(dstNewFolder):
            os.makedirs(dstNewFolder)
        newFolderNameFile = dstNewFolder + '//' + fileName
        shutil.move(src, newFolderNameFile)
        print(newFolderNameFile)
        observer.stop()

fileFolder = "F://Downloads2"

eventHandler = MyFileHandler()
observer = Observer()
observer.schedule(eventHandler, fileFolder, recursive=True)
observer.start()

try:
    time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
print("here")
