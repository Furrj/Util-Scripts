#!/usr/bin/env bash

set -e

session_name="test"
client="client"
api="api"
postgres="postgres"

tmux new-session -d -s $session_name

tmux rename-window -t 0 $client
tmux send-keys -t $client "cd /home/fraterhqc/repos/projects/spelldle/client" C-m C-l

tmux new-window -t $session_name:1 -n $api
tmux send-keys -t $api "cd /home/fraterhqc/repos/projects/spelldle/api" C-m C-l

tmux new-window -t $session_name:2 -n $postgres
docker start postgres
tmux send-keys -t $postgres "docker exec -it postgres bash" C-m
tmux send-keys -t $postgres "psql -U postgres" C-m
tmux send-keys -t $postgres "\c spelldle" C-m C-l