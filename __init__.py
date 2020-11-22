from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys
from time import gmtime, strftime
from os.path import expanduser
home = expanduser("~")
import json

with open(os.path.join(home, "./config.json"), "r") as write_file:
    config = json.load(write_file)

if config['DBS_ANTS']:
	ants_path = os.path.join('/opt/ANTs/bin/')
else:
	ants_path = None
