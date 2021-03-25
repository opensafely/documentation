## What are Codelists?

Codes are alphanumerical codes that are attached to a clinical or event
description. There are a few different code systems such as SNOMED and CTV3,
which means one clinical diagnosis can have different codes, depending on the
system used. Most code systems arrange their codes in a hierachical structure,
meaning a code can be a parent of another code or codes, and a child of another
code. This hierarchy allows all possible events within the clinical environment
to be organised in a relatively systematic way.

Each code refers to a particular event or clinical term such as "Type 1 Diabetes
Mellitus". Even within a single coding system, there are multiple codes for each
disease or symptoms with very precise terms. Clinicians use these codes
precisely, though not always consistently, in their every day work. This means
that to find all the patients with Type 1 diabetes, you may have to search for
30 plus codes in the clinical record.

## OpenCodelists
We built a system for building, reviewing and maintaining codelists at
[codelists.opensafely.org](https://codelists.opensafely.org/).
We've made an introductory video to help explain OpenCodelists in more detail. Codelists 
that are hosted on this website can be used directly in the Study Definition. This means 
there is no need to download or alter these codelists in the study definition, and 
they can be reused.

<div class="video-wrapper">
  <iframe width="1280" height="720" src="https://www.youtube.com/watch?v=ayRtpbcPFLA" frameborder="0" allowfullscreen></iframe>
</div>

## Applying the principle of open working to making codelists

!!! note "Our recommended codelist workflow is still in flux"
    We are developing several new features on OpenSAFELY Codelists to help audit and quality-assess codelists. In the mean time, here is what was suggest as best practice for recording your decision-making


- Make an issue in [codelist repo](https://github.com/opensafely/codelist-development) for the Codelist to be discussed
- Discuss all decisions along the way in the issue, for example, why you decided to exclude
"historical asthma" from an asthma codelist
- Who signed off the codelist should be easy to find and transparent. It should be in the Github issue (preferably
by the person signing off so they can be contacted via Github) and on the published website.
- Write a good description for the website on what it does and does not include and summarise
any key decisions
- All study repos will at some point become public (if they are not already), so bear in mind the
discussion and conversations will be available for examination
- These discussions should be linked to from the website - i.e. link the issue to the
final codelist where it appears in OpenSAFELY Codelists



---8<-- 'includes/glossary.md'
