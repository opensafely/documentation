#### Initial release

During the initial design and development phase of Data Builder, Data
Builder has a `v0` major version. With `v0`, there are no guarantees
about backwards compatibility between versions.

Once Data Builder's design has stabilised, and it is suitable for users to
use more widely, we will release a Data Builder with version `v1`.

Any further change to the major version from `v1` onwards indicates
backwards incompatible changes. For example, a `v1` compatible study
may require some modification to work with `v2` of Data Builder.

#### Specifying a Data Builder version to use

With Data Builder, specify an [available
version](https://github.com/opensafely-core/base-docker/pkgs/container/databuilder/versions)
in your `project.yaml`, in one of the following formats:

* *major*, for example, `databuilder:v0`
* *minor*, for example, `databuilder:v0.1`
* *patch*, for example, `databuilder:v0.1.2`

* By specifying a *patch* version, your code will use the same version
  of Data Builder.
* By specifying a *major* or *minor* version, your code may run a newer
  version of Data Builder, once a newer major or minor version becomes
  available.
  * If running locally, you can update Docker images via the
    [OpenSAFELY CLI](opensafely-cli.md#updating-docker-images).

#### Changes in the use of `latest` version

!!! warning
    Research studies often specified cohort-extractor's version as `latest`.

    We no longer support specifying `latest` as a version.

    This change avoids ambiguity over precisely which Data Builder version
    was used by a given study.

    If you do specify `latest` by mistake, you will instead see an error
    mentioning `manifest unknown`. This error tells you that the version
    is not available.

