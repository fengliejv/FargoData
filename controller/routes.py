from flask import current_app as app

@app.route('/')
def home():
    return "Hello, Flask with APScheduler!"


from TimeJob.scrap.quartr_calendar_get import get_quartr_calendar
@app.route('/get_quartr_calendar')
def get_quartr():
    return get_quartr_calendar()