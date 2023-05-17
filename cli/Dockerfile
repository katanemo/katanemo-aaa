FROM python:3

WORKDIR /usr/src/app

COPY cli cli
COPY python-sdk python-sdk
RUN cd cli && pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/app/cli

ENTRYPOINT [ "python", "-m", "katutil"]
CMD ["--help"]
