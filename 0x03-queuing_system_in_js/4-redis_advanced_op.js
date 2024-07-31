import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Function to set hash values
function setHashValue(hashName, field, value) {
  client.hset(hashName, field, value, redis.print);
}

// Create Hash
const hashName = 'HolbertonSchools';
setHashValue(hashName, 'Portland', 50);
setHashValue(hashName, 'Seattle', 80);
setHashValue(hashName, 'New York', 20);
setHashValue(hashName, 'Bogota', 20);
setHashValue(hashName, 'Cali', 40);
setHashValue(hashName, 'Paris', 2);

// Display Hash
client.hgetall(hashName, (err, object) => {
  if (err) {
    console.error(err);
  } else {
    console.log(object);
  }
});
