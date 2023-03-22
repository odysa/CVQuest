# Stage 1: Build Svelte application
FROM node:19 AS svelte-builder

WORKDIR /app/site

COPY site/package*.json ./
RUN npm i --legacy-peer-deps

COPY site/ .
RUN npm run build

# Stage 2: Set up Python environment
FROM python:3.9
ARG OPENAI_API_KEY

WORKDIR /app

RUN printenv > .env

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY --from=svelte-builder /app/site/build /app/site/build

EXPOSE 8080

# Start the application
CMD ["bash", "run.sh"]
