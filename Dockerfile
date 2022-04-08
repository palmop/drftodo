FROM python:3.8 as base
WORKDIR /webapp
RUN pip install pipenv

COPY . .
ENV PYTHONUNBUFFERED=1

FROM base as dev
# this is a dev image build, so install dev packages
RUN pipenv install --system --dev

CMD ["./init.sh"]