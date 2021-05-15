FROM golang:1.16.4-buster

WORKDIR /usr/src/app

COPY . .
RUN go mod download
RUN go build

EXPOSE 3000
CMD ["./goapp"]
