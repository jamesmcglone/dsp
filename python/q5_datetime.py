from datetime import datetime

def time_difference1(a, b):
	
	start = datetime.strptime(a, '%m-%d-%Y')
	stop = datetime.strptime(b, '%m-%d-%Y')
	print abs((stop-start).days)

def time_difference2(a, b):
	
	start = datetime.strptime(a, '%m%d%Y')
	stop = datetime.strptime(b, '%m%d%Y')
	print abs((stop-start).days)

def time_difference3(a, b):
	pass
	start = datetime.strptime(a, '%d-%b-%Y')
	stop = datetime.strptime(b, '%d-%b-%Y')
	print abs((stop-start).days)


####a) 
date_start1 = '01-02-2013'  
date_stop1 = '07-28-2015'   

####b)  
date_start2 = '12312013'  
date_stop2 = '05282015'  

####c)  
date_start3 = '15-Jan-1994'  
date_stop3 = '14-Jul-2015'  


time_difference1(date_start1, date_stop1)
time_difference2(date_start2, date_stop2)
time_difference3(date_start3, date_stop3)
