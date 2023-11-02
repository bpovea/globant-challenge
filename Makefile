git-hooks:
	pre-commit install

start:
	docker-compose up -d local-stack challenge-db
	sleep 5
	make migrate

down:
	make stop-dependencies

stop-dependencies:
	docker-compose down --remove-orphans

kill:
	make stop-dependencies

migrate:
	docker-compose run challenge-migration

clean:
	docker-compose rm -f -v -s local-stack challenge-db
	docker-compose up --force-recreate -d local-stack challenge-db
	make migrate