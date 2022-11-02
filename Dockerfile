FROM pandauserbotfile/pandauserbot:python202

RUN git clone -b main https://github.com/arsyabot/pyroline /home/albypyrobot/ \
    && chmod 777 /home/albypyrobot \
    && mkdir /home/albypyrobot/bin/

COPY ./sample_config.env ./config.env* /home/albypyrobot/

WORKDIR /home/albypyrobot/

RUN pip install -r requirements.txt

ENTRYPOINT [ "bash", "start.sh" ]
