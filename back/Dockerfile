FROM archlinux

ENV PG_HOST=''
ENV PG_USER=''
ENV PG_PASS=''
ENV PG_DB=''

ADD ./server.py .
RUN pacman -Syy --noconfirm python python-pip python-fastapi uvicorn python-psycopg2

EXPOSE 8000/tcp
CMD ["uvicorn", "server:app", "--host", "0.0.0.0"]