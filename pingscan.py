import os
import ipaddress
import subprocess

user_input = raw_input("Please enter network address:\n")
network = ipaddress.ip_network(unicode(user_input))

print network.num_addresses

with open(os.devnull, 'w') as DEVNULL:
	for ip in network.hosts():
		try:
			subprocess.check_call(
				['ping', '-c', '3', str(ip)],
				stdout=DEVNULL,
				stderr=DEVNULL
			)

			print ip, "is responding"
		except subprocess.CalledProcessError:
			#print ip, "is NOT responding"
			continue











		# if not os.system("ping -c 1" + str(ip)):
		# 	print ip, " is active.\n"
		# else:
		# 	#print ip, " is down.\n"
		# 	continue