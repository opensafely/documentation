If you accidentally include multiple calls to `set_population()`, it is the call that appears closest to the end of the dataset definition
that takes effect.

In future, calling `set_population()` more than once will cause a dataset definition to fail;
see the associated [Data Builder](https://github.com/opensafely-core/databuilder/issues/775) issue.
