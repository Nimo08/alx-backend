import kue from 'kue';

const blocked  = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
    job.progress(0, 100);
    if (blocked.includes(phoneNumber)) {
        const errMessage = `Phone number ${phoneNumber} is blacklisted`;
        done(new Error(errMessage));
    } else {
        job.progress(50, 100);
        console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
        setTimeout(() => {
            done();
        }, 2000);
    }
}

const queue = kue.createQueue({
    concurrency: 2
});
queue.process('push_notification_code_2', (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
})
