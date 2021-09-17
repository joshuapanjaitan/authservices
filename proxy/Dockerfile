FROM nginxinc/nginx-unprivileged:1-alpine
 
COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./uwsgi_params /etc/nginx/uwsgi_params

ENV LISTEN_PORT=8000
ENV APP_HOST=auth
ENV APP_PORT=9000

USER root
RUN mkdir -p /vol/static
RUN chmod 755 /vol/static

USER nginx 
