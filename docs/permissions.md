# Permissions in OpenSAFELY

After the data controller has [approved your project](https://www.opensafely.org/onboarding-new-users/), we will add any Github usernames listed in your approval to our `opensafely` Github organisation.  We also will transfer your existing OpenSAFELY study repository (if you have one) into the same organisation. This allows OpenSAFELY to enforce certain security standards, such as [multi-factor authentication](https://docs.github.com/en/github/authenticating-to-github/securing-your-account-with-two-factor-authentication-2fa).

Additionally, the OpenSAFELY framework requires a user to be a member of the `opensafely` Github organisation in order to [run jobs in the secure backends](job-server.md).

## Adding collaborators

While your repository is private, you may need to add new collaborators who are not named in your original application. Any new collaborators have the same information governance obligations as the original study authors, and must therefore sign the same access agreements; please send any such requests to [team@opensafely.org](mailto:team@opensafely.org).


## Project Member Management

When they are approved to use the platform, every OpenSAFELY user is assigned roles that define what they are permitted to do.
By default, most researchers using the platform will have the **ProjectDeveloper** role, which permits them to:

* create workspaces
* run jobs
* cancel jobs
* view job outputs
* publish draft outputs

Additionally, users with the **ProjectCoordinator** role can:

* Invite users to a project, with the desired roles
* Modify roles for any existing members of a project
* Remove members from a project


## Releasing Outputs

!!! note
    Releasing of outputs to the job server is currently being rolled out.
    See [team manual](https://bennettinstitute-team-manual.pages.dev/tech-team/playbooks/job-server-releasing-outputs/) for instructions on setting up a user.
    The new release process is described separately in [Google Docs](https://docs.google.com/document/d/1PSzMoCFov2olJpxrFGT1DccWUqGDA67mUvPIyIhOcew/edit#heading=h.aokkzsfuxo4n).


For releasing outputs we have some additional roles:

**ProjectCollaborator:**

* View released outputs
* View draft published outputs

**OutputChecker:**

* Release outputs from Level 4 environments
* Delete outputs in a release

**OutputPublisher:**

* Confirm publication of outputs

---8<-- 'includes/glossary.md'
