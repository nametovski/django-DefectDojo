# DefectDojo

<table>
    <tr styl="margin: 0; position: absolute; top: 50%; -ms-transform: translateY(-50%); transform: translateY(-50%);">
        <th>
            <a href="https://opensourcesecurityindex.io/" target="_blank" rel="noopener">
                <img style="width: 282px; height: 56px" src="https://opensourcesecurityindex.io/badge.svg"
                alt="Open Source Security Index - Fastest Growing Open Source Security Projects" width="282" height="56" />
            </a>
        </th>
        <th>
            <p>
                <a href="https://www.owasp.org/index.php/OWASP_DefectDojo_Project"><img src="https://img.shields.io/badge/owasp-flagship%20project-orange.svg" alt="OWASP Flagship"></a>
                <a href="https://github.com/DefectDojo/django-DefectDojo/releases/latest"><img src="https://img.shields.io/github/release/DefectDojo/django-DefectDojo.svg" alt="GitHub release"></a>
                <a href="https://www.youtube.com/channel/UCWw9qzqptiIvTqSqhOFuCuQ"><img src="https://img.shields.io/badge/youtube-subscribe-%23c4302b.svg" alt="YouTube Subscribe"></a>
                <a href="https://twitter.com/defectdojo/"><img src="https://img.shields.io/twitter/follow/defectdojo.svg?style=social&amp;label=Follow" alt="Twitter Follow"></a>
            </p>
            <p>
                <a href="https://github.com/DefectDojo/django-DefectDojo/actions"><img src="https://github.com/DefectDojo/django-DefectDojo/actions/workflows/unit-tests.yml/badge.svg?branch=master" alt="Unit Tests"></a>
                <a href="https://github.com/DefectDojo/django-DefectDojo/actions"><img src="https://github.com/DefectDojo/django-DefectDojo/actions/workflows/integration-tests.yml/badge.svg?branch=master" alt="Integration Tests"></a>
                <a href="https://bestpractices.coreinfrastructure.org/projects/2098"><img src="https://bestpractices.coreinfrastructure.org/projects/2098/badge" alt="CII Best Practices"></a>
            </p>
        </th>
    </tr>
 </table>

![Screenshot of DefectDojo](https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/dev/docs/assets/images/screenshot1.png)

[DefectDojo](https://www.defectdojo.com/) is a DevSecOps, ASPM (application security posture management), and
vulnerability management tool.  DefectDojo orchestrates end-to-end security testing, vulnerability tracking,
deduplication, remediation, and reporting.

## Demo

Try out DefectDojo on our demo server at [demo.defectdojo.org](https://demo.defectdojo.org)

Log in with username `admin` and password `1Defectdojo@demo#appsec`. Please note that the demo is publicly accessible
and regularly reset. Do not put sensitive data in the demo. An easy way to test Defect Dojo is to upload some [sample scan reports](https://github.com/DefectDojo/django-DefectDojo/tree/master/unittests/scans).

## Quick Start for Compose V2

From July 2023 Compose V1 [stopped receiving updates](https://docs.docker.com/compose/reference/).

Compose V2 integrates compose functions into the Docker platform, continuing to support most of the previous
docker-compose features and flags. You can run Compose V2 by replacing the hyphen (-) with a space, using
`docker compose` instead of `docker-compose`.

```sh
# Clone the project
git clone https://github.com/DefectDojo/django-DefectDojo
cd django-DefectDojo

# Check if your installed toolkit is compatible
./docker/docker-compose-check.sh

# Building Docker images
docker compose build

# Run the application (for other profiles besides postgres-redis see  
# https://github.com/DefectDojo/django-DefectDojo/blob/dev/readme-docs/DOCKER.md)
docker compose up -d

# Obtain admin credentials. The initializer can take up to 3 minutes to run.
# Use docker compose logs -f initializer to track its progress.
docker compose logs initializer | grep "Admin password:"
```

## For Docker Compose V1

You can run Compose V1 by calling `docker-compose` (by adding the hyphen (-) between `docker compose`). 

Following commands are using original version so you might need to adjust them:
```sh
docker/docker-compose-check.sh
docker/entrypoint-initializer.sh
docker/setEnv.sh
```

Navigate to `http://localhost:8080` to see your new instance!

## Documentation

* [Official Docs](https://docs.defectdojo.com/)
* [REST APIs](https://docs.defectdojo.com/en/open_source/api-v2-docs/)
* [Client APIs and Wrappers](https://docs.defectdojo.com/en/open_source/api-v2-docs/#clients--api-wrappers)
* Authentication options:
    * [OAuth2/SAML2](https://docs.defectdojo.com/en/open_source/archived_docs/integrations/social-authentication/)
    * [LDAP](https://docs.defectdojo.com/en/open_source/ldap-authentication/)
* [Supported tools](https://docs.defectdojo.com/en/connecting_your_tools/parsers/)

## Supported Installation Options

* [Docker / Docker Compose](readme-docs/DOCKER.md)
* [SaaS](https://www.defectdojo.com/) - Includes Support & Supports the Project
## MCP Server

DefectDojo ships with a small MCP server that communicates directly with the API. Start it with:

```bash
python dojo_mcp.py
```

The server exposes tools to query products, engagements and findings and to update finding status. It is also
included as the `mcp` service in `docker-compose.yml`, listening on port `8010`.
Set `DEFECTDOJO_API_TOKEN` if authentication is required.


### Using Copilot Agent in VS Code

1. Install the **GitHub Copilot Chat** extension.
2. Add a workspace setting `.vscode/settings.json`:
   ```json
   {
       "github.copilot.agent.custom": {
           "dojo": "http://localhost:8010/mcp"
       }
   }
   ```
3. Launch the MCP server with `python dojo_mcp.py`.
4. Copilot sends a JSON-RPC `initialize` request to the MCP server when connecting. Ensure the service is running and reachable.

## Community, Getting Involved, and Updates

[<img src="https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/dev/docs/assets/images/slack-logo-icon.png" alt="Slack" height="50"/>](https://owasp.org/slack/invite)
[<img src="https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/dev/docs/assets/images/Linkedin-logo-icon-png.png" alt="LinkedIn" height="50"/>](https://www.linkedin.com/company/defectdojo)
[<img src="https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/dev/docs/assets/images/Twitter_Logo.png" alt="Twitter" height="50"/>](https://twitter.com/defectdojo)
[<img src="https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/dev/docs/assets/images/YouTube-Emblem.png" alt="Youtube" height="50"/>](https://www.youtube.com/channel/UCWw9qzqptiIvTqSqhOFuCuQ)

[Join the OWASP Slack community](https://owasp.org/slack/invite) and participate in the discussion! You can find us in
our channel there, [#defectdojo](https://owasp.slack.com/channels/defectdojo). Follow DefectDojo on
[Twitter](https://twitter.com/defectdojo), [LinkedIn](https://www.linkedin.com/company/defectdojo), and
[YouTube](https://www.youtube.com/channel/UCWw9qzqptiIvTqSqhOFuCuQ) for project updates!

## Contributing

Please see our [contributing guidelines](readme-docs/CONTRIBUTING.md) for more
information.

## Pro Edition
[Upgrade to DefectDojo Pro](https://www.defectdojo.com/) today to take your DevSecOps to 11. DefectDojo Pro is
designed to meet you wherever you are on your security journey and help you scale, with enhanced dashboards, additional
smart features, tunable deduplication, and support from DevSecOps experts.

Alternatively, for information please email info@defectdojo.com

## About Us

DefectDojo is maintained by:
* Greg Anderson ([@devGregA](https://github.com/devgrega) | [LinkedIn](https://www.linkedin.com/in/g-anderson/))
* Matt Tesauro ([@mtesauro](https://github.com/mtesauro) | [LinkedIn](https://www.linkedin.com/in/matttesauro/) |
  [@matt_tesauro](https://twitter.com/matt_tesauro))

Core Moderators can help you with pull requests or feedback on dev ideas:
* Cody Maffucci ([@Maffooch](https://github.com/maffooch) | [LinkedIn](https://www.linkedin.com/in/cody-maffucci))

Moderators can help you with pull requests or feedback on dev ideas:
* Charles Neill ([@cneill](https://github.com/cneill) | [@ccneill](https://twitter.com/ccneill))
* Blake Owens ([@blakeaowens](https://github.com/blakeaowens))

## Hall of Fame
* Jannik Jürgens ([@alles-klar](https://github.com/alles-klar)) - Jannik was a long time contributor and moderator for 
  DefectDojo and made significant contributions to many areas of the platform. Jannik was instrumental in pioneering 
  and optimizing deployment methods.
* Valentijn Scholten ([@valentijnscholten](https://github.com/valentijnscholten) |
  [Sponsor](https://github.com/sponsors/valentijnscholten) |
  [LinkedIn](https://www.linkedin.com/in/valentijn-scholten/)) - Valentijn served as a core moderator for 3 years.
  Valentijn's contributions were numerous and extensive. He overhauled, improved, and optimized many parts of the
  codebase. He consistently fielded questions, provided feedback on pull requests, and provided a helping hand wherever
  it was needed.
* Fred Blaise ([@madchap](https://github.com/madchap) | [LinkedIn](https://www.linkedin.com/in/fredblaise/)) - Fred
  served as a core moderator during a critical time for DefectDojo. He contributed code, helped the team stay organized,
  and architected important policies and procedures.
* Aaron Weaver ([@aaronweaver](https://github.com/aaronweaver) | [LinkedIn](https://www.linkedin.com/in/aweaver/)) -
  Aaron has been a long time contributor and user of DefectDojo. He did the second major UI overhaul and his
  contributions include automation enhancements, CI/CD engagements, increased metadata at the product level, and many
  more.

## Security

Please report Security issues via our [disclosure policy](readme-docs/SECURITY.md).

## License

DefectDojo is licensed under the [BSD 3-Clause License](LICENSE.md)
