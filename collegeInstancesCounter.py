import urllib.request
import re
import json
from selenium import webdriver


file = open('data1.json', 'r', encoding="utf8")

Shenkar_counter = 0
bezalel_counter = 0	
Technion_counter = 0
		
for line in file:
	
	if re.search('ShenkarConfessions', line):
		Shenkar_counter += 1
	if re.search('bezalelconf', line):
		bezalel_counter +=1
	if re.search('TechnionConfessions', line):
		Technion_counter +=1
		
print("Shenkar:",Shenkar_counter)
print("Bezalel:" ,bezalel_counter)
print("Technion:" ,Technion_counter)
print("Sum:", Shenkar_counter+bezalel_counter+Technion_counter)



	
