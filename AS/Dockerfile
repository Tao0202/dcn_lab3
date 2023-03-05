# start by pulling the python image
FROM python:3.8-alpine

# switch working directory
WORKDIR /app

# copy every content from the local file to the image
COPY . /app
# expose port and reconfigure transport protocol
EXPOSE 53533/udp
# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["AuthoritativeServer.py" ]