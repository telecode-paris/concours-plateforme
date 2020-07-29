# This image docker serve the camisole binary with frontend application (nodejs) for the ip7 team
# https://camisole.prologin.org/installation.html

# Docker Hub https://hub.docker.com/r/archlinux/base/
FROM archlinux/base
LABEL maintainer "joseph0priou@gmail.com"
LABEL version "1.0"
LABEL owner "ip7"

SHELL [ "/bin/bash", "-eux", "-o", "pipefail", "-c" ]

# Update cache
# Install common deps
RUN \
        pacman -Syu --noconfirm \
    &&  pacman -S --noconfirm \
            sudo \
            base-devel \
            git \
            wget \
            yajl \
            python3 \
            python-aiohttp \
            python-msgpack \
            python-yaml \
            nodejs \
            npm \
            jdk8-openjdk \
            jre8-openjdk \
            sqlite3

# Create ip7 user
RUN \
        useradd -m --home-dir /home/ip7 --shell=/bin/false ip7 \
    &&  usermod --home /home/ip7 -L ip7 \
    &&  echo "ip7 ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers \
    &&  echo "root ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

USER ip7
WORKDIR /home/ip7

# Install yaourt
# From here https://www.ostechnix.com/install-yaourt-arch-linux/
RUN \
        git clone https://aur.archlinux.org/package-query.git \
    &&  cd package-query/ \
    &&  makepkg -si --noconfirm \
    &&  cd .. \
    &&  git clone https://aur.archlinux.org/yaourt.git \
    &&  cd yaourt \
    &&  makepkg -si --noconfirm \
    &&  cd .. \
    &&  rm -dR yaourt/ package-query/

# Install camisole deps
RUN \
        yaourt -S --noconfirm \
            camisole-git \
            jdk11-openjdk ocaml \
            isolate-git

# Install camisole
RUN \
        git clone https://github.com/prologin/camisole \
    &&  cd camisole \
    &&  python3 setup.py build \
    &&  sudo python3 setup.py install \
    &&  cd .. \
    &&  sudo rm -rf camisole

# Install deps
COPY package.json .

RUN npm install
RUN npm i request --save

# add subjects and website
COPY static static
COPY views views
COPY subjects subjects
COPY \
    index.js \
    add_users.js \
    insert_user.js \
    update_data.js \
    launch.sh \
    database.sql \
    ./

RUN \
    sudo chown -R ip7 \
        views \
        static \
        subjects \
        index.js \
        add_users.js \
        insert_user.js \
        update_data.js \
        launch.sh \
        database.sql

VOLUME [ "/home/ip7/save" ]
SHELL [ "/bin/sh", "-c" ]
ENTRYPOINT ["sudo", "/bin/sh", "launch.sh"]
