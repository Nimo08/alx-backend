import express from 'express';
import redis from 'redis';
import { promisify } from 'util';
import kue from 'kue';


const redisClient = redis.createClient();


const setAsync = promisify(redisClient.set).bind(redisClient);
const getAsync = promisify(redisClient.get).bind(redisClient);

const queue = kue.createQueue();


const app = express();
const port = 1245;


let numberOfAvailableSeats = 50;


let reservationEnabled = true;


async function reserveSeat(number) {
    await setAsync('available_seats', number);
}


async function getCurrentAvailableSeats() {
    const seats = await getAsync('available_seats');
    return parseInt(seats);
}


app.get('/available_seats', async (req, res) => {
    res.json({ numberOfAvailableSeats });
});


app.get('/reserve_seat', async (req, res) => {
    if (!reservationEnabled) {
        return res.json({ status: "Reservation are blocked" });
    }

    const job = queue.create('reserve_seat').save((err) => {
        if (err) {
            return res.json({ status: "Reservation failed" });
        }
        return res.json({ status: "Reservation in process" });
    });

    job.on('complete', (result) => {
        console.log(`Seat reservation job ${job.id} completed`);
    });

    job.on('failed', (err) => {
        console.error(`Seat reservation job ${job.id} failed: ${err}`);
    });
});


app.get('/process', async (req, res) => {
    res.json({ status: "Queue processing" });


    queue.process('reserve_seat', async (job, done) => {
        const availableSeats = await getCurrentAvailableSeats();
        if (availableSeats === 0) {
            reservationEnabled = false;
            done(new Error('Not enough seats available'));
        } else {
            await reserveSeat(availableSeats - 1);
            done();
        }
    });
});


app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
