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

SUPERSET_DOCKER_RUN := docker exec -i -t superset-toolbox

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

sep--sep-a: ## ========== 开发时命令 ==============


up: ## up
	docker-compose up

toolbox: ## Enter Shell
	$(SUPERSET_DOCKER_RUN) /bin/bash

dbshell: ## Enter psql as postgres
	$(PG_DOCKER_RUN) su postgres -c "psql -U superset"

sep--sep-e: ## ========== Docker 镜像相关 ==============
	echo "## ========== 本行只是优雅的分割线  ==============="

docker-build-superset: ## > docker build superset
	docker build -t 'superset:local' -f 'compose/superset/Dockerfile' .

docker-build-f-superset: ## > docker build superset --no-cache
	docker build -t 'superset:local' -f 'compose/superset/Dockerfile' --no-cache .

