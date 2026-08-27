# Authentication Policy

**SYNTHETIC DOCUMENT -- for local RAG learning purposes only. This is entirely fictional and does not represent any real organization's policy.**

## Multi-Factor Authentication (MFA)

MFA is required for all remote access, including VPN and cloud console logins.

MFA is required for all privileged account logins, with no exceptions.

Service accounts are exempt from interactive MFA but must use certificate-based authentication instead.

## Impossible Travel

A login flagged as impossible travel (two logins from locations that cannot be physically reached in the elapsed time) must be treated as a suspected account compromise, and the account's active sessions must be revoked immediately, pending analyst confirmation.

## Privileged Accounts

Privileged accounts (Domain Admin, Enterprise Admin) must rotate passwords every 60 days.

Privileged accounts may only be used from designated privileged access workstations (PAWs), never from a standard end-user laptop.

## Service Accounts

Service accounts must never be used for interactive logins.

Any interactive login using a service account must be treated as a Critical severity alert.
