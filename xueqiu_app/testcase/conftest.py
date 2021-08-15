import os
import signal
import subprocess
import pytest


@pytest.fixture(scope='class', autouse=True)
def record():
    """
    在函数调用前开始录制，调用结束后，停止录制
    """
    # 录制命令，需要先本地安装scrcpy
    cmd = 'scrcpy --record ../result/tmp.mp4'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    yield
    # 通过pid杀掉进程，然后Kill signal.
    os.kill(p.pid, signal.SIGINT)
