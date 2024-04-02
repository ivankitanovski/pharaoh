# pharaoh

Rename the `.template.env` file to `.env` inside the `pharaoh` directory.

Make sure to populate the values in there.

If you have docker and docker-compose, just run:

    docker-compose build
    docker-compose up

This will run the app with an empty database. To add an admin user,
while the containers are running, invoke:

    docker exec -it pharaoh_app python manage.py createsuperuser

And, that's it.
