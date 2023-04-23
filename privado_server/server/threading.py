import os
import subprocess

from concurrent.futures import ThreadPoolExecutor
from server.exception import PSException, SubprocessError, SubprocessUnzipError

class Thread_Pool:
    def __init__(self):
        self.executor = ThreadPoolExecutor(4)
        self.STORAGE = "/home/ubuntu/project/storage/"
        self.privado = "privado"
        self.unzip = "unzip"

    def task(self, user, file):
        try:
            # handle uploaded file
            raw_file_path = self.STORAGE + str(file)
            user_folder = self.STORAGE + user

            # with open(raw_file_path, "wb+") as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            
            # unzip the file to user folder
            rc = subprocess.run([self.unzip, raw_file_path, "-d", user_folder]).returncode

            if rc != 0:
                raise SubprocessUnzipError("unzip error")
            
            # privado scan the file
            rc = subprocess.run([self.privado, "scan", user_folder + "/" + str(file)[:-4] + "/"]).returncode

            if rc != 0:
                raise SubprocessUnzipError("privado scan error")

        except Exception as e:
            raise SubprocessError(e)


    def privado_scan(self, user, file):
        self.executor.submit(self.task, user, file)


        