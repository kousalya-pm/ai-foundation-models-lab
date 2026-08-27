# Incident Response Policy

**SYNTHETIC DOCUMENT -- for local RAG learning purposes only. This is entirely fictional and does not represent any real organization's policy.**

## Escalation Requirements

Any alert classified as ransomware at Critical severity must be escalated to the Incident Commander within 15 minutes of detection.

Any confirmed data exfiltration event must be escalated to both the Incident Commander and the Legal/Privacy team.

## Account Actions

Analysts may NOT disable a privileged account (Domain Admin, Enterprise Admin, or a service account with elevated rights) without written approval from a Tier 3 analyst or the SOC Manager.

Standard user accounts suspected of compromise may be disabled by any Tier 1 or higher analyst without prior approval, but the action must be logged in the case ticket.

## Endpoint Containment

Endpoint isolation (network quarantine) requires analyst approval from a Tier 2 or higher analyst before being executed, except during an active ransomware outbreak, where Tier 1 analysts may isolate immediately and report after the fact.

## Communication

Any incident classified Critical must generate a status update every 30 minutes until contained.
