# Authentication Policy

**Synthetic Acme Corporation policy created for this experiment -- not a real company, not real data.**

## Impossible Travel

Impossible travel involving a privileged account must be escalated immediately to the on-call security lead.

Impossible travel involving a standard (non-privileged) account should be flagged for analyst review within the same shift, but does not require immediate escalation.

## Multi-Factor Authentication Anomalies

Three failed MFA challenges followed by a successful authentication requires investigation before the session is considered legitimate.

A single failed MFA challenge followed by success is not considered anomalous on its own and requires no action.

## Service Accounts

Service accounts may not authenticate interactively. Any interactive login using a service account must be treated as a security event.
