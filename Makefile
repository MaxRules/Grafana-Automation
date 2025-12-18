install:
	poetry install

test:
	poetry run pytest -q

lint:
	poetry run flake8

build:
	docker build -t grafana-automation:local .

compose-up:
	docker-compose up -d --build

compose-down:
	docker-compose down
