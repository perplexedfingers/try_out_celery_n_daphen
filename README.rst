``celery -A tasks worker --loglevel=info``
``daphne -b 0.0.0.0 -p 8000 try_out.asgi:application``
