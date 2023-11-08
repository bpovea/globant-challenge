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
	make start-flask

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

start-flask:
	flask --app src/run.py run --debug

run-section-1:
	curl --location 'http://127.0.0.1:5000/populate_data' \
	--header 'Content-Type: application/json' \
	--data '{ \
		"chunk_size": 1000, \
		"delimiter": ",", \
		"jobs_file_path": "s3://globant-challenge/data/jobs.csv", \
		"departments_file_path": "s3://globant-challenge/data/departments.csv", \
		"employees_file_path": "s3://globant-challenge/data/hired_employees.csv" \
	}'

run-section-2-1:
	curl --location --request GET 'http://127.0.0.1:5000//reports/employees_hired_by_job' \
	--header 'Content-Type: application/json' \
	--data '{ \
		"chunk_size": 1000, \
		"output_path": "s3://globant-challenge/output/employees_hired_by_job.csv", \
		"year": 2021 \
	}'
	aws s3 cp s3://globant-challenge/output/employees_hired_by_job.csv ./ --endpoint-url http://localhost:4566

run-section-2-2:
	curl --location --request GET 'http://127.0.0.1:5000//reports/employees_hired_by_department' \
	--header 'Content-Type: application/json' \
	--data '{ \
		"chunk_size": 1000, \
		"output_path": "s3://globant-challenge/output/employees_hired_by_department.csv", \
		"year": 2021 \
	}'
	aws s3 cp s3://globant-challenge/output/employees_hired_by_department.csv ./ --endpoint-url http://localhost:4566
