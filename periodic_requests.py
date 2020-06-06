import requests
import pytz
from apscheduler.schedulers.twisted import TwistedScheduler
from twisted.internet import reactor


def send_request():
    requests.post(url=' https://nameless-thicket-74802.herokuapp.com/schedule.json',
                  data={
                      'project': 'default',
                      'spider': 'best_movies'
                  }
                  )


if __name__ == '__main__':
    scheduler = TwistedScheduler(timezone=pytz.utc)
    scheduler.add_job(send_request,'cron',day_of_week='sat-sun',hour='10',minute='40')
    scheduler.start()
    reactor.run()
