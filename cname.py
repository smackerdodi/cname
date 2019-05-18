import sys
import time
import queue
import threading

import dns.resolver
import win_unicode_console
from colorama import Fore, Style, init

#introduction
print(Fore.WHITE + '''/
                          _                _           _ _ 
 ___ _ __ ___   __ _  ___| | _____ _ __ __| | ___   __| (_)
/ __| '_ ` _ \ / _` |/ __| |/ / _ \ '__/ _` |/ _ \ / _` | |
\__ \ | | | | | (_| | (__|   <  __/ | | (_| | (_) | (_| | |
|___/_| |_| |_|\__,_|\___|_|\_\___|_|  \__,_|\___/ \__,_|_|
''')
print(Fore.GREEN + '''/              CODED BY : DAOUD YOUSSEF          
''')                                              
print (Fore.RED + 'PREPARING FOR BEGIN SCRIPT')
for i in range(5,0,-1):
    time.sleep(1)
print(str(i) + i * " . ")


#enable coloring on win
try:
	win_unicode_console.enable()
	init()
except:
	pass

#queue and lock var
domains = queue.Queue()
lock = threading.Lock()

# reading file
sublist = sys.argv[1]
subfile = open(sublist, 'r')

#setting dns resolver
my_resolver = dns.resolver.Resolver()
my_resolver.nameservers = ['8.8.8.8']

#populate queue with domains
for sub in subfile:
	domains.put(sub.strip())

subfile.close()

#checking cname
def Check(domain):
	try:
		answer=my_resolver.query(domain, 'CNAME')
		for data in answer:
			with lock:
				print(Fore.WHITE + (domain))
				print(Fore.GREEN +'C_NAME is :'+ Fore.YELLOW + str(data))
	except:
		with lock:
			print(Fore.WHITE + (domain) + Fore.RED + (' has no cname'))
	domains.task_done()

#starting threads
while not domains.empty():
	threading.Thread(target=Check,args=(domains.get(),)).start()

#wait until all threads done
domains.join()
