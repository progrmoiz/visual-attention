import datetime
import os
from subprocess import call

start_time = datetime.datetime(2018, 9, 1, 9, 40, 0)
start_sec1 = datetime.datetime(2018, 9, 1, 9, 51, 50)
start_sec2 = datetime.datetime(2018, 9, 1, 9, 58, 20)
start_sec3 = datetime.datetime(2018, 9, 1, 10, 11, 43)
finish_time = datetime.datetime(2018, 9, 1, 10, 27, 57)
foldername = 'talha_bhutto'

SECTION_A = 'section_1'
SECTION_B = 'section_2'
SECTION_C = 'section_3'

n_array = []
os.chdir('/home/kite/Videos/Test_VIDEOS/%s' % foldername)
call(['mkdir', '-p', SECTION_A, SECTION_B, SECTION_C])

print('renaming files...')
for filename in os.listdir('.'):
    if filename.startswith("image_"):
        s = int(filename[6:-4])
        n = start_time + datetime.timedelta(0, s)
        n_array.append(n)
        print(n.time())
        os.rename(filename, 'image_%s.jpg' % n.time())

n_array.sort()

print('moving files...')
for n in n_array:
    filename = 'image_%s.jpg' % n.time()
    if n > start_sec1 and n <= start_sec2:
        call(['mv', filename, "%s/%s" % (SECTION_A, filename)])
    elif n > start_sec2 and n <= start_sec3:
        call(['mv', filename, "%s/%s" % (SECTION_B, filename)])
    elif n > start_sec3 and n <= finish_time:
        call(['mv', filename, "%s/%s" % (SECTION_C, filename)])
