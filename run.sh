set -e

sudo docker build -t reposcan ./app
docker rmi `docker images --filter dangling=true -q`
sudo docker run --rm -it -p 5000:5000 reposcan