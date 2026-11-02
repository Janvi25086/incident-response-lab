# Security Incident Response Plan

## Incident
Hardcoded API key, password and user ID.

## Category
Credential Exposure

## Severity
High (Simulated)

## Response Plan
1. Identify exposed credentials.
2. Detect vulnerabilities using Gitleaks.
3. Assess exposure and revoke compromised credentials.
4. Reduce unnecessary permissions using Least Privilege.
5. Remove hardcoded credentials.
6. Store credentials using environment variables.
7. Test the corrected application.
8. Document the incident using GitHub Issues.
## Containment Actions

1. Identified exposed API key, password and user ID.
2. Assessed the affected source code and Git history.
3. Planned revocation and replacement of compromised
   credentials.
4. Restricted GitHub Actions workflow permissions
   to read-only access.
5. Reviewed repository collaborator permissions.
6. Applied the Principle of Least Privilege.
## Eradication and Recovery

1. Removed hardcoded API key, password and user ID.
2. Replaced hardcoded credentials with environment variables.
3. Created a .gitignore file to protect sensitive files.
4. Configured dummy environment variables for testing.
5. Executed the Python application successfully.
6. Verified that hardcoded credentials are absent
   from the current source code.
7. Committed and pushed the security fix.
