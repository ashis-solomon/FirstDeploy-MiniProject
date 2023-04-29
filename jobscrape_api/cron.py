from datetime import datetime
import time
from jobscrape_api.models import ScrapeJob

def my_scheduled_job():
    print(f'CRRROOOONNN!! {datetime.now()}')
    print('----------------------------------------------')
    while(True):
        time.sleep(20)
        job = ScrapeJob(job_name=str(datetime.now().strftime('%H:%M:%S')))
        job.save()