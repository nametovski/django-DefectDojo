---
title: "DefectDojo Pro Changelog"
description: "DefectDojo Changelog"
exclude_search: true
---

Here are the release notes for **DefectDojo Pro (Cloud Version)**. These release notes are focused on UX, so will not include all code changes.

For Open Source release notes, please see the [Releases page on GitHub](https://github.com/DefectDojo/django-DefectDojo/releases), or alternatively consult the Open Source [upgrade notes](/en/open_source/upgrading/upgrading_guide/).


## June 2025: v2.47

### July 1, 2025: v2.47.4

- **(Pro UI)** Products, Engagements, Tests, Findings and Endpoints can be edited directly from their respective tables via a modal.
- **(Pro UI)** Calendar view now supports additional query parameters for filtering Tests or Engagements.
- **(Pro UI)** Engagements, Tests and the entire Calendar can be exported as .ics files.

![image](images/pro_ics_export.png)

### June 23, 2025: v2.47.3

- **(Pro UI)** Finding Templates can now be added in the Pro UI, from **Findings > Finding Templates** on the sidebar.
- **(Pro UI)** A better error message is displayed when Jira Instance deletion is unsuccessful.
- **(Pro UI)** Product Types can now be edited through a modal: **"⋮" > Edit Product Type** will open a pop-up modal window instead of taking a user to a new page.

![image](images/pro_product_type_modal.png)

### June 16, 2025: v2.47.2

- **(Pro UI)** Endpoint Metadata can now be uploaded to Products.  You can now import a .csv list of all endpoints associated with a Product, from **View Product > Endpoints > Import Endpoint Metadata**

![image](images/pro_endpoint_metadata.png)

- **(Pro UI)** Pie Charts for Metrics now dynamically update based on selected categories.
- **(Pro UI)** Finding metadata (specifically notes, endpoints, and file path/line number) are now visible from the Findings table if present.
- **(Pro UI)** Findings table now uses icons to identify linked Endpoints, Notes or Files.  Clicking the Endpoints or Notes icon opens a window which lists all Endpoints or Notes.

![image](images/pro_finding_icons.png)

- **(Pro UI)** Login page has been redesigned.

![image](images/pro_login.png)

### June 9, 2025: v2.47.1

- **(Pro UI)** Vulnerable Endpoints table has now been added to Finding pages.

![image](images/pro_vulnerable_endpoints.png)

- **(Pro UI)** "Original Finding" link has been added to Finding Metadata table for Duplicate Findings.
- **(Pro UI)** CI/CD Metadata has been added to Engagement view.

### June 2, 2025: v2.47.0

- **(Pro UI)** Finding review can now be set through the Pro UI.  You can now Request Review or clear a Finding review from Finding tables, or from the Finding View.

![image](images/pro_request_review.png)

- **(Pro UI)** Artifact files can now be uploaded through the Pro UI to Findings.  These files can be viewed or deleted on the **Finding Overview > Files** tab of a Finding page.

![image](images/pro_upload_file.png)


## May 2025: v2.46

### ⚠️ Tag Format Change 

As of version 2.46.0, Tags can no longer contain the following characters:
- Commas (,)
- Quotations (both single ' and double ")
- Spaces

To ensure a smooth transition, an automatic migration will be applied to existing tags as follows:
- Commas → Replaced with hyphens (-)
- Quotations (single and double) → Removed
- Spaces → Replaced with underscores (_)
Examples
- example,tag → example-tag
- 'SingleQuoted' → SingleQuoted
- "DoubleQuoted" → DoubleQuoted
- space separated tag → space_separated_tag

This update improves consistency, enhances DefectDojo's search capabilities, and aligns with best practices for tag formatting.

We recommend reviewing your current tags to ensure they align with the new format.  Following the deployment of these new behaviors, requests sent to the API or through the UI with any of the violations listed above will result in an error, with the details of the error raised in the response.

#### May 26, 2025: v2.46.4

- **(Pro Metrics)** Rework of filter menu within insights dashboards to remove cross Product Type and Product filtering capabilities.
- **(Pro UI)** Clickable links within insights dashboards.
- **(Pro UI)** You can now differentiate between **AppSec** and **SOC** Test Types, to specify whether Findings in DefectDojo were created by an AppSec or SOC process.  You can assign the SOC label by editing a Test Type in the Pro UI:

![image](images/pro_test_types.png)

Whether a Finding is "AppSec" or "SOC" depends on the parent Test Type.  If a Test Type does not have SOC set, all of the Findings associated with this Test Type will be considered "AppSec".

The Priority Insights dashboard can quickly render a list of all SOC or AppSec Findings, ordered by Priority.

![image](images/pro_soc_filter.png)

- **(Pro UI)** More detailed messages in Bulk Edit provide a better explanation of why some Findings may have been skipped.

#### May 19, 2025: v2.46.3

- **(Calendar)** New filters have been added to Calendar view: Unassigned Lead, and Engagement/Test Type.
- **(Dashboard)** Added Finding Status filter for Dashboard tiles.
- **(Engagements)** A repository URI can be added to an Engagement via **Edit Engagement > Optional Fields > Repo**.  If this field is set, Findings under that Engagement will automatically generate clickable links to the source code if File Path is set on the Finding.  See [docs](/en/working_with_findings/organizing_engagements_tests/source-code-repositories/) for more details.
- **(Findings)** Added "Jira Issue URL" column to the CSV export of Finding tables.
- **(Metrics)** Priority Dashboard has been added to Metrics, to display your organization's risk profile at a glance.
![image](images/pro_dashboard_priority.png)
- **(Universal Parser)** Added a 'SOC Alerts' flag to Universal Parser, to indicate whether the Findings from the parser originate from a Security Operations Center.

#### May 12, 2025: v2.46.2

- **(Findings)** Component Name and Version have been added to the metadata table on a Finding View.
- **(Metrics)** Pro Insights Dashboards can now be filtered by Tag.
- **(Users)** The Users table can now be exported as a .csv file.

#### May 7, 2025: v2.46.1

Hotfix release - no significant feature changes.

#### May 5, 2025: v2.46.0


- **(Import)** Mitigated timestamp in reports are no longer ignored/overwritten on Reimport.
- **(Tools)** Fortify Webinspect has been added as a supported tool.
- **(Tools)** Added JSON as a supported tool for Immuniweb.
- **(Tools)** Nessus (Tenable) parser now handles additional fields.
- **(Tools)** Wiz parser now handles additional fields and unique_id_from_tool.


## Apr 2025: v2.45

#### Apr 28, 2025: v2.45.3

- **(Import)** Reimporting a scan can now handle special statuses assigned by a tool.  Now, if a Finding was initially imported as Active, but the status was changed to False Positive, Out Of Scope or Risk Accepted by a subsequent report, that status will now be respected and applied to the Finding by Reimport.
- **(Tools)** Fortify parser can now assign False Positive status to Findings according to the audit.xml file.

#### Apr 22, 2025: v2.45.2

![image](images/risk_table.png)

- **(Pro UI)** Added a link to Universal Importer to the sidebar, which provides access to the [Universal Importer and DefectDojo CLI](/en/connecting_your_tools/external_tools/) tools.
- **(Pro UI)** Added smart Prioritization and Risk fields to DefectDojo Pro, which can be used to more easily triage Findings based on the impact of the Product they affect.  See [Priority](/en/working_with_findings/finding_priority/) documentation for more information.
- **(Tools)** Updated Fortify Webinspect parser to handle Fortify's new XML report format.

#### Apr 14, 2025: v2.45.1

- **(Connectors)** Added a Connector for Wiz: see [tools reference](/en/connecting_your_tools/connectors/connectors_tool_reference/) for configuration instructions.

#### Apr 7, 2025: v2.45.0

- **(Pro UI)** Added Calendar view to Pro UI: Calendar view now displays Tests and Engagements, and can be filtered.  Clicking on a Calendar entry now displays a more detailed description of the object.
![image](images/pro_calendar_view.png)
- **(Universal Parser)** Added the ability to map an EPSS score from a file.  Note that this field **will** be updated by EPSS database sync, but this gives a user the ability to capture that field from initial import.

## Mar 2025: v2.44

#### Mar 31, 2025: v2.44.4

- **(Pro UI)** Group and Configuration permissions can now be assigned quickly from a User page.  For more information, see [DefectDojo Pro Permissions](/en/customize_dojo/user_management/pro_permissions_overhaul/).

#### Mar 24, 2025: v2.44.3

- **(Import)** Generic Findings Import will now parse tags in the JSON payload when Async Import is enabled.

#### Mar 17, 2025: v2.44.2

- **(Pro UI)** Added a new method to quickly assign permissions to Products or Product Types.  See our [Pro Permissions](/en/customize_dojo/user_management/pro_permissions_overhaul/) for more details.

![image](images/pro_permissions_2.png)

#### Mar 10, 2025: v2.44.1

- **(Pro UI)** Added a field in the View Engagement page which allows a user to navigate to the linked Jira Epic, if one exists.
- **(Universal Parser)** XML is now a supported file type for Universal Parser.
- **(SSO)** SSO can now be set up with any kind of [OIDC Configuration](https://auth0.com/docs/authenticate/protocols/openid-connect-protocol).  See OIDC Settings in the Pro UI:

![image](images/oidc.png)

#### Mar 3, 2025: v2.44.0

- **(Pro UI)** Breadcrumbs have been overhauled to better represent the context each page exists in.  Breadcrumbs will now include filtering and query parameters.  The titles of tables now better represent their context, for example when looking at the Engagements list for a particular Product, the view will be titled {Product Name} Engagements, rather than All Engagements as before.

## Feb 2025: v2.43

#### Feb 24, 2025: v2.43.4

- **(API)** API can now filter Findings by tag using AND, in addition to OR.  This can be done with the `tags__and` API filter.
- **(Connectors)** Users of AWS Security Hub, Snyk can now set a minimum Severity level for Findings to limit the amount of data imported via Connector.  Findings below the minimum Severity level will not be imported.  If Minimum Severity is changed, existing Findings below the new Minimum Severity will be Closed (not deleted).
- **(Pro Metrics)** Tool Insights can now be filtered with specific Date values, rather than simply 'past 30 days', etc.

#### Feb 19, 2025: v2.43.3

- **(API)** `/audit_log` has been added as an API endpoint for DefectDojo Pro, which can return a JSON report of all user activity, or filter by object ID. <span style="background-color:rgba(242, 86, 29, 0.5)">(Pro)</span>
- **(Pro UI)** Vulnerability ID can now be edited for a given Finding, using the Edit Finding page.  This allows users to manually identify duplicates by assigning a matching Vulnerability ID to an additional Finding.

#### Feb 12, 2025: v2.43.2

- **(Pro UI)** Tests and Risk Acceptances can now be added directly from the All Tests / All Risk Acceptances lists.
- **(CLI Tools)** Added a `background-import` flag to allow for asynchronous imports or reimports.
- **(Connectors)** Users of Burp, SonarQube and Dependency-Track Connectors can now set a minimum Severity level for Findings to limit the amount of data imported via Connector.  Findings below the minimum Severity level will not be imported.  If Minimum Severity is changed, existing Findings below the new Minimum Severity will be Closed (not deleted).
- **(API)** Fixed issue where Findings created by API with methods other than `/import` / `/reimport` were not being identified as duplicates.
- **(Findings)** 'Close Old Findings' will now apply 'Unique ID From Tool' deduplication, if this algorithm is in use for a set of Findings.

#### Feb 10, 2025: v2.43.1

- **(Pro UI)** Added 'Has Jira' (True/False) as a filter, to filter Findings, Products or Engagements that have associated Jira data.
- **(Pro UI)** Notes can now be added to Engagement / Findings / Tests from All Engagements / Findings / Tests lists as well as View Engagement / Findings / Tests pages.
- **(Pro UI)** Added ability to Close Finding from a Finding List, without needing to first open the Edit Finding form.
- **(CLI Tools)** Improved help text for Universal Importer / DefectDojo CLI. Many guides and examples are now in our [docs](/en/connecting_your_tools/external_tools/) instead of being displayed in the CLI itself.
- **(Tools)** Updated Burp scan to use Hashcode Deduplication.  Default hashcode forms are `title`, `file_path`, `severity`, and `vuln_id_from_tool`.
- **(Tools)** Corrected issue with AWS Inspector2 OSS parser related to `mitigated date` being handled incorrectly.

#### Feb 3, 2025: v2.43.0

- **(Pro UI)** Users can now upload local SAML metadata when configuring SAML.
- **(Pro UI)** Added new section on Risk Acceptance Form to allow users to upload 'Proof'; any relevant files that can be used to support a Risk Acceptance (emails, screenshots of communication, policies, etc).
- **(Connectors)** Users of Semgrep and Tenable Connectors can now set a minimum Severity level for Findings to limit the amount of data imported via Connector.  Findings below the minimum Severity level will not be imported.  If Minimum Severity is changed, existing Findings below the new Minimum Severity will be Closed (not deleted).
- **(Reimport)** Clarified 'no change' state in Import History with message 'There were no findings created, closed, or modified'.
- **(Jira)** Next-Gen Epic creation from an Engagement no longer requires an Epic Name to be set, and will instead use an Epic ID value if Epic Name fails.
- **(Jira)** Removed HTML encoding from strings that are sent to Jira, to prevent escape characters from being added to issue descriptions unnecessarily.
- **(System Settings)** Split up the 'Disclaimer' function, allowing boilerplate 'Disclaimer' text to be displayed in Notifications, Reports, or Notes.

## Jan 2025: v2.42

#### Jan 27, 2025: v2.42.3

- **(Connectors)** Added 'minimum severity' filter for Semgrep and Tenable Connectors.  If you want to only upload Findings of a certain severity and up, you can set a filter for this under 'Minimum Severity' in your Connector options.

![image](images/connectors_min_severity.png)

Previously synced Findings that are no longer within the filter parameters will be set to Closed upon the following Sync operation.
- **(API)** Prefetching multiple parameters now returns all prefetched objects in an array.

#### Jan 21, 2025: v2.42.2

- **(Classic UI)** Corrected link to Smart Upload form.
- **(CLI Tools)** Fixed issue with .exe extensions not getting added to Windows binaries
- **(Findings)** `Mitigated` filter now uses datetime instead of date for filtering.
- **(OAuth)** Clarified Azure AD labels to better align with Azure's language.  Default value for Azure Resource is now set. <span style="background-color:rgba(242, 86, 29, 0.5)">(Pro)</span>
- **(RBAC)** Request Review now applies RBAC properly with regard to User Groups.

#### Jan 13, 2025: v2.42.1

- **(API)** Pro users can now specify the fields they want to return in a given API payload.  For example, this request will only return the title, severity and description fields for each Finding.  <span style="background-color:rgba(242, 86, 29, 0.5)">(Pro)</span>
```
curl -X 'GET' \
  'https://localhost/api/v2/findings/?response_fields=title,severity,description' \
  -H 'accept: application/json'
```
- **(Findings)** Excel and CSV exports now include tags.
- **(Reports)** Reports now exclude unenforced SLAs from Executive Summary to avoid confusion.
- **(Risk Acceptance)** Simple Risk Acceptances now have a 'paper trail' created - when they are added or removed, a note will be added to the Finding to log the action.
- **(Tools)** ImageTags are now included with AWS SecurityHub and AWS inspector parsers.

#### Jan 6, 2025: v2.42.0

- **(API)** `/test_reimport` results can now be ordered via id, created, modified, version, branch_tag, build_id, and commit_hash.
- **(Jira)** When a Risk Acceptance expires, linked Jira Group issues will now be updated to reflect the status change.

## Dec 2024: v2.41

#### Dec 31, 2024: v2.41.4

- **(API)** 'Force To Active / Verified' flag is no longer required when calling `/import-scan`, `/reimport-scan` endponts: a value of True now forces to Active, False now forces to Inactive, while setting a value of none (or not using the flag) will use the tool's status.
- **(Pro UI)** Added ability to regenerate / copy your API token.
- **(Pro UI)** Fixed bug preventing date / planned remediation dates from being added via Bulk Edit.
- **(Import)** Added fields for EPSS score and percentile to Generic Findings Import parser.

#### Dec 24, 2024: v2.41.3

- **(API)** Added `/request_response_pairs` endpoint.
- **(Pro UI)** When sorting by Severity, Findings will now be ordered by **severity level** rather than alphabetically.
- **(Pro UI)** On the Findings table, the Endpoint Hosts column has been replaced with a numerical count of affected Endpoints.
- **(Pro UI)** On the Findings table, the Vulnerability ID field can now be filtered with "starts_with", "ends_with" filters.
- **(Pro UI)** Added Edit Test Type form: you can now edit the properties of a custom Test Type to determine if it is Active or Inactive, or a Static Scan or Dynamic Scan Test.
- **(Pro UI)** Same Tool Deduplication Settings / Test Type field is now searchable.
- **(Tools)** Qualys HackerGuardian now uses hashcode against "title", "severity", "description" for deduplication.
- **(Tools)** Horusec scan now uses hashcode against "title", "description", "file_path", and "line" for deduplication.

#### Dec 16, 2024: v2.41.2

- **(Connectors)** Remove the 'Beta' logo from Connectors

#### Dec 9, 2024: v2.41.1

- **(API)** When using the jira_finding_mappings API endpoint, trying to update a finding's Jira mapping with a Jira issue that is already assigned to another finding will now raise a validation error.
- **(Pro UI)** A Test's Import History is now paginated by default.
- **(Findings)** New Filter: 'Has Any JIRA' which accounts for Findings with single Issues or Findings that were pushed to Jira as part of a Group.
- **(Classic UI)** Filters have been added to the Product Type view.  This is useful for when a single Product Type contains many Products which need to be filtered down.
- **(Classic UI)** Reported Finding Severity by Month graph now tracks the X axis by month correctly.

#### Dec 2, 2024: v2.41.0

- **(API)** `engagements/{id}/update_jira_epic` endpoint path added so that users can now push an updated Engagement to Jira, without creating a new Jira Epic.
- **(Pro UI)** Columns can now be reordered in tables, by clicking and dragging the column header.

![image](images/reorder-columns.png)

- **(Pro UI)** Notes can now be added to a Test directly from the Test page.
- **(Classic UI)** Reviewers are now displayed on Finding pages.
- **(Docs)** New integrated docs site: https://docs.defectdojo.com/

## Nov 2024: v2.40

#### Nov 25, 2024: v2.40.4

- **(Pro UI)**  Improved Metadata tables with Parent object relationships for Products, Engagements, Tests, Findings, Endpoints/Hosts
- **(Pro UI)**  Deleting an object now returns you to a page which makes more sense.
- **(Endpoints)**  Endpoints can now be sorted by ID.
- **(Review Request)**  When a user requests a review, both the requester and the requestee are now captured in audit logs.
- **(Tools)**  Trivy Operator now parses the ‘cluster compliance report’ from scans.
- **(Tools)**  CheckMarx One parser can now handle cases where a result has no description.
- **(Tools)**  AnchorCTL Policies tool has been fortified to handle new severity values.


#### Nov 17, 2024: v2.40.2

- **(API)** Added an API endpoint to get the DefectDojo version number: `/api/v2/version` <span style="background-color:rgba(242, 86, 29, 0.5)">(Pro)</span>
- **(API)**  Multiple Metadata objects can now be added to a single Endpoint, Finding or Product via POST or PATCH to `/api/v2/metadata/` .  Previously, only one Metadata key/value pair could be updated per call.
- **(Pro UI)**  You can now Clear Alerts in the Pro UI.
- **(Pro UI)**  Corrected an issue with Pro UI’s form validation when trying to connect a Jira Project with an Engagement.  
- **(Pro UI)**  Fixed an issue in the Pro UI where new Product Tiles could not be created.
- **(Reports)**  Changes have been made to the Report Generator's description text to clarify how new reports are created from existing reports.
- **(Findings)**  “Verified” is now an optional status for many Finding workflows.  This can be changed from the System Settings page in the Legacy UI (not yet implemented in Pro UI).
- **(Tools)**  Update to AWS Prowler parser - can now handle the ‘event_time’ parameter


#### Nov 14, 2024: v2.40.1

- **(API)** Added a method to validate for file extensions, when 'artifact' files are added to a test (images, for example)
- **(Cloud Portal)** Fixed an issue where QR codes were not being generated correctly for MFA setup.  <span style="background-color:rgba(242, 86, 29, 0.5)">(Pro)</span>
- **(Dashboards)** Insights dashboards can now filter by Product Tag  <span style="background-color:rgba(242, 86, 29, 0.5)">(Pro)</span>
- **(Notifications)** Added a new notification template for ‘Engagement Closed’ - Email, Alerts, Teams, Slack
- **(Tools)** Fixed an issue with the Burp Entreprise HTML parser not correctly handling certain reports
- **(Tags)** Tags are now forced to lowercase when created



#### Nov 4, 2024: v2.40.0

- **(API)** Engagement_End_Date is now honored when submitted via /import /reimport endpoint.
- **(API)** Corrected an issue with the /import endpoint where old Findings were not being mitigated correctly.
- **(Pro UI)**  Certain Error 400 notifications will now be displayed as ‘toasts’ in the Pro UI with a better error description, rather than redirecting to a generic 400 page.
- **(Pro UI)**  Dojo-CLI and Universal Importer are now available for download in-app.  See External Tools menu in the top-right hand menu of the Pro UI.
- **(Connectors)**  Multiple connectors of the same type can now be added.  Each Connector will create a unique Engagement which will be populated with Findings.  <span style="background-color:rgba(242, 86, 29, 0.5)">(Pro)</span>
- **(Connectors)**  AWS Security Hub connector can now find any AWS delegated accounts associated with a centralized account.  All Security Hub Findings from a connector will be tagged with the appropriate AwsAccountId field, and additional Products can be added for each.  <span style="background-color:rgba(242, 86, 29, 0.5)">(Pro)</span>
- **(CLI Tools)**  Dojo-CLI tool now available: a command-line tool which you can use to manage imports and exports to your Cloud instance.  To get started, download the app from the External Tools menu.
- **(Deduplication)**  There’s no longer a brief service interruption when changes are applied to Deduplication Settings.  Those changes can be applied without restarting the service.
- **(Tools)**  Added a new parser for AWS Inspector2 Findings.

#### Setting up multiple AWS Hub accounts with a Connector

If you manage Security Hub findings for multiple accounts from a centralized administrator account, you will need to
create the IAM user under that account and configure the Connector with it in order to retrieve findings from those
sub-accounts with a single connector configuration. 

"Member" accounts (either invited manually or automatically associated when using AWS Organizations) will be detected by the Discover operation, and Products will be created for each of your account + region pairs based on the administrator account's cross-region aggregation settings. 

See [this
section of the AWS Docs](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation.html#finding-aggregation-admin-member) about cross-region aggregation with multiple accounts for more information.
* Once you have created your IAM user and assigned it the necessary permissions using an appropriate policy/role, you will
need to generate an access key and provide the "Access Key" and "Secret Key" components in the relevant connector
configuration fields.
* The "Location" field should be populated with the appropriate API endpoint for your region. For example, to retrieve results from the us-east-1 region, you would supply https://securityhub.us-east-1.amazonaws.com.
* Note that we rely on Security Hub's cross-region aggregation to pull findings from more than one region. If cross-region aggregation is enabled, you should supply the API endpoint for your "Aggregation Region". Additional linked regions will have ProductRecords created for them in DefectDojo based on your AWS account IDs and the region names.

## Oct 2024: v2.39

#### Oct 29, 2024: v2.39.4

- **(API)**  Corrected 'multiple positional arguments' issue with `/import` endpoint
- **(Metrics)**  Dashboards can now handle multiple Products or Product Types simultaneously: this includes the Executive, Program, Remediation and Tool insights dashboards.  <span style="background-color:rgba(242, 86, 29, 0.5)">(Pro)</span>
- **(Tools)**  OSV, Tenable parsers have been made more robust


#### Oct 21, 2024: v2.39.1

- **(Pro UI)**  Parent Object links have been added to the Metadata table to help contextualize the page you're on
- **(Pro UI)**  Improved "Toggle Columns" menu on tables
- **(Pro UI)**  Added additional helptext for Simple Risk Acceptance, SLA Enforcement
- **(Pro UI)**  Improved Test View with better Import History and Active Finding Severity Breakdown elements
- **(Import)**  Development Environments which do not already exist can now be created via 'auto create context'
- **(Metrics)**  All Metrics dashboards can now be exported as a PDF (Remediation Insights, Program Insights, Tool Insights)  <span style="background-color:rgba(242, 86, 29, 0.5)">(Pro)</span>


#### Oct 7, 2024: v2.39.0

- **(Pro UI)**  Dropdown menus for Import Scan / Reimport Scan no longer block the active element of a form.
- **(Pro UI)**  Finding counts by Severity now disregard Out Of Scope / False Positive Findings.
- **(Dashboard)**  Tile filters with a Boolean filter of False are now saving correctly.  E.G. If you tried to create a Tile with a filter condition of “Has Jira = No” previously this would not be applied correctly.  
- **(Jira)**  Added help text for 'Push All Issues'.
- **(Tools)**  AWS Security Hub EPSS score now parses correctly.

## Sept 2024: v2.38

#### Sept 30, 2024: v2.38.4

- **(API)**  Object History can now be accessed via the API.
- **(API Docs)**  Generating the response schema for certain API endpoints no longer breaks the Swagger interface.
- **(Metrics)**  Added Executive Insights dashboard, Select a Product or Product type, and you can view an executive summary of that Product/Product Type’s security posture with relevant stats.  <span style="background-color:rgba(242, 86, 29, 0.5)">(Pro)</span>
- **(Passwords)**  Password creation for new users can now be made optional upon request.  This feature is toggled via the back-end.


#### Sept 23, 2024: v2.38.3

- **(API)**  `/global_role` endpoint now supports prefetching.
- **(API)**  It is now possible to prefetch a Finding with attached files via API.
- **(Login)**  A new "Forgot Username" link has been added to the login form.  The link will navigate to a page which requests the user's email address. The username will be sent to that address if it exists.
- **Risk Acceptances**  Notes are now added to Findings when they are removed from Risk Acceptances.
- **(Risk Acceptance)**  Risk Acceptance overhaul. Feature has been extended with new functions.  See [Risk Acceptance documentation](/en/working_with_findings/findings_workflows/risk_acceptances/) for more details.
- **Tools**  Qualys HackerGuardian parser added.
- **Tools**  Semgrep Parser updated with new severity mappings. HackerOne parser updated and now supports bug bounty reports.
- **Tools**  fixed an issue where certain tools would not process asyncronously: Whitehat_Sentinel, SSLyze, SSLscan, Qualys_Webapp, Mend, Intsights, H1, and Blackduck.


#### Sept 16, 2024: v2.38.2

- **(Pro UI)**  Jira integration in Pro UI now has parity with Legacy UI.  Ability to Push To Jira has been added, and the Jira ticket view has been added to Findings, Engagements, and all other related objects in DefectDojo.
- **(Finding SLAs)**  Added “Mitigated Within SLA” Finding filter, so that users can now count how many Findings were mitigated on time, and how many were not.  Previously, we were only able to filter Findings that were currently violating SLA or not, rather than ones that had historically violated SLA or not.
- **(Metrics)**  “Mitigated Within SLA” simple metric added to Remediation Insights page.
- **(Reports)**  Custom Content text box no longer renders as HTML.
- **(Tools)**  Wiz Parser now supports SCA format.
- **(Tools)**  Fortify now supports a wider range of .fpr files.
- **(Tools)**  Changed name of Netsparker Scan to Invicti Scan following their acquisition.  Integrations that use the ‘Netsparker’ terminology will still work as expected, but now ‘Invicti’ appears in our tools list.
- **(Universal Importer)** Tag Inheritance has been added to Universal Importer.  Tags can now be added to Findings from that tool.  <span style="background-color:rgba(242, 86, 29, 0.5)">(Pro)</span>



#### Sept 9, 2024: v2.38.1

- **(Pro UI)**  Clearing a date filter and re-applying it no longer throws a 400 error.
- **(Dashboard)**  Dashboard Tag Filters now work correctly in both legacy and Pro UIs.  
- **(MFA)**  When an admin enforced Global MFA on a DefectDojo instance, there was a loop state that could occur with new users attempting to set up their accounts.  This issue has been corrected, and new users can set a password before enabling MFA.
- **(Permissions)**  When a user had permission to edit a Product, but not a Product Type, there was a bug where they were unable to submit an ‘Edit Product’ form (due to interaction with the Product Type). This has been corrected.
- **(Reimport)**  Reimport now correctly records additional vulnerability IDs beyond 1.  In the past, Findings that had more than one Vulnerability ID (a CVE, for example) would have those additional Vulnerability IDs discarded on reimport, so users were potentially losing those additional Vulnerability IDs.
- **(Tools)**  Threat Composer parser added
- **(Tools)**  Legitify parser added
- **(Tools)**  EPSS score / percentile will now be imported from Aquasec files


#### Sept 3, 2024: v2.38.0

- **(API)**  Better naming conventions on Mitigated and Discovered date filters: these are now labeled Mitigated/Discovered On, Mitigated/Discovered Before, Mitigated/Discovered After.
- **(Pro UI)**  Pre-filtered Finding Routes added to Sidebar: you can now quickly filter for Active Findings, Mitigated Findings, All Risk Acceptances, All Finding Groups.
- **(Pro UI)**  Pro UI Findings datatable can now apply every filter that the legacy UI could: filter Findings by (Last Reviewed, Mitigated Date, Endpoint Host, Reviewers… etc).
- **(Pro UI)**  Pro UI OAuth settings leading to a 404 loop - bug fixed and menu now works as expected.
- **(Pro UI)**  Vulnerable Hosts page no longer returns 404.
- **(Pro UI)**  Sorting the Findings data table by Reporter now functions correctly.
- **(Connectors)**  Dependency-Track Connector now available.   <span style="background-color:rgba(242, 86, 29, 0.5)">(Pro)</span>
- **(Deduplication Tuner)**  Deduplication Tuner now available in Pro UI under Enterprise Settings > Deduplication Tuner.
- **(Filters)**  Filtering Findings by Date now applies the filter as expected.
- **(Filters)**  Sorting by Severity now orders by lowest-highest severity instead of alphabetically
- **(Reimport)**  Reimporting Findings that have been Risk-Accepted no longer changes their status to ‘Mitigated’.
- **(Risk Acceptance)**  Updating the Simple Risk Acceptance or the Full Risk Acceptance flag on a Product now updates the Product as expected.

## Aug 2024: v2.37

#### Aug 28, 2024: v2.37.3

- **(API)**  New Endpoint: /finding_groups allows you to GET, add Findings to, delete, or otherwise interact with Finding Groups.  <span style="background-color:rgba(242, 86, 29, 0.5)">(Pro)</span>
- **(Pro UI)**  Relative date ranges for Findings have been added to Finding Filters (last 30 days, last 90 days, etc)
- **(Pro UI)**  Bulk Edit / Risk Acceptance / Finding Group actions are now available in Pro UI.	
- **(Pro UI)**  Finding Groups are now available in the Pro UI.  Selecting multiple Findings allows you to create a Finding Group, provided those Findings are in the same Test.
- **(Pro UI)**  Enhanced Endpoint View now available in Pro UI.
- **(Pro UI)**  Jira Instances can now be added and edited via Pro UI.
- **(Connectors)**  SonarQube / SonarCloud Connector added.  <span style="background-color:rgba(242, 86, 29, 0.5)">(Pro)</span>
- **(Questionnaires)**  Anonymous Questionnaires can now be added to an Engagement after they are completed.  This solves an issue where users wanted to have their team complete questionnaires related to a Product without giving the user access to the complete Product on DefectDojo.
- **(Reports)**  Report issue where images would disappear from reports has been corrected
- **(SLAs)**  “SLA Violation in _ Days” notifications are no longer being sent for unenforced SLAs.
- **(Tools)**  New Parser: AppCheck Web Application Scanning
- **(Tools)**  Nmap Parser now handles script output

#### Aug 7, 2024: v2.37.0

- **(API)**  Created a method to handle simultaneous async reimports to the same Test via API
- **(API)**  Minimum Severity flag now works as expected on /import, /reimport endpoints (Clearsale)
- **(API)**  API errors now default to "Expose error details"
- **(Pro UI)**  New Filter: by calculated SLA date (you can now filter for SLA due dates between a particular date range, for example)
- **(Pro UI)**  New Filter: age of Finding
- **(Pro UI)**  Improvements to pagination / loading behavior for large amounts of Findings
- **(Pro UI)**  Added ability to Reimport Findings in new UI:
- **(Connectors)**  Tenable Connector Released
- **(Dashboard)**  Risk Acceptance tile now correctly filters Findings
- **(Jira)**  Manually syncing multiple Findings with Jira (via Bulk Edit) now pushes notes correctly
- **(Reports)**  Adding the WYSIWYG Heading to a Custom Report now applies a custom Header, instead of a generic ‘WYSIWYG Heading’
- **(SAML)**  Fixed issue where reconfiguring SAML could cause lockout
- **(Tools)**  Wizcli Parser released
- **(Tools)**  Rapplex Parser released
- **(Tools)**  Kiuwan SCA Parser released
- **(Tools)**  Test Types can now be set to Inactive so that they won’t appear in menus.  This ‘inactive’ setting can only be applied in the legacy UI, via Engagements > Test Types (or defectdojo.com/test_type)

## Jul 2024: v2.36.0

- **(Notifications)**  Improved email notifications with collapsible Finding lists for greater readability
- **(SLAs)**  SLAs can now be optionally enforced.  For each SLA associated with a Product you can set or unset the Enforce __ Finding Days box in the relevant SLA Configuration screen.  When this box is unchecked, SLAs for Findings that match that Severity level will not be tracked or displayed in the UI.
