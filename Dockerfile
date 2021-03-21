FROM python:3.8.8-alpine3.13
MAINTAINER nickolay.romeyko@gmail.com
COPY . /python-test-calculator
WORKDIR /python-test-calculator
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null