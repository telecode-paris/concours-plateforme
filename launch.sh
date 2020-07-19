#!/bin/sh

echo "IP7 super docker container started"

export PORT=8080
DURATION=10800

# Create database only if needed
if [ ! -f save/database.db ]; then
    echo "Create database"
    sqlite3 database.db -init database.sql

    echo "Generate problems"
    (cd subjects && python3 main.py > problems.sql)

    echo "Insert problems into database"
    sqlite3 database.db -init subjects/problems.sql

    START=1555333200
    DEADLINE=$(( START + DURATION ))

    echo "Set contest start to ${START} and deadline to ${DEADLINE}"
    echo "insert into contest_data (contest_start, contest_deadline) values(${START}, ${DEADLINE});" | sqlite3 database.db

    node add_users.js
    sudo sqlite3 database.db ".clone save/database.db"
else
    echo "A save/database.db already exists"
fi

echo "Launching camisole"
nohup python3 -m camisole serve -p 9000 &

echo "Lauching website"
npm run prod
