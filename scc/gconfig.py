# Worker Settings
workers = 1
threads = 5
worker_class = 'gevent'  # Use gevent async workers
worker_connections = 1000  # Maximum concurrent connections per worker

# Server Settings
bind = "0.0.0.0:5220"

# Timeout Settings
timeout = 15  # Automatically restart workers if they take too long
graceful_timeout = 2 # Graceful shutdown for workers

# Worker Restart Settings
max_requests = 500  # Restart workers after processing 1000 requests
max_requests_jitter = 50  # Add randomness to avoid mass restarts

# Logging Settings
accesslog = "-"  # Log HTTP requests to a file
errorlog = "-"  # Log errors to a file
loglevel = "info"  # Set log verbosity (debug, info, warning, error, critical)


