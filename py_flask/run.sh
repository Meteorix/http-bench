/home/gzliuxin/.local/bin/gunicorn flasky:app --workers=4 --bind=0.0.0.0:5000 --pid=pid --worker-class=meinheld.gmeinheld.MeinheldWorker
