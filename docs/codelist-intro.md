## What are Codelists?

Codes are alphanumerical codes that are attached to a clinical or event description. There are a few different 
code systems such as SNOMED and CTV3 and so there are variations in the codes. Code systems arrange their codes in a
hierachical structure, meaning a code can be a parent of another code or codes, and a child of another code. This 
hierachy allows all possible events within the clinical environment to be organised in a more systematic way. 

Each code refers to a particular event or clinical term such as "Type 1 Diabetes Mellitus". There are multiple 
codes for each disease or symptoms with very precise terms. Clinicians use these codes precisely in their
every day work. This means that to find all the patients with Type 1
diabetes, you may have to search for 30 plus codes in the clinical record. 

## How did we deal with Codelists?

We built a system for 
building, reviewing and maintaining codelists at [codelists.opensafely.org](https://codelists.opensafely.org/). 

Codelists that are hosted on this website are pulled directly into the Study Definition. This means there is no need
to download or alter these codelists in the study definition, and they can be reused. 

## Applying the principle of open working to making codelists

- Make an issue in [codelist repo](https://github.com/opensafely/codelist-development) for the Codelist to be discussed
- Discuss all decisions along the way in the issue, for example, why you decided to exclude
"historical asthma" from an asthma codelist
- Who signed off the codelist should be easy to find and transparent. It should be in the github issue (preferably 
by the person signing off so they can be contacted via Github) and on the published website. 
- Write a good description for the website on what it does and does not include and summarise
any key decisions
- All study repos will become public if they are not already at some point so the 
discussion and conversations will be available for examination
- These discussions should be linked to from the website - i.e. link the issue to the
final product



---8<-- 'includes/glossary.md'
