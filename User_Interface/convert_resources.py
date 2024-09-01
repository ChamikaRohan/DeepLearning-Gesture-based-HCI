import subprocess
import sys

qrc_file = 'C:/Academic/FYP/image-processing-real-time/UI_Design/Resources.qrc'
output_file = 'C:/Academic/FYP/image-processing-real-time/UI_Design/resources_rc.py'

# Use the pyrcc tool
subprocess.run([sys.executable, '-m', 'PyQt5.pyrcc_main', qrc_file, '-o', output_file])