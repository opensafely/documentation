!!! warning
    dm+d codes for Virtual Medicinal Products (VMPs) can change.
    cohort-extractor handles this by automatically expanding a medication codelist
    to include all current and previous codes of any VMPs in the codelist.
    However, this means that when a VMP code has changed, a query using
    `patients.with_these_medications(codelist, returning="code", ...)`
    might return a code that is not in the provided codelist.
