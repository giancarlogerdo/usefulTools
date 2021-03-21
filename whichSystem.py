#!/usr/bin/python3

#Author @s4vitar (Marcelo Vázquez)
#Edited by: @sikumy

import re, sys, subprocess


def helpPanel():

	print("\n[!] Usage: python3 " + sys.argv[0] + " <ip-address>")
	sys.exit(1)

if len(sys.argv) != 2:
	helpPanel()

def get_ttl(ip_address):

	proc = subprocess.Popen(["/usr/bin/ping -c 1 %s " % ip_address, ""], stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)

	(out,err) = proc.communicate()

	out = out.split()
	out = out[12].decode('utf-8')

	ttl_value = re.findall(r"\d{1,3}", out)[0]

	return ttl_value


def get_os(ttl):

	ttl = int(ttl)

	if ttl >= 0 and ttl <= 64:
		return "Linux"
	elif ttl >= 65 and ttl <= 128:
		return "Windows"
	else:
		return "Not found"


if __name__ == '__main__':

	try:

		ip_address = sys.argv[1]

		ttl = get_ttl(ip_address)

		os_name = get_os(ttl)

		print("\n\t--> %s (ttl -> %s): %s" % (ip_address, ttl, os_name))

	except:
		helpPanel()

