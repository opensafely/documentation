All outputs from OpenSAFELY pipelines are subject to [tiered levels of scrutiny](security-levels.md), to provide assurance that identifiable data is not leaked accidentally, or maliciously.

The final tier is review of so-called "Level 4" outputs, where the OpenSAFELY framework stores outputs labelled as `moderately_sensitive` in the `project.yaml` file.

If you have Level 4 access you can use [Airlock](outputs/viewing-with-airlock.md) to review your aggregated results and request files to be released.


!!! note

    **Mac users**

    If intending to use a Mac for Level 4 access, please check your
    hardware is suitable first.

    Level 4 access requires a working Windows installation. Mac users
    with older *Intel* hardware have had success in accessing Level 4
    when running Windows in a virtual machine.

    However, Mac users with newer Macs that have *Apple* processors
    **cannot run Windows in a virtual machine that is compatible with
    the client necessary for Level 4 access.**

    Macs from 2020 onwards are likely to have an Apple processor.
    You can check by going to the Apple menu in the top left of your
    screen and choosing "About This Mac". If the chip or processor
    information includes "Intel", it is an older model. If the chip
    starts with "Apple M...", it is a newer model which is
    incompatible with the client.

    Macs with Apple processors are still suitable for writing, testing
    and submitting OpenSAFELY code to be run on the secure server.
    **This issue only affects access to Level 4 server.**

    See [this support
    discussion](https://github.com/opensafely/documentation/discussions/251#discussioncomment-1767887)
    for a description of the problem.
