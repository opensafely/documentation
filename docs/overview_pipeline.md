# Workflow Overview
The process of conducting an analysis via OpenSAFELY can be broken down into the following steps:

1. Design a study protocol with a clear research question. The protocol are discussed and written 
(preferably in a google document so multiple authors can edit and review)
2. Institutional Ethics Approval once protocol is finalised.
3. Create a study-specific repository from the template provided, and upload the protocol to the repository. This provides
a version control of a protocol. 
4. Codelists that do not exist already are developed and put onto the opencodelist webpage
5. Study population and study variables are defined within a Python script that is developed locally (i.e on your machine) and uploaded to Github for comments, reviews, and other contributions. This process is iterative.
6. When the study definition script is “run” on a local computer, it creates a dummy dataset which approximates 
the structure of the source data. This dummy dataset has all the necessary covariates, as specified in your 
study definition script, with the right type of data (for example numbers, dates or count variables) 
(but currently does not respect expected between-variable relationships such as metformin 
prescriptions only for people with diabetes).
7. Analytic code is developed against this dummy dataset. This can be using Stata, R or Python. As part of this, 
researchers must highlight which files they will need access to and mark each file with a security-risk level.
8. All code needs to be pushed to the corresponding research repo. It must pass some basic checks such as 
pre-configured unit tests and be subject to code review before merging with master branch. 
8. Once the analytic code and the study population code is finalised and uploaded to GitHub, the code is deployed and 
executed securely by requesting a run in the [OpenSAFELY Job server](job_server.md). 
The real study population is extracted, and the analytic code run.
9. Analytic output files earmarked for publication (e.g.log files, PDFs, notebooks, graphics) are reviewed by 
authorised users on the review server and any sensitive data is removed.
10. Summary results are returned to the external researcher via GitHub and can be reviewed by the team.
