FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /source

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    binutils libproj-dev gdal-bin uwsgi

RUN apt-get update && apt-get install -y gettext libgettextpo-dev

COPY requirements.txt /source/

RUN pip install -r requirements.txt
RUN pip3 install xlrd

CMD ["/bin/bash"]
