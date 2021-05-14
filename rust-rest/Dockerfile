FROM rust:1.52-slim-buster

WORKDIR /usr/src/app
COPY . .

RUN cargo build

EXPOSE 8080
CMD ["cargo", "run"]
