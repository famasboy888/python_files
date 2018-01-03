from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron', hour=9, minute=0)
def scheduled_job():
    print('This job is run every weekday at 9am.')

sched.start()
