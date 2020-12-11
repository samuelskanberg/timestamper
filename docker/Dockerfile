FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY src /code/
COPY docker/entrypoint.sh /

CMD ["/entrypoint.sh"]
