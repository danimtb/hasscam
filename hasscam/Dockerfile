ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Setup
RUN apk add --update python python-dev py-pip build-base \
    && pip install --no-cache --upgrade pip
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

# Copy data for add-on
COPY hasscam.py /

CMD ["python", "hasscam.py"]
