__author__ = 'm.gh@linuxmail.org'

import os
from distutils.core import setup

def read(file_name):
	return open(os.path.join(os.path.dirname(__file__) , file_name)).read()

setup(
	name = "detect_linux_distro",
	version = "0.5",
	author_email = "m.gh@linuxmail.org",
	description = "Detect linux distribution",
	long_description = read("readme"),
	license = read("license"),
	keywords = "detect os linux distribution release",
	url = "https://github.com/m-gh/detect_linux_distro",
	packages = ["detect_linux_distro"],
)
