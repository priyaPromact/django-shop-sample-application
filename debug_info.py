import sys
sys.path.append('/home/vagrant/deliveristaenv/local/bin/api-dependencies/pycharm-debug.egg')

import pydevd
pydevd.settrace('10.1.81.33', port=21000, stdoutToServer=True, stderrToServer=True)