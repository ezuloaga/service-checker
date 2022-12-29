## Update production server
`rm -rf ~/docker/service-checker/`

`cd ~/docker`

`git clone https://github.com/ezuloaga/service-checker.git ~/docker/service-checker`

`cd ~/docker/service-checker/`

`sudo docker-compose up -d --build`
