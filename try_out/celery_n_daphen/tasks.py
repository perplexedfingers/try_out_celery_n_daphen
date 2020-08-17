import time

from try_out import celery_app


def yo(self, retval, task_id, args, kwargs):
    print(retval)


@celery_app.task(on_success=yo)
def long_running_operation():
    print('AA')
    time.sleep(5)
    print('BB')
    return 'done'
