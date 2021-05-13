FROM node:15.14.0-buster-slim

WORKDIR /usr/src/app

COPY package.json ./
RUN npm install --production

COPY app.js ./

EXPOSE 3000
CMD [ "node", "app.js" ]