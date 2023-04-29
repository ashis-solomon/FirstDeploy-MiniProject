from datetime import datetime
from jobscrape_api.models import ScrapeJob

def my_scheduled_job():
    print(f'CRRROOOONNN!! {datetime.now()}')
    print('----------------------------------------------')
    job = ScrapeJob(job_name=str(datetime.now().strftime('%H:%M:%S')))
    job.save()