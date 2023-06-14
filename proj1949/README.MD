# Django Application Deployment with Gunicorn, Nginx, and Amazon EC2

This repository contains the code and configuration files for deploying a Django application using Gunicorn and Nginx on an Amazon EC2 instance. Additionally, a domain has been registered in Route 53 and configured as the endpoint for the EC2 instance.

Deployment Steps
To deploy your Django application using this setup, follow these steps:

- Register a domain in Route 53 and configure it to point to your EC2 instance's IP address.
- Launch an Amazon EC2 instance and ensure it has the necessary security group and IAM role permissions.
- Clone this repository to your local machine.
- Configure the Django application according to your project requirements.
- Push the code from your local machine to the GitHub repository associated with this deployment.
- SSH into the EC2 instance.
- Install Gunicorn and other dependencies on the EC2 instance.
- Pull the latest code from the GitHub repository on the EC2 instance.
- Configure Gunicorn to run your Django application.
- Install and configure Nginx as a reverse proxy server.
- Restart Nginx to apply the changes.
- Access your Django application using the registered domain.
- With this deployment setup, your Django application is hosted on an EC2 instance, and Nginx acts as a reverse proxy server, directing traffic from the registered domain to your application running on Gunicorn.

Please refer to the configuration files and documentation within this repository for more detailed instructions on customizing and managing your Django application deployment.

If you have any questions or encounter any issues during the deployment process, feel free to reach out for assistance.





