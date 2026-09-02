# Endpoint Response Policy

**Synthetic Acme Corporation policy created for this experiment -- not a real company, not real data.**

## Production Endpoints

Production endpoints require analyst approval before isolation. Automated isolation of a production endpoint is not permitted under any circumstance, regardless of confidence level.

## Developer Laptops

Developer laptops may be automatically isolated only when malware has been confirmed (not merely suspected) on the device. Suspected-but-unconfirmed malware requires analyst review before isolation.

## Domain Controllers

Domain controllers may never be automatically isolated, regardless of confidence level or incident severity. Isolation of a domain controller always requires explicit analyst and incident-commander approval.
