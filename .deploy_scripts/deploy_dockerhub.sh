#!/bin/sh
/usr/local/bin/docker login -u $DOCKER_USER -p $DOCKER_PASS
if [ "$BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$BRANCH"
fi
/usr/local/bin/docker build -f Dockerfile -t $DOCKER_USER/$GITHUB_REPO:$TAG .
/usr/local/bin/docker push $DOCKER_USER/$GITHUB_REPO:$TAG
