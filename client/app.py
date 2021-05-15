import logging
import sys
from time import sleep, time

import requests
from decouple import config

LOG_LEVEL = config("LOG_LEVEL", default="INFO", cast=str).upper()
COUNT = config("COUNT", default=1, cast=int)
HOSTS = config("HOSTS", default="", cast=str)

logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger("client")


def request(host):
    min = sys.float_info.max
    max = sys.float_info.min
    for sequence in range(COUNT):
        route = f"http://{host}/fibonacci/v1/sequence/{sequence}"
        start = time()
        try:
            requests.get(route)
        except BaseException as error:
            logger.error(error)
        total = time() - start
        min = total if total < min else min 
        max = total if total > max else max 
        logger.debug("{:.5f}s | {}".format(total, route))
    return min, max

def main():
    logger.info("Waiting the containers up...")
    sleep(10)
    logger.info("Benchmark started...")
    results = []
    for host in HOSTS.split(","):
        start = time()
        min, max = request(host)
        total = time() - start
        results.append({"host": host, "total": total, "min": min, "max": max})
    logger.info("Benchmark finished!")
    logger.info(f"Report (Count {COUNT}):")
    for res in sorted(results, key=lambda r: r["total"]):
        logger.info("- {} finished at {:.5f}s | avg: {:.5f}s | min: {:.5f}s | max: {:.5f}s".format(res["host"], res["total"], res["total"] / COUNT, res["min"], res["max"]))


if __name__ == "__main__":
    main()
