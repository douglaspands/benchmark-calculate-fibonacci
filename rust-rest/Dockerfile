FROM rust:1.52-slim-buster

WORKDIR /usr/src/app
COPY ./Cargo.toml ./
COPY ./src ./src

RUN cargo build

CMD ["rust-rest"]
