# Imports the Google Cloud client library
from google.cloud import bigquery

# Instantiates a client
bigquery_client = bigquery.Client(project='localcover-55')

"""
# The name for the new dataset
dataset_id = 'lc_api_hehe'

# Prepares a reference to the new dataset
dataset_ref = bigquery_client.dataset(dataset_id)
dataset = bigquery.Dataset(dataset_ref)

# Creates the new dataset
dataset = bigquery_client.create_dataset(dataset)

print('Dataset {} created.'.format(dataset.dataset_id))
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