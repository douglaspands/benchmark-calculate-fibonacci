FROM hayd/debian-deno:1.5.2

USER deno

WORKDIR /usr/src/app

COPY app.ts ./
RUN deno cache app.ts

EXPOSE 8000
CMD [ "run", "--allow-net", "app.ts" ]