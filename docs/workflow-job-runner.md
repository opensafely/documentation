Analysis scripts are submitted to the server via the job server website at [https://jobs.opensafely.org](https://jobs.opensafely.org).

Here you select a repo+branch, a set of actions to run (definined in the project pipeline), and the back-end you want to run against.

The Job Runner will take care of the rest.  Errors are reported back; however, to avoid disclosure of potentially-senitive information, some kinds of errors are redacted. In these cases you will need to access a secure server to review the log files (or ask someone to do this for you).

The job runner will produce the desired outputs on the secure server, which must be reviewed before release via GitHub.

See the [Project Pipelines section](pipelines.md) for more details of how actions are run, and how outputs are defined.

---8<-- 'includes/glossary.md'
