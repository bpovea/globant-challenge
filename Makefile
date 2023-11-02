git-hooks:
	pre-commit install

.env:
	cp .env.example .env

terraform:
	cd ./iac && terraform init
	cd ./iac && terraform apply -input=false -auto-approve

start: .env
	docker-compose up -d local-stack challenge-db
	sleep 5
	make migrate
	make terraform

down:
	make stop-dependencies

stop-dependencies:
	docker-compose down --remove-orphans

kill:
	make stop-dependencies

migrate: .env
	docker-compose run challenge-migration

clean: .env
	docker-compose rm -f -v -s local-stack challenge-db
	docker-compose up --force-recreate -d local-stack challenge-db
	make migrate
	make terraform

delete:
	docker container rm $(docker container list -a | awk '/Exit/{ print $1 }')