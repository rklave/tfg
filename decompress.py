from compress import op
from compress import opc1
import subprocess



subprocess.check_output("ffmpeg -y -i " + op + " rawvideo -s 1920x1080 " + opc1)