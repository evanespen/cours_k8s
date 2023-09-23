FROM archlinux

ENV API_URL=''
ENV PORT=8001

RUN mkdir /app

ADD index.html main.css main.js /app/
ADD entrypoint.sh /

RUN pacman -Syy python --noconfirm

ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]