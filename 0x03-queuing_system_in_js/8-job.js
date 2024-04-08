import kue from 'kue';

export default function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }
    jobs.forEach((jobData) => {
        const job = queue.create('push_notification_code_3', jobData).save((err) => {
            if (err) {
                console.error(err);
            } else {
                console.log(`Notification job created: ${job.id}`)
            }
        })
        job.on('complete', () => {
            console.log(`Notification job ${job.id} completed`);
        })
        job.on('failed', (err) => {
            console.error(`Notification job ${job.id} failed: ${err}`);
        })
        job.on('progress', (progress) => {
            console.log(`Notification job ${job.id} ${progress}% complete`)
        })
    })
}
