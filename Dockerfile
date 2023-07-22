# package needed to run python
FROM python:3.8

# option to create pyc file
ENV PYTHONDONTWRITEBYTECODE 1
# show all status or logs on terminal
ENV PYTHONUNBUFFERED 1

# default working directory on container
WORKDIR /app
# copy the file which contains allj requirements
COPY requirements.txt .
# upgrade pip and install all requirements
RUN pip install --upgrade pip && pip install -r requirements.txt
# copy all necessary files to container
COPY . /app/