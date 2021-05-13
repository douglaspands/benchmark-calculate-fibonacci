from decouple import config
import requests
from time import time, sleep

COUNT = config("COUNT", default=1, cast=int)
HOSTS = config("HOSTS", default="", cast=str).split(",")


def request(host):
    for sequence in range(COUNT):
        route = f"http://{host}/fibonacci/v1/sequence/{sequence}"
        start = time()
        res = requests.get(route)
        print("{:.3f}seg".format(time() - start), f"| {route} |", repr(res.json()))


def main():
    print("Waited the containers starting...")
    sleep(10)
    print("Benchmark started...")
    for host in HOSTS:
        start = time()
        request(host)
        print("{} finished at {:.3f}seg".format(host, time() - start))
    print("Benchmark finished!")


if __name__ == "__main__":
    main()
