# nestechback

To create a superuser from your host machine, you should use the docker-compose run command. Here's how you can do it:
`docker-compose run app python manage.py createsuperuser`

To create a super user when using docker-compose-deploy.yml:
1- `docker exec -it nestechback-app-1 sh`
2- `python manage.py createsuperuser`