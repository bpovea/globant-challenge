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
	make copy-initial-data

down:
	make stop-dependencies

stop-dependencies:
	docker-compose down --remove-orphans

kill:
	make stop-dependencies

migrate: .env
	docker-compose run challenge-migration

clean: .env
	make delete
	make start

delete:
	docker-compose rm -f -v -s local-stack challenge-db challenge-migration

copy-initial-data:
	aws s3 cp ./data s3://globant-challenge/data/ --recursive --endpoint-url http://localhost:4566
