# app.py
from prometheus_client import start_http_server, Counter, Gauge
import time, random

REQUESTS = Counter('sample_requests_total', 'Total sample requests')
IN_PROGRESS = Gauge('sample_inprogress', 'In-progress sample jobs')

def do_work():
    REQUESTS.inc()
    IN_PROGRESS.inc()
    time.sleep(random.random() * 1.2)
    IN_PROGRESS.dec()

if __name__ == "__main__":
    # Exposes metrics on :8000/metrics
    start_http_server(8000)
    while True:
        do_work()

