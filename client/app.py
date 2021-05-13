import logging
from time import sleep, time

import requests
from decouple import config

LOG_LEVEL = config("LOG_LEVEL", default="INFO", cast=str).upper()
COUNT = config("COUNT", default=1, cast=int)
HOSTS = config("HOSTS", default="", cast=str).split(",")

logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger("client")


def request(host):
    for sequence in range(COUNT):
        route = f"http://{host}/fibonacci/v1/sequence/{sequence}"
        start = time()
        res = requests.get(route)
        logger.debug("{:.3f}s | {} | {}".format(time() - start, route, repr(res.json())))


def main():
    logger.info("Waiting the containers up...")
    sleep(10)
    logger.info("Benchmark started...")
    results = []
    for host in HOSTS:
        start = time()
        request(host)
        results.append("{} finished at {:.3f}s".format(host, time() - start))
    logger.info("Benchmark finished!")
    logger.info("Report:")
    for res in results:
        logger.info(f"- {res}")


if __name__ == "__main__":
    main()
