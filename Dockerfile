FROM python:3

ADD tinyipam requirements.txt /tinyipam/
WORKDIR /tinyipam/

RUN pip3 install -r requirements.txt && pip3 install gunicorn

EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]

