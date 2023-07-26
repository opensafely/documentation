!!! warning

    These notes are a work-in-progress.
    This page provides an overview as guidance only,
    and not a series of definite instructions.
    We plan to further expand on this information.

## Audience

This page is aimed at people who want to run their own installation of OpenSAFELY
as a proof-of-concept trial prior to integrating into the live system.

These people are likely to have one of the following professional roles:

* software developers
* clinical data providers
* system integrators

### Assumed knowledge

It is taken that you have some familiarity with OpenSAFELY.

If not, you should first refer to:

* [this general overview of OpenSAFELY](https://www.opensafely.org/about/)
* [the typical researcher workflow](workflow.md)
* [the introductory tutorial](getting-started.md)

## Software components

The [OpenSAFELY technical architecture diagram](technical-architecture.md) shows all of the platform software components
and how they interact.

The specific steps required to create a minimal setup are:

1. Deploy a [*job runner*](https://github.com/opensafely-core/job-runner) within your secure environment.
   A minimal configuration simply runs Docker containers
   and stores any resulting container output on a local disk.

2. Deploy a [*job server*](https://github.com/opensafely-core/job-server)
   that the *job runner* polls for jobs that end users request to be run.

     It is possible to use our existing instance of this server at our [*jobs site*](https://jobs.opensafely.org);
     [contact us](how-to-get-help.md#data-providers)
     if you would like us to configure this for you.

3. Create a secure network with our [*GitHub proxy*](https://github.com/opensafely-core/proxy).
   This provides access to repositories with research study code to run
   and Docker images used to run the code.

4. To provide *access to your database* from within your setup,
   integrate into our [*cohort-extractor*](https://github.com/opensafely-core/cohort-extractor) ETL tool:

     * via an implementation of a backend interface; [this is an example for TPP](https://github.com/opensafely-core/cohort-extractor/blob/main/cohortextractor/tpp_backend.py)
     * and, if you are using an as-yet unsupported database, a database connector

    !!! warning

        A simpler replacement for cohort-extractor,
        [ehrQL](https://github.com/opensafely-core/ehrql),
        is in development.

        You may prefer to wait for a stable version of ehrQL
        before attempting to integrate.

5. *Releasing job outputs* requires:

     * the [*release-hatch*](https://github.com/opensafely-core/release-hatch) tool for reviewing outputs
     * the [*output-publisher*](https://github.com/opensafely-core/output-publisher) tool for publishing outputs

### Deployment

We use Ubuntu in our deployments.
Our deployments use [deploy scripts](https://github.com/opensafely-core/backend-server)
that you can refer to.

## Support

See our [support page](how-to-get-help.md#data-providers-and-system-integrators)
for details of how to get more assistance on integration.

---8<-- 'includes/glossary.md'
