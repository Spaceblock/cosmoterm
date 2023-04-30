# Contributing Guidelines

This project welcomes everyone who'd like to contribute with his pull request.
However, there are some conventions below: we all should follow them for project's wellbeing, otherwise it can turn difficult to maintain

------

1. Choice of technologies and architectural decisions should be discussed before being implemented.
GitHub pages really suits for such a purpose
2. All changes made to code should be discribed in CHANGELOG.md like
[that](https://keepachangelog.com/en/1.0.0/)
3. `master` is a protected branch.
This means all changes should be merged into main via Pull Request (PR), after being reviewed carefully.
4. The main development branch is called `development`.
5. On every step of project's life it should be given a version with `git tag`.
For instance, *v0.0.1* or *v0.0.2* - according by [semantic versioning](https://semver.org)
6. All contributed code should follow code styling rules and practicies.
PEP8 has to be followed, in particullar.
7. We're following TDD (test driven development).
This means tests should be written before the functionality itself.
8. We're following "clean code" practices: no comments in code, but all names are clear.
Code should be well-documented.
Documentation is to be stored either in `docs/`, or in `README.md`, or in GitHub wiki pages
9. All new features should be documented in README.md, changelog.md and documentation
10. Software is distributed under GNU AFFERO Public License v3

by @mb6ockatf, 30.04.2023