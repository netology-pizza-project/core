FROM node:20.10-alpine as builder
RUN mkdir -p /home/node/src/node_modules && chown -R node:node /home/node/src
WORKDIR /home/node/app
COPY --chown=node:node package*.json ./
COPY --chown=node:node . .
#USER node
RUN npm i
RUN npm run build

FROM nginx:stable-alpine3.19-perl
RUN mkdir "app"
COPY --from=builder /home/node/app/dist /app
COPY nginx/default.conf /etc/nginx/conf.d/