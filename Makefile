.PHONY:  help test
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-30s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)


init: ## init
	docker-compose up airflow-init

start:
	docker-compose up

initadmin:
	docker-compose run --rm airflow-cli bash -c "airflow users create --username admin --firstname Peter --lastname Parker --role Admin --email spiderman@superhero.org"
