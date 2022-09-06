#!/usr/bin/env python3

import socket
import shutil

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ipadd = s.getsockname()[0]

db_inc_bk = open('db.inc.php','wt')

db_inc = open('/var/www/html/opensips-cp/config/db.inc.php').read()
for line in db_inc.split('\n'):
	if line==' $config->db_host = "localhost";':
		db_inc_bk.write(' $config->db_host = "%s";' % ipadd)
		db_inc_bk.write('\n')
	else:
		db_inc_bk.write(line)
		db_inc_bk.write('\n')

db_inc_bk.close()

boxes_bk = open('boxes.global.inc.php','wt')

boxes = open('/var/www/html/opensips-cp/config/boxes.global.inc.php').read()
for line in boxes.split('\n'):
	if line=='''$boxes[$box_id]['mi']['conn']="json:127.0.0.1:8989/mi";''':
		boxes_bk.write('''$boxes[$box_id]['mi']['conn']="json:%s:8989/mi";''' % ipadd)
		boxes_bk.write('\n')
	else:
		boxes_bk.write(line)
		boxes_bk.write('\n')

boxes_bk.close()

shutil.copyfile('db.inc.php', '/var/www/html/opensips-cp/config/db.inc.php')
shutil.copyfile('boxes.global.inc.php', '/var/www/html/opensips-cp/config/boxes.global.inc.php')