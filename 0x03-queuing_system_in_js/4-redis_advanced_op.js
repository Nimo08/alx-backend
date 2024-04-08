import redis from 'redis';

const client = redis.createClient();

const hashKey = 'HolbertonSchools';
const hashValue = {
    Portland: '50',
    Seattle: '80',
    'New York': '20',
    Bogota: '20',
    Cali: '40',
    Paris: '2',
}
for (const field in hashValue) {
    client.hset(hashKey, field, hashValue[field], redis.print);

}
client.hgetall(hashKey, (err, reply) => {
    if (err) {
        console.error(err);
    } else {
        console.log(reply);
    }
})
