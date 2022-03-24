## What is a code review?

A code review is a critical quality assurance practice. It involves systematically
checking a fellow programmer's (or researcher's) code for potential errors or possible 
improvements. 

It is an everyday activity in the software development world and improves
both quality and speed in programming. Code reviews also offer opportunities for both code author and code reviewer to learn from each other. Code reviews are standard practice within OpenSAFELY studies and the default should be to always get your code reviewed.

## When to ask for code review?

Code reviews should be the default. A good way of conceptualising when to ask for a review is to think about commits and branches. All your work should be done in branches and you should aim to 
merge your branches frequently. A user makes a branch to change a feature or adding some new analysis and make several commits to the new branch. When the time comes to merge this back to main, there is a natural inflexion point to do a code review, and each merge should be 
accompanied with a code review. If you are in a hurry, and no-one has time to do a more thorough 
code review, bear in mind that even a cursory code review is better than no code review. 

Merging a new branch should not be your only trigger for a review. If you are stuck or unsure what direction to take, a code review can clarify what path to take. In general, the more frequent the reviews, the better quality the code tends to be. 
