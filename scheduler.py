from apscheduler.schedulers.background import BackgroundScheduler
from ai_parser import parse_command
from executor import execute

scheduler = BackgroundScheduler()

def run_scheduled(command_text):
    command = parse_command(command_text)
    execute(command)

def schedule_task(command_text, seconds):
    scheduler.add_job(
        run_scheduled,
        'interval',
        seconds=seconds,
        args=[command_text]
    )

def start_scheduler():
    scheduler.start()