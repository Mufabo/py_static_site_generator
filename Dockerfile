FROM python:3.12-bullseye
SHELL ["/bin/bash", "-c"]
RUN curl -sS https://webi.sh/golang | sh
RUN source ~/.config/envman/PATH.env
RUN go install github.com/bootdotdev/bootdev@latest