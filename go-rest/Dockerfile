FROM golang:1.16.4-buster

WORKDIR /usr/src/app

COPY go.mod . 
RUN go mod download

COPY main.go ./
RUN go build

EXPOSE 3000
CMD ./app
