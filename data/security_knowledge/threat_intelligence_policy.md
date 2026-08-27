# Threat Intelligence Handling Policy

**SYNTHETIC DOCUMENT -- for local RAG learning purposes only. This is entirely fictional and does not represent any real organization's policy.**

## Suspicious IP Handling

IP addresses flagged by threat intelligence feeds with High reputation confidence (score 80-100) may be automatically blocked at the perimeter firewall.

IP addresses flagged with Medium reputation confidence (score 40-79) require analyst verification before blocking.

IP addresses flagged with Low reputation confidence (score below 40) should not be blocked automatically; they should be logged for monitoring only.

## Analyst Verification

Verification means cross-checking the IP against at least two independent threat intelligence sources before taking a blocking action based on Medium confidence.

## Feed Freshness

Threat intelligence indicators older than 90 days must be treated as stale and should not be used as sole justification for a blocking decision.
