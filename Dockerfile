FROM python:3.8

RUN pip install pipenv

ENV PROJECT_DIR /usr/local/src/webapp
COPY . ${PROJECT_DIR}/
WORKDIR ${PROJECT_DIR}

RUN pipenv install --system --deploy
RUN pipfile2req > requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8080
