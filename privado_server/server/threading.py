import os
import logging
import subprocess

from concurrent.futures import ThreadPoolExecutor
from server.exception import PSException, SubprocessError, SubprocessUnzipError

class Thread_Pool:
    def __init__(self):
        self.executor = ThreadPoolExecutor(4)
        self.STORAGE = "/home/ubuntu/project/storage/"
        self.privado = "privado"
        self.unzip = "unzip"
        self._log = logging.getLogger("subprocess")

    def task(self, user, file):
        try:
            # handle uploaded file
            raw_file_path = self.STORAGE + str(file)
            user_folder = self.STORAGE + user

            with open(raw_file_path, "wb+") as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            
            self._log.info("Subprocess: saved zip file {}").format(raw_file_path)

            # unzip the file to user folder
            rc = subprocess.run([self.unzip, raw_file_path, "-d", user_folder])

            self._log.info("Subprocess: unzip file to {}").format(user_folder)

            if rc != 0:
                raise SubprocessUnzipError(e)

        except Exception as e:
            raise SubprocessError(e)


    def privado_scan(self, user, file):
        self.executor.submit(self.task, user, file)
        print("submit a subprocess")


        