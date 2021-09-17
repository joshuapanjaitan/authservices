#Get Python BASE Image
FROM python:3.9-alpine

#SET up the path for variabel ENV
ENV PATH="/scripts:${PATH}"

#Download All Dependencies from Requirement .txt
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp 

#Copy Streamming-app to Docker Image
RUN mkdir /auth
COPY ./auth /auth
WORKDIR /auth
COPY ./scripts /scripts

#run scripts
RUN chmod +x /scripts/*

#create folder on Docker Image to serve static & media file
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

#access docker file via user
RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user

CMD ["entrypoint.sh"]
