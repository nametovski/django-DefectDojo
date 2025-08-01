---
title: "GitLab SAST Report"
toc_hide: true
---
Import SAST Report vulnerabilities in JSON format: https://docs.gitlab.com/ee/user/application_security/sast/#reports-json-format

### Sample Scan Data
Sample GitLab SAST Report scans can be found [here](https://github.com/DefectDojo/django-DefectDojo/tree/master/unittests/scans/gitlab_sast).

### Default Deduplication Hashcode Fields
By default, DefectDojo identifies duplicate Findings using these [hashcode fields](https://docs.defectdojo.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- title
- cwe
- line
- file path
- description
