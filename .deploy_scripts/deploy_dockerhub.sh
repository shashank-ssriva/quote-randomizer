#!/bin/sh
docker login -u $DOCKER_USER -p $DOCKER_PASS
if [ "$BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$BRANCH"
fi
docker build -f Dockerfile -t $DOCKER_USER/$GITHUB_REPO:$TAG .
docker push $DOCKER_USER/$GITHUB_REPO:$TAG
