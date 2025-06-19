## What is GitHub Codespaces?

[Codespaces](https://github.com/features/codespaces) is a coding environment
hosted online by GitHub.
Codespaces can be accessed via your web browser
without any additional installation.

A codespace provides:

* a "virtual machine" — a computer running as software inside *another* computer
  — that is hosted by GitHub
* a Visual Studio Code environment
  for editing your project and running commands

When you open a codespace in browser,
you get access to the Visual Studio Code environment.
Through that interface,
you can run commands inside the codespace's virtual machine.
This is just as if it were a real desktop or laptop that you were working on,
except this virtual machines has been configured for OpenSAFELY use.

The OpenSAFELY research template contains a GitHub Codespaces configuration
to allow you to run OpenSAFELY
**without any installation required on your own computer**.

This removes the need to have anything other than a web browser installed
to work on OpenSAFELY projects.

These cloud-hosted virtual machines have no persistent storage,
which is to say any data on them will be lost when the machine is deleted
if not saved elsewhere.
Codespaces are primarily designed for writing code
(such as an OpenSAFELY study)
and are tightly integrated with GitHub,
making it easy to commit and push your work to GitHub avoiding any data loss.

## Understanding GitHub Codespaces billing

Anyone working on a repository in the GitHub `opensafely` organization can use Codespaces free of charge.

If you use Codespaces for a repository that is not in the `opensafely` organization, then you may receive a message from GitHub about billing. Codespaces is a paid-for product, however GitHub gives all users a decent-sized free monthly allowance. You will not be charged unless you have provided GitHub with a payment method and set a Codespaces spending limit. GitHub's documentation on [billing](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces) has more information.
