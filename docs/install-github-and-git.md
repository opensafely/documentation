OpenSAFELY uses [**GitHub**](https://github.com/) to store the code used to create and analyse the study data.
GitHub is based on [**git**](https://git-scm.com/), an industry-standard version control system that helps multiple contributors manage and share code effectively.
GitHub also supports convenient publication of your code, so that anybody can view it, comment on it, and use it themselves.
We require that anyone who uses OpenSAFELY publish their code on publication of their papers.

A good starting point for understanding version control in the context of scientific research has been written by The Turing Way collaborative.
If you are completely new to these concepts or want to understand more then we suggest reading through their [chapter on version control](https://the-turing-way.netlify.app/reproducible-research/vcs.html).

To get set up, you will need:

* A [**GitHub**](https://github.com/) account
* [**git**](https://git-scm.com/) installed on your local machine


## New to git
For Windows or macOS users new to git, [**GitHub Desktop**](https://desktop.github.com/) provides a useful GUI for editing files and gitting.
To install GitHub Desktop, visit the [GitHub Desktop homepage](https://desktop.github.com/) and click install for your operating system.
Once installed, it will ask you to create or sign-in to your GitHub account.
Follow the instructions as appropriate.

Once signed in, you'll be taken to a _Let's get started_ page.
Note, you'll still need to install the [command line version of git](https://git-scm.com/) alongside GitHub Desktop, as well as the other OpenSAFELY requirements, before diving in.

## Old to git
If you already have git installed and prefer using your existing git workflow, then this is fine.

If you're not sure if you already have git installed, type `git --version` into any command line terminal.

## Creating a GitHub account

### Via GitHub's site (recommended)

It is possible to sign up on GitHub's site
as mentioned in the [Getting Started tutorial](getting-started/tutorial/create-a-github-account/index.md).

### Via GitHub Desktop

If you [install GitHub Desktop](https://desktop.github.com/), the
GitHub Desktop installation process will also walk you through the
process of creating an account, if you don't already have one.

If you already have a GitHub account, GitHub have guides on
authenticating an existing account with [GitHub
Desktop](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/installing-and-authenticating-to-github-desktop/authenticating-to-github).

(If you already have `git` configured and are reasonably confident using
it, GitHub Desktop is not required. You need to be able to `clone` the
template repository that you will create, then `add`, `commit` and
`push` changes to that repository to GitHub.)

## Access to the [OpenSAFELY GitHub organisation](https://github.com/opensafely)
This is only necessary for running code against the real data. **Ask us for access.**
If you're not sure if you already have access, go to [*Settings > Organizations*](https://github.com/settings/organizations) in GitHub and see if `opensafely` is listed.

You will need [**two-factor authentication (2FA)**](https://help.github.com/en/github/authenticating-to-github/securing-your-account-with-two-factor-authentication-2fa) for your GitHub account to join the organisation. This provides extra security for your account by requiring something you have (for example, an authenticator application on your phone) as well as something you know (your password).

To set up 2FA, [follow these instructions](https://help.github.com/en/github/authenticating-to-github/configuring-two-factor-authentication).
If you're not sure if you already have 2FA enabled, go to [*Settings > Security > Two-factor authentication*](https://github.com/settings/security) in GitHub and check that at least one method is *Configured*.



---8<-- 'includes/glossary.md'
