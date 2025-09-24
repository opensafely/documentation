## How can I be a good reviewer?

### How to perform a code review

Each code review might differ in precisely how it is carried out.
You should use your own best judgement when reviewing to consider *what* should be reviewed and *how*.

!!! note
    Google have some [useful question prompts](https://google.github.io/eng-practices/review/reviewer/looking-for.html) for reviewers to consider. "CL" in that document means "changelist": you can think of "pull request" in place of "changelist".

#### Resources you have available to you to evaluate the changes

* The code itself, including any comments.
  The changes should typically usually be examined by the reviewer.
    * For more complex changes, you may want to review the changes commit-by-commit:
      the Commits tab on the pull request allows you to see view each commit in turn.
    * For very extensive changes, it may not be practical to review all the changes;
      for example, when automated tools change formatting that are not practical to review line-by-line manually.
* Commit messages the author has written.
  These may give extra context for the reasoning behind changes.
* Comments made in any GitHub issue threads associated with the pull request,
  or the pull request itself.
* Running the code to see if the changes do what they claim.
* Checking there are no newly failing tests because of the new changes.
    * In well-organised projects, there should be automated checks on GitHub that run the tests without you needing to run them manually.

#### Some suggestions from current users of OpenSAFELY

- Code review should be a collaborative conversation.
  Don't be afraid to check assumptions or clarify intentions within the review.
  You can add messages to the end of the review request.
- Actionable feedback with suggestions is helpful.
- It can be helpful to highlight the levels of code review comments.
  If something is nice-to-have-but-not-important,
  you can prefix it with `Nit:`.
  For example, "Nit: I think this would be cleared if you didn't use an underscore in this variable name".
- Being clear about what exactly you have reviewed or how thorough the review was.
  For example, being clear that you read through the code but did not run it
  (and therefore may miss running errors in implementation).
  Unit tests should catch that the code is runnable,
  but will not necessarily check it is correct.
- Answer specific questions in the review request.
- Avoiding jabs on coding style.
- Being clear if you do not have time to do a thorough review.
