!!! warning

    These notes are a work-in-progress.
    This functionality is in limited release and subject to change. 

## Audience

This documentation is aimed at researchers who want feedback on the performance of their job requests, as well as the performance context in which their job requests happen (i.e. was the server busy or quiet at the time).

## Timings

Basic timing information is available from job and job request detail pages, for example:

![Timings for job request 8676](images/job_request_8676_timings.png)

The runtime for a job request is the combined runtime for all completed jobs of a job request, i.e. the runtime of each completed job is added together.

## Monitoring

### Background information

We monitor jobs indirectly. Every 30 seconds or so the job-runner sends a status update to the job-server for each currently running job. These status updates are used to display the current status in job-server and also sent to Honeycomb which allows us to explore the history of a job. 

On important thing to note is that, because a job_request can contain multiple jobs, if one job from a job_request completes successfully, it currently continues to send "success" status until all jobs from that job_request have completed. These can cause some unexpected effects in our visualisations.

Current limitations of the monitoring system:

* we can only display one visualisation per window
* we cannot embed visualisations in the job server pages
* we cannot pre-highlight one particular job/job_request in a visualisation of multiple jobs/job_requests
* time is generally always displayed in seconds (e.g. 500k seconds ~= 138hrs ~= 5.8days)


### Performance questions

#### Queueing time

We can visualise how long a job was queued for with the "This job request" link. This will show the honeycomb events for this specific job request, grouped by the reported status of the job. Nb. The height of the graph relates only to the number of reports from the job-runner to the job-server, so does not tell us anything about the job request itself.

For example, [job request 7254](https://jobs.opensafely.org/qmul/bmi-and-hba1c/bmi_and_hba1c/7254/) queued from the 27th April 2022 until the 3rd of May 2022, as we can see in this visualisation:
![Monitoring report for job request 7254](images/qmul_bmi-and-hba1c_bmi_and_hba1c_7254.png)

In comparison, [job request 7652](https://jobs.opensafely.org/university-of-nottingham/postopcovid/postopcovid/7652/) did not queue at all:
![Monitoring report for job request 7652](images/university-of-nottingham_postopcovid_postopcovid_7652.png)
