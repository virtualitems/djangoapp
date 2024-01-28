from multiprocessing import cpu_count

# as user
user = 'djangouser'
group = 'www-data'

# unix domain socket
timeout = 500

# processing
worker_class = 'uvicorn.workers.UvicornWorker'
workers = cpu_count() * 2

# paths
chdir = '/home/djangouser/djangoapp'
pythonpath = '/home/djangouser/djangoapp'

# logging
loglevel = 'debug'
