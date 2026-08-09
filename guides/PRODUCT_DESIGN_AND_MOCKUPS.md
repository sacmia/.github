# Product workflows, UX/UI, and mockups

Use this process before implementing a new user-facing feature or materially changing
an existing flow. Any Sacmia-approved AI tool may help draft the artifacts, but the
product owner and human reviewers approve the behaviour and design.

```text
product decision -> user flow -> screen inventory -> low-fidelity mockups
-> human review -> approved feature documents -> implementation
```

A mockup is not a complete requirement. It must be supported by written flows, states,
rules, and acceptance criteria.

## Standard steps

1. **Confirm the design assignment.** Obtain the feature name, problem, target users,
   platforms, scope, and known acceptance criteria. Record unanswered product questions
   instead of asking AI to invent answers.
2. **Create a documentation branch and AI session.** Start from the latest
   `development`, create `docs/<feature-name>-design`, and use one dedicated AI session
   and one pull request for the design package.
3. **Read the existing product context.** Review organization standards, all project
   and AI instruction files, architecture, current feature documents, design system,
   related screens, and existing mockups. Preserve established terminology and
   patterns.
4. **Write the user flow before drawing screens.** Identify actors, permissions,
   preconditions, entry points, the successful path, alternate paths, validation
   failures, cancellation, retry, and completion.
5. **Create the screen inventory.** List every required screen, modal, dialog, and
   important transition. Identify shared components and differences between mobile,
   tablet, and web where relevant.
6. **Define every important state.** Include initial, loading, empty, populated,
   validation error, server error, offline or retry, permission denied, expired session,
   disabled, success, and destructive-confirmation states when applicable.
7. **Create low-fidelity mockups first.** Focus on layout, hierarchy, navigation,
   content, and actions. Do not spend time polishing colours or illustrations until the
   flow is approved. Use fake data and safe placeholders only.
8. **Check usability and accessibility.** Verify clear labels, keyboard navigation for
   web, screen-reader meaning, touch-target size, contrast intent, text scaling,
   responsive behaviour, error recovery, and no colour-only communication.
9. **Write the implementation handoff.** Document field rules, validation, navigation,
   roles and permissions, data required, API dependencies, responsive behaviour,
   accessibility, acceptance criteria, and unresolved questions. Do not invent API or
   database contracts; coordinate them with the architecture documents.
10. **Get human review and approval.** The product owner confirms behaviour and scope;
    a developer checks feasibility and consistency; a tester checks states and
    acceptance criteria. Update the same design session and pull request for review
    fixes.
11. **Merge the approved design package into `development`.** The flow documents and
    mockups become the feature's source of truth. Clearly mark unresolved decisions and
    do not begin blocked implementation.
12. **Start implementation separately.** Create the feature branch and a fresh AI
    implementation session. Require it to read the approved design package before
    proposing code changes.

Backend-only work may not need visual mockups, but it still needs written behaviour,
authorization, validation, failure paths, acceptance criteria, and an approved API or
technical contract.

## Recommended project structure

Follow an existing repository convention when it has one. Otherwise use:

```text
docs/
  features/
    <feature-name>/
      README.md
      user-flow.md
      ui-spec.md
      open-questions.md
      mockups/
        README.md
        <screen-name>.png
```

- `README.md`: purpose, users, scope, exclusions, dependencies, and acceptance criteria.
- `user-flow.md`: actors, preconditions, numbered flows, alternatives, errors, and
  completion rules.
- `ui-spec.md`: screen inventory, components, content, actions, validation, states,
  responsive behaviour, and accessibility.
- `open-questions.md`: owner, decision needed, blocking phase, and final resolution.
- `mockups/README.md`: mockup status, tool/source link when approved, version, and a map
  from each image to its screen specification.

Keep editable design sources in an approved company workspace when the repository
cannot store them. Store reviewable exports with the feature documents and avoid links
that require a personal account. Never include credentials, customer information,
production screenshots, or confidential data in prompts or mockups.

## Copyable prompt to start product design

Replace every value inside `<angle brackets>` and paste this into a fresh session in
any approved AI tool:

```text
Help me prepare the product-design package for <FEATURE NAME> in <REPOSITORY NAME>.
Repository path: <LOCAL REPOSITORY PATH>
Required branch: docs/<feature-name>-design
Platforms: <MOBILE, WEB, OR BOTH>
Known user roles: <ROLES>
Approved product input: <FEATURE DOCUMENT OR TASK PATH>

Before creating or changing files:
1. Confirm the repository path, branch, and git status.
2. Read the current Sacmia engineering standards, AI-assisted development guide, and
   product-design guide:
   - https://github.com/sacmia/.github/blob/main/SACMIA_ENGINEERING_STANDARDS.md
   - https://github.com/sacmia/.github/blob/main/guides/AI_ASSISTED_DEVELOPMENT.md
   - https://github.com/sacmia/.github/blob/main/guides/PRODUCT_DESIGN_AND_MOCKUPS.md
3. Read the repository's README.md, developer workflow, architecture, feature
   documents, design system, related flows, existing mockups, and all AI instruction
   files that exist, including CLAUDE.md or AGENTS.md.
4. Inspect existing terminology and UI patterns.

Do not implement application code and do not invent product decisions. First show me:
- your understanding of the users, problem, scope, and exclusions;
- conflicts, missing decisions, assumptions, and security or privacy concerns;
- proposed actors, user flows, alternate and failure paths;
- proposed screen inventory and required UI states;
- the exact Markdown and mockup files you recommend creating; and
- the review and accessibility checklist you will use.

Use safe placeholder data. Wait for my approval before writing files or generating
mockups.
```

After the proposal and product decisions are approved, use:

```text
Create the approved flow documents, UI specification, open-question log, and
low-fidelity mockups on the current documentation branch. Keep every screen traceable
to a flow step and acceptance criterion. Include all approved states, validation,
permissions, responsive behaviour, and accessibility notes. Do not write application
code. Validate links and Markdown, show the complete changed-file list, and wait for
my review before committing or opening a pull request.
```

## Review checklist

- [ ] Scope, exclusions, roles, and terminology are approved
- [ ] Happy path, alternate paths, errors, cancellation, retry, and completion exist
- [ ] Every screen and important state is documented
- [ ] Mockups and written flows agree with each other
- [ ] Permissions and sensitive-data boundaries are explicit
- [ ] Mobile, web, and responsive differences are documented where relevant
- [ ] Accessibility and error recovery are included
- [ ] Acceptance criteria are testable
- [ ] Open questions have an owner and blocking phase
- [ ] No application code, secrets, real customer data, or unrelated files are included
- [ ] Product owner, developer, and tester reviews are recorded in the pull request
