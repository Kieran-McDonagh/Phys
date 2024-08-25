# Phys

To get the project running on your PC:

1. To get a secret key, open your terminal and run:
   `openssl rand -hex 32`

2. Create a .env file with the following information:

```
    MONGO_URI = "mongodb://mongo:27017/test_database"
    SECRET_KEY = <secret key string>
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = <time in minutes>
```
