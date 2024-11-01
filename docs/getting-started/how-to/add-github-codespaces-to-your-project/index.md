This page describes how to add GitHub Codespaces to your project.

!!! warning
    Codespaces are automatically deleted after a period of inactivity and any changes not pushed to the GitHub repo will be lost.
    For the `opensafely` organization,
    this period is 30 days.

## Does your project already have GitHub Codespaces?

Newer projects already have GitHub Codespaces.
However, older projects don't.
To find out whether your project is newer or older:

* Click on your project in the [opensafely](https://github.com/opensafely) organisation on GitHub.
* Can you see a `.devcontainer` folder?
  If not, then your project is **older**.
* Click on the `.devcontainer` folder to open it.
* Click on the `devcontainer.json` file to open it.
* Can you see the following line towards the top of the file?
  If not, then your project is **older**.
  ```json
  "image": "ghcr.io/opensafely-core/research-template:v0",
  ```
* If you've got this far, then your project is **newer**.

## Adding GitHub Codespaces to your project

We will use Git to add GitHub Codespaces to your project.
There are many ways to use Git.
For example, we could use Git with the `git` command-line tool, with GitHub Desktop, or with VS Code.
Here, we will use Git with `git`, because `git` commands are succinct.
The documentation for
[GitHub Desktop](https://docs.github.com/en/desktop) and
[VS Code](https://code.visualstudio.com/docs/sourcecontrol/overview)
describes how to translate `git` commands into equivalent user-interface commands.

Here, you will run `git` commands on your computer.

### Identify your project's working branch

The *working branch* contains work that is "done".
It is often called `main` and it is often associated with a workspace on OS Jobs.

We will add GitHub Codespaces to the working branch.

### Create a new branch

Switch to the working branch:

```sh
git switch <working branch>
```

Create a new branch called `github-codespaces`:

```sh
git switch --create=github-codespaces
```

### Copy files

* Visit the [opensafely/research-template](https://github.com/opensafely/research-template) project on GitHub.
* Click on the `.devcontainer` folder to open it.
* Click on the first file to open it.
* Click on "Download raw file" (![The "Download raw file" icon](download_raw_file.png)) to download the first file to your computer.
* Repeat for the remaining files.
* Copy each file to the `.devcontainer` folder in your project.

!!! warn "Dotfiles"
    Dotfiles are files and folders that start with a dot (`.`).
    Many tools for browsing files and folders,
    such as File Explorer on Windows or Finder on macOS,
    hide dotfiles by default, so as not to clutter the display.

!!! info "My project doesn't have a `.devcontainer` folder"
    If your project doesn't have a `.devcontainer` folder,
    then create one.
    It's important that it starts with a dot (`.`).

### Update `.gitignore`

* Visit the [opensafely/research-template](https://github.com/opensafely/research-template) project on GitHub.
* Click on the `.gitignore` file to open it.
* Use your preferred text editor to open the `.gitignore` in your project ready for updating.
* Copy the contents of the `.gitignore` from the `research-template` repository,
  and paste them into your text editor,
  replacing the previously existing contents of your `.gitignore` entirely.
* Your project's `.gitignore` should look identical to the `.gitignore` in the `research-template`.
* Save your project's updated `.gitignore`.

### Add, commit, and push

Add and commit the files you copied in the previous step:

```sh
git add .
git commit --message="Add GitHub Codespaces"
```

Push to GitHub:

```sh
git push --set-upstream
```

### Create a pull request

* Click on your project in the [opensafely](https://github.com/opensafely) organisation on GitHub.
* Click on "Pull requests".
* Click on "New pull request".
* Beneath "Compare changes" there are two boxes labelled "base" and "compare".
    * The "base" box should contain the name of the working branch.
    * The "compare" box should contain `github-codespaces`.
* Click on "Create pull request".

### Approve and merge the pull request

* Click on "Files changed"
* Click on "Review changes"
* Click on "Approve"
* Click on "Submit review"
* Click on "Merge pull request"

### Housekeeping

Switch to the working branch:

```sh
git switch <working branch>
```

Pull from GitHub:

```sh
git pull
```

Delete the `github-codespaces` branch:

```sh
git branch --delete github-codespaces
```

### Start a Codespace

The
"[How to use GitHub Codespaces in your project](../use-github-codespaces-in-your-project/index.md)"
page has more information about using GitHub Codespaces in your project,
including how to start a Codespace :rocket:.
