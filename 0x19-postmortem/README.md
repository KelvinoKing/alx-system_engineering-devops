# Web Service Outage Postmortem

## Overview

This repository contains the postmortem documentation for a recent web service outage that occurred on January 20, 2024. The incident was related to an Apache server failure caused by an incorrect file extension. The purpose of this README.md is to provide a comprehensive understanding of the incident, its timeline, root cause, resolution, and corrective/preventative measures taken.

## Incident Summary

**Duration:**
- Start Time: January 20, 2024, 08:00 AM (UTC)
- End Time: January 20, 2024, 10:30 AM (UTC)

**Impact:**
- Intermittent service downtime for approximately 2.5 hours.
- Users experienced slow response times and occasional 503 errors.
- Approximately 30% of users were affected.

**Root Cause:**
- Incorrect file extension: A crucial file, "calculate.pph," instead of "calculate.php," led to Apache server failures.

## Timeline

- **08:00 AM (UTC):**
  - Issue detected through monitoring alerts showing increased server error rates.

- **08:15 AM (UTC):**
  - Investigated logs for potential network issues.
  - Assumed initial hypothesis: Network issues causing connectivity problems.

- **08:45 AM (UTC):**
  - No evidence of network issues found.
  - Misleading investigation: Focused on database queries and potential bottlenecks.

- **09:15 AM (UTC):**
  - Incident escalated to the infrastructure team as the problem persisted.
  - Continued investigating database queries and caching mechanisms.

- **09:45 AM (UTC):**
  - Realized the issue was specific to a particular file - "calculate.pph."
  - Misleading investigation: Initially suspected a corrupted file or a malware attack.

- **10:00 AM (UTC):**
  - Incident escalated to the development team for deeper code-level analysis.
  - Identified the incorrect file extension as the root cause.

- **10:30 AM (UTC):**
  - Resolved the issue by renaming the file to "calculate.php."

## Root Cause and Resolution

**Root Cause:**
- The critical file "calculate.pph" had an incorrect file extension, causing Apache to misinterpret it and leading to server failures.

**Resolution:**
- Renamed the file to the correct extension, "calculate.php," restoring the proper functioning of the web service.

## Corrective and Preventative Measures

**Improvements/Fixes:**
- Implement stricter file extension checks during code reviews to prevent similar issues in the future.
- Enhance monitoring to include real-time file integrity checks for critical components.

**Tasks to Address the Issue:**
1. Conduct a comprehensive review of all file extensions within the codebase.
2. Implement automated testing for file extensions during the CI/CD pipeline.
3. Update documentation and guidelines for developers to emphasize proper file naming conventions.
4. Enhance monitoring alerts for quicker identification of specific file-related issues.
5. Conduct a post-incident review with the team to share insights and lessons learned.

## Conclusion

This incident serves as a valuable learning experience to strengthen our system's resilience. The outlined measures aim to minimize the likelihood of similar incidents in the future, fostering a more robust and reliable web service. Feedback and contributions are welcome to continually improve our systems and processes.
