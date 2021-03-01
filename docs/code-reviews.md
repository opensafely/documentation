## What is a code review?

A code review is a critical quality assurance practice. It involves systematically
checking a fellow programmer's (or researcher's) code for errors or possible 
improvements. 

It is an everyday activity in the software development world and improves
both quality and speed in programming. 

## How to ask for a review

Github has a feature built into the workflow that allows easy code review with collaborators, and we would recommend 
that you use this tool. 

In this screenshot, the user is making a new Pull Request. In the top right-hand corner, marked by the 
red box, there is a tagging function when you can search or select collaborators to do a code review. 
Once you have tagged them and made the Pull Request, the person will receive a notification to their 
email, and it will also come up in the Pull Request section of their Github main screen. 

Whilst this is minimum for requesting a review, it is strongly encouraged to add some information to 
your request to aid the reviewer. Thinking about the purpose of the review can be helpful as this may 
vary from review to review. Naming the pull request something informative and useful is a good start, 
and even better is filling in the textbox of the Pull Request with information about what you are 
seeking. For example, are you looking for a check of the implementation of the logic or methods 
outlined in the protocol (in which case, linking the protocol can aid this), or are you looking for a 
review of how well you document your code and if it is clear and understandable? Being transparent 
will help your reviewer do a better job quicker. 
 
## When to ask for Code Review?
This question's answer will vary from user to user, but it is most useful with every change to the code. In fact, when we surveyed the OpenSAFELY team, most people reported they would like reviews to be as frequent as possible. A good way of conceptualising when to ask for a review is to think about commits and branches. A user makes a branch to change a feature or adding some new analysis, and while making that change, they do several commits to the new branch. When the time comes to merge this back to master, there is a natural inflexion point to do a code review. When you are making a Pull Request, you can tag a reviewer easily. 

Merging a new branch should not be your only trigger for a review. If you are stuck or unsure what direction to take, a code review can clarify what path to take. In general, the more frequent the reviews, the better quality the code tends to be. 

## How can I be a good review-ee?
Experiences of reviewing were gathered during the code review survey, and some best practices are listed below. 

- Good descriptive names for Pull Requests and commits help the reviewer follow the logic of the code and the changes made
- A clear description of the expectations of the review is helpful, for example, are you expected to run the code or just review it in the browser?
- Multiple smaller Pull Requests are easier than one large 
- Code comments and documentations make the logic easier to follow 
- Naming the order of the files, for example, `01_Data_Extraction.py`, `02_Data_Cleaning.py`, etc. 


## How can I be a good reviewer?
A survey of the OpenSAFELY team about code reviewers revealed some excellent practices for going forward, and adopting these as a team will improve our overall reviewing procedure and quality. 

- Code review should be a collaborative conversation and don't be afraid to check assumptions or clarify intentions within the review (you can add messages to the end of the review request). 
- Actionable feedback with suggestions is helpful. 
- Being clear about what exactly you have reviewed or how thorough the review was—for example, being clear if you read through the code but did not run it (and therefore may miss running errors). 
- Answer specific questions in the review request.
- Avoiding jabs on coding style. 
- Being clear if you do not have time to do a thorough review 

## Team Suggestions
These suggestions again come from the team survey and various conversations within the team. 

Code reviews should be normalised within the team by the PIs or team leads by offers to review code where possible or to identify like reviewers. 
New projects can have a "buddy" who can help to review the code, and means they will be familiar with the protocol and code changes from the start
Multiple reviewers can be helpful 
Code comments and good documentation with linked protocols speed everything up.