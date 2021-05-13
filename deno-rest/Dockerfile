FROM hayd/debian-deno:1.5.2

USER deno

WORKDIR /usr/src/app

COPY main.ts ./
RUN deno cache main.ts

EXPOSE 8000
CMD [ "run", "--allow-net", "main.ts" ]