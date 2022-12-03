FROM alpine:latest

ARG TargetEnvironmentType
ARG Version="0.1.10"
LABEL maintainer "marius.goecke@gmail.com"

RUN addgroup -S icecast && adduser -S icecast

RUN apk add --update icecast mailcap && rm -rf /var/cache/apk/*

COPY EntryPointScript.sh /EntryPointScript.sh
RUN chmod +x /EntryPointScript.sh

EXPOSE 8000
VOLUME ["/var/log/icecast"]
ENTRYPOINT ["/EntryPointScript.sh"]
CMD icecast -c /etc/icecast.xml
