# Security for developers

Security is part of every feature. If unsure, stop and ask a team lead rather than
guessing or hiding a mistake.

## Accounts and devices

- Enable two-factor authentication on GitHub and company accounts.
- Use unique passwords stored in the approved password manager.
- Use only the access required for your role and never share an account.
- Keep the operating system, browser, editor, and development tools updated.
- Lock the device when unattended and report a lost or compromised device promptly.

## Secrets and sensitive data

Passwords, tokens, private keys, connection strings, secret environment files,
production data, and customer data must not appear in:

- Git commits or repository files;
- AI prompts or coding-assistant conversations;
- Slack messages, tickets, PR descriptions, or screenshots;
- application logs, test output, sample data, or documentation.

Use placeholders in documentation and the approved encrypted secret store for real
values. A `.gitignore` entry is helpful but does not make a secret safe after commit.

## Environment separation

- Use local and development accounts and data for development and testing.
- Do not copy production data to a laptop or development environment.
- Never reuse development credentials, databases, buckets, domains, or test accounts
  in production.
- Do not change production, cloud accounts, deployments, DNS, or access permissions
  without explicit approval from the responsible owner.
- Authenticate and authorize on the server; hiding a control in the UI is not security.

## If a secret may be exposed

1. Stop using and sharing it.
2. Tell the team lead or security contact immediately.
3. Revoke or rotate the secret through the responsible account owner.
4. Check logs and access history for misuse.
5. Remove the value from code and history using the approved incident process.

Deleting the latest commit or message is not enough because copies may still exist.
Report concerns privately to `dev@sacmia.com`; do not open a public issue containing
sensitive details.

## Before every pull request

- Review the complete diff for credentials, personal data, unsafe logs, and test data.
- Validate untrusted input and enforce permissions on every protected server operation.
- Return explicit response fields so private database values cannot leak accidentally.
- Confirm new dependencies are necessary, maintained, and obtained from trusted sources.
- Add tests for role boundaries and forbidden access where relevant.
