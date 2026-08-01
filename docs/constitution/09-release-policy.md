# Article 9 — Release Policy

1. Releases are cut only from `main` and tagged with a semantic version.
2. A release requires: all tests passing in continuous integration; documentation updated; ADRs recorded for every significant decision included in the release.
3. No production release may occur before continuous integration exists for the test suite. Development builds, alpha builds, nightly builds, and internal testing remain permitted before CI maturity.
4. Release notes enumerate changes, breaking changes, and deprecations.
5. The Maintainer approves every release.
