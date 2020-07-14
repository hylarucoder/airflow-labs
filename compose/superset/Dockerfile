FROM python:3.8.3-buster
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN sed -i 's/deb.debian.org/mirrors.cloud.tencent.com/g' /etc/apt/sources.list
RUN sed -i 's/security.debian.org/mirrors.cloud.tencent.com/g' /etc/apt/sources.list
RUN apt-get update && apt-get upgrade -y && apt-get install -y vim git gcc build-essential libffi-dev
ENV PYPI=https://mirrors.cloud.tencent.com/pypi/simple
ENV PIP_DEFAULT_TIMEOUT=1000
RUN pip install -U pip -i $PYPI
RUN pip install -U poetry -i $PYPI
ENV POETRY_VIRTUALENVS_CREATE=false
WORKDIR /etc/superset
COPY ./compose/superset/pyproject.toml .
COPY ./compose/superset/poetry.lock .
COPY README.md .
RUN poetry export -f requirements.txt --dev | pip install -i $PYPI -r /dev/stdin
COPY . .
# INSTALL PROJECT
RUN poetry install
RUN pip uninstall python-openid python3-openid -y && pip install -U python3-openid -i $PYPI
CMD ["start"]
