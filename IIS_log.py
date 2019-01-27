import fileinput, sys
from pprint import pprint

header = ['date', 'time', 's-sitename','s-computername', 's-ip', 'cs-method', 'cs-uri-stem', 'cs-uri-query', 's-port', 'cs-username', 'c-ip','cs-version' ,'cs(User-Agent)', 'cs(Referer)', 'cs-host', 'sc-status', 'sc-substatus', 'sc-win32-status','time-taken', 'OriginalIP']

l = [] # a list to hold a <dict> for each line in the IIS log file

for line in fileinput.input(sys.argv[1]):
 if not line.startswith('#'):
  fields = line.split()
  #pprint (fields) # debug
  d = dict(zip(header, fields)) # create a <dict> based on <headers> & <split> log lines
  l.append(d)
  
pprint(len(l)) # size of <list> => number of entries in IIS log file

# simple filter - it would be nice if I could filter on MULTIPLE KEYS & MUTLIPLE VALUES...
# i.e. return a list with "s-port=443" and "date=2016-03-01" and "cs-username=moo.com" and "sc-status!=200"
# but I aint got the tekkers!
def moo(key, key_values, list_of_dicts):
 return list(filter(lambda d: d[key] not in key_values, list_of_dicts))

filter_key = 'c-ip'

exclude_list = ['1.2.3.4', '5.6.7.8', '9.10.11.12']

ex1 = moo(filter_key, exclude_list, l)

for v in ex1:
 pprint (v)
 
pprint(len(ex1))