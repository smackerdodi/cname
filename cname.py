import sys
import dns
import dns.resolver
import colorama
import time
from colorama import Fore, Style
from requests.exceptions import ConnectionError
print(Style.BRIGHT + Fore.WHITE + '''/

                          _                _           _ _ 
 ___ _ __ ___   __ _  ___| | _____ _ __ __| | ___   __| (_)
/ __| '_ ` _ \ / _` |/ __| |/ / _ \ '__/ _` |/ _ \ / _` | |
\__ \ | | | | | (_| | (__|   <  __/ | | (_| | (_) | (_| | |
|___/_| |_| |_|\__,_|\___|_|\_\___|_|  \__,_|\___/ \__,_|_|

''')
print(Fore.GREEN + '''/              CODED BY : DAOUD YOUSSEF          


''')                                              
print (Style.BRIGHT + Fore.RED + 'PREPARING FOR BEGIN SCRIPT')
for i in range(5,0,-1):
    time.sleep(1)
    print(str(i) + i * " . ")
sublist=sys.argv[1]
outlist=sys.argv[2]
my_resolver = dns.resolver.Resolver()
my_resolver.nameservers = ['8.8.8.8']
subfile=open(sublist, 'r')
outfile=open(outlist, 'a')
numberofsubd = sum(1 for line in open(sublist))
print(Style.BRIGHT + Fore.CYAN + "Number of Subdomains = " + str(numberofsubd))
line = 0
for sub in subfile:
	line+=1
	try:
		subd=sub.strip()
		answer=my_resolver.resolve(sub.strip(), 'CNAME')
		for data in answer:
			c=subd+ " : " + str(data)
			print(Style.BRIGHT + Fore.WHITE + (subd))
			print(Style.BRIGHT + Fore.GREEN +'C_NAME is :'+ Fore.YELLOW + str(data))
			outfile.write(c+"\n")
	except :    
   		print(Style.BRIGHT + Fore.RED + '\x1b[2K' + str(line) + "|" + str(numberofsubd) , end='\r')
subfile.close()


