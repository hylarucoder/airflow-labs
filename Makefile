.PHONY: help
.DEFAULT_GOAL := help
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

sep--sep-a: ## ========== 开发时命令 ==============

up: ## up
	docker compose up

sep--sep-e: ## ========== Docker 镜像相关 ==============
	echo "## ========== 本行只是优雅的分割线  ==============="

docker-build: ## > docker build airflow
	docker build -t 'airflow:local' -f 'compose/airflow/Dockerfile' .

docker-build-nocache: ## > docker build airflow --no-cache
	docker build -t 'airflow:local' -f 'compose/airflow/Dockerfile' --no-cache .

start:
	docker compose run --rm airflow-web

list-dag:
	docker compose run --rm --no-deps airflow-init airflow dags list 

dbinit:
	docker compose run --rm airflow-init airflow db init
	docker compose run --rm airflow-init airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin

shell:
	docker compose run --rm airflow-init airflow db shell

worker-info:
	docker compose run airflow-worker airflow info
