#!/bin/sh
#wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
/usr/local/bin/heroku container:login
/usr/local/bin/heroku container:push web --app $HEROKU_APP_NAME
/usr/local/bin/heroku container:release web --app $HEROKU_APP_NAME