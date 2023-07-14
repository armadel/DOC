FROM python:3.7-alpine

COPY todolist.py /

CMD ["python", "/todolist.py"] 