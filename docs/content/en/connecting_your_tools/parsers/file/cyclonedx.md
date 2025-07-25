---
title: "CycloneDX"
toc_hide: true
---
CycloneDX is a lightweight software bill of materials (SBOM) standard designed for use in application security contexts and supply chain component analysis.

From: https://www.cyclonedx.org/

Example with Anchore Grype:

{{< highlight bash >}}
./grype defectdojo/defectdojo-django:1.13.1 -o cyclonedx > report.xml
{{< /highlight >}}

Example with `cyclonedx-bom` tool:

{{< highlight bash >}}
pip install cyclonedx-bom
cyclonedx-py
{{< /highlight >}}

{{< highlight bash >}}
  Usage:  cyclonedx-py [OPTIONS]
  Options:
    -i <path> - the alternate filename to a frozen requirements.txt
    -o <path> - the bom file to create
    -j        - generate JSON instead of XML
{{< /highlight >}}

### Sample Scan Data
Sample CycloneDX scans can be found [here](https://github.com/DefectDojo/django-DefectDojo/tree/master/unittests/scans/cyclonedx).

### Default Deduplication Hashcode Fields
By default, DefectDojo identifies duplicate Findings using these [hashcode fields](https://docs.defectdojo.com/en/working_with_findings/finding_deduplication/about_deduplication/):

- vuln id from tool
- component name
- component version
