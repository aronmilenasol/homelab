.PHONY: setup-localstack configure-aws up down restart logs clean

setup-localstack:
	bash scripts/setup-localstack.sh

configure-s3:
	bash scripts/configure-aws.sh

up:
	docker compose up -d

down:
	docker compose down

restart: down up

logs:
	docker compose logs -f

clean: down
	rm -rf volume backups tmp
