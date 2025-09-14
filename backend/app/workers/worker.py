import os

import rq
from redis import Redis


def main() -> None:
    redis = Redis(host=os.getenv("REDIS_HOST", "localhost"), port=6379)
    worker = rq.Worker([rq.Queue("default", connection=redis)])
    worker.work()

if __name__ == "__main__":
    main()
