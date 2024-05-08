# Stage 1: Build
FROM python:3.12-bookworm as build

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
# Enable venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

# Stage 2: Runtime
FROM python:3.12-slim-bookworm as runtime

RUN apt-get update \
  && apt-get install -y --no-install-recommends libpq-dev \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean \
  && useradd --create-home --no-log-init dtech

USER dtech
WORKDIR /home/dtech

# set environment variables
ENV VIRTUAL_ENV=/home/dtech/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY --from=build --chown=dtech:dtech /opt/venv venv
COPY --chown=dtech:dtech . .
