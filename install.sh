#!/bin/bash

apt update
apt install -y python3 python3-pip

echo "[CONF]\nTOKEN=$2" > token.conf

if [ "$1" != "" ]
then
    echo "[Unit]
    Description=$1_bot Application Service
    Requires=networking.service
    After=networking.service

    [Service]
    Type=simple
    WorkingDirectory=`pwd`
    ExecStart=/usr/bin/python3 worker.py
    PIDFile=/run/$1_bot.pid
    Restart=always

    [Install]
    WantedBy=multi-user.target" > /etc/systemd/system/$1_bot.service

    systemctl enable $1_bot

    if [ "$2" != "" ]
    then
        systemctl start $1_bot
    fi
fi

