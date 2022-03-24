## How to ask for a review

GitHub has a feature built into the workflow that allows easy code review with collaborators, and we would recommend 
that you use this tool. GitHub has some [documentation on pull requests and code reviews](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-request-reviews) which we recommend for background reading.

![An example of GitHub's pull request feature.](./images/code-review-main.png)

In this screenshot, the user is making a new pull request. In the top right-hand corner (marked by the
red box), there is a tagging function under Reviewers where you can search or select collaborators to do a code review. 
Once you have tagged them and made the pull request, the person will receive a notification to their
email, and it will also come up in the pull request section of their GitHub main screen.

![An example of a pull request description as shown on GitHub.](./images/pr-desc.png)

It is strongly encouraged to add some information to 
your request to aid the reviewer. 
 
## How can I write a good pull request?

Some best practice gathered from current users of OpenSAFELY are described below:

 - Thinking about the purpose of the review can be helpful as this may
vary from review to review. For example, are you looking for a check of the implementation of the logic or methods
outlined in the protocol (in which case, linking the protocol can aid this), or are you looking for a
review of how well you document your code and if it is clear and understandable? Being transparent
will help your reviewer do a better job quicker.
- Good descriptive names for pull requests and commits help the reviewer follow the logic of the code and the changes made (see example of commits below).
- Multiple smaller pull requests are easier than one large.
- Code comments and documentations make the logic easier to follow.
- Naming the order of the files, for example, `01_Data_Extraction.py`, `02_Data_Cleaning.py`, etc.
- Allow sufficient time for the review.

### Examples of good commit messages
![An example of a good commit message as shown on GitHub.](./images/good-pr-pic.png)

## How can I be a good reviewer?
Some best practices gathered from current users of OpenSAFELY are described below:

- Code review should be a collaborative conversation and don't be afraid to check assumptions or clarify intentions within the review (you can add messages to the end of the review request).
- Actionable feedback with suggestions is helpful.
- It can be helpful to highlight the levels of code review comments. For example,
if something is nice-to-have-but-not-important, you can prefix it with `Nit:`. For example,
`Nit: I think this would be cleared if you didn't use an underscore in this variable name`
- Being clear about what exactly you have reviewed or how thorough the review was - for example, being clear if you read through the code but did not run it (and therefore may miss running errors in implementation). Unit tests should catch that the code is runnable, but will not necessarily check it is correct.
- Answer specific questions in the review request.
- Avoiding jabs on coding style.
- Being clear if you do not have time to do a thorough review.

## What actions can we take as a team to encourage code reviews?

- Those in leadership roles should volunteer their time do code reviews, or help find code reviewers, to help embed the culture of code-reviews widely.
- New projects can have a "buddy" who can help to review the code, and means they will be familiar with the protocol and code changes from the start.

