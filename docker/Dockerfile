FROM node:18.20.7-alpine3.21

WORKDIR /app
COPY package*.json .
RUN ["npm", "ci"]

# ENV NODE_ENV=production

COPY . .
EXPOSE 8080

USER node

CMD ["node", "server.js"]