import time
import datetime
import os

def deleteOldFiles(folder, time_in_seconds):
    current_time = time.mktime(datetime.datetime.now().timetuple())
    print("Current time:", current_time)
    directory = folder
    print("\n----Loop----\n")
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            try:
                fileWithPath = os.path.abspath(os.path.join(dirpath, f))
                creation_time = os.path.getctime(fileWithPath)
                print("file available:",fileWithPath)
                print("Difference: {}  > time_in_seconds: {}".format(current_time-creation_time, time_in_seconds))
                if (current_time - creation_time) > time_in_seconds:
                    print("Time difference:",current_time - creation_time)
                    os.unlink(fileWithPath)
                    print('{} removed'.format(fileWithPath))
                    print("\n")
                else:
                    print('{} not removed'.format(fileWithPath))
            except Exception as e:
                print("Error removing file")
                print(e)
                print("\n")

if __name__ == '__main__':
    while(True):
        deleteOldFiles("audio", 20.0)
        time.sleep(1.0)