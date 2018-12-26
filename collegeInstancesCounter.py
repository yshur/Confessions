import urllib.request
import re
import json
from selenium import webdriver

file = open('data100.json', 'r', encoding="utf8")

Shenkar_counter = 0
bezalel_counter = 0
sapir_counter = 0	
idc_counter = 0	
telhai_counter = 0
hit_counter = 0 
rupin_counter = 0 	
technion_counter = 0	
hui_counter = 0	
ariel_counter = 0
bgu_counter = 0
tlv_counter = 0
biuconfessions2018_counter = 0 
huji_counter = 0

		
for line in file:
	
	if re.search('ShenkarConfessions', line):
		Shenkar_counter += 1
	if re.search('bezalelconf', line):
		bezalel_counter +=1
	if re.search('IDCHerzliyaConfessions', line):
		idc_counter +=1
	if re.search('sapirconfession', line):
		sapir_counter +=1
	if re.search('telhaiconfessions', line):
		telhai_counter +=1
	if re.search('hitconfessionsisrael', line):
		hit_counter +=1
	if re.search('RuppinConfession', line):
		rupin_counter +=1		
	if re.search('TechnionConfessions', line):
		technion_counter +=1
	if re.search('HUIConfessions', line):
		hui_counter +=1	
	if re.search('ArielUConfessions', line):
		ariel_counter +=1	
	if re.search('BGUConfession', line):
		bgu_counter +=1	
	if re.search('tel.aviv.university.confessions', line):
		tlv_counter +=1
	if re.search('biuconfessions2018', line):
		biuconfessions2018_counter +=1
	if re.search('HUJI.Confessions', line):
		huji_counter +=1		
	
print("Shenkar:",Shenkar_counter)
print("Bezalel:" ,bezalel_counter)
print("Idc:" ,idc_counter)
print("Sapir:" ,sapir_counter)
print("TelHai:" ,telhai_counter)
print("Hit:" ,hit_counter)
print("Rupin:" ,rupin_counter)
print("Technion:" ,technion_counter)
print("Hui:" ,hui_counter)
print("Ariel:" ,ariel_counter)
print("Bgu:" ,bgu_counter)
print("Tlv:" ,tlv_counter)
print("Bar-Ilan:" ,biuconfessions2018_counter)
print("Huji:" ,huji_counter)

print("Sum College:", Shenkar_counter+bezalel_counter+idc_counter+sapir_counter+hit_counter+telhai_counter+rupin_counter)
print("Sum University:",technion_counter+hui_counter+ariel_counter+bgu_counter+tlv_counter+biuconfessions2018_counter+huji_counter)
print("Sum Total:", Shenkar_counter+bezalel_counter+idc_counter+sapir_counter+hit_counter+telhai_counter+rupin_counter+technion_counter+hui_counter+ariel_counter+bgu_counter+tlv_counter+biuconfessions2018_counter+huji_counter)




	
