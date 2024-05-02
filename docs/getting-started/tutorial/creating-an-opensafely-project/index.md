## Running OpenSAFELY

## 8. Next steps

Congratulations! You've covered all the basics that you need to develop a study
on your own computer, verify that it can run against real data, and publish it
to GitHub.

To write a real study and run it against actual patient data, you will first need to get permission for your project from the data controllers for the NHS England OpenSAFELY COVID-19 service.
[Read about our pilot onboarding programme](https://www.opensafely.org/onboarding-new-users/).
Once approved, your GitHub user account will be added to our `opensafely` GitHub organisation, along with your study repository, which gives you the ability to run your study against real data. [Read more about permissions](../../../jobs-site.md#permissions).

In the meantime, take a look at the rest of our documentation for more
detail on the subjects covered in this tutorial. For example:

* There is a more complete [guide to the OpenSAFELY command-line
  tool](../../../opensafely-cli.md).
* The [ehrQL documentation](../../../ehrql/index.md) contains a tutorial for ehrQL,
  as well as a complete [schema reference](../../../ehrql/reference/schemas.md).
* You'll find more information about the contents of `project.yaml` in the
  [Actions reference](../../../actions-intro.md).
* OpenSAFELY walkthroughs (see [this notebook](https://github.com/opensafely/os-demo-research#opensafely-demo-materials))
  to guide you through the platform workflow on your own computer with dummy data, rather than using the documentation pages alone
* There is a final step we've not described here: [a
  website](https://jobs.opensafely.org/) called the ["OpenSAFELY Job
  Server"](../../../jobs-site.md) where you can submit your repository actions to be run
  automatically within the secure EHR vendor environments. Right now you can
  only use this to run real jobs, but we're working on adding the ability to
  test your repository against dummy data.
* You'll be using `git` and GitHub a lot, and it's a critical but complex part
  of the OpenSAFELY ecosystem. If you're not familiar with these concepts, it's
  a good idea to read our [git workflow page](../../../git-workflow.md) and its linked content.
