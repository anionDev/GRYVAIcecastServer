FROM alpine:latest

ARG TargetEnvironmentType
ARG Version="0.1.3"
LABEL maintainer "marius.goecke@gmail.com"
LABEL version="v$Version"
LABEL description="GRYVAIcecastServer is a docker-image for simply running an Icecast-server in a docker-container."

RUN addgroup -S icecast && adduser -S icecast

RUN apk add --update icecast mailcap && \
    rm -rf /var/cache/apk/* && \
    mkdir /var/log/icecast && \
    touch /var/log/icecast/access.log && \
    touch /var/log/icecast/error.log && \
    chmod -R 777 /var/log/icecast

COPY GRYVAIcecastServer/EntryPointScript.sh /EntryPointScript.sh
RUN chmod +x /EntryPointScript.sh

EXPOSE 8000
VOLUME ["/var/log/icecast"]
ENTRYPOINT ["/EntryPointScript.sh"]
