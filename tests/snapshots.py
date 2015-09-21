#! /usr/bin/python
"""example script for api usage """

from __future__ import print_function

import time
import qapy
from os import walk
from os.path import join

from qapy.disk import QUploadMode


if __name__ == "__main__":
    q = qapy.QApy('example/qarnot.conf')
    with q.create_task("example task", "python", 3) as task:
        task.resources.add_file("example/script_verbose.py",
                                mode=QUploadMode.background)
        task.constants['PYTHON_SCRIPT'] = "script_verbose.py"
        task.submit()
        task.snapshot(10)

        while not task.wait(10):
            out = task.download_results("output/")
            print(task.fresh_stdout(), end='')
            for dirname, dirs, files in walk(out):
                for filename in files:
                    with open(join(dirname,filename)) as f:
                        print(f.read())

        out = task.download_results("output/")
        print(task.fresh_stdout(), end='')
        for dirname, dirs, files in walk(out):
            for filename in files:
                with open(join(dirname,filename)) as f:
                    print(f.read())
