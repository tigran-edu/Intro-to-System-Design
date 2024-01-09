A Simple API server for link compression(like https://bitly.com/) with nginx and redis

**System start:**
```
docker compose build
docker compose up server1 server2 redis nginx
```

**Usage**

POST
```
curl -X POST localhost:80/create --data url=your_url
```
GET
```
curl -X GET localhost:80/link/url_token
```
