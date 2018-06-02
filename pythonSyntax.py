# Imports the Google Cloud client library



from google.cloud import bigquery

# Instantiates a client
client = bigquery.Client(project='localcover-55')
DATASET_ID = 'yixin'
dataset_ref = client.dataset(DATASET_ID)
dataset = bigquery.Dataset(dataset_ref)

###############file dependency #############
# to import MyClass from MyFolder.py
from MyFolder import MyClass

# constructor
def __init__(self, attr1, attr2, attrDefalt = ''):
        self.m_attr1 = attr1
        self.m_attr2 = attr2

# memberFunction
def memberFunction(self, param1):
    # function body
    return

# create obj and call memberFunction
myObj = MyClass(arg1,arg2...)
myObj.memberFunction(arg)

############### loop conditions ###################

while condition1 or condition2:

if condition1 and condition2：
elif condition3:
else:

if not var:
	return not var
	
if not var:
    return None

############### string operations ###################

# if a str is null
if not str:

# return true if str is null
return not text        

#get length of str
len(str)

pattern ="zhangyixinc"
print(pattern[3:])#ngyixin
print(pattern[3])#n
print(pattern[-1])#c ,-1 means the last one, this can also be used in list,
#use list[-1] to get the last item in the list


############functions#############

func=lambda x:x+1
print(func(1))
#2
print(func(2))
#3
 
#以上lambda等同于以下函数
def func(x):
   return(x+1)
   
#sort:
intervals.sort(key=lambda x: x.start)

#min:
nameList = ["zyx","nc"]
print(min(nameList))   #output the minmum of the list: nc

################ container #######################




A = ["a", "b", "c", "d"]
B = [1, 2, 3, 4]
#zip(A,B) = ("a",1),("b",2),("c",3),("d",4)

C = set(zip(A, B)) #convert zip to set
print(C)

#output
# {('c', 3), ('a', 1), ('d', 4), ('b', 2)}

lenth = len(A)
print("length = ", lenth)
length =  4

E = range(0, len(A))
print("range = ",E)
# range =  range(0, 4)

F = dict(zip(A, E)) #convert zip to dict
print("dict zip = ",F)
# dict zip =  {'a': 0, 'b': 1, 'c': 2, 'd': 3}


a=[1,2,3]
b=[4,5,6,7]
c=[8,9,10,11,12]
zz=zip(a,b,c)
ss = set(zip(a,b,c))
print(set(ss))

#output
# {(1, 4, 8), (3, 6, 10), (2, 5, 9)}

x,y,z=zip(*zz)#inverse zip operation
print(x)
print(y)
print(z)

#output
# (1, 2, 3)
# (4, 5, 6)
# (8, 9, 10)

strName = []
strName.append("nancy")
strName.append("linda")
enumVar =enumerate(zip(*strName)) 
setVar = set(zip(*strName))
print(set(enumVar))
# {(2, ('n', 'n')), (4, ('y', 'a')), (0, ('n', 'l')), (1, ('a', 'i')), (3, ('c', 'd'))}

print(setVar)
# {('y', 'a'), ('n', 'l'), ('a', 'i'), ('n', 'n'), ('c', 'd')}

for i,letter_group in enumVar:
    print(letter_group)
    print(set(letter_group))
    print("len = ",len(letter_group))
    print("set len = ",len(set(letter_group)))

#a is one of the elements in the set {}
a in {'*', '.'}

# ('n', 'l')
# {'l', 'n'}
# len =  2
# set len =  2
# ('a', 'i')
# {'i', 'a'}
# len =  2
# set len =  2
# ('n', 'n')
# {'n'}
# len =  2
# set len =  1
# ('c', 'd')
# {'d', 'c'}
# len =  2
# set len =  2
# ('y', 'a')
# {'a', 'y'}
# len =  2
# set len =  2
######################### append, pop, join ##########

A = ['*']
A.append('(')   # A = ['*','(']   
createOneSolution(A)
A.pop()    # A = ['*']

#join is to conbine several elements to one string
seq1 = ['hello','good','boy','doiido']
str_output1 = ' '.join(seq1)    #hello good boy doiido
str_output2 = ':'.join(seq1)    #hello:good:boy:doiido

############### embeded func defination ####################
def generateParenthesis(self, n):
    def createOneSolution(A = []):  #embeded function, no need to write "self"
        if len(A) == 2*n:
            if isValid(A):
            # add A to solution set
            ans.append("".join(A))
        else:
            ...
    
    def isValid(S):
        ...
        return True

    ans = []
    createOneSolution()

    return ans

######################### loop ######################


list1 = ["This", "is", "a", "test"]
for i in range (len(list1)):
    print(i ,list1[i]) 
# 0 This
# 1 is
# 2 a
# 3 test

	
print("\n")
for index, item in enumerate(list1):
    print(index, item) 
	

# 0 This
# 1 is
# 2 a
# 3 test
# 5


############## log in datastore  #######################
"""
import datetime
import logging
import uuid

from google.cloud import datastore

logging.basicConfig()
LOG = logging.getLogger()
LOG.setLevel(logging.DEBUG)
logging.basicConfig()

CLIENT = datastore.Client()
"""
##########################################


####################### create a new dataset #################
"""
# The name for the new dataset
dataset_id = 'lc_api_12101153'

# Prepares a reference to the new dataset
dataset_ref = bigquery_client.dataset(dataset_id)
dataset = bigquery.Dataset(dataset_ref)

# Creates the new dataset
dataset = bigquery_client.create_dataset(dataset)

print('Dataset {} created.'.format(dataset.dataset_id))
"""
###################################################

"""
for dataset in bigquery_client.list_datasets():  # API request(s)
    do_something_with(dataset)
"""

############## make a query, it has an error "not iterable" #########################

"""
QUERY = (
        'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
        'WHERE state = "TX" '
        'LIMIT 100')
"""  

""" 
QUERY = (
        'SELECT salesWeek FROM `localcover-55.yixin.x008_LRDiv1` '
        'LIMIT 100')

query_job = bigquery_client.query(QUERY)
for row in query_job:  # API request
    # Row values can be accessed by field name or index
    assert row[0] == row.salesWeek == row['salesWeek']

"""

##################################################

"""
QUERY = (
        'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
        'WHERE state = "TX" '
        'LIMIT 100')
"""
"""
QUERY = (
        'SELECT salesWeek FROM `localcover-55.yixin.x008_LRDiv1` '
        'LIMIT 100')
"""   
QUERY = (
        '''SELECT salesWeek FROM `localcover-55.yixin.x008_LRDiv1`
        LIMIT 100''')

TIMEOUT = 30  # in seconds
query_job = client.query(QUERY)  # API request - starts the query
assert query_job.state == 'RUNNING'

# Waits for the query to finish
iterator = query_job.result(timeout=TIMEOUT)
rows = list(iterator)

assert query_job.state == 'DONE'
assert len(rows) == 100
row = rows[0]
assert row[0] == row.salesWeek == row['salesWeek']
print(row['salesWeek'])

##################create table#######################
"""
SCHEMA = [
    bigquery.SchemaField('full_name', 'STRING', mode='required'),
    bigquery.SchemaField('age', 'INTEGER', mode='required'),
]
table_ref = dataset.table('my_table')
table = bigquery.Table(table_ref, schema=SCHEMA)
table = client.create_table(table)      # API request

assert table.table_id == 'my_table'
"""
##########################################################

table_ref = dataset.table('my_table')
table = bigquery.Table(table_ref)

table.table_id == 'my_table'
table = client.get_table(table)  # API request

ROWS_TO_INSERT = [
    (u'Phred Phlyntstone', 32),
    (u'Wylma Phlyntstone', 29),
]

errors = client.create_rows(table, ROWS_TO_INSERT)  # API request

assert errors == []

"""
from google.cloud import bigquery
client = bigquery.Client()

QUERY = (
        'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
        'WHERE state = "TX" '
        'LIMIT 100')
query_job = client.query(QUERY)

for row in query_job:  # API request
   # Row values can be accessed by field name or index
   assert row[0] == row.name == row['name']

"""


"""
QUERY_W_PARAM = (
        'SELECT name, state '
        'FROM `bigquery-public-data.usa_names.usa_1910_2013` '
        'WHERE state = @state '
        'LIMIT 100')

TIMEOUT = 30  # in seconds
param = bigquery.ScalarQueryParameter('state', 'STRING', 'TX')
job_config = bigquery.QueryJobConfig()
job_config.query_parameters = [param]
query_job = client.query(
        QUERY_W_PARAM, job_config=job_config)  # API request - starts the query
assert query_job.state == 'RUNNING'

# Waits for the query to finish
iterator = query_job.result(timeout=None)
rows = list(iterator)

assert query_job.state == 'DONE'
assert len(rows) == 100
row = rows[0]
assert row[0] == row.name == row['name']
assert row.state == 'TX'
"""