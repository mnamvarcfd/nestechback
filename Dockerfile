FROM python:3.9-alpine3.13
LABEL maintainer="Morteza_Namvar"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./scripts /scripts
COPY ./app /app

WORKDIR /app
EXPOSE 8000

ARG DEV=false

RUN python -m venv /py
RUN /py/bin/pip install --upgrade pip
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps build-base postgresql-dev musl-dev zlib zlib-dev linux-headers
RUN /py/bin/pip install -r /tmp/requirements.txt
RUN /py/bin/pip install drf-spectacular
RUN if [ "$DEV" = "true" ]; then /py/bin/pip install -r /tmp/requirements.dev.txt; fi
RUN rm -rf /tmp
RUN apk del .tmp-build-deps
RUN adduser --disabled-password --no-create-home django-user
RUN mkdir -p /vol/web/media 
RUN mkdir -p /vol/web/static 
RUN chown -R django-user:django-user /vol
RUN chmod -R 755 /vol
RUN chown -R django-user:django-user /vol/web
RUN source /py/bin/activate && pip list
RUN chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER django-user

CMD ["run.sh"]