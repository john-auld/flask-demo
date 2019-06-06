# Demo of running a flask app using gunicorn as a systemd service

- Edit the user name, paths and port in flask-demo.service
- sudo cp flask-demo.service /etc/systemd/system/flask-demo.service
- sudo systemctl enable flask-demo
- sudo systemctl start flask-demo
- curl http://localhost:8000/

You should see "OK" as the response of the curl command.

## [Systemd sandboxing](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#Sandboxing) options
The setting "ProtectSystem = full" makes the file system read only, but write access can be allowed to specific directories using the ReadWritePaths option.

## gunicorn docs

http://docs.gunicorn.org/en/stable/deploy.html