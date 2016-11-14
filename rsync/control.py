
#!/usr/bin/env python
# -*- coding: utf_8 -*-v
import subprocess

cmd = "rsync -avrz noop.php root@192.168.49.143:/opt/data/file"
subprocess.call(cmd, shell=True)