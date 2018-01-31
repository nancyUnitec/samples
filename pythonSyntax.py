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

############### string operations ###################

# if a str is null
if not str:

# return true if str is null
return not text        

#get length of str
len(str)

################ container #######################




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