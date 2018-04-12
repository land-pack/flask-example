############################################################
# Dockerfile to build Python WSGI Application Containers
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu
FROM landpack/nasa


# Expose ports
ADD /nasa /nasa

EXPOSE 5000

# Set the default directory where CMD will execute
WORKDIR /nasa

# Set the default command to execute    
# when creating a new container
# i.e. using CherryPy to serve the application
CMD python app.py
