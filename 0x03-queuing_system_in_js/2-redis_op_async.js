import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const readFileAsync = promisify(client.get).bind(client);

client.on('connect', () => {
    console.log('Redis client connected to the server');
})
client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
})

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
    try {
        const value = await readFileAsync(schoolName);
        console.log(value);
    } catch (error) {
        console.error(error);
    }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
