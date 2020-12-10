FROM tiangolo/uwsgi-nginx-flask:python3.8
COPY ./requirements /tmp/
RUN pip install -r /tmp/requirements
COPY ./app /app