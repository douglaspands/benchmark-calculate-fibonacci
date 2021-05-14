import logging
from time import sleep, time

import requests
from decouple import config

LOG_LEVEL = config("LOG_LEVEL", default="INFO", cast=str).upper()
COUNT = config("COUNT", default=1, cast=int)
HOSTS = config("HOSTS", default="", cast=str)

logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger("client")


def request(host):
    for sequence in range(COUNT):
        route = f"http://{host}/fibonacci/v1/sequence/{sequence}"
        start = time()
        res = requests.get(route)
        logger.debug("{:.5f}s | {} | {}".format(time() - start, route, repr(res.json())))


def main():
    logger.info("Waiting the containers up...")
    sleep(10)
    logger.info("Benchmark started...")
    results = []
    for host in HOSTS.split(","):
        start = time()
        request(host)
        total = time() - start
        results.append({"host": host, "total": total})
    logger.info("Benchmark finished!")
    logger.info(f"Report (Count {COUNT}):")
    for res in sorted(results, key=lambda r: r["total"]):
        logger.info("- {} finished at {:.5f}s (avg: {:.5f}s)".format(res["host"], res["total"], res["total"] / COUNT))


if __name__ == "__main__":
    main()
