All outputs from OpenSAFELY pipelines are subject to [tiered levels of scrutiny](security-levels.md), to provide assurance that identifiable data is not leaked accidentally, or maliciously.

The final tier is review of so-called "Level 4" outputs, where the OpenSAFELY framework stores outputs labelled as `moderately_sensitive` in the `project.yaml` file.

If you have Level 4 access you can log in and review your aggregated results, and perform any necessary redactions before requesting files to be released. 
You will find your files to review in `D:\Level4Files\workspaces\<workspacename>`.

!!! note

    **Mac users**

    If intending to use a Mac for Level 4 access, please check your
    hardware is suitable first.

    Level 4 access requires a working Windows installation. Mac users
    with older *Intel* hardware have had success in accessing Level 4
    when running Windows in a virtual machine.

    However, Mac users with newer Macs that have *Apple* processors —
    for example, the M1 processor — can only run Windows in a virtual
    machine via the Windows on ARM release: **this configuration is
    currently incompatible with the client necessary for Level 4
    access.**

    Macs with Apple processors are still suitable for writing, testing
    and submitting OpenSAFELY code to be run on the secure server.
    **This issue only affects access to Level 4 server.**

    See [this support
    discussion](https://github.com/opensafely/documentation/discussions/251#discussioncomment-1767887)
    for a description of the problem.

Level 4 outputs **can only be released by specific members of the OpenSAFELY team**. When you are ready to request a release of your aggregated results, and only the minimum outputs necessary (for which you have also applied any necessary disclosure controls, such as small number suppression) **please [complete this form](documents/OpenSAFELY_Output_Review_Form_15_11_21.docx) and email us at <datarelease@opensafely.org>**.

!!! warning
    ** Data may only be shared with individuals without Level 4 access after they have been released outside of the secure area. You MUST NOT screen share (or share via any other means) any results that have not been released through the official process.**

!!! warning
    ** DO NOT release your aggregated study results to your GitHub repository yourself (unless you have been given permission by OpenSAFELY).**

!!! note
    Individual researchers who have Level 4 access have responsibility for redacting sensitive information, or choosing not to publish it at all. The study author should do everything they can to make this easy; for example, carrying out low number suppression automatically, documenting code clearly, and only selecting essential items for publication when deciding what to label as `moderately_sensitive`. The researcher must ensure that their release request adheres to the [Permitted Study Results Policy](https://www.opensafely.org/policies-for-researchers/#permitted-study-results-policy). This policy is subject to change and so must be checked before every request for release."
    
TIP: Our resources for checking outputs are not unlimited, therefore it is advised to ensure you have all of your outputs ready at the same time for your project (or its current phase) so they can be reviewed together. Another reason to ensure your analyses are complete is that re-running your study definition a short time later (e.g. to create an additional variable) may produce small differences in the previous results, e.g. due to movement of patients or codes added retrospectively to patient records. If you have already released similar results, any small changes in new outputs may be subject to small number suppresion which may prevent the new outputs being released at all. (One solution to minimise this issue is to round all of your results, e.g. to the nearest 5). 

Once released, your results will be available in a new branch (`release-candidates`). This branch should be merged into `main`. A new branch of the same name will be created with any further releases so there is no need to keep the branch open.

## How output checkers release files

Outputs are reviewed and approved on the secure servers, using a command-line tool. This can only be done by users with the [`OutputChecker` role](permissions.md). Approved users can request to access [the work-in-progress documentation here](https://docs.google.com/document/d/16E-TBeK19njc5-SfvWG60AihmpieIscCm_kFG7JeeP8/edit).

## Disclosivity checks and redaction

Work through the moderately sensitive files in the workspace folder systematically to identify any tables, figures, and other outputted text and objects that may be a disclosure risk. 
**The general principle is that any statistic describing 5 or fewer patients, either directly or indirectly, should be redacted**.
For example: 

  * Frequency tables containing counts between 1-5 should be redacted. The whole table, or at a minimum multiple rows within the table, should be redacted because values removed by single cell (or row, or column) redaction could be inferred from unredacted values. 
  * Summaries of numeric variables describing 5 or fewer patients should be redacted. 
  * Graphical figures whose underlying values describe 5 or fewer patients should be redacted. Figures which include print-outs of patient counts (such as KM plots) should be checked and redacted. 
  * Counts of zero can be retained. 
  * Other outputs, such as log files that reveal information about the underlying data, should also be checked and redacted if necessary. **It is very unlikely that outputs such as log files should be required for publication outside the secure environment.**

Where possible it should be clear what has been redacted, so for example do not redact table titles and category names. 
By convention redactions take the form `[REDACTED]` to make redacted elements easier to search for.
	
Ideally there shouldn't be any files in the folder that are not intended for release (whether potentially disclosive or not) as these should have been removed by the analysis scripts or placed elsewhere. 
If they are there, delete them.

This current approach to disclosure control is conservative and deliberately reduces the need for judgement calls. 
It may be possible for exceptions to be made if they can be justified as being both analytically necessary and definitely non-disclosive. This must be discussed with the OpenSAFELY team.

**If you are unsure about anything, please email us: <disclosurecontrol@opensafely.org>.**

## Redaction data breaches and how to recover from them

### The issues

One of the great strengths of using git is that it is easy to recreate the contents of any file in the repository exactly as it appeared at any point in the repository's stored history. However, this means that if any sensitive data is inadvertently committed to a repository, we need to be careful to completely remove that data from the history.

Access to `output-publisher` repositories is intended to be restricted, and their histories are not transferred to study repos in the release process. However, study repos are intended to eventually become public, so if sensitive data is committed then care should be taken to fully clean up. From the moment that the `osrelease` command is run in an `output-publisher` repo, we need to be careful with the study repo's git history.

For example, if sensitive data was committed to a study repo, it is explicitly not safe to use either git's `revert` command, or to delete the file and commit the deletion. Both of these methods would leave the commit containing the sensitive data in the history of the git repository - and would be trivial for anyone to recover in the future.

Another aspect of git is that it uses a decentralised model. This means that everyone that has a copy of a git repository has their own copy of the entire history. So, if there is a sensitive data leak, it is not sufficient to clean just your own copy of the git history & the history on GitHub, you should also clean the git histories of all other copies.

## What to do if you find a data breach

If you discover files in a study repository that have been insufficiently redacted and still contain sensitive information, you should immediately contact and email the following (providing as much information as possible): Amir Mehrkar (<amir.mehrkar@phc.ox.ac.uk>); Ben Goldacre (<ben.goldacre@phc.ox.ac.uk>); <disclosurecontrol@opensafely.org>.

If you are able, you can attempt to make the repository safe by temporarily restricting access to it. For instance, if the repository is public (accessible to the world), make it private (accessible only to the OpenSAFELY team). If the repository has external contributors that are not authorised to handle sensitive data, consider temporarily removing their access to the repository. This will reduce the scope for harm until the sensitive information can be removed from the repository.

If you are an author of the study, you should also liaise with an engineer from the OpenSAFELY team as soon as possible to safely clean the sensitive information from the repository. Depending on the exact situation this may be relatively straightforward or relatively complicated. You should also attempt to trace all copies of the repository for cleaning or deletion.

---8<-- 'includes/glossary.md'
