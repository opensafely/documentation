All outputs from OpenSAFELY pipelines are subject to [tiered levels of scrutiny](security-levels.md), to provide assurance that identifiable data is not leaked accidentally, or maliciously.

The final tier is review of so-called "Level 4" outputs, where the OpenSAFELY framework stores outputs labelled as `moderately_sensitive` in the `project.yaml` file.

If you have Level 4 access you can log in and review your aggregated results, and perform any necessary redactions before requesting files to be released. 
You will find your files to review in `D:\Level4Files\workspaces\<workspacename>`.

Level 4 outputs **can only be released by specific members of the OpenSAFELY team**. When you are ready to request an OUTPUT REVIEW and RELEASE of your aggregated results, and only the minimum outputs necessary (for which you have also applied any necessary disclosure controls, such as small number suppression) **please [complete this form](documents/OpenSAFELY_Output_Review_Form.docx) and email us at <datarelease@opensafely.org>**.

!!! warning
    ** Data may only be shared IN CONFIDENCE with wider members of the research team, including external collaborators, after they have been released outside of the secure Level 4 area. You MUST NOT screen share (or share via any other means) any results from the Level 4 environment that have not been submitted for OUTPUT REVIEW. See below for publication guidance.**

!!! warning
    ** DO NOT release your aggregated study results to your GitHub repository yourself (unless you have been given permission by OpenSAFELY).**

!!! note
    Individual researchers who have Level 4 access have responsibility for redacting sensitive information or choosing not to publish it at all. The study author should do everything they can to make this easy; for example, carrying out low number suppression automatically, documenting code clearly, and only selecting essential items for publication when deciding what to label as `moderately_sensitive`.
    
Once released, your results will be available in a new branch (`release-candidates`). This branch should be merged into `main`. A new branch of the same name will be created with any further releases so there is no need to keep the branch open.

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

## Publication of your study results (released from the Level 4 environment) and GitHub repository

### Study results
Once the Level 4 outputs have been released (as per the above process), you can share the data **in confidence** with wider members of the research team, including external collaborators. For example, the study author may copy the outputs from the GitHub repository to a document being prepared for publication, or to seek feedback and contribution from other colleagues to inform the final paper or report. 

However, **for publication (e.g. MedRxiv), or circulation of the findings outside of the immediate research team or collaborators** (e.g. presentations given to interested groups), the final paper/report/presentation (etc.), including a brief lay summary of the important conclusions, **must first be emailed to <amir.mehrkar@phc.ox.ac.uk> who will seek final approval for release from NHS England.** The purpose of this approval step is to check that the paper/report aligns with the stated application purpose.

### Study GitHub repository

Similarly, **the study repository must be kept private until project completion and NHS England approval has been obtained**; however, the OpenSAFELY Oversight Board has recommended that all study GitHub repositories (to include the study definition code, codelists and released results) be make public 12 months after any code has been executed against the underlying patient data.

!!! warning
    ** YOU MUST NOT publish any results or circulate findings with any interested groups outside of the immediate research team / collaborators, or make public your study GitHub repository, until you have received approval from NHS England. To obtain approval email <amir.mehrkar@phc.ox.ac.uk> with your paper/report/presentation including a brief lay summary of the important conclusions.**

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
