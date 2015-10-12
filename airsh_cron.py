#!/user/bin/env python 
import smbus
import time
import sys
import LCD2004 as LCD

#Parse XML data from US site
from xml.dom import minidom
import urllib
import os
import struct

url_str = 'http://www.stateair.net/web/rss/1/4.xml'
xml_str = urllib.urlopen(url_str).read()
xmldoc = minidom.parseString(xml_str)

obs_aqi = xmldoc.getElementsByTagName('AQI')
aqi = obs_aqi[0].firstChild.nodeValue

obs_pm25 = xmldoc.getElementsByTagName('Conc')
pm25 = obs_pm25[0].firstChild.nodeValue
 
obs_date = xmldoc.getElementsByTagName('description')
lasttime = obs_date[1].firstChild.nodeValue[0:16]

LCD.init_lcd()

if(aqi!=-99):
	LCD.print_lcd(0, 0, ' Shanghai USC')
	LCD.print_lcd(0, 1, '   AQI')
	LCD.print_lcd(12, 1, aqi)
	LCD.print_lcd(0, 2, '   PM2.5')
	LCD.print_lcd(12, 2, pm25)
	LCD.print_lcd(0, 3, ' * ' + lasttime)
else:
	LCD.print_lcd(0,0,'Data Not Ready')
