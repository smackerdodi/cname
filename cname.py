import sys
import time
import queue
import threading

import dns.resolver
from colorama import Fore, Style, init


#enable coloring on win
try:
	import win_unicode_console
	win_unicode_console.enable()
	init()
except:
	pass

#queue and lock var
domains = queue.Queue()
lock = threading.Lock()

# reading file
sublist = sys.argv[1]
try:
	subfile = open(sublist, 'r')
except:
	subfile = sublist.split(",")

#setting dns resolver
my_resolver = dns.resolver.Resolver()
my_resolver.nameservers = ['8.8.8.8']

#populate queue with domains
for sub in subfile:
	domains.put(sub.strip())

try:
	subfile.close()
except:
	pass

#checking cname
def Check(domain):
	try:
		answer=my_resolver.query(domain, 'CNAME')
		for data in answer:
			with lock:
				print(Fore.WHITE + domain + Fore.GREEN +' --> '+ Fore.YELLOW + str(data))
	except:
		pass
	domains.task_done()

#starting threads
while not domains.empty():
	domain = domains.get()
	try:
		threading.Thread(target=Check,args=(domain,)).start()
	#avoid thread start error
	except RuntimeError:
		domains.task_done()
		domains.put(domain)

#wait until all threads done
domains.join()
