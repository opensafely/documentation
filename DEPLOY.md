# Deploying

[Production](https://docs.opensafely.org) is served by [Render](https://opensafely-documentation.onrender.com).

Pull requests will generate a preview deployment of your changes.

## Cloudflare Pages

We have previously used Cloudflare Pages but have temporarily switched to Render.
This is to access more recent Python versions than Cloudflare currently offer.
The [Cloudflare Pages deployment](https://opensafely-docs.pages.dev/) is paused,
to simplify a potential switch back to Cloudflare Pages in future.

## Redirects

These should be recorded in the [`docs/_redirects`](docs/_redirects) file.

### Render

Manually update the configuration in the Render dashboard to reflect the current version of the `_redirects` file on the `main` branch.
Unlike Cloudflare Pages, a Render redirect for a source URL *without* a trailing slash **will also redirect the same source URL with a trailing slash**.

### Cloudflare Pages

Redirects are handled automatically by the `_redirects` file using [Cloudflare Pages' Redirect config](https://developers.cloudflare.com/pages/platform/redirects).
