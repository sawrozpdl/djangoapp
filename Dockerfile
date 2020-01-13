FROM python:latest
ENV PYTHONUNBUFFERED 1
ENV PORT=80
ENV SECRET_KEY=dlkfjdskljflkj
ENV DEBUG=$DEBUG
RUN mkdir /src
WORKDIR /src
COPY requirements.txt /src/
RUN pip install -r requirements.txt
COPY . .
CMD python manage.py runserver 0.0.0.0:$PORT
EXPOSE $PORT