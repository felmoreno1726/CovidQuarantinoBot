rasa run actions > ./server.log 2>&1 &
server_pid=$!
rasa shell
kill -9 $server_pid
