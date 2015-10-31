For the periodic emails to send, run the following three commands in three different windows:

redis-server (install redis before running this command)
celery -A ecs160 worker -l info
celery -A ecs160 beat -l info

