## Depend:
````    
pip --no-cache install mongoengine==0.15.0 
pip --no-cache install flask==1.0.2 
pip --no-cache install uwsgi==2.0.17 
sudo apt-get install mongodb 
````    

## Nginx:
````
...
server {
    listen 80;
    location /index {
        alias /home/ubuntu/code/frontend/;
    }
    location /src {
        alias /home/ubuntu/code/frontend/src/;
    }
    location / {
        proxy_pass http://127.0.0.1:9999;
    }
}
...
````

## Use:
````    
sudo uwsgi --ini wsgi wsgi.ini
````    


