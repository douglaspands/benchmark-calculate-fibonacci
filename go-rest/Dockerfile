FROM golang:1.16.4-buster as build

WORKDIR /usr/src/app

COPY go.mod . 
RUN go mod download
COPY main.go ./
RUN go build

FROM golang:1.16.4-buster as runner

COPY --from=build /usr/src/app /usr/src/app
WORKDIR /usr/src/app
EXPOSE 3000
CMD ./app