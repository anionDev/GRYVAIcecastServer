FROM alpine:latest
LABEL maintainer "marius.goecke@gmail.com"

RUN addgroup -S icecast && adduser -S icecast

RUN apk add --update icecast mailcap && rm -rf /var/cache/apk/*

COPY EntryPointScript.sh /EntryPointScript.sh
RUN chmod +x /EntryPointScript.sh

#USER icecast
EXPOSE 8000
VOLUME ["/var/log/icecast"]
ENTRYPOINT ["/EntryPointScript.sh"]
CMD icecast -c /etc/icecast.xml
