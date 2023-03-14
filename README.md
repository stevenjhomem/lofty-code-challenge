Welcome to my project for the Lofty job application!

1. Be sure that you have properly installed Docker locally. 
2. If you do not have docker installed, please go to this url and follow the instructions for your machine: - https://docs.docker.com/get-docker/
3. Be sure to open Docker for desktop so that your Docker Daemon is running before we run our first command. 
4. Clone the repo using the following git command if you have not done so already:
   - ```git clone https://github.com/stevenjhomem/lofty-code-challenge.git```
5. After successfully cloning the repo, be sure to navigate to the root directory of the project in your terminal. 
6. Now, run the following command to build the project in the development container:
   - ```docker compose up --build``` 
7. We first need to make migrations. Please run the following commands:
   - ```docker compose exec web python manage.py makemigrations```
   - ```docker compose exec web python manage.py migrate```
8. We will now need you to create a superuser. Please run the following command in your terminal: 
   - ```docker compose exec web python source/manage.py createsuperuser``` 
   - Feel free to leave the email portion blank. 
9. Once you have successfully created a superuser, please navigate to the following URL and login: 
   - ```127.0.0.1:8000/admin```
10. We will now begin the seeding process for our database. Please run the following command:
    - ```docker compose exec web python source/manage.py seed --total_seeds=24```
    - If successful, this will seed our database with 24 instances of random dogs. 
    - Each instance of a dog should have a breed, an image, a modified image, and any metadata from the original image.
11. Upon completion, please navigate to the admin site and enter the Dog Image Set and verify that the new data is there. 
    - This satisfies this portion of the technical interview: Create a service that populates the database with 24 images of dogs along with any metadata with the image
12. Now, in order to see the auto-increment aspect of the challenge, navigate to the Key Value App in our admin site.
    - Create a new key. You need atleast a string, I would try just abcd. And give it a value of any number greater than 0. 
    - Now, that we have a key instance with a value that is greater than 0. We can run the following command:
       - ```docker compose exec web python source/manage.py increment_the_incremented```
       - This will run continuously every 6 seconds. 
       - You may stop this command from running by hitting Control + C. 
       - Once you stop this command, you can go back to admin and notice that the original key now has a greater value.
13. I have installed Swagger for our API documentation. To navigate to our API documentation, be sure you have created a superuser and logged into the admin site. Please visit this site: 
       - http://127.0.0.1:8000/api/schema/swagger-ui/#/
       - You can test the endpoints within the API a couple of ways:
       - You can use the execute button with the Swagger UI.
       - You can hit the URLs the old-fashioned way. This is recommended for dogs/{dog_id} endpoint as it is returning a html template.
14. When you are ready, be sure to run the following command to shut down your connection to the docker container:
   - ```docker compose down```