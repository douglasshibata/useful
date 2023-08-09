# PUll the image
```bash
docker pull mongo
```

# Run a container
```bash
docker run --name containername mongo
```

# Interact with the database through the bash shell client
```bash
docker exec -it containername bash
```
# Launch the MongoDB shell client
```bash
mongosh
```