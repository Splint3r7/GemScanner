#!/usr/bin/env python
#GemScanner

import requests
from bs4 import BeautifulSoup
from colorama import init , Style, Back,Fore
import argparse
import sys,os

if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')

def logo():
	print("""
 	 ____                ____
 	/ ___| ___ _ __ ___ / ___|  ___ __ _ _ __  _ __   ___ _ __
	| |  _ / _ | '_ ` _ \\___ \ / __/ _` | '_ \| '_ \ / _ | '__|
	| |_| |  __| | | | | |___) | (_| (_| | | | | | | |  __| |
 	\____|\___|_| |_| |_|____/ \___\__,_|_| |_|_| |_|\___|_|

 	GemScanner - Finds depreciated versions of your gems.
 	Author: Splint3r7 - ( https://github.com/Splint3r7 )

		""")

parser = argparse.ArgumentParser(description="Script to find depreciated versions in Gemfile.lock")

parser.add_argument('-f','--file',
                            help = "Path to Gemfile.lock",
                            type = str,
                            required = True)

parser.add_argument('-o','--output',
                            help = "Output file",
                            type = str,
                            required = True)

args = parser.parse_args()

file_path = args.file
out_file = args.output


def versions_f(_gemname_, _fullname_, _gemversion_):


	print ("[+] {}".format(_fullname_))
	try:
		
		req = requests.get("https://rubygems.org/gems/"+_gemname_)
		soup = BeautifulSoup(req.content, 'html.parser')
		versions = soup.find_all("a", class_="t-list__item")
		results = []
		for version in versions:
			version = version.get_text()
			results.append(version)
		
		res = results[:1]
		for c_version in res:
			if c_version in _gemversion_:
				print(Style.DIM+Fore.GREEN+"[!] Already on latest version: "+Style.RESET_ALL+"| {}".format(c_version)+"\n")
				pass
			else:
				print(Style.BRIGHT+Fore.RED+"[!] Current Version: "+Style.RESET_ALL+"| {}".format(c_version)+"\n")
				pass

		filew.write(_gemname_+"\n"+_fullname_+"\n"+c_version+"\n"+"\n")
	
	except Exception as e:
		pass
	
if __name__ == "__main__":

	logo()
	filew = open(out_file, "a+")
	with open(file_path, "r") as f:
		lines = f.readlines()
	
		for line in lines:
			line = line.strip()
			if "(" in line:
				fullname = line
				line_arr = line.split(" ", 1)
				gem_name = line_arr[0]
				gem_version = line_arr[1]
				versions_f(gem_name, fullname, gem_version)

	filew.close()