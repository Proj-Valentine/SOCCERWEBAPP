import multiprocessing

bind = "127.0.0.1:8000"  # Localhost IP address and port number
workers = multiprocessing.cpu_count()  # Use the number of available CPU cores
errorlog = '-'  # Log errors to stdout
accesslog = '-'  # Log access to stdout
loglevel = 'info'  # Set the desired log level (e.g., info, debug, warning)

# Application specific settings
pythonpath = '/home/ec2-user/SOCCERWEBAPP/proj1949'
module = 'proj1949.wsgi:application'
