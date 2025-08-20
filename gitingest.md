Directory structure:
└── coderamp-labs-gitingest/
    ├── README.md
    ├── CHANGELOG.md
    ├── CODE_OF_CONDUCT.md
    ├── compose.yml
    ├── CONTRIBUTING.md
    ├── Dockerfile
    ├── eslint.config.cjs
    ├── LICENSE
    ├── pyproject.toml
    ├── release-please-config.json
    ├── renovate.json
    ├── requirements-dev.txt
    ├── requirements.txt
    ├── SECURITY.md
    ├── .dockerignore
    ├── .env.example
    ├── .pre-commit-config.yaml
    ├── .release-please-manifest.json
    ├── src/
    │   ├── gitingest/
    │   │   ├── __init__.py
    │   │   ├── __main__.py
    │   │   ├── clone.py
    │   │   ├── config.py
    │   │   ├── entrypoint.py
    │   │   ├── ingestion.py
    │   │   ├── output_formatter.py
    │   │   ├── query_parser.py
    │   │   ├── schemas/
    │   │   │   ├── __init__.py
    │   │   │   ├── cloning.py
    │   │   │   ├── filesystem.py
    │   │   │   └── ingestion.py
    │   │   └── utils/
    │   │       ├── __init__.py
    │   │       ├── auth.py
    │   │       ├── compat_func.py
    │   │       ├── compat_typing.py
    │   │       ├── exceptions.py
    │   │       ├── file_utils.py
    │   │       ├── git_utils.py
    │   │       ├── ignore_patterns.py
    │   │       ├── ingestion_utils.py
    │   │       ├── logging_config.py
    │   │       ├── notebook.py
    │   │       ├── os_utils.py
    │   │       ├── pattern_utils.py
    │   │       ├── query_parser_utils.py
    │   │       └── timeout_wrapper.py
    │   ├── server/
    │   │   ├── __init__.py
    │   │   ├── __main__.py
    │   │   ├── form_types.py
    │   │   ├── main.py
    │   │   ├── metrics_server.py
    │   │   ├── models.py
    │   │   ├── query_processor.py
    │   │   ├── routers_utils.py
    │   │   ├── s3_utils.py
    │   │   ├── server_config.py
    │   │   ├── server_utils.py
    │   │   ├── routers/
    │   │   │   ├── __init__.py
    │   │   │   ├── dynamic.py
    │   │   │   ├── index.py
    │   │   │   └── ingest.py
    │   │   └── templates/
    │   │       ├── base.jinja
    │   │       ├── git.jinja
    │   │       ├── index.jinja
    │   │       ├── swagger_ui.jinja
    │   │       └── components/
    │   │           ├── _macros.jinja
    │   │           ├── footer.jinja
    │   │           ├── git_form.jinja
    │   │           ├── navbar.jinja
    │   │           ├── result.jinja
    │   │           └── tailwind_components.html
    │   └── static/
    │       ├── llms.txt
    │       ├── robots.txt
    │       └── js/
    │           ├── git.js
    │           ├── git_form.js
    │           ├── index.js
    │           ├── navbar.js
    │           ├── posthog.js
    │           └── utils.js
    ├── tests/
    │   ├── __init__.py
    │   ├── conftest.py
    │   ├── test_cli.py
    │   ├── test_clone.py
    │   ├── test_git_utils.py
    │   ├── test_gitignore_feature.py
    │   ├── test_ingestion.py
    │   ├── test_notebook_utils.py
    │   ├── test_pattern_utils.py
    │   ├── test_summary.py
    │   ├── .pylintrc
    │   ├── query_parser/
    │   │   ├── __init__.py
    │   │   ├── test_git_host_agnostic.py
    │   │   └── test_query_parser.py
    │   └── server/
    │       ├── __init__.py
    │       └── test_flow_integration.py
    ├── .docker/
    │   └── minio/
    │       └── setup.sh
    └── .github/
        ├── ISSUE_TEMPLATE/
        │   ├── bug_report.yml
        │   └── feature_request.yml
        └── workflows/
            ├── ci.yml
            ├── codeql.yml
            ├── dependency-review.yml
            ├── deploy-pr.yml
            ├── docker-build.ecr.yml
            ├── docker-build.ghcr.yml
            ├── pr-title-check.yml
            ├── publish_to_pypi.yml
            ├── rebase-needed.yml
            ├── release-please.yml
            ├── scorecard.yml
            └── stale.yml


Files Content:

================================================
FILE: README.md
================================================
# Gitingest

[![Screenshot of Gitingest front page](https://raw.githubusercontent.com/coderamp-labs/gitingest/refs/heads/main/docs/frontpage.png)](https://gitingest.com)

<!-- Badges -->
<!-- markdownlint-disable MD033 -->
<p align="center">
  <!-- row 1 — install & compat -->
  <a href="https://pypi.org/project/gitingest"><img src="https://img.shields.io/pypi/v/gitingest.svg" alt="PyPI"></a>
  <a href="https://pypi.org/project/gitingest"><img src="https://img.shields.io/pypi/pyversions/gitingest.svg" alt="Python Versions"></a>
  <br>
  <!-- row 2 — quality & community -->
  <a href="https://github.com/coderamp-labs/gitingest/actions/workflows/ci.yml?query=branch%3Amain"><img src="https://github.com/coderamp-labs/gitingest/actions/workflows/ci.yml/badge.svg?branch=main" alt="CI"></a>

  <a href="https://github.com/astral-sh/ruff"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff"></a>
  <a href="https://scorecard.dev/viewer/?uri=github.com/coderamp-labs/gitingest"><img src="https://api.scorecard.dev/projects/github.com/coderamp-labs/gitingest/badge" alt="OpenSSF Scorecard"></a>
  <br>
  <a href="https://github.com/coderamp-labs/gitingest/blob/main/LICENSE"><img src="https://img.shields.io/github/license/coderamp-labs/gitingest.svg" alt="License"></a>
  <a href="https://pepy.tech/project/gitingest"><img src="https://pepy.tech/badge/gitingest" alt="Downloads"></a>
  <a href="https://github.com/coderamp-labs/gitingest"><img src="https://img.shields.io/github/stars/coderamp-labs/gitingest" alt="GitHub Stars"></a>
  <a href="https://discord.com/invite/zerRaGK9EC"><img src="https://img.shields.io/badge/Discord-Join_chat-5865F2?logo=discord&logoColor=white" alt="Discord"></a>
  <br>
  <a href="https://trendshift.io/repositories/13519"><img src="https://trendshift.io/api/badge/repositories/13519" alt="Trendshift" height="50"></a>
</p>
<!-- markdownlint-enable MD033 -->

Turn any Git repository into a prompt-friendly text ingest for LLMs.

You can also replace `hub` with `ingest` in any GitHub URL to access the corresponding digest.

<!-- Extensions -->
[gitingest.com](https://gitingest.com) · [Chrome Extension](https://chromewebstore.google.com/detail/adfjahbijlkjfoicpjkhjicpjpjfaood) · [Firefox Add-on](https://addons.mozilla.org/firefox/addon/gitingest)

<!-- Languages -->
[Deutsch](https://www.readme-i18n.com/coderamp-labs/gitingest?lang=de) |
[Español](https://www.readme-i18n.com/coderamp-labs/gitingest?lang=es) |
[Français](https://www.readme-i18n.com/coderamp-labs/gitingest?lang=fr) |
[日本語](https://www.readme-i18n.com/coderamp-labs/gitingest?lang=ja) |
[한국어](https://www.readme-i18n.com/coderamp-labs/gitingest?lang=ko) |
[Português](https://www.readme-i18n.com/coderamp-labs/gitingest?lang=pt) |
[Русский](https://www.readme-i18n.com/coderamp-labs/gitingest?lang=ru) |
[中文](https://www.readme-i18n.com/coderamp-labs/gitingest?lang=zh)

## 🚀 Features

- **Easy code context**: Get a text digest from a Git repository URL or a directory
- **Smart Formatting**: Optimized output format for LLM prompts
- **Statistics about**:
  - File and directory structure
  - Size of the extract
  - Token count
- **CLI tool**: Run it as a shell command
- **Python package**: Import it in your code

## 📚 Requirements

- Python 3.8+
- For private repositories: A GitHub Personal Access Token (PAT). [Generate your token **here**!](https://github.com/settings/tokens/new?description=gitingest&scopes=repo)

### 📦 Installation

Gitingest is available on [PyPI](https://pypi.org/project/gitingest/).
You can install it using `pip`:

```bash
pip install gitingest
```

or

```bash
pip install gitingest[server]
```

to include server dependencies for self-hosting.

However, it might be a good idea to use `pipx` to install it.
You can install `pipx` using your preferred package manager.

```bash
brew install pipx
apt install pipx
scoop install pipx
...
```

If you are using pipx for the first time, run:

```bash
pipx ensurepath
```

```bash
# install gitingest
pipx install gitingest
```

## 🧩 Browser Extension Usage

<!-- markdownlint-disable MD033 -->
<a href="https://chromewebstore.google.com/detail/adfjahbijlkjfoicpjkhjicpjpjfaood" target="_blank" title="Get Gitingest Extension from Chrome Web Store"><img height="48" src="https://github.com/user-attachments/assets/20a6e44b-fd46-4e6c-8ea6-aad436035753" alt="Available in the Chrome Web Store" /></a>
<a href="https://addons.mozilla.org/firefox/addon/gitingest" target="_blank" title="Get Gitingest Extension from Firefox Add-ons"><img height="48" src="https://github.com/user-attachments/assets/c0e99e6b-97cf-4af2-9737-099db7d3538b" alt="Get The Add-on for Firefox" /></a>
<a href="https://microsoftedge.microsoft.com/addons/detail/nfobhllgcekbmpifkjlopfdfdmljmipf" target="_blank" title="Get Gitingest Extension from Microsoft Edge Add-ons"><img height="48" src="https://github.com/user-attachments/assets/204157eb-4cae-4c0e-b2cb-db514419fd9e" alt="Get from the Edge Add-ons" /></a>
<!-- markdownlint-enable MD033 -->

The extension is open source at [lcandy2/gitingest-extension](https://github.com/lcandy2/gitingest-extension).

Issues and feature requests are welcome to the repo.

## 💡 Command line usage

The `gitingest` command line tool allows you to analyze codebases and create a text dump of their contents.

```bash
# Basic usage (writes to digest.txt by default)
gitingest /path/to/directory

# From URL
gitingest https://github.com/coderamp-labs/gitingest

# or from specific subdirectory
gitingest https://github.com/coderamp-labs/gitingest/tree/main/src/gitingest/utils
```

For private repositories, use the `--token/-t` option.

```bash
# Get your token from https://github.com/settings/personal-access-tokens
gitingest https://github.com/username/private-repo --token github_pat_...

# Or set it as an environment variable
export GITHUB_TOKEN=github_pat_...
gitingest https://github.com/username/private-repo

# Include repository submodules
gitingest https://github.com/username/repo-with-submodules --include-submodules
```

By default, files listed in `.gitignore` are skipped. Use `--include-gitignored` if you
need those files in the digest.

By default, the digest is written to a text file (`digest.txt`) in your current working directory. You can customize the output in two ways:

- Use `--output/-o <filename>` to write to a specific file.
- Use `--output/-o -` to output directly to `STDOUT` (useful for piping to other tools).

See more options and usage details with:

```bash
gitingest --help
```

## 🐍 Python package usage

```python
# Synchronous usage
from gitingest import ingest

summary, tree, content = ingest("path/to/directory")

# or from URL
summary, tree, content = ingest("https://github.com/coderamp-labs/gitingest")

# or from a specific subdirectory
summary, tree, content = ingest("https://github.com/coderamp-labs/gitingest/tree/main/src/gitingest/utils")
```

For private repositories, you can pass a token:

```python
# Using token parameter
summary, tree, content = ingest("https://github.com/username/private-repo", token="github_pat_...")

# Or set it as an environment variable
import os
os.environ["GITHUB_TOKEN"] = "github_pat_..."
summary, tree, content = ingest("https://github.com/username/private-repo")

# Include repository submodules
summary, tree, content = ingest("https://github.com/username/repo-with-submodules", include_submodules=True)
```

By default, this won't write a file but can be enabled with the `output` argument.

```python
# Asynchronous usage
from gitingest import ingest_async
import asyncio

result = asyncio.run(ingest_async("path/to/directory"))
```

### Jupyter notebook usage

```python
from gitingest import ingest_async

# Use await directly in Jupyter
summary, tree, content = await ingest_async("path/to/directory")

```

This is because Jupyter notebooks are asynchronous by default.

## 🐳 Self-host

### Using Docker

1. Build the image:

   ``` bash
   docker build -t gitingest .
   ```

2. Run the container:

   ``` bash
   docker run -d --name gitingest -p 8000:8000 gitingest
   ```

The application will be available at `http://localhost:8000`.

If you are hosting it on a domain, you can specify the allowed hostnames via env variable `ALLOWED_HOSTS`.

   ```bash
   # Default: "gitingest.com, *.gitingest.com, localhost, 127.0.0.1".
   ALLOWED_HOSTS="example.com, localhost, 127.0.0.1"
   ```

### Environment Variables

The application can be configured using the following environment variables:

- **ALLOWED_HOSTS**: Comma-separated list of allowed hostnames (default: "gitingest.com, *.gitingest.com, localhost, 127.0.0.1")
- **GITINGEST_METRICS_ENABLED**: Enable Prometheus metrics server (set to any value to enable)
- **GITINGEST_METRICS_HOST**: Host for the metrics server (default: "127.0.0.1")
- **GITINGEST_METRICS_PORT**: Port for the metrics server (default: "9090")
- **GITINGEST_SENTRY_ENABLED**: Enable Sentry error tracking (set to any value to enable)
- **GITINGEST_SENTRY_DSN**: Sentry DSN (required if Sentry is enabled)
- **GITINGEST_SENTRY_TRACES_SAMPLE_RATE**: Sampling rate for performance data (default: "1.0", range: 0.0-1.0)
- **GITINGEST_SENTRY_PROFILE_SESSION_SAMPLE_RATE**: Sampling rate for profile sessions (default: "1.0", range: 0.0-1.0)
- **GITINGEST_SENTRY_PROFILE_LIFECYCLE**: Profile lifecycle mode (default: "trace")
- **GITINGEST_SENTRY_SEND_DEFAULT_PII**: Send default personally identifiable information (default: "true")
- **S3_ALIAS_HOST**: Public URL/CDN for accessing S3 resources (default: "127.0.0.1:9000/gitingest-bucket")
- **S3_DIRECTORY_PREFIX**: Optional prefix for S3 file paths (if set, prefixes all S3 paths with this value)

### Using Docker Compose

The project includes a `compose.yml` file that allows you to easily run the application in both development and production environments.

#### Compose File Structure

The `compose.yml` file uses YAML anchoring with `&app-base` and `<<: *app-base` to define common configuration that is shared between services:

```yaml
# Common base configuration for all services
x-app-base: &app-base
  build:
    context: .
    dockerfile: Dockerfile
  ports:
    - "${APP_WEB_BIND:-8000}:8000"  # Main application port
    - "${GITINGEST_METRICS_HOST:-127.0.0.1}:${GITINGEST_METRICS_PORT:-9090}:9090"  # Metrics port
  # ... other common configurations
```

#### Services

The file defines three services:

1. **app**: Production service configuration
   - Uses the `prod` profile
   - Sets the Sentry environment to "production"
   - Configured for stable operation with `restart: unless-stopped`

2. **app-dev**: Development service configuration
   - Uses the `dev` profile
   - Enables debug mode
   - Mounts the source code for live development
   - Uses hot reloading for faster development

3. **minio**: S3-compatible object storage for development
   - Uses the `dev` profile (only available in development mode)
   - Provides S3-compatible storage for local development
   - Accessible via:
     - API: Port 9000 ([localhost:9000](http://localhost:9000))
     - Web Console: Port 9001 ([localhost:9001](http://localhost:9001))
   - Default admin credentials:
     - Username: `minioadmin`
     - Password: `minioadmin`
   - Configurable via environment variables:
     - `MINIO_ROOT_USER`: Custom admin username (default: minioadmin)
     - `MINIO_ROOT_PASSWORD`: Custom admin password (default: minioadmin)
   - Includes persistent storage via Docker volume
   - Auto-creates a bucket and application-specific credentials:
     - Bucket name: `gitingest-bucket` (configurable via `S3_BUCKET_NAME`)
     - Access key: `gitingest` (configurable via `S3_ACCESS_KEY`)
     - Secret key: `gitingest123` (configurable via `S3_SECRET_KEY`)
   - These credentials are automatically passed to the app-dev service via environment variables:
     - `S3_ENDPOINT`: URL of the MinIO server
     - `S3_ACCESS_KEY`: Access key for the S3 bucket
     - `S3_SECRET_KEY`: Secret key for the S3 bucket
     - `S3_BUCKET_NAME`: Name of the S3 bucket
     - `S3_REGION`: Region for the S3 bucket (default: us-east-1)
     - `S3_ALIAS_HOST`: Public URL/CDN for accessing S3 resources (default: "127.0.0.1:9000/gitingest-bucket")

#### Usage Examples

To run the application in development mode:

```bash
docker compose --profile dev up
```

To run the application in production mode:

```bash
docker compose --profile prod up -d
```

To build and run the application:

```bash
docker compose --profile prod build
docker compose --profile prod up -d
```

## 🤝 Contributing

### Non-technical ways to contribute

- **Create an Issue**: If you find a bug or have an idea for a new feature, please [create an issue](https://github.com/coderamp-labs/gitingest/issues/new) on GitHub. This will help us track and prioritize your request.
- **Spread the Word**: If you like Gitingest, please share it with your friends, colleagues, and on social media. This will help us grow the community and make Gitingest even better.
- **Use Gitingest**: The best feedback comes from real-world usage! If you encounter any issues or have ideas for improvement, please let us know by [creating an issue](https://github.com/coderamp-labs/gitingest/issues/new) on GitHub or by reaching out to us on [Discord](https://discord.com/invite/zerRaGK9EC).

### Technical ways to contribute

Gitingest aims to be friendly for first time contributors, with a simple Python and HTML codebase. If you need any help while working with the code, reach out to us on [Discord](https://discord.com/invite/zerRaGK9EC). For detailed instructions on how to make a pull request, see [CONTRIBUTING.md](./CONTRIBUTING.md).

## 🛠️ Stack

- [Tailwind CSS](https://tailwindcss.com) - Frontend
- [FastAPI](https://github.com/fastapi/fastapi) - Backend framework
- [Jinja2](https://jinja.palletsprojects.com) - HTML templating
- [tiktoken](https://github.com/openai/tiktoken) - Token estimation
- [posthog](https://github.com/PostHog/posthog) - Amazing analytics
- [Sentry](https://sentry.io) - Error tracking and performance monitoring

### Looking for a JavaScript/FileSystemNode package?

Check out the NPM alternative 📦 Repomix: <https://github.com/yamadashy/repomix>

## 🚀 Project Growth

[![Star History Chart](https://api.star-history.com/svg?repos=coderamp-labs/gitingest&type=Date)](https://star-history.com/#coderamp-labs/gitingest&Date)



================================================
FILE: CHANGELOG.md
================================================
# Changelog

## [0.3.1](https://github.com/coderamp-labs/gitingest/compare/v0.3.0...v0.3.1) (2025-07-31)


### Bug Fixes

* make cache aware of subpaths ([#481](https://github.com/coderamp-labs/gitingest/issues/481)) ([8b59bef](https://github.com/coderamp-labs/gitingest/commit/8b59bef541f858ef44eba8fce6ace77df9dea01c))

## [0.3.0](https://github.com/coderamp-labs/gitingest/compare/v0.2.1...v0.3.0) (2025-07-30)


### Features

* **logging:** implement loguru ([#473](https://github.com/coderamp-labs/gitingest/issues/473)) ([d061b48](https://github.com/coderamp-labs/gitingest/commit/d061b4877a253ba3f0480d329f025427c7f70177))
* serve cached digest if available ([#462](https://github.com/coderamp-labs/gitingest/issues/462)) ([efe5a26](https://github.com/coderamp-labs/gitingest/commit/efe5a2686142b5ee4984061ebcec23c3bf3495d5))


### Bug Fixes

* handle network errors gracefully in token count estimation ([#437](https://github.com/coderamp-labs/gitingest/issues/437)) ([5fbb445](https://github.com/coderamp-labs/gitingest/commit/5fbb445cd8725e56972f43ec8b5e12cb299e9e83))
* improved server side cleanup after ingest ([#477](https://github.com/coderamp-labs/gitingest/issues/477)) ([2df0eb4](https://github.com/coderamp-labs/gitingest/commit/2df0eb43989731ae40a9dd82d310ff76a794a46d))


### Documentation

* **contributing:** update PR title guidelines to enforce convention ([#476](https://github.com/coderamp-labs/gitingest/issues/476)) ([d1f8a80](https://github.com/coderamp-labs/gitingest/commit/d1f8a80826ca38ec105a1878742fe351d4939d6e))

## [0.2.1](https://github.com/coderamp-labs/gitingest/compare/v0.2.0...v0.2.1) (2025-07-27)


### Bug Fixes

* remove logarithm conversion from the backend and correctly process max file size in kb ([#464](https://github.com/coderamp-labs/gitingest/issues/464)) ([932bfef](https://github.com/coderamp-labs/gitingest/commit/932bfef85db66704985c83f3f7c427756bd14023))

## [0.2.0](https://github.com/coderamp-labs/gitingest/compare/v0.1.5...v0.2.0) (2025-07-26)

### Features

* `include_submodules` option ([#313](https://github.com/coderamp-labs/gitingest/issues/313)) ([38c2317](https://github.com/coderamp-labs/gitingest/commit/38c23171a14556a2cdd05c0af8219f4dc789defd))
* add Tailwind CSS pipeline, tag-aware cloning & overhaul CI/CD ([#352](https://github.com/coderamp-labs/gitingest/issues/352)) ([b683e59](https://github.com/coderamp-labs/gitingest/commit/b683e59b5b1a31d27cc5c6ce8fb62da9b660613b))
* add Tailwind CSS pipeline, tag-aware cloning & overhaul CI/CD ([#352](https://github.com/coderamp-labs/gitingest/issues/352)) ([016817d](https://github.com/coderamp-labs/gitingest/commit/016817d5590c1412498b7532f6e854d20239c6be))
* **ci:** build Docker Image on PRs ([#382](https://github.com/coderamp-labs/gitingest/issues/382)) ([bc8cdb4](https://github.com/coderamp-labs/gitingest/commit/bc8cdb459482948c27e780b733ac7216d822529a))
* implement prometheus exporter ([#406](https://github.com/coderamp-labs/gitingest/issues/406)) ([1016f6e](https://github.com/coderamp-labs/gitingest/commit/1016f6ecb3b1b066d541d1eba1ddffec49b15f16))
* implement S3 integration for storing and retrieving digest files ([#427](https://github.com/coderamp-labs/gitingest/issues/427)) ([414e851](https://github.com/coderamp-labs/gitingest/commit/414e85189fb9055491530ba8c0665c798474451e))
* integrate Sentry for error tracking and performance monitoring ([#408](https://github.com/coderamp-labs/gitingest/issues/408)) ([590e55a](https://github.com/coderamp-labs/gitingest/commit/590e55a4d28a4f5c0beafbd12c525828fa79e221))
* Refactor backend to a rest api ([#346](https://github.com/coderamp-labs/gitingest/issues/346)) ([2b1f228](https://github.com/coderamp-labs/gitingest/commit/2b1f228ae1f6d1f7ee471794d258b13fcac25a96))
* **ui:** add inline PAT info tooltip inside token field ([#348](https://github.com/coderamp-labs/gitingest/issues/348)) ([2592303](https://github.com/coderamp-labs/gitingest/commit/25923037ea6cd2f8ef33a6cf1f0406c2b4f0c9b6))


### Bug Fixes

* enable metrics if env var is defined instead of being "True" ([#407](https://github.com/coderamp-labs/gitingest/issues/407)) ([fa2e192](https://github.com/coderamp-labs/gitingest/commit/fa2e192c05864c8db90bda877e9efb9b03caf098))
* fix docker container not launching ([#449](https://github.com/coderamp-labs/gitingest/issues/449)) ([998cea1](https://github.com/coderamp-labs/gitingest/commit/998cea15b4f79c5d6f840b5d3d916f83c8be3a07))
* frontend directory tree ([#363](https://github.com/coderamp-labs/gitingest/issues/363)) ([0fcf8a9](https://github.com/coderamp-labs/gitingest/commit/0fcf8a956f7ec8403a025177f998f92ddee96de0))
* gitignore and gitingestignore files are now correctly processed … ([#416](https://github.com/coderamp-labs/gitingest/issues/416)) ([74e503f](https://github.com/coderamp-labs/gitingest/commit/74e503fa1140feb74aa5350a32f0025c43097da1))
* Potential fix for code scanning alert no. 75: Uncontrolled data used in path expression ([#421](https://github.com/coderamp-labs/gitingest/issues/421)) ([9ceaf6c](https://github.com/coderamp-labs/gitingest/commit/9ceaf6cbbb0cdefbc79f78c5285406b9188b2d3d))
* reset pattern form when switching between include/exclude patterns ([#417](https://github.com/coderamp-labs/gitingest/issues/417)) ([7085e13](https://github.com/coderamp-labs/gitingest/commit/7085e138a74099b1df189b3bf9b8a333c8769380))
* temp files cleanup after ingest([#309](https://github.com/coderamp-labs/gitingest/issues/309)) ([e669e44](https://github.com/coderamp-labs/gitingest/commit/e669e444fa1e6130f3f22952dd81f0ca3fe08fa5))
* **ui:** update layout in PAT section to avoid overlaps & overflows ([#331](https://github.com/coderamp-labs/gitingest/issues/331)) ([b39ef54](https://github.com/coderamp-labs/gitingest/commit/b39ef5416c1f8a7993a8249161d2a898b7387595))
* **windows:** warn if Git long path support is disabled, do not fail ([b8e375f](https://github.com/coderamp-labs/gitingest/commit/b8e375f71cae7d980cf431396c4414a6dbd0588c))


### Documentation

* add GitHub Issue Form for bug reports ([#403](https://github.com/coderamp-labs/gitingest/issues/403)) ([4546449](https://github.com/coderamp-labs/gitingest/commit/4546449bbc1e4a7ad0950c4b831b8855a98628fd))
* add GitHub Issue Form for feature requests ([#404](https://github.com/coderamp-labs/gitingest/issues/404)) ([9b1fc58](https://github.com/coderamp-labs/gitingest/commit/9b1fc58900ae18a3416fe3cf9b5e301a65a8e9fd))
* Fix CLI help text accuracy ([#332](https://github.com/coderamp-labs/gitingest/issues/332)) ([fdcbc53](https://github.com/coderamp-labs/gitingest/commit/fdcbc53cadde6a5dc3c3626120df1935b63693b2))


### Code Refactoring

* centralize PAT validation, streamline repo checks & misc cleanup ([#349](https://github.com/coderamp-labs/gitingest/issues/349)) ([cea0edd](https://github.com/coderamp-labs/gitingest/commit/cea0eddce8c6846bc6271cb3a8d15320e103214c))
* centralize PAT validation, streamline repo checks & misc cleanup ([#349](https://github.com/coderamp-labs/gitingest/issues/349)) ([f8d397e](https://github.com/coderamp-labs/gitingest/commit/f8d397e66e3382d12f8a0ed05d291a39db830bda))



================================================
FILE: CODE_OF_CONDUCT.md
================================================
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
<romain@coderamp.io>.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant](https://www.contributor-covenant.org),
version 2.0, available at
<https://www.contributor-covenant.org/version/2/0/code_of_conduct.html>.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

For answers to common questions about this code of conduct, see the FAQ at
<https://www.contributor-covenant.org/faq>. Translations are available at
<https://www.contributor-covenant.org/translations>.



================================================
FILE: compose.yml
================================================
x-base-environment: &base-environment
  # Python Configuration
  PYTHONUNBUFFERED: "1"
  PYTHONDONTWRITEBYTECODE: "1"
  # Host Configuration
  ALLOWED_HOSTS: ${ALLOWED_HOSTS:-gitingest.com,*.gitingest.com,localhost,127.0.0.1}
  # Metrics Configuration
  GITINGEST_METRICS_ENABLED: ${GITINGEST_METRICS_ENABLED:-true}
  GITINGEST_METRICS_HOST: ${GITINGEST_METRICS_HOST:-0.0.0.0}
  GITINGEST_METRICS_PORT: ${GITINGEST_METRICS_PORT:-9090}
  # Sentry Configuration
  GITINGEST_SENTRY_ENABLED: ${GITINGEST_SENTRY_ENABLED:-false}
  GITINGEST_SENTRY_DSN: ${GITINGEST_SENTRY_DSN:-}
  GITINGEST_SENTRY_TRACES_SAMPLE_RATE: ${GITINGEST_SENTRY_TRACES_SAMPLE_RATE:-1.0}
  GITINGEST_SENTRY_PROFILE_SESSION_SAMPLE_RATE: ${GITINGEST_SENTRY_PROFILE_SESSION_SAMPLE_RATE:-1.0}
  GITINGEST_SENTRY_PROFILE_LIFECYCLE: ${GITINGEST_SENTRY_PROFILE_LIFECYCLE:-trace}
  GITINGEST_SENTRY_SEND_DEFAULT_PII: ${GITINGEST_SENTRY_SEND_DEFAULT_PII:-true}

x-prod-environment: &prod-environment
  GITINGEST_SENTRY_ENVIRONMENT: ${GITINGEST_SENTRY_ENVIRONMENT:-production}

x-dev-environment: &dev-environment
  DEBUG: "true"
  LOG_LEVEL: "DEBUG"
  RELOAD: "true"
  GITINGEST_SENTRY_ENVIRONMENT: ${GITINGEST_SENTRY_ENVIRONMENT:-development}
  # S3 Configuration for development
  S3_ENABLED: "true"
  S3_ENDPOINT: http://minio:9000
  S3_ACCESS_KEY: ${S3_ACCESS_KEY:-gitingest}
  S3_SECRET_KEY: ${S3_SECRET_KEY:-gitingest123}
  S3_BUCKET_NAME: ${S3_BUCKET_NAME:-gitingest-bucket}
  S3_REGION: ${S3_REGION:-us-east-1}
  S3_DIRECTORY_PREFIX: ${S3_DIRECTORY_PREFIX:-dev}
  S3_ALIAS_HOST: ${S3_ALIAS_HOST:-http://127.0.0.1:9000/${S3_BUCKET_NAME:-gitingest-bucket}}

x-app-base: &app-base
  ports:
    - "${APP_WEB_BIND:-8000}:8000"  # Main application port
    - "${GITINGEST_METRICS_HOST:-127.0.0.1}:${GITINGEST_METRICS_PORT:-9090}:9090"  # Metrics port
  user: "1000:1000"
  command: ["python", "-m", "server"]

services:
  # Production service configuration
  app:
    <<: *app-base
    image: ghcr.io/coderamp-labs/gitingest:latest
    profiles:
      - prod
    environment:
      <<: [*base-environment, *prod-environment]
    restart: unless-stopped

  # Development service configuration
  app-dev:
    <<: *app-base
    build:
      context: .
      dockerfile: Dockerfile
    profiles:
      - dev
    environment:
      <<: [*base-environment, *dev-environment]
    volumes:
      # Mount source code for live development
      - ./src:/app:ro
    # Use --reload flag for hot reloading during development
    command: ["python", "-m", "server"]
    depends_on:
      minio-setup:
        condition: service_completed_successfully

  # MinIO S3-compatible object storage for development
  minio:
    image: minio/minio:latest
    profiles:
      - dev
    ports:
      - "9000:9000"  # API port
      - "9001:9001"  # Console port
    environment: &minio-environment
      MINIO_ROOT_USER: ${MINIO_ROOT_USER:-minioadmin}
      MINIO_ROOT_PASSWORD: ${MINIO_ROOT_PASSWORD:-minioadmin}
    volumes:
      - minio-data:/data
    command: server /data --console-address ":9001"
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9000/minio/health/live"]
      interval: 30s
      timeout: 30s
      start_period: 30s
      start_interval: 1s

  # MinIO setup service to create bucket and user
  minio-setup:
    image: minio/mc
    profiles:
      - dev
    depends_on:
      minio:
        condition: service_healthy
    environment:
      <<: *minio-environment
      S3_ACCESS_KEY: ${S3_ACCESS_KEY:-gitingest}
      S3_SECRET_KEY: ${S3_SECRET_KEY:-gitingest123}
      S3_BUCKET_NAME: ${S3_BUCKET_NAME:-gitingest-bucket}
    volumes:
      - ./.docker/minio/setup.sh:/setup.sh:ro
    entrypoint: sh
    command: -c /setup.sh

volumes:
  minio-data:
    driver: local



================================================
FILE: CONTRIBUTING.md
================================================
# Contributing to Gitingest

Thanks for your interest in contributing to **Gitingest** 🚀 Our goal is to keep the codebase friendly to first-time
contributors.
If you ever get stuck, reach out on [Discord](https://discord.com/invite/zerRaGK9EC).

---

## How to Contribute (non-technical)

- **Create an Issue** – found a bug or have a feature idea?
  [Open an issue](https://github.com/coderamp-labs/gitingest/issues/new).
- **Spread the Word** – tweet, blog, or tell a friend.
- **Use Gitingest** – real-world usage gives the best feedback. File issues or ping us
  on [Discord](https://discord.com/invite/zerRaGK9EC) with anything you notice.

---

## How to submit a Pull Request

> **Prerequisites**: The project uses **Python 3.9+** and `pre-commit` for development.

1. **Fork** the repository.

2. **Clone** your fork:

   ```bash
   git clone https://github.com/coderamp-labs/gitingest.git
   cd gitingest
   ```

3. **Set up the dev environment**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -e ".[dev,server]"
   pre-commit install
   ```

4. **Create a branch** for your changes:

   ```bash
   git checkout -b your-branch
   ```

5. **Make your changes** (and add tests when relevant).

6. **Stage** the changes:

   ```bash
   git add .
   ```

7. **Run the backend test suite**:

   ```bash
   pytest
   ```

8. *(Optional)* **Run `pre-commit` on all files** to check hooks without committing:

   ```bash
   pre-commit run --all-files
   ```

9. **Run the local server** to sanity-check:

    ```bash
    python -m server
    ```

   Open [http://localhost:8000](http://localhost:8000) to confirm everything works.

10. **Commit** (signed):

    ```bash
    git commit -S -m "Your commit message"
    ```

    If *pre-commit* complains, fix the problems and repeat **5 – 9**.

11. **Push** your branch:

    ```bash
    git push origin your-branch
    ```

12. **Open a pull request** on GitHub with a clear description.

    > **Important:** Pull request titles **must follow
    the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification**. This helps with
    changelogs and automated releases.

13. **Iterate** on any review feedback—update your branch and repeat **6 – 11** as needed.

*(Optional) Invite a maintainer to your branch for easier collaboration.*



================================================
FILE: Dockerfile
================================================
# Stage 1: Install Python dependencies
FROM python:3.13.5-slim@sha256:4c2cf9917bd1cbacc5e9b07320025bdb7cdf2df7b0ceaccb55e9dd7e30987419 AS python-builder

WORKDIR /build

RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends gcc python3-dev; \
    rm -rf /var/lib/apt/lists/*

COPY pyproject.toml .
COPY src/ ./src/

RUN set -eux; \
    pip install --no-cache-dir --upgrade pip; \
    pip install --no-cache-dir --timeout 1000 .[server,mcp]

# Stage 2: Runtime image
FROM python:3.13.5-slim@sha256:4c2cf9917bd1cbacc5e9b07320025bdb7cdf2df7b0ceaccb55e9dd7e30987419

ARG UID=1000
ARG GID=1000
ARG APP_REPOSITORY=https://github.com/coderamp-labs/gitingest
ARG APP_VERSION=unknown
ARG APP_VERSION_URL=https://github.com/coderamp-labs/gitingest

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    APP_REPOSITORY=${APP_REPOSITORY} \
    APP_VERSION=${APP_VERSION} \
    APP_VERSION_URL=${APP_VERSION_URL}

RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends git curl; \
    apt-get clean; \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN set -eux; \
    groupadd -g "$GID" appuser; \
    useradd -m -u "$UID" -g "$GID" appuser

COPY --from=python-builder --chown=$UID:$GID /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --chown=$UID:$GID src/ ./

RUN set -eux; \
    chown -R appuser:appuser /app
USER appuser

EXPOSE 8000
EXPOSE 9090
CMD ["python", "-m", "server"]



================================================
FILE: eslint.config.cjs
================================================
const js = require('@eslint/js');
const globals = require('globals');
const importPlugin = require('eslint-plugin-import');

module.exports = [
  js.configs.recommended,

  {
    files: ['src/static/js/**/*.js'],

    languageOptions: {
      parserOptions: { ecmaVersion: 2021, sourceType: 'module' },
      globals: {
        ...globals.browser,
        changePattern: 'readonly',
        copyFullDigest: 'readonly',
        copyText: 'readonly',
        downloadFullDigest: 'readonly',
        handleSubmit: 'readonly',
        posthog: 'readonly',
        submitExample: 'readonly',
        toggleAccessSettings: 'readonly',
        toggleFile: 'readonly',
      },
    },

    plugins: { import: importPlugin },

    rules: {
      // Import hygiene (eslint-plugin-import)
      'import/no-extraneous-dependencies': 'error',
      'import/no-unresolved': 'error',
      'import/order': ['warn', { alphabetize: { order: 'asc' } }],

      // Safety & bug-catchers
      'consistent-return': 'error',
      'default-case': 'error',
      'no-implicit-globals': 'error',
      'no-shadow': 'error',

      // Maintainability / complexity
      complexity: ['warn', 10],
      'max-depth': ['warn', 4],
      'max-lines': ['warn', 500],
      'max-params': ['warn', 5],

      // Stylistic consistency (auto-fixable)
      'arrow-parens': ['error', 'always'],
      curly: ['error', 'all'],
      indent: ['error', 4, { SwitchCase: 2 }],
      'newline-per-chained-call': ['warn', { ignoreChainWithDepth: 2 }],
      'no-multi-spaces': 'error',
      'object-shorthand': ['error', 'always'],
      'padding-line-between-statements': [
        'warn',
        { blankLine: 'always', prev: '*', next: 'return' },
        { blankLine: 'always', prev: ['const', 'let', 'var'], next: '*' },
        { blankLine: 'any', prev: ['const', 'let', 'var'], next: ['const', 'let', 'var'] },
      ],
      'quote-props': ['error', 'consistent-as-needed'],
      quotes: ['error', 'single', { avoidEscape: true }],
      semi: 'error',

      // Modern / performance tips
      'arrow-body-style': ['warn', 'as-needed'],
      'prefer-arrow-callback': 'error',
      'prefer-exponentiation-operator': 'error',
      'prefer-numeric-literals': 'error',
      'prefer-object-has-own': 'warn',
      'prefer-object-spread': 'error',
      'prefer-template': 'error',
    },
  },
];



================================================
FILE: LICENSE
================================================
MIT License

Copyright (c) 2024 Romain Courtois

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



================================================
FILE: pyproject.toml
================================================
[project]
name = "gitingest"
version = "0.3.1"
description="CLI tool to analyze and create text dumps of codebases for LLMs"
readme = {file = "README.md", content-type = "text/markdown" }
requires-python = ">= 3.8"
dependencies = [
    "click>=8.0.0",
    "gitpython>=3.1.0",
    "httpx",
    "loguru>=0.7.0",
    "pathspec>=0.12.1",
    "pydantic",
    "python-dotenv",
    "starlette>=0.40.0",  # Minimum safe release (https://osv.dev/vulnerability/GHSA-f96h-pmfr-66vw)
    "strenum; python_version < '3.11'",
    "tiktoken>=0.7.0",  # Support for o200k_base encoding
    "typing_extensions>= 4.0.0; python_version < '3.10'",
]

license = {file = "LICENSE"}
authors = [
    { name = "Romain Courtois", email = "romain@coderamp.io" },
    { name = "Filip Christiansen"},
]
classifiers=[
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
]

[project.optional-dependencies]
dev = [
    "eval-type-backport",
    "pre-commit",
    "pytest",
    "pytest-asyncio",
    "pytest-mock",
]

server = [
    "boto3>=1.28.0",  # AWS SDK for S3 support
    "fastapi[standard]>=0.109.1",  # Minimum safe release (https://osv.dev/vulnerability/PYSEC-2024-38)
    "prometheus-client",
    "sentry-sdk[fastapi]",
    "slowapi",
    "uvicorn>=0.11.7",  # Minimum safe release (https://osv.dev/vulnerability/PYSEC-2020-150)
]

[project.scripts]
gitingest = "gitingest.__main__:main"

[project.urls]
homepage = "https://gitingest.com"
github = "https://github.com/coderamp-labs/gitingest"

[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[tool.setuptools]
packages = {find = {where = ["src"]}}
include-package-data = true

# Linting configuration
[tool.pylint.format]
max-line-length = 119

[tool.pylint.'MESSAGES CONTROL']
disable = [
    "too-many-arguments",
    "too-many-positional-arguments",
    "too-many-locals",
    "too-few-public-methods",
    "broad-exception-caught",
    "duplicate-code",
    "fixme",
]

[tool.ruff]
line-length = 119
fix = true

[tool.ruff.lint]
select = ["ALL"]
ignore = [  # https://docs.astral.sh/ruff/rules/...
    "D107", # undocumented-public-init
    "FIX002", # line-contains-todo
    "TD002", # missing-todo-author
    "PLR0913", # too-many-arguments,

    # TODO: fix the following issues:
    "TD003", # missing-todo-link, TODO: add issue links
    "S108", # hardcoded-temp-file, TODO: replace with tempfile
    "BLE001", # blind-except, TODO: replace with specific exceptions
    "FAST003", # fast-api-unused-path-parameter, TODO: fix
]
per-file-ignores = { "tests/**/*.py" = ["S101"] } # Skip the "assert used" warning

[tool.ruff.lint.pylint]
max-returns = 10

[tool.ruff.lint.isort]
order-by-type = true
case-sensitive = true

[tool.pycln]
all = true

# TODO: Remove this once we figure out how to use ruff-isort
[tool.isort]
profile = "black"
line_length = 119
remove_redundant_aliases = true
float_to_top = true  # https://github.com/astral-sh/ruff/issues/6514
order_by_type = true
filter_files = true

# Test configuration
[tool.pytest.ini_options]
pythonpath = ["src"]
testpaths = ["tests/"]
python_files = "test_*.py"
asyncio_mode = "auto"
asyncio_default_fixture_loop_scope = "function"
python_classes = "Test*"
python_functions = "test_*"



================================================
FILE: release-please-config.json
================================================
{
  "$schema": "https://raw.githubusercontent.com/googleapis/release-please/main/schemas/config.json",
  "packages": {
    ".": {
      "release-type": "python",
      "bump-minor-pre-major": true
    }
  }
}



================================================
FILE: renovate.json
================================================
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": [
    "config:recommended"
  ]
}



================================================
FILE: requirements-dev.txt
================================================
-r requirements.txt
eval-type-backport
pre-commit
pytest
pytest-asyncio
pytest-cov
pytest-mock



================================================
FILE: requirements.txt
================================================
boto3>=1.28.0  # AWS SDK for S3 support
click>=8.0.0
fastapi[standard]>=0.109.1  # Vulnerable to https://osv.dev/vulnerability/PYSEC-2024-38
httpx
loguru>=0.7.0
pathspec>=0.12.1
prometheus-client
pydantic
python-dotenv
sentry-sdk[fastapi]
slowapi
starlette>=0.40.0  # Vulnerable to https://osv.dev/vulnerability/GHSA-f96h-pmfr-66vw
tiktoken>=0.7.0  # Support for o200k_base encoding
uvicorn>=0.11.7  # Vulnerable to https://osv.dev/vulnerability/PYSEC-2020-150



================================================
FILE: SECURITY.md
================================================
# Security Policy

## Reporting a Vulnerability

If you have discovered a vulnerability inside the project, report it privately at <romain@coderamp.io>. This way the maintainer can work on a proper fix without disclosing the problem to the public before it has been solved.



================================================
FILE: .dockerignore
================================================
# -------------------------------------------------
# Base: reuse patterns from .gitignore
# -------------------------------------------------

# Operating-system
.DS_Store
Thumbs.db

# Editor / IDE settings
.vscode/
!.vscode/launch.json
.idea/
*.swp

# Python virtual-envs & tooling
.venv*/
.python-version
__pycache__/
*.egg-info/
*.egg
.ruff_cache/

# Test artifacts & coverage
.pytest_cache/
.coverage
coverage.xml
htmlcov/

# Build, distribution & docs
build/
dist/
*.wheel

# Logs & runtime output
*.log
logs/
*.tmp
tmp/

# Project-specific files
history.txt
digest.txt


# -------------------------------------------------
# Extra for Docker
# -------------------------------------------------

# Git history
.git/
.gitignore

# Tests
tests/

# Docs
docs/
*.md
LICENSE

# Local overrides & secrets
.env

# Docker files
.dockerignore
Dockerfile*

# -------------------------------------------------
# Files required during build
# -------------------------------------------------
!pyproject.toml
!src/



================================================
FILE: .env.example
================================================
# Gitingest Environment Variables

# Host Configuration
# Comma-separated list of allowed hostnames
# Default: "gitingest.com, *.gitingest.com, localhost, 127.0.0.1"
ALLOWED_HOSTS=gitingest.com,*.gitingest.com,localhost,127.0.0.1

# GitHub Authentication
# Personal Access Token for accessing private repositories
# Generate your token here: https://github.com/settings/tokens/new?description=gitingest&scopes=repo
# GITHUB_TOKEN=your_github_token_here

# Metrics Configuration
# Set to any value to enable the Prometheus metrics server
# GITINGEST_METRICS_ENABLED=true
# Host for the metrics server (default: "127.0.0.1")
GITINGEST_METRICS_HOST=127.0.0.1
# Port for the metrics server (default: "9090")
GITINGEST_METRICS_PORT=9090

# Sentry Configuration
# Set to any value to enable Sentry error tracking
# GITINGEST_SENTRY_ENABLED=true
# Sentry DSN (required if Sentry is enabled)
# GITINGEST_SENTRY_DSN=your_sentry_dsn_here
# Sampling rate for performance data (default: "1.0", range: 0.0-1.0)
GITINGEST_SENTRY_TRACES_SAMPLE_RATE=1.0
# Sampling rate for profile sessions (default: "1.0", range: 0.0-1.0)
GITINGEST_SENTRY_PROFILE_SESSION_SAMPLE_RATE=1.0
# Profile lifecycle mode (default: "trace")
GITINGEST_SENTRY_PROFILE_LIFECYCLE=trace
# Send default personally identifiable information (default: "true")
GITINGEST_SENTRY_SEND_DEFAULT_PII=true
# Environment name for Sentry (default: "")
GITINGEST_SENTRY_ENVIRONMENT=development

# MinIO Configuration (for development)
# Root user credentials for MinIO admin access
MINIO_ROOT_USER=minioadmin
MINIO_ROOT_PASSWORD=minioadmin

# S3 Configuration (for application)
# Set to "true" to enable S3 storage for digests
# S3_ENABLED=true
# Endpoint URL for the S3 service (MinIO in development)
S3_ENDPOINT=http://minio:9000
# Access key for the S3 bucket (created automatically in development)
S3_ACCESS_KEY=gitingest
# Secret key for the S3 bucket (created automatically in development)
S3_SECRET_KEY=gitingest123
# Name of the S3 bucket (created automatically in development)
S3_BUCKET_NAME=gitingest-bucket
# Region for the S3 bucket (default for MinIO)
S3_REGION=us-east-1
# Public URL/CDN for accessing S3 resources
S3_ALIAS_HOST=127.0.0.1:9000/gitingest-bucket
# Optional prefix for S3 file paths (if set, prefixes all S3 paths with this value)
# S3_DIRECTORY_PREFIX=my-prefix



================================================
FILE: .pre-commit-config.yaml
================================================
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: check-added-large-files
        description: 'Prevent large files from being committed.'
        args: ['--maxkb=10000']

      - id: check-case-conflict
        description: 'Check for files that would conflict in case-insensitive filesystems.'

      - id: fix-byte-order-marker
        description: 'Remove utf-8 byte order marker.'

      - id: mixed-line-ending
        description: 'Replace mixed line ending.'

      - id: destroyed-symlinks
        description: 'Detect symlinks which are changed to regular files with a content of a path which that symlink was pointing to.'

      - id: check-ast
        description: 'Check for parseable syntax.'

      - id: end-of-file-fixer
        description: 'Ensure that a file is either empty, or ends with one newline.'

      - id: trailing-whitespace
        description: 'Trim trailing whitespace.'
        exclude: CHANGELOG.md

      - id: check-docstring-first
        description: 'Check a common error of defining a docstring after code.'

      - id: requirements-txt-fixer
        description: 'Sort entries in requirements.txt.'

  - repo: https://github.com/MarcoGorelli/absolufy-imports
    rev: v0.3.1
    hooks:
      - id: absolufy-imports
        description: 'Automatically convert relative imports to absolute. (Use `args: [--never]` to revert.)'

  - repo: https://github.com/asottile/pyupgrade
    rev: v3.20.0
    hooks:
      - id: pyupgrade
        description: 'Automatically upgrade syntax for newer versions.'
        args: [--py3-plus, --py36-plus]

  - repo: https://github.com/pre-commit/pygrep-hooks
    rev: v1.10.0
    hooks:
      - id: python-check-blanket-noqa
        description: 'Enforce that `# noqa` annotations always occur with specific codes.'

      - id: python-check-blanket-type-ignore
        description: 'Enforce that `# type: ignore` annotations always occur with specific codes.'

      - id: python-use-type-annotations
        description: 'Enforce that python3.6+ type annotations are used instead of type comments.'

  - repo: https://github.com/PyCQA/isort
    rev: 6.0.1
    hooks:
      - id: isort
        description: 'Sort imports alphabetically, and automatically separated into sections and by type.'

  - repo: https://github.com/pre-commit/mirrors-eslint
    rev: v9.30.1
    hooks:
      - id: eslint
        description: 'Lint javascript files.'
        files: \.js$
        args: [--max-warnings=0, --fix]
        additional_dependencies:
          [
            'eslint@9.30.1',
            '@eslint/js@9.30.1',
            'eslint-plugin-import@2.32.0',
            'globals@16.3.0',
          ]

  - repo: https://github.com/djlint/djLint
    rev: v1.36.4
    hooks:
      - id: djlint-reformat-jinja

  - repo: https://github.com/igorshubovych/markdownlint-cli
    rev: v0.45.0
    hooks:
      - id: markdownlint
        description: 'Lint markdown files.'
        args: ['--disable=line-length', '--ignore=CHANGELOG.md']

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.12.2
    hooks:
      - id: ruff-check
      - id: ruff-format

  - repo: https://github.com/jsh9/pydoclint
    rev: 0.6.7
    hooks:
      - id: pydoclint
        name: pydoclint for source
        args: [--style=numpy]
        files: ^src/

  - repo: https://github.com/pycqa/pylint
    rev: v3.3.7
    hooks:
      - id: pylint
        name: pylint for source
        files: ^src/
        additional_dependencies:
          [
            boto3>=1.28.0,
            click>=8.0.0,
            'fastapi[standard]>=0.109.1',
            gitpython>=3.1.0,
            httpx,
            loguru>=0.7.0,
            pathspec>=0.12.1,
            prometheus-client,
            pydantic,
            pytest-asyncio,
            pytest-mock,
            python-dotenv,
            'sentry-sdk[fastapi]',
            slowapi,
            starlette>=0.40.0,
            strenum; python_version < '3.11',
            tiktoken>=0.7.0,
            typing_extensions>= 4.0.0; python_version < '3.10',
            uvicorn>=0.11.7,
          ]

      - id: pylint
        name: pylint for tests
        files: ^tests/
        args:
          - --rcfile=tests/.pylintrc
        additional_dependencies:
          [
            boto3>=1.28.0,
            click>=8.0.0,
            'fastapi[standard]>=0.109.1',
            gitpython>=3.1.0,
            httpx,
            loguru>=0.7.0,
            pathspec>=0.12.1,
            prometheus-client,
            pydantic,
            pytest-asyncio,
            pytest-mock,
            python-dotenv,
            'sentry-sdk[fastapi]',
            slowapi,
            starlette>=0.40.0,
            strenum; python_version < '3.11',
            tiktoken>=0.7.0,
            typing_extensions>= 4.0.0; python_version < '3.10',
            uvicorn>=0.11.7,
          ]

  - repo: meta
    hooks:
      - id: check-hooks-apply
      - id: check-useless-excludes
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.16.3
    hooks:
      - id: gitleaks



================================================
FILE: .release-please-manifest.json
================================================
{".":"0.3.1"}



================================================
FILE: src/gitingest/__init__.py
================================================
"""Gitingest: A package for ingesting data from Git repositories."""

from gitingest.entrypoint import ingest, ingest_async

__all__ = ["ingest", "ingest_async"]



================================================
FILE: src/gitingest/__main__.py
================================================
"""Command-line interface (CLI) for Gitingest."""

# pylint: disable=no-value-for-parameter
from __future__ import annotations

import asyncio
from typing import TypedDict

import click
from typing_extensions import Unpack

from gitingest.config import MAX_FILE_SIZE, OUTPUT_FILE_NAME
from gitingest.entrypoint import ingest_async

# Import logging configuration first to intercept all logging
from gitingest.utils.logging_config import get_logger

# Initialize logger for this module
logger = get_logger(__name__)


class _CLIArgs(TypedDict):
    source: str
    max_size: int
    exclude_pattern: tuple[str, ...]
    include_pattern: tuple[str, ...]
    branch: str | None
    include_gitignored: bool
    include_submodules: bool
    token: str | None
    output: str | None


@click.command()
@click.argument("source", type=str, default=".")
@click.option(
    "--max-size",
    "-s",
    default=MAX_FILE_SIZE,
    show_default=True,
    help="Maximum file size to process in bytes",
)
@click.option("--exclude-pattern", "-e", multiple=True, help="Shell-style patterns to exclude.")
@click.option(
    "--include-pattern",
    "-i",
    multiple=True,
    help="Shell-style patterns to include.",
)
@click.option("--branch", "-b", default=None, help="Branch to clone and ingest")
@click.option(
    "--include-gitignored",
    is_flag=True,
    default=False,
    help="Include files matched by .gitignore and .gitingestignore",
)
@click.option(
    "--include-submodules",
    is_flag=True,
    help="Include repository's submodules in the analysis",
    default=False,
)
@click.option(
    "--token",
    "-t",
    envvar="GITHUB_TOKEN",
    default=None,
    help=(
        "GitHub personal access token (PAT) for accessing private repositories. "
        "If omitted, the CLI will look for the GITHUB_TOKEN environment variable."
    ),
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="Output file path (default: digest.txt in current directory). Use '-' for stdout.",
)
def main(**cli_kwargs: Unpack[_CLIArgs]) -> None:
    """Run the CLI entry point to analyze a repo / directory and dump its contents.

    Parameters
    ----------
    **cli_kwargs : Unpack[_CLIArgs]
        A dictionary of keyword arguments forwarded to ``ingest_async``.

    Notes
    -----
    See ``ingest_async`` for a detailed description of each argument.

    Examples
    --------
    Basic usage:
        $ gitingest
        $ gitingest /path/to/repo
        $ gitingest https://github.com/user/repo

    Output to stdout:
        $ gitingest -o -
        $ gitingest https://github.com/user/repo --output -

    With filtering:
        $ gitingest -i "*.py" -e "*.log"
        $ gitingest --include-pattern "*.js" --exclude-pattern "node_modules/*"

    Private repositories:
        $ gitingest https://github.com/user/private-repo -t ghp_token
        $ GITHUB_TOKEN=ghp_token gitingest https://github.com/user/private-repo

    Include submodules:
        $ gitingest https://github.com/user/repo --include-submodules

    """
    asyncio.run(_async_main(**cli_kwargs))


async def _async_main(
    source: str,
    *,
    max_size: int = MAX_FILE_SIZE,
    exclude_pattern: tuple[str, ...] | None = None,
    include_pattern: tuple[str, ...] | None = None,
    branch: str | None = None,
    include_gitignored: bool = False,
    include_submodules: bool = False,
    token: str | None = None,
    output: str | None = None,
) -> None:
    """Analyze a directory or repository and create a text dump of its contents.

    This command scans the specified ``source`` (a local directory or Git repo),
    applies custom include and exclude patterns, and generates a text summary of
    the analysis.  The summary is written to an output file or printed to ``stdout``.

    Parameters
    ----------
    source : str
        A directory path or a Git repository URL.
    max_size : int
        Maximum file size in bytes to ingest (default: 10 MB).
    exclude_pattern : tuple[str, ...] | None
        Glob patterns for pruning the file set.
    include_pattern : tuple[str, ...] | None
        Glob patterns for including files in the output.
    branch : str | None
        Git branch to ingest. If ``None``, the repository's default branch is used.
    include_gitignored : bool
        If ``True``, also ingest files matched by ``.gitignore`` or ``.gitingestignore`` (default: ``False``).
    include_submodules : bool
        If ``True``, recursively include all Git submodules within the repository (default: ``False``).
    token : str | None
        GitHub personal access token (PAT) for accessing private repositories.
        Can also be set via the ``GITHUB_TOKEN`` environment variable.
    output : str | None
        The path where the output file will be written (default: ``digest.txt`` in current directory).
        Use ``"-"`` to write to ``stdout``.

    Raises
    ------
    click.Abort
        Raised if an error occurs during execution and the command must be aborted.

    """
    try:
        # Normalise pattern containers (the ingest layer expects sets)
        exclude_patterns = set(exclude_pattern) if exclude_pattern else set()
        include_patterns = set(include_pattern) if include_pattern else set()

        output_target = output if output is not None else OUTPUT_FILE_NAME

        if output_target == "-":
            click.echo("Analyzing source, preparing output for stdout...", err=True)
        else:
            click.echo(f"Analyzing source, output will be written to '{output_target}'...", err=True)

        summary, _, _ = await ingest_async(
            source,
            max_file_size=max_size,
            include_patterns=include_patterns,
            exclude_patterns=exclude_patterns,
            branch=branch,
            include_gitignored=include_gitignored,
            include_submodules=include_submodules,
            token=token,
            output=output_target,
        )
    except Exception as exc:
        # Convert any exception into Click.Abort so that exit status is non-zero
        click.echo(f"Error: {exc}", err=True)
        raise click.Abort from exc

    if output_target == "-":  # stdout
        click.echo("\n--- Summary ---", err=True)
        click.echo(summary, err=True)
        click.echo("--- End Summary ---", err=True)
        click.echo("Analysis complete! Output sent to stdout.", err=True)
    else:  # file
        click.echo(f"Analysis complete! Output written to: {output_target}")
        click.echo("\nSummary:")
        click.echo(summary)


if __name__ == "__main__":
    main()



================================================
FILE: src/gitingest/clone.py
================================================
"""Module containing functions for cloning a Git repository to a local path."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import git

from gitingest.config import DEFAULT_TIMEOUT
from gitingest.utils.git_utils import (
    check_repo_exists,
    checkout_partial_clone,
    create_git_repo,
    ensure_git_installed,
    git_auth_context,
    is_github_host,
    resolve_commit,
)
from gitingest.utils.logging_config import get_logger
from gitingest.utils.os_utils import ensure_directory_exists_or_create
from gitingest.utils.timeout_wrapper import async_timeout

if TYPE_CHECKING:
    from gitingest.schemas import CloneConfig

# Initialize logger for this module
logger = get_logger(__name__)


@async_timeout(DEFAULT_TIMEOUT)
async def clone_repo(config: CloneConfig, *, token: str | None = None) -> None:
    """Clone a repository to a local path based on the provided configuration.

    This function handles the process of cloning a Git repository to the local file system.
    It can clone a specific branch, tag, or commit if provided, and it raises exceptions if
    any errors occur during the cloning process.

    Parameters
    ----------
    config : CloneConfig
        The configuration for cloning the repository.
    token : str | None
        GitHub personal access token (PAT) for accessing private repositories.

    Raises
    ------
    ValueError
        If the repository is not found, if the provided URL is invalid, or if the token format is invalid.
    RuntimeError
        If Git operations fail during the cloning process.

    """
    # Extract and validate query parameters
    url: str = config.url
    local_path: str = config.local_path
    partial_clone: bool = config.subpath != "/"

    logger.info(
        "Starting git clone operation",
        extra={
            "url": url,
            "local_path": local_path,
            "partial_clone": partial_clone,
            "subpath": config.subpath,
            "branch": config.branch,
            "tag": config.tag,
            "commit": config.commit,
            "include_submodules": config.include_submodules,
        },
    )

    logger.debug("Ensuring git is installed")
    await ensure_git_installed()

    logger.debug("Creating local directory", extra={"parent_path": str(Path(local_path).parent)})
    await ensure_directory_exists_or_create(Path(local_path).parent)

    logger.debug("Checking if repository exists", extra={"url": url})
    if not await check_repo_exists(url, token=token):
        logger.error("Repository not found", extra={"url": url})
        msg = "Repository not found. Make sure it is public or that you have provided a valid token."
        raise ValueError(msg)

    logger.debug("Resolving commit reference")
    commit = await resolve_commit(config, token=token)
    logger.debug("Resolved commit", extra={"commit": commit})

    # Clone the repository using GitPython with proper authentication
    logger.info("Executing git clone operation", extra={"url": "<redacted>", "local_path": local_path})
    try:
        clone_kwargs = {
            "single_branch": True,
            "no_checkout": True,
            "depth": 1,
        }

        with git_auth_context(url, token) as (git_cmd, auth_url):
            if partial_clone:
                # For partial clones, use git.Git() with filter and sparse options
                cmd_args = ["--single-branch", "--no-checkout", "--depth=1"]
                cmd_args.extend(["--filter=blob:none", "--sparse"])
                cmd_args.extend([auth_url, local_path])
                git_cmd.clone(*cmd_args)
            elif token and is_github_host(url):
                # For authenticated GitHub repos, use git_cmd with auth URL
                cmd_args = ["--single-branch", "--no-checkout", "--depth=1", auth_url, local_path]
                git_cmd.clone(*cmd_args)
            else:
                # For non-authenticated repos, use the standard GitPython method
                git.Repo.clone_from(url, local_path, **clone_kwargs)

        logger.info("Git clone completed successfully")
    except git.GitCommandError as exc:
        msg = f"Git clone failed: {exc}"
        raise RuntimeError(msg) from exc

    # Checkout the subpath if it is a partial clone
    if partial_clone:
        logger.info("Setting up partial clone for subpath", extra={"subpath": config.subpath})
        await checkout_partial_clone(config, token=token)
        logger.debug("Partial clone setup completed")

    # Perform post-clone operations
    await _perform_post_clone_operations(config, local_path, url, token, commit)

    logger.info("Git clone operation completed successfully", extra={"local_path": local_path})


async def _perform_post_clone_operations(
    config: CloneConfig,
    local_path: str,
    url: str,
    token: str | None,
    commit: str,
) -> None:
    """Perform post-clone operations like fetching, checkout, and submodule updates.

    Parameters
    ----------
    config : CloneConfig
        The configuration for cloning the repository.
    local_path : str
        The local path where the repository was cloned.
    url : str
        The repository URL.
    token : str | None
        GitHub personal access token (PAT) for accessing private repositories.
    commit : str
        The commit SHA to checkout.

    Raises
    ------
    RuntimeError
        If any Git operation fails.

    """
    try:
        repo = create_git_repo(local_path, url, token)

        # Ensure the commit is locally available
        logger.debug("Fetching specific commit", extra={"commit": commit})
        repo.git.fetch("--depth=1", "origin", commit)

        # Write the work-tree at that commit
        logger.info("Checking out commit", extra={"commit": commit})
        repo.git.checkout(commit)

        # Update submodules
        if config.include_submodules:
            logger.info("Updating submodules")
            repo.git.submodule("update", "--init", "--recursive", "--depth=1")
            logger.debug("Submodules updated successfully")
    except git.GitCommandError as exc:
        msg = f"Git operation failed: {exc}"
        raise RuntimeError(msg) from exc



================================================
FILE: src/gitingest/config.py
================================================
"""Configuration file for the project."""

import tempfile
from pathlib import Path

MAX_FILE_SIZE = 10 * 1024 * 1024  # Maximum size of a single file to process (10 MB)
MAX_DIRECTORY_DEPTH = 20  # Maximum depth of directory traversal
MAX_FILES = 10_000  # Maximum number of files to process
MAX_TOTAL_SIZE_BYTES = 500 * 1024 * 1024  # Maximum size of output file (500 MB)
DEFAULT_TIMEOUT = 60  # seconds

OUTPUT_FILE_NAME = "digest.txt"

TMP_BASE_PATH = Path(tempfile.gettempdir()) / "gitingest"



================================================
FILE: src/gitingest/entrypoint.py
================================================
"""Main entry point for ingesting a source and processing its contents."""

from __future__ import annotations

import asyncio
import errno
import shutil
import stat
import sys
from contextlib import asynccontextmanager
from pathlib import Path
from typing import TYPE_CHECKING, AsyncGenerator, Callable
from urllib.parse import urlparse

from gitingest.clone import clone_repo
from gitingest.config import MAX_FILE_SIZE
from gitingest.ingestion import ingest_query
from gitingest.query_parser import parse_local_dir_path, parse_remote_repo
from gitingest.utils.auth import resolve_token
from gitingest.utils.compat_func import removesuffix
from gitingest.utils.ignore_patterns import load_ignore_patterns
from gitingest.utils.logging_config import get_logger
from gitingest.utils.pattern_utils import process_patterns
from gitingest.utils.query_parser_utils import KNOWN_GIT_HOSTS

if TYPE_CHECKING:
    from types import TracebackType

    from gitingest.schemas import IngestionQuery

# Initialize logger for this module
logger = get_logger(__name__)


async def ingest_async(
    source: str,
    *,
    max_file_size: int = MAX_FILE_SIZE,
    include_patterns: str | set[str] | None = None,
    exclude_patterns: str | set[str] | None = None,
    branch: str | None = None,
    tag: str | None = None,
    include_gitignored: bool = False,
    include_submodules: bool = False,
    token: str | None = None,
    output: str | None = None,
) -> tuple[str, str, str]:
    """Ingest a source and process its contents.

    This function analyzes a source (URL or local path), clones the corresponding repository (if applicable),
    and processes its files according to the specified query parameters. It returns a summary, a tree-like
    structure of the files, and the content of the files. The results can optionally be written to an output file.

    Parameters
    ----------
    source : str
        The source to analyze, which can be a URL (for a Git repository) or a local directory path.
    max_file_size : int
        Maximum allowed file size for file ingestion. Files larger than this size are ignored (default: 10 MB).
    include_patterns : str | set[str] | None
        Pattern or set of patterns specifying which files to include. If ``None``, all files are included.
    exclude_patterns : str | set[str] | None
        Pattern or set of patterns specifying which files to exclude. If ``None``, no files are excluded.
    branch : str | None
        The branch to clone and ingest (default: the default branch).
    tag : str | None
        The tag to clone and ingest. If ``None``, no tag is used.
    include_gitignored : bool
        If ``True``, include files ignored by ``.gitignore`` and ``.gitingestignore`` (default: ``False``).
    include_submodules : bool
        If ``True``, recursively include all Git submodules within the repository (default: ``False``).
    token : str | None
        GitHub personal access token (PAT) for accessing private repositories.
        Can also be set via the ``GITHUB_TOKEN`` environment variable.
    output : str | None
        File path where the summary and content should be written.
        If ``"-"`` (dash), the results are written to ``stdout``.
        If ``None``, the results are not written to a file.

    Returns
    -------
    tuple[str, str, str]
        A tuple containing:
        - A summary string of the analyzed repository or directory.
        - A tree-like string representation of the file structure.
        - The content of the files in the repository or directory.

    """
    logger.info("Starting ingestion process", extra={"source": source})

    token = resolve_token(token)

    source = removesuffix(source.strip(), ".git")

    # Determine the parsing method based on the source type
    if urlparse(source).scheme in ("https", "http") or any(h in source for h in KNOWN_GIT_HOSTS):
        # We either have a full URL or a domain-less slug
        logger.info("Parsing remote repository", extra={"source": source})
        query = await parse_remote_repo(source, token=token)
        query.include_submodules = include_submodules
        _override_branch_and_tag(query, branch=branch, tag=tag)

    else:
        # Local path scenario
        logger.info("Processing local directory", extra={"source": source})
        query = parse_local_dir_path(source)

    query.max_file_size = max_file_size
    query.ignore_patterns, query.include_patterns = process_patterns(
        exclude_patterns=exclude_patterns,
        include_patterns=include_patterns,
    )

    if query.url:
        _override_branch_and_tag(query, branch=branch, tag=tag)

    query.include_submodules = include_submodules

    logger.debug(
        "Configuration completed",
        extra={
            "max_file_size": query.max_file_size,
            "include_submodules": query.include_submodules,
            "include_gitignored": include_gitignored,
            "has_include_patterns": bool(query.include_patterns),
            "has_exclude_patterns": bool(query.ignore_patterns),
        },
    )

    async with _clone_repo_if_remote(query, token=token):
        if query.url:
            logger.info("Repository cloned, starting file processing")
        else:
            logger.info("Starting local directory processing")

        if not include_gitignored:
            logger.debug("Applying gitignore patterns")
            _apply_gitignores(query)

        logger.info("Processing files and generating output")
        summary, tree, content = ingest_query(query)

        if output:
            logger.debug("Writing output to file", extra={"output_path": output})
        await _write_output(tree, content=content, target=output)

        logger.info("Ingestion completed successfully")
        return summary, tree, content


def ingest(
    source: str,
    *,
    max_file_size: int = MAX_FILE_SIZE,
    include_patterns: str | set[str] | None = None,
    exclude_patterns: str | set[str] | None = None,
    branch: str | None = None,
    tag: str | None = None,
    include_gitignored: bool = False,
    include_submodules: bool = False,
    token: str | None = None,
    output: str | None = None,
) -> tuple[str, str, str]:
    """Provide a synchronous wrapper around ``ingest_async``.

    This function analyzes a source (URL or local path), clones the corresponding repository (if applicable),
    and processes its files according to the specified query parameters. It returns a summary, a tree-like
    structure of the files, and the content of the files. The results can optionally be written to an output file.

    Parameters
    ----------
    source : str
        The source to analyze, which can be a URL (for a Git repository) or a local directory path.
    max_file_size : int
        Maximum allowed file size for file ingestion. Files larger than this size are ignored (default: 10 MB).
    include_patterns : str | set[str] | None
        Pattern or set of patterns specifying which files to include. If ``None``, all files are included.
    exclude_patterns : str | set[str] | None
        Pattern or set of patterns specifying which files to exclude. If ``None``, no files are excluded.
    branch : str | None
        The branch to clone and ingest (default: the default branch).
    tag : str | None
        The tag to clone and ingest. If ``None``, no tag is used.
    include_gitignored : bool
        If ``True``, include files ignored by ``.gitignore`` and ``.gitingestignore`` (default: ``False``).
    include_submodules : bool
        If ``True``, recursively include all Git submodules within the repository (default: ``False``).
    token : str | None
        GitHub personal access token (PAT) for accessing private repositories.
        Can also be set via the ``GITHUB_TOKEN`` environment variable.
    output : str | None
        File path where the summary and content should be written.
        If ``"-"`` (dash), the results are written to ``stdout``.
        If ``None``, the results are not written to a file.

    Returns
    -------
    tuple[str, str, str]
        A tuple containing:
        - A summary string of the analyzed repository or directory.
        - A tree-like string representation of the file structure.
        - The content of the files in the repository or directory.

    See Also
    --------
    ``ingest_async`` : The asynchronous version of this function.

    """
    return asyncio.run(
        ingest_async(
            source=source,
            max_file_size=max_file_size,
            include_patterns=include_patterns,
            exclude_patterns=exclude_patterns,
            branch=branch,
            tag=tag,
            include_gitignored=include_gitignored,
            include_submodules=include_submodules,
            token=token,
            output=output,
        ),
    )


def _override_branch_and_tag(query: IngestionQuery, branch: str | None, tag: str | None) -> None:
    """Compare the caller-supplied ``branch`` and ``tag`` with the ones already in ``query``.

    If they differ, update ``query`` to the chosen values and issue a warning.
    If both are specified, the tag wins over the branch.

    Parameters
    ----------
    query : IngestionQuery
        The query to update.
    branch : str | None
        The branch to use.
    tag : str | None
        The tag to use.

    """
    if tag and query.tag and tag != query.tag:
        msg = f"Warning: The specified tag '{tag}' overrides the tag found in the URL '{query.tag}'."
        logger.warning(msg)

    query.tag = tag or query.tag

    if branch and query.branch and branch != query.branch:
        msg = f"Warning: The specified branch '{branch}' overrides the branch found in the URL '{query.branch}'."
        logger.warning(msg)

    query.branch = branch or query.branch

    if tag and branch:
        msg = "Warning: Both tag and branch are specified. The tag will be used."
        logger.warning(msg)

    # Tag wins over branch if both supplied
    if query.tag:
        query.branch = None


def _apply_gitignores(query: IngestionQuery) -> None:
    """Update ``query.ignore_patterns`` in-place.

    Parameters
    ----------
    query : IngestionQuery
        The query to update.

    """
    for fname in (".gitignore", ".gitingestignore"):
        query.ignore_patterns.update(load_ignore_patterns(query.local_path, filename=fname))


@asynccontextmanager
async def _clone_repo_if_remote(query: IngestionQuery, *, token: str | None) -> AsyncGenerator[None]:
    """Async context-manager that clones ``query.url`` if present.

    If ``query.url`` is set, the repo is cloned, control is yielded, and the temp directory is removed on exit.
    If no URL is given, the function simply yields immediately.

    Parameters
    ----------
    query : IngestionQuery
        Parsed query describing the source to ingest.
    token : str | None
        GitHub personal access token (PAT) for accessing private repositories.

    """
    kwargs = {}
    if sys.version_info >= (3, 12):
        kwargs["onexc"] = _handle_remove_readonly
    else:
        kwargs["onerror"] = _handle_remove_readonly

    if query.url:
        clone_config = query.extract_clone_config()
        await clone_repo(clone_config, token=token)
        try:
            yield
        finally:
            shutil.rmtree(query.local_path.parent, **kwargs)
    else:
        yield


def _handle_remove_readonly(
    func: Callable,
    path: str,
    exc_info: BaseException | tuple[type[BaseException], BaseException, TracebackType],
) -> None:
    """Handle permission errors raised by ``shutil.rmtree()``.

    * Makes the target writable (removes the read-only attribute).
    * Retries the original operation (``func``) once.

    """
    # 'onerror' passes a (type, value, tb) tuple; 'onexc' passes the exception
    if isinstance(exc_info, tuple):  # 'onerror' (Python <3.12)
        exc: BaseException = exc_info[1]
    else:  # 'onexc' (Python 3.12+)
        exc = exc_info

    # Handle only'Permission denied' and 'Operation not permitted'
    if not isinstance(exc, OSError) or exc.errno not in {errno.EACCES, errno.EPERM}:
        raise exc

    # Make the target writable
    Path(path).chmod(stat.S_IWRITE)
    func(path)


async def _write_output(tree: str, content: str, target: str | None) -> None:
    """Write combined output to ``target`` (``"-"`` ⇒ stdout).

    Parameters
    ----------
    tree : str
        The tree-like string representation of the file structure.
    content : str
        The content of the files in the repository or directory.
    target : str | None
        The path to the output file. If ``None``, the results are not written to a file.

    """
    data = f"{tree}\n{content}"
    loop = asyncio.get_running_loop()
    if target == "-":
        await loop.run_in_executor(None, sys.stdout.write, data)
        await loop.run_in_executor(None, sys.stdout.flush)
    elif target is not None:
        await loop.run_in_executor(None, Path(target).write_text, data, "utf-8")



================================================
FILE: src/gitingest/ingestion.py
================================================
"""Functions to ingest and analyze a codebase directory or single file."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from gitingest.config import MAX_DIRECTORY_DEPTH, MAX_FILES, MAX_TOTAL_SIZE_BYTES
from gitingest.output_formatter import format_node
from gitingest.schemas import FileSystemNode, FileSystemNodeType, FileSystemStats
from gitingest.utils.ingestion_utils import _should_exclude, _should_include
from gitingest.utils.logging_config import get_logger

if TYPE_CHECKING:
    from gitingest.schemas import IngestionQuery

# Initialize logger for this module
logger = get_logger(__name__)


def ingest_query(query: IngestionQuery) -> tuple[str, str, str]:
    """Run the ingestion process for a parsed query.

    This is the main entry point for analyzing a codebase directory or single file. It processes the query
    parameters, reads the file or directory content, and generates a summary, directory structure, and file content,
    along with token estimations.

    Parameters
    ----------
    query : IngestionQuery
        The parsed query object containing information about the repository and query parameters.

    Returns
    -------
    tuple[str, str, str]
        A tuple containing the summary, directory structure, and file contents.

    Raises
    ------
    ValueError
        If the path cannot be found, is not a file, or the file has no content.

    """
    logger.info(
        "Starting file ingestion",
        extra={
            "slug": query.slug,
            "subpath": query.subpath,
            "local_path": str(query.local_path),
            "max_file_size": query.max_file_size,
        },
    )

    subpath = Path(query.subpath.strip("/")).as_posix()
    path = query.local_path / subpath

    if not path.exists():
        logger.error("Path not found", extra={"path": str(path), "slug": query.slug})
        msg = f"{query.slug} cannot be found"
        raise ValueError(msg)

    if (query.type and query.type == "blob") or query.local_path.is_file():
        # TODO: We do this wrong! We should still check the branch and commit!
        logger.info("Processing single file", extra={"file_path": str(path)})

        if not path.is_file():
            logger.error("Expected file but found non-file", extra={"path": str(path)})
            msg = f"Path {path} is not a file"
            raise ValueError(msg)

        relative_path = path.relative_to(query.local_path)

        file_node = FileSystemNode(
            name=path.name,
            type=FileSystemNodeType.FILE,
            size=path.stat().st_size,
            file_count=1,
            path_str=str(relative_path),
            path=path,
        )

        if not file_node.content:
            logger.error("File has no content", extra={"file_name": file_node.name})
            msg = f"File {file_node.name} has no content"
            raise ValueError(msg)

        logger.info(
            "Single file processing completed",
            extra={
                "file_name": file_node.name,
                "file_size": file_node.size,
            },
        )
        return format_node(file_node, query=query)

    logger.info("Processing directory", extra={"directory_path": str(path)})

    root_node = FileSystemNode(
        name=path.name,
        type=FileSystemNodeType.DIRECTORY,
        path_str=str(path.relative_to(query.local_path)),
        path=path,
    )

    stats = FileSystemStats()

    _process_node(node=root_node, query=query, stats=stats)

    logger.info(
        "Directory processing completed",
        extra={
            "total_files": root_node.file_count,
            "total_directories": root_node.dir_count,
            "total_size_bytes": root_node.size,
            "stats_total_files": stats.total_files,
            "stats_total_size": stats.total_size,
        },
    )

    return format_node(root_node, query=query)


def _process_node(node: FileSystemNode, query: IngestionQuery, stats: FileSystemStats) -> None:
    """Process a file or directory item within a directory.

    This function handles each file or directory item, checking if it should be included or excluded based on the
    provided patterns. It handles symlinks, directories, and files accordingly.

    Parameters
    ----------
    node : FileSystemNode
        The current directory or file node being processed.
    query : IngestionQuery
        The parsed query object containing information about the repository and query parameters.
    stats : FileSystemStats
        Statistics tracking object for the total file count and size.

    """
    if limit_exceeded(stats, depth=node.depth):
        return

    for sub_path in node.path.iterdir():
        if query.ignore_patterns and _should_exclude(sub_path, query.local_path, query.ignore_patterns):
            continue

        if query.include_patterns and not _should_include(sub_path, query.local_path, query.include_patterns):
            continue

        if sub_path.is_symlink():
            _process_symlink(path=sub_path, parent_node=node, stats=stats, local_path=query.local_path)
        elif sub_path.is_file():
            if sub_path.stat().st_size > query.max_file_size:
                logger.debug(
                    "Skipping file: would exceed max file size limit",
                    extra={
                        "file_path": str(sub_path),
                        "file_size": sub_path.stat().st_size,
                        "max_file_size": query.max_file_size,
                    },
                )
                continue
            _process_file(path=sub_path, parent_node=node, stats=stats, local_path=query.local_path)
        elif sub_path.is_dir():
            child_directory_node = FileSystemNode(
                name=sub_path.name,
                type=FileSystemNodeType.DIRECTORY,
                path_str=str(sub_path.relative_to(query.local_path)),
                path=sub_path,
                depth=node.depth + 1,
            )

            _process_node(node=child_directory_node, query=query, stats=stats)

            if not child_directory_node.children:
                continue

            node.children.append(child_directory_node)
            node.size += child_directory_node.size
            node.file_count += child_directory_node.file_count
            node.dir_count += 1 + child_directory_node.dir_count
        else:
            logger.warning("Unknown file type, skipping", extra={"file_path": str(sub_path)})

    node.sort_children()


def _process_symlink(path: Path, parent_node: FileSystemNode, stats: FileSystemStats, local_path: Path) -> None:
    """Process a symlink in the file system.

    This function checks the symlink's target.

    Parameters
    ----------
    path : Path
        The full path of the symlink.
    parent_node : FileSystemNode
        The parent directory node.
    stats : FileSystemStats
        Statistics tracking object for the total file count and size.
    local_path : Path
        The base path of the repository or directory being processed.

    """
    child = FileSystemNode(
        name=path.name,
        type=FileSystemNodeType.SYMLINK,
        path_str=str(path.relative_to(local_path)),
        path=path,
        depth=parent_node.depth + 1,
    )
    stats.total_files += 1
    parent_node.children.append(child)
    parent_node.file_count += 1


def _process_file(path: Path, parent_node: FileSystemNode, stats: FileSystemStats, local_path: Path) -> None:
    """Process a file in the file system.

    This function checks the file's size, increments the statistics, and reads its content.
    If the file size exceeds the maximum allowed, it raises an error.

    Parameters
    ----------
    path : Path
        The full path of the file.
    parent_node : FileSystemNode
        The dictionary to accumulate the results.
    stats : FileSystemStats
        Statistics tracking object for the total file count and size.
    local_path : Path
        The base path of the repository or directory being processed.

    """
    if stats.total_files + 1 > MAX_FILES:
        logger.warning(
            "Maximum file limit reached",
            extra={
                "current_files": stats.total_files,
                "max_files": MAX_FILES,
                "file_path": str(path),
            },
        )
        return

    file_size = path.stat().st_size
    if stats.total_size + file_size > MAX_TOTAL_SIZE_BYTES:
        logger.warning(
            "Skipping file: would exceed total size limit",
            extra={
                "file_path": str(path),
                "file_size": file_size,
                "current_total_size": stats.total_size,
                "max_total_size": MAX_TOTAL_SIZE_BYTES,
            },
        )
        return

    stats.total_files += 1
    stats.total_size += file_size

    child = FileSystemNode(
        name=path.name,
        type=FileSystemNodeType.FILE,
        size=file_size,
        file_count=1,
        path_str=str(path.relative_to(local_path)),
        path=path,
        depth=parent_node.depth + 1,
    )

    parent_node.children.append(child)
    parent_node.size += file_size
    parent_node.file_count += 1


def limit_exceeded(stats: FileSystemStats, depth: int) -> bool:
    """Check if any of the traversal limits have been exceeded.

    This function checks if the current traversal has exceeded any of the configured limits:
    maximum directory depth, maximum number of files, or maximum total size in bytes.

    Parameters
    ----------
    stats : FileSystemStats
        Statistics tracking object for the total file count and size.
    depth : int
        The current depth of directory traversal.

    Returns
    -------
    bool
        ``True`` if any limit has been exceeded, ``False`` otherwise.

    """
    if depth > MAX_DIRECTORY_DEPTH:
        logger.warning(
            "Maximum directory depth limit reached",
            extra={
                "current_depth": depth,
                "max_depth": MAX_DIRECTORY_DEPTH,
            },
        )
        return True

    if stats.total_files >= MAX_FILES:
        logger.warning(
            "Maximum file limit reached",
            extra={
                "current_files": stats.total_files,
                "max_files": MAX_FILES,
            },
        )
        return True  # TODO: end recursion

    if stats.total_size >= MAX_TOTAL_SIZE_BYTES:
        logger.warning(
            "Maximum total size limit reached",
            extra={
                "current_size_mb": stats.total_size / 1024 / 1024,
                "max_size_mb": MAX_TOTAL_SIZE_BYTES / 1024 / 1024,
            },
        )
        return True  # TODO: end recursion

    return False



================================================
FILE: src/gitingest/output_formatter.py
================================================
"""Functions to ingest and analyze a codebase directory or single file."""

from __future__ import annotations

import ssl
from typing import TYPE_CHECKING

import requests.exceptions
import tiktoken

from gitingest.schemas import FileSystemNode, FileSystemNodeType
from gitingest.utils.compat_func import readlink
from gitingest.utils.logging_config import get_logger

if TYPE_CHECKING:
    from gitingest.schemas import IngestionQuery

# Initialize logger for this module
logger = get_logger(__name__)

_TOKEN_THRESHOLDS: list[tuple[int, str]] = [
    (1_000_000, "M"),
    (1_000, "k"),
]


def format_node(node: FileSystemNode, query: IngestionQuery) -> tuple[str, str, str]:
    """Generate a summary, directory structure, and file contents for a given file system node.

    If the node represents a directory, the function will recursively process its contents.

    Parameters
    ----------
    node : FileSystemNode
        The file system node to be summarized.
    query : IngestionQuery
        The parsed query object containing information about the repository and query parameters.

    Returns
    -------
    tuple[str, str, str]
        A tuple containing the summary, directory structure, and file contents.

    """
    is_single_file = node.type == FileSystemNodeType.FILE
    summary = _create_summary_prefix(query, single_file=is_single_file)

    if node.type == FileSystemNodeType.DIRECTORY:
        summary += f"Files analyzed: {node.file_count}\n"
    elif node.type == FileSystemNodeType.FILE:
        summary += f"File: {node.name}\n"
        summary += f"Lines: {len(node.content.splitlines()):,}\n"

    tree = "Directory structure:\n" + _create_tree_structure(query, node=node)

    content = _gather_file_contents(node)

    token_estimate = _format_token_count(tree + content)
    if token_estimate:
        summary += f"\nEstimated tokens: {token_estimate}"

    return summary, tree, content


def _create_summary_prefix(query: IngestionQuery, *, single_file: bool = False) -> str:
    """Create a prefix string for summarizing a repository or local directory.

    Includes repository name (if provided), commit/branch details, and subpath if relevant.

    Parameters
    ----------
    query : IngestionQuery
        The parsed query object containing information about the repository and query parameters.
    single_file : bool
        A flag indicating whether the summary is for a single file (default: ``False``).

    Returns
    -------
    str
        A summary prefix string containing repository, commit, branch, and subpath details.

    """
    parts = []

    if query.user_name:
        parts.append(f"Repository: {query.user_name}/{query.repo_name}")
    else:
        # Local scenario
        parts.append(f"Directory: {query.slug}")

    if query.tag:
        parts.append(f"Tag: {query.tag}")
    elif query.branch and query.branch not in ("main", "master"):
        parts.append(f"Branch: {query.branch}")

    if query.commit:
        parts.append(f"Commit: {query.commit}")

    if query.subpath != "/" and not single_file:
        parts.append(f"Subpath: {query.subpath}")

    return "\n".join(parts) + "\n"


def _gather_file_contents(node: FileSystemNode) -> str:
    """Recursively gather contents of all files under the given node.

    This function recursively processes a directory node and gathers the contents of all files
    under that node. It returns the concatenated content of all files as a single string.

    Parameters
    ----------
    node : FileSystemNode
        The current directory or file node being processed.

    Returns
    -------
    str
        The concatenated content of all files under the given node.

    """
    if node.type != FileSystemNodeType.DIRECTORY:
        return node.content_string

    # Recursively gather contents of all files under the current directory
    return "\n".join(_gather_file_contents(child) for child in node.children)


def _create_tree_structure(
    query: IngestionQuery,
    *,
    node: FileSystemNode,
    prefix: str = "",
    is_last: bool = True,
) -> str:
    """Generate a tree-like string representation of the file structure.

    This function generates a string representation of the directory structure, formatted
    as a tree with appropriate indentation for nested directories and files.

    Parameters
    ----------
    query : IngestionQuery
        The parsed query object containing information about the repository and query parameters.
    node : FileSystemNode
        The current directory or file node being processed.
    prefix : str
        A string used for indentation and formatting of the tree structure (default: ``""``).
    is_last : bool
        A flag indicating whether the current node is the last in its directory (default: ``True``).

    Returns
    -------
    str
        A string representing the directory structure formatted as a tree.

    """
    if not node.name:
        # If no name is present, use the slug as the top-level directory name
        node.name = query.slug

    tree_str = ""
    current_prefix = "└── " if is_last else "├── "

    # Indicate directories with a trailing slash
    display_name = node.name
    if node.type == FileSystemNodeType.DIRECTORY:
        display_name += "/"
    elif node.type == FileSystemNodeType.SYMLINK:
        display_name += " -> " + readlink(node.path).name

    tree_str += f"{prefix}{current_prefix}{display_name}\n"

    if node.type == FileSystemNodeType.DIRECTORY and node.children:
        prefix += "    " if is_last else "│   "
        for i, child in enumerate(node.children):
            tree_str += _create_tree_structure(query, node=child, prefix=prefix, is_last=i == len(node.children) - 1)
    return tree_str


def _format_token_count(text: str) -> str | None:
    """Return a human-readable token-count string (e.g. 1.2k, 1.2 M).

    Parameters
    ----------
    text : str
        The text string for which the token count is to be estimated.

    Returns
    -------
    str | None
        The formatted number of tokens as a string (e.g., ``"1.2k"``, ``"1.2M"``), or ``None`` if an error occurs.

    """
    try:
        encoding = tiktoken.get_encoding("o200k_base")  # gpt-4o, gpt-4o-mini
        total_tokens = len(encoding.encode(text, disallowed_special=()))
    except (ValueError, UnicodeEncodeError) as exc:
        logger.warning("Failed to estimate token size", extra={"error": str(exc)})
        return None
    except (requests.exceptions.RequestException, ssl.SSLError) as exc:
        # If network errors, skip token count estimation instead of erroring out
        logger.warning("Failed to download tiktoken model", extra={"error": str(exc)})
        return None

    for threshold, suffix in _TOKEN_THRESHOLDS:
        if total_tokens >= threshold:
            return f"{total_tokens / threshold:.1f}{suffix}"

    return str(total_tokens)



================================================
FILE: src/gitingest/query_parser.py
================================================
"""Module containing functions to parse and validate input sources and patterns."""

from __future__ import annotations

import uuid
from pathlib import Path
from typing import Literal

from gitingest.config import TMP_BASE_PATH
from gitingest.schemas import IngestionQuery
from gitingest.utils.git_utils import fetch_remote_branches_or_tags, resolve_commit
from gitingest.utils.logging_config import get_logger
from gitingest.utils.query_parser_utils import (
    PathKind,
    _fallback_to_root,
    _get_user_and_repo_from_path,
    _is_valid_git_commit_hash,
    _normalise_source,
)

# Initialize logger for this module
logger = get_logger(__name__)


async def parse_remote_repo(source: str, token: str | None = None) -> IngestionQuery:
    """Parse a repository URL and return an ``IngestionQuery`` object.

    If source is:
      - A fully qualified URL ('https://gitlab.com/...'), parse & verify that domain
      - A URL missing 'https://' ('gitlab.com/...'), add 'https://' and parse
      - A *slug* ('pandas-dev/pandas'), attempt known domains until we find one that exists.

    Parameters
    ----------
    source : str
        The URL or domain-less slug to parse.
    token : str | None
        GitHub personal access token (PAT) for accessing private repositories.

    Returns
    -------
    IngestionQuery
        A dictionary containing the parsed details of the repository.

    """
    parsed_url = await _normalise_source(source, token=token)
    host = parsed_url.netloc
    user, repo = _get_user_and_repo_from_path(parsed_url.path)

    _id = uuid.uuid4()
    slug = f"{user}-{repo}"
    local_path = TMP_BASE_PATH / str(_id) / slug
    url = f"https://{host}/{user}/{repo}"

    query = IngestionQuery(
        host=host,
        user_name=user,
        repo_name=repo,
        url=url,
        local_path=local_path,
        slug=slug,
        id=_id,
    )

    path_parts = parsed_url.path.strip("/").split("/")[2:]

    # main branch
    if not path_parts:
        return await _fallback_to_root(query, token=token)

    kind = PathKind(path_parts.pop(0))  # may raise ValueError
    query.type = kind

    # TODO: Handle issues and pull requests
    if query.type in {PathKind.ISSUES, PathKind.PULL}:
        msg = f"Warning: Issues and pull requests are not yet supported: {url}. Returning repository root."
        return await _fallback_to_root(query, token=token, warn_msg=msg)

    # If no extra path parts, just return
    if not path_parts:
        msg = f"Warning: No extra path parts: {url}. Returning repository root."
        return await _fallback_to_root(query, token=token, warn_msg=msg)

    if query.type not in {PathKind.TREE, PathKind.BLOB}:
        # TODO: Handle other types
        msg = f"Warning: Type '{query.type}' is not yet supported: {url}. Returning repository root."
        return await _fallback_to_root(query, token=token, warn_msg=msg)

    # Commit, branch, or tag
    ref = path_parts[0]

    if _is_valid_git_commit_hash(ref):  # Commit
        query.commit = ref
        path_parts.pop(0)  # Consume the commit hash
    else:  # Branch or tag
        # Try to resolve a tag
        query.tag = await _configure_branch_or_tag(
            path_parts,
            url=url,
            ref_type="tags",
            token=token,
        )

        # If no tag found, try to resolve a branch
        if not query.tag:
            query.branch = await _configure_branch_or_tag(
                path_parts,
                url=url,
                ref_type="branches",
                token=token,
            )

    # Only configure subpath if we have identified a commit, branch, or tag.
    if path_parts and (query.commit or query.branch or query.tag):
        query.subpath += "/".join(path_parts)

    query.commit = await resolve_commit(query.extract_clone_config(), token=token)

    return query


def parse_local_dir_path(path_str: str) -> IngestionQuery:
    """Parse the given file path into a structured query dictionary.

    Parameters
    ----------
    path_str : str
        The file path to parse.

    Returns
    -------
    IngestionQuery
        A dictionary containing the parsed details of the file path.

    """
    path_obj = Path(path_str).resolve()
    slug = path_obj.name if path_str == "." else path_str.strip("/")
    return IngestionQuery(local_path=path_obj, slug=slug, id=uuid.uuid4())


async def _configure_branch_or_tag(
    path_parts: list[str],
    *,
    url: str,
    ref_type: Literal["branches", "tags"],
    token: str | None = None,
) -> str | None:
    """Configure the branch or tag based on the remaining parts of the URL.

    Parameters
    ----------
    path_parts : list[str]
        The path parts of the URL.
    url : str
        The URL of the repository.
    ref_type : Literal["branches", "tags"]
        The type of reference to configure. Can be "branches" or "tags".
    token : str | None
        GitHub personal access token (PAT) for accessing private repositories.

    Returns
    -------
    str | None
        The branch or tag name if found, otherwise ``None``.

    """
    _ref_type = "tags" if ref_type == "tags" else "branches"

    try:
        # Fetch the list of branches or tags from the remote repository
        branches_or_tags: list[str] = await fetch_remote_branches_or_tags(url, ref_type=_ref_type, token=token)
    except RuntimeError as exc:
        # If remote discovery fails, we optimistically treat the first path segment as the branch/tag.
        msg = f"Warning: Failed to fetch {_ref_type}: {exc}"
        logger.warning(msg)
        return path_parts.pop(0) if path_parts else None

    # Iterate over the path components and try to find a matching branch/tag
    candidate_parts: list[str] = []

    for part in path_parts:
        candidate_parts.append(part)
        candidate_name = "/".join(candidate_parts)
        if candidate_name in branches_or_tags:
            # We found a match — now consume exactly the parts that form the branch/tag
            del path_parts[: len(candidate_parts)]
            return candidate_name

    # No match found; leave path_parts intact
    return None



================================================
FILE: src/gitingest/schemas/__init__.py
================================================
"""Module containing the schemas for the Gitingest package."""

from gitingest.schemas.cloning import CloneConfig
from gitingest.schemas.filesystem import FileSystemNode, FileSystemNodeType, FileSystemStats
from gitingest.schemas.ingestion import IngestionQuery

__all__ = ["CloneConfig", "FileSystemNode", "FileSystemNodeType", "FileSystemStats", "IngestionQuery"]



================================================
FILE: src/gitingest/schemas/cloning.py
================================================
"""Schema for the cloning process."""

from __future__ import annotations

from pydantic import BaseModel, Field


class CloneConfig(BaseModel):  # pylint: disable=too-many-instance-attributes
    """Configuration for cloning a Git repository.

    This model holds the necessary parameters for cloning a repository to a local path, including
    the repository's URL, the target local path, and optional parameters for a specific commit, branch, or tag.

    Attributes
    ----------
    url : str
        The URL of the Git repository to clone.
    local_path : str
        The local directory where the repository will be cloned.
    commit : str | None
        The specific commit hash to check out after cloning.
    branch : str | None
        The branch to clone.
    tag : str | None
        The tag to clone.
    subpath : str
        The subpath to clone from the repository (default: ``"/"``).
    blob : bool
        Whether the repository is a blob (default: ``False``).
    include_submodules : bool
        Whether to clone submodules (default: ``False``).

    """

    url: str
    local_path: str
    commit: str | None = None
    branch: str | None = None
    tag: str | None = None
    subpath: str = Field(default="/")
    blob: bool = Field(default=False)
    include_submodules: bool = Field(default=False)



================================================
FILE: src/gitingest/schemas/filesystem.py
================================================
"""Schema for the filesystem representation."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import TYPE_CHECKING

from gitingest.utils.compat_func import readlink
from gitingest.utils.file_utils import _decodes, _get_preferred_encodings, _read_chunk
from gitingest.utils.notebook import process_notebook

if TYPE_CHECKING:
    from pathlib import Path

SEPARATOR = "=" * 48  # Tiktoken, the tokenizer openai uses, counts 2 tokens if we have more than 48


class FileSystemNodeType(Enum):
    """Enum representing the type of a file system node (directory or file)."""

    DIRECTORY = auto()
    FILE = auto()
    SYMLINK = auto()


@dataclass
class FileSystemStats:
    """Class for tracking statistics during file system traversal."""

    total_files: int = 0
    total_size: int = 0


@dataclass
class FileSystemNode:  # pylint: disable=too-many-instance-attributes
    """Class representing a node in the file system (either a file or directory).

    Tracks properties of files/directories for comprehensive analysis.
    """

    name: str
    type: FileSystemNodeType
    path_str: str
    path: Path
    size: int = 0
    file_count: int = 0
    dir_count: int = 0
    depth: int = 0
    children: list[FileSystemNode] = field(default_factory=list)

    def sort_children(self) -> None:
        """Sort the children nodes of a directory according to a specific order.

        Order of sorting:
          2. Regular files (not starting with dot)
          3. Hidden files (starting with dot)
          4. Regular directories (not starting with dot)
          5. Hidden directories (starting with dot)

        All groups are sorted alphanumerically within themselves.

        Raises
        ------
        ValueError
            If the node is not a directory.

        """
        if self.type != FileSystemNodeType.DIRECTORY:
            msg = "Cannot sort children of a non-directory node"
            raise ValueError(msg)

        def _sort_key(child: FileSystemNode) -> tuple[int, str]:
            # returns the priority order for the sort function, 0 is first
            # Groups: 0=README, 1=regular file, 2=hidden file, 3=regular dir, 4=hidden dir
            name = child.name.lower()
            if child.type == FileSystemNodeType.FILE:
                if name == "readme" or name.startswith("readme."):
                    return (0, name)
                return (1 if not name.startswith(".") else 2, name)
            return (3 if not name.startswith(".") else 4, name)

        self.children.sort(key=_sort_key)

    @property
    def content_string(self) -> str:
        """Return the content of the node as a string, including path and content.

        Returns
        -------
        str
            A string representation of the node's content.

        """
        parts = [
            SEPARATOR,
            f"{self.type.name}: {str(self.path_str).replace(os.sep, '/')}"
            + (f" -> {readlink(self.path).name}" if self.type == FileSystemNodeType.SYMLINK else ""),
            SEPARATOR,
            f"{self.content}",
        ]

        return "\n".join(parts) + "\n\n"

    @property
    def content(self) -> str:  # pylint: disable=too-many-return-statements
        """Return file content (if text / notebook) or an explanatory placeholder.

        Heuristically decides whether the file is text or binary by decoding a small chunk of the file
        with multiple encodings and checking for common binary markers.

        Returns
        -------
        str
            The content of the file, or an error message if the file could not be read.

        Raises
        ------
        ValueError
            If the node is a directory.

        """
        if self.type == FileSystemNodeType.DIRECTORY:
            msg = "Cannot read content of a directory node"
            raise ValueError(msg)

        if self.type == FileSystemNodeType.SYMLINK:
            return ""  # TODO: are we including the empty content of symlinks?

        if self.path.suffix == ".ipynb":  # Notebook
            try:
                return process_notebook(self.path)
            except Exception as exc:
                return f"Error processing notebook: {exc}"

        chunk = _read_chunk(self.path)

        if chunk is None:
            return "Error reading file"

        if chunk == b"":
            return "[Empty file]"

        if not _decodes(chunk, "utf-8"):
            return "[Binary file]"

        # Find the first encoding that decodes the sample
        good_enc: str | None = next(
            (enc for enc in _get_preferred_encodings() if _decodes(chunk, encoding=enc)),
            None,
        )

        if good_enc is None:
            return "Error: Unable to decode file with available encodings"

        try:
            with self.path.open(encoding=good_enc) as fp:
                return fp.read()
        except (OSError, UnicodeDecodeError) as exc:
            return f"Error reading file with {good_enc!r}: {exc}"



================================================
FILE: src/gitingest/schemas/ingestion.py
================================================
"""Module containing the dataclasses for the ingestion process."""

from __future__ import annotations

from pathlib import Path  # noqa: TC003 (typing-only-standard-library-import) needed for type checking (pydantic)
from uuid import UUID  # noqa: TC003 (typing-only-standard-library-import) needed for type checking (pydantic)

from pydantic import BaseModel, Field

from gitingest.config import MAX_FILE_SIZE
from gitingest.schemas.cloning import CloneConfig


class IngestionQuery(BaseModel):  # pylint: disable=too-many-instance-attributes
    """Pydantic model to store the parsed details of the repository or file path.

    Attributes
    ----------
    host : str | None
        The host of the repository.
    user_name : str | None
        The username or owner of the repository.
    repo_name : str | None
        The name of the repository.
    local_path : Path
        The local path to the repository or file.
    url : str | None
        The URL of the repository.
    slug : str
        The slug of the repository.
    id : UUID
        The ID of the repository.
    subpath : str
        The subpath to the repository or file (default: ``"/"``).
    type : str | None
        The type of the repository or file.
    branch : str | None
        The branch of the repository.
    commit : str | None
        The commit of the repository.
    tag : str | None
        The tag of the repository.
    max_file_size : int
        The maximum file size to ingest in bytes (default: 10 MB).
    ignore_patterns : set[str]
        The patterns to ignore (default: ``set()``).
    include_patterns : set[str] | None
        The patterns to include.
    include_submodules : bool
        Whether to include all Git submodules within the repository. (default: ``False``)
    s3_url : str | None
        The S3 URL where the digest is stored if S3 is enabled.

    """

    host: str | None = None
    user_name: str | None = None
    repo_name: str | None = None
    local_path: Path
    url: str | None = None
    slug: str
    id: UUID
    subpath: str = Field(default="/")
    type: str | None = None
    branch: str | None = None
    commit: str | None = None
    tag: str | None = None
    max_file_size: int = Field(default=MAX_FILE_SIZE)
    ignore_patterns: set[str] = Field(default_factory=set)  # TODO: ssame type for ignore_* and include_* patterns
    include_patterns: set[str] | None = None
    include_submodules: bool = Field(default=False)
    s3_url: str | None = None

    def extract_clone_config(self) -> CloneConfig:
        """Extract the relevant fields for the CloneConfig object.

        Returns
        -------
        CloneConfig
            A CloneConfig object containing the relevant fields.

        Raises
        ------
        ValueError
            If the ``url`` parameter is not provided.

        """
        if not self.url:
            msg = "The 'url' parameter is required."
            raise ValueError(msg)

        return CloneConfig(
            url=self.url,
            local_path=str(self.local_path),
            commit=self.commit,
            branch=self.branch,
            tag=self.tag,
            subpath=self.subpath,
            blob=self.type == "blob",
            include_submodules=self.include_submodules,
        )



================================================
FILE: src/gitingest/utils/__init__.py
================================================
"""Utility functions for the gitingest package."""



================================================
FILE: src/gitingest/utils/auth.py
================================================
"""Utilities for handling authentication."""

from __future__ import annotations

import os

from gitingest.utils.git_utils import validate_github_token


def resolve_token(token: str | None) -> str | None:
    """Resolve the token to use for the query.

    Parameters
    ----------
    token : str | None
        GitHub personal access token (PAT) for accessing private repositories.

    Returns
    -------
    str | None
        The resolved token.

    """
    token = token or os.getenv("GITHUB_TOKEN")
    if token:
        validate_github_token(token)
    return token



================================================
FILE: src/gitingest/utils/compat_func.py
================================================
"""Compatibility functions for Python 3.8."""

import os
from pathlib import Path


def readlink(path: Path) -> Path:
    """Read the target of a symlink.

    Compatible with Python 3.8.

    Parameters
    ----------
    path : Path
        Path to the symlink.

    Returns
    -------
    Path
        The target of the symlink.

    """
    return Path(os.readlink(path))


def removesuffix(s: str, suffix: str) -> str:
    """Remove a suffix from a string.

    Compatible with Python 3.8.

    Parameters
    ----------
    s : str
        String to remove suffix from.
    suffix : str
        Suffix to remove.

    Returns
    -------
    str
        String with suffix removed.

    """
    return s[: -len(suffix)] if s.endswith(suffix) else s



================================================
FILE: src/gitingest/utils/compat_typing.py
================================================
"""Compatibility layer for typing."""

try:
    from enum import StrEnum  # type: ignore[attr-defined]  # Py ≥ 3.11
except ImportError:
    from strenum import StrEnum  # type: ignore[import-untyped] # Py ≤ 3.10

try:
    from typing import ParamSpec, TypeAlias  # type: ignore[attr-defined]  # Py ≥ 3.10
except ImportError:
    from typing_extensions import ParamSpec, TypeAlias  # type: ignore[attr-defined]  # Py ≤ 3.9

try:
    from typing import Annotated  # type: ignore[attr-defined]  # Py ≥ 3.9
except ImportError:
    from typing_extensions import Annotated  # type: ignore[attr-defined]  # Py ≤ 3.8

__all__ = ["Annotated", "ParamSpec", "StrEnum", "TypeAlias"]



================================================
FILE: src/gitingest/utils/exceptions.py
================================================
"""Custom exceptions for the Gitingest package."""


class AsyncTimeoutError(Exception):
    """Exception raised when an async operation exceeds its timeout limit.

    This exception is used by the ``async_timeout`` decorator to signal that the wrapped
    asynchronous function has exceeded the specified time limit for execution.
    """


class InvalidNotebookError(Exception):
    """Exception raised when a Jupyter notebook is invalid or cannot be processed."""

    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidGitHubTokenError(ValueError):
    """Exception raised when a GitHub Personal Access Token is malformed."""

    def __init__(self) -> None:
        msg = (
            "Invalid GitHub token format. To generate a token, go to "
            "https://github.com/settings/tokens/new?description=gitingest&scopes=repo."
        )
        super().__init__(msg)



================================================
FILE: src/gitingest/utils/file_utils.py
================================================
"""Utility functions for working with files and directories."""

from __future__ import annotations

import locale
import platform
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

try:
    locale.setlocale(locale.LC_ALL, "")
except locale.Error:
    locale.setlocale(locale.LC_ALL, "C")

_CHUNK_SIZE = 1024  # bytes


def _get_preferred_encodings() -> list[str]:
    """Get list of encodings to try, prioritized for the current platform.

    Returns
    -------
    list[str]
        List of encoding names to try in priority order, starting with the
        platform's default encoding followed by common fallback encodings.

    """
    encodings = [locale.getpreferredencoding(), "utf-8", "utf-16", "utf-16le", "utf-8-sig", "latin"]
    if platform.system() == "Windows":
        encodings += ["cp1252", "iso-8859-1"]
    return list(dict.fromkeys(encodings))


def _read_chunk(path: Path) -> bytes | None:
    """Attempt to read the first *size* bytes of *path* in binary mode.

    Parameters
    ----------
    path : Path
        The path to the file to read.

    Returns
    -------
    bytes | None
        The first ``_CHUNK_SIZE`` bytes of ``path``, or ``None`` on any ``OSError``.

    """
    try:
        with path.open("rb") as fp:
            return fp.read(_CHUNK_SIZE)
    except OSError:
        return None


def _decodes(chunk: bytes, encoding: str) -> bool:
    """Return ``True`` if ``chunk`` decodes cleanly with ``encoding``.

    Parameters
    ----------
    chunk : bytes
        The chunk of bytes to decode.
    encoding : str
        The encoding to use to decode the chunk.

    Returns
    -------
    bool
        ``True`` if the chunk decodes cleanly with the encoding, ``False`` otherwise.

    """
    try:
        chunk.decode(encoding)
    except UnicodeDecodeError:
        return False
    return True



================================================
FILE: src/gitingest/utils/git_utils.py
================================================
"""Utility functions for interacting with Git repositories."""

from __future__ import annotations

import asyncio
import base64
import re
import sys
from contextlib import contextmanager
from pathlib import Path
from typing import TYPE_CHECKING, Final, Generator, Iterable
from urllib.parse import urlparse, urlunparse

import git

from gitingest.utils.compat_func import removesuffix
from gitingest.utils.exceptions import InvalidGitHubTokenError
from gitingest.utils.logging_config import get_logger

if TYPE_CHECKING:
    from gitingest.schemas import CloneConfig

# Initialize logger for this module
logger = get_logger(__name__)

# GitHub Personal-Access tokens (classic + fine-grained).
#   - ghp_ / gho_ / ghu_ / ghs_ / ghr_  → 36 alphanumerics
#   - github_pat_                       → 22 alphanumerics + "_" + 59 alphanumerics
_GITHUB_PAT_PATTERN: Final[str] = r"^(?:gh[pousr]_[A-Za-z0-9]{36}|github_pat_[A-Za-z0-9]{22}_[A-Za-z0-9]{59})$"


def is_github_host(url: str) -> bool:
    """Check if a URL is from a GitHub host (github.com or GitHub Enterprise).

    Parameters
    ----------
    url : str
        The URL to check

    Returns
    -------
    bool
        True if the URL is from a GitHub host, False otherwise

    """
    hostname = urlparse(url).hostname or ""
    return hostname.startswith("github.")


async def run_command(*args: str) -> tuple[bytes, bytes]:
    """Execute a shell command asynchronously and return (stdout, stderr) bytes.

    This function is kept for backward compatibility with non-git commands.
    Git operations should use GitPython directly.

    Parameters
    ----------
    *args : str
        The command and its arguments to execute.

    Returns
    -------
    tuple[bytes, bytes]
        A tuple containing the stdout and stderr of the command.

    Raises
    ------
    RuntimeError
        If command exits with a non-zero status.

    """
    # Execute the requested command
    proc = await asyncio.create_subprocess_exec(
        *args,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if proc.returncode != 0:
        msg = f"Command failed: {' '.join(args)}\nError: {stderr.decode().strip()}"
        raise RuntimeError(msg)

    return stdout, stderr


async def ensure_git_installed() -> None:
    """Ensure Git is installed and accessible on the system.

    On Windows, this also checks whether Git is configured to support long file paths.

    Raises
    ------
    RuntimeError
        If Git is not installed or not accessible.

    """
    try:
        # Use GitPython to check git availability
        git_cmd = git.Git()
        git_cmd.version()
    except git.GitCommandError as exc:
        msg = "Git is not installed or not accessible. Please install Git first."
        raise RuntimeError(msg) from exc
    except Exception as exc:
        msg = "Git is not installed or not accessible. Please install Git first."
        raise RuntimeError(msg) from exc

    if sys.platform == "win32":
        try:
            longpaths_value = git_cmd.config("core.longpaths")
            if longpaths_value.lower() != "true":
                logger.warning(
                    "Git clone may fail on Windows due to long file paths. "
                    "Consider enabling long path support with: 'git config --global core.longpaths true'. "
                    "Note: This command may require administrator privileges.",
                    extra={"platform": "windows", "longpaths_enabled": False},
                )
        except git.GitCommandError:
            # Ignore if checking 'core.longpaths' fails.
            pass


async def check_repo_exists(url: str, token: str | None = None) -> bool:
    """Check whether a remote Git repository is reachable.

    Parameters
    ----------
    url : str
        URL of the Git repository to check.
    token : str | None
        GitHub personal access token (PAT) for accessing private repositories.

    Returns
    -------
    bool
        ``True`` if the repository exists, ``False`` otherwise.

    """
    try:
        # Try to resolve HEAD - if repo exists, this will work
        await _resolve_ref_to_sha(url, "HEAD", token=token)
    except (ValueError, Exception):
        # Repository doesn't exist, is private without proper auth, or other error
        return False

    return True


def _parse_github_url(url: str) -> tuple[str, str, str]:
    """Parse a GitHub URL and return (hostname, owner, repo).

    Parameters
    ----------
    url : str
        The URL of the GitHub repository to parse.

    Returns
    -------
    tuple[str, str, str]
        A tuple containing the hostname, owner, and repository name.

    Raises
    ------
    ValueError
        If the URL is not a valid GitHub repository URL.

    """
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        msg = f"URL must start with http:// or https://: {url!r}"
        raise ValueError(msg)

    if not parsed.hostname or not parsed.hostname.startswith("github."):
        msg = f"Un-recognised GitHub hostname: {parsed.hostname!r}"
        raise ValueError(msg)

    parts = removesuffix(parsed.path, ".git").strip("/").split("/")
    expected_path_length = 2
    if len(parts) != expected_path_length:
        msg = f"Path must look like /<owner>/<repo>: {parsed.path!r}"
        raise ValueError(msg)

    owner, repo = parts
    return parsed.hostname, owner, repo


async def fetch_remote_branches_or_tags(url: str, *, ref_type: str, token: str | None = None) -> list[str]:
    """Fetch the list of branches or tags from a remote Git repository.

    Parameters
    ----------
    url : str
        The URL of the Git repository to fetch branches or tags from.
    ref_type: str
        The type of reference to fetch. Can be "branches" or "tags".
    token : str | None
        GitHub personal access token (PAT) for accessing private repositories.

    Returns
    -------
    list[str]
        A list of branch names available in the remote repository.

    Raises
    ------
    ValueError
        If the ``ref_type`` parameter is not "branches" or "tags".
    RuntimeError
        If fetching branches or tags from the remote repository fails.

    """
    if ref_type not in ("branches", "tags"):
        msg = f"Invalid fetch type: {ref_type}"
        raise ValueError(msg)

    await ensure_git_installed()

    # Use GitPython to get remote references
    try:
        fetch_tags = ref_type == "tags"
        to_fetch = "tags" if fetch_tags else "heads"

        # Build ls-remote command
        cmd_args = [f"--{to_fetch}"]
        if fetch_tags:
            cmd_args.append("--refs")  # Filter out peeled tag objects
        cmd_args.append(url)

        # Run the command with proper authentication
        with git_auth_context(url, token) as (git_cmd, auth_url):
            # Replace the URL in cmd_args with the authenticated URL
            cmd_args[-1] = auth_url  # URL is the last argument
            output = git_cmd.ls_remote(*cmd_args)

        # Parse output
        return [
            line.split(f"refs/{to_fetch}/", 1)[1]
            for line in output.splitlines()
            if line.strip() and f"refs/{to_fetch}/" in line
        ]
    except git.GitCommandError as exc:
        msg = f"Failed to fetch {ref_type} from {url}: {exc}"
        raise RuntimeError(msg) from exc


def create_git_repo(local_path: str, url: str, token: str | None = None) -> git.Repo:
    """Create a GitPython Repo object with authentication if needed.

    Parameters
    ----------
    local_path : str
        The local path where the git repository is located.
    url : str
        The repository URL to check if it's a GitHub repository.
    token : str | None
        GitHub personal access token (PAT) for accessing private repositories.

    Returns
    -------
    git.Repo
        A GitPython Repo object configured with authentication.

    Raises
    ------
    ValueError
        If the local path is not a valid git repository.

    """
    try:
        repo = git.Repo(local_path)

        # Configure authentication if needed
        if token and is_github_host(url):
            auth_header = create_git_auth_header(token, url=url)
            # Set the auth header in git config for this repo
            key, value = auth_header.split("=", 1)
            repo.git.config(key, value)

    except git.InvalidGitRepositoryError as exc:
        msg = f"Invalid git repository at {local_path}"
        raise ValueError(msg) from exc

    return repo


def create_git_auth_header(token: str, url: str = "https://github.com") -> str:
    """Create a Basic authentication header for GitHub git operations.

    Parameters
    ----------
    token : str
        GitHub personal access token (PAT) for accessing private repositories.
    url : str
        The GitHub URL to create the authentication header for.
        Defaults to "https://github.com" if not provided.

    Returns
    -------
    str
        The git config command for setting the authentication header.

    Raises
    ------
    ValueError
        If the URL is not a valid GitHub repository URL.

    """
    hostname = urlparse(url).hostname
    if not hostname:
        msg = f"Invalid GitHub URL: {url!r}"
        raise ValueError(msg)

    basic = base64.b64encode(f"x-oauth-basic:{token}".encode()).decode()
    return f"http.https://{hostname}/.extraheader=Authorization: Basic {basic}"


def create_authenticated_url(url: str, token: str | None = None) -> str:
    """Create an authenticated URL for Git operations.

    This is the safest approach for multi-user environments - no global state.

    Parameters
    ----------
    url : str
        The repository URL.
    token : str | None
        GitHub personal access token (PAT) for accessing private repositories.

    Returns
    -------
    str
        The URL with authentication embedded (for GitHub) or original URL.

    """
    if not (token and is_github_host(url)):
        return url

    parsed = urlparse(url)
    # Add token as username in URL (GitHub supports this)
    netloc = f"x-oauth-basic:{token}@{parsed.hostname}"
    if parsed.port:
        netloc += f":{parsed.port}"

    return urlunparse(
        (
            parsed.scheme,
            netloc,
            parsed.path,
            parsed.params,
            parsed.query,
            parsed.fragment,
        ),
    )


@contextmanager
def git_auth_context(url: str, token: str | None = None) -> Generator[tuple[git.Git, str]]:
    """Context manager that provides Git command and authenticated URL.

    Returns both a Git command object and the authenticated URL to use.
    This avoids any global state contamination between users.

    Parameters
    ----------
    url : str
        The repository URL to check if authentication is needed.
    token : str | None
        GitHub personal access token (PAT) for accessing private repositories.

    Yields
    ------
    Generator[tuple[git.Git, str]]
        Tuple of (Git command object, authenticated URL to use).

    """
    git_cmd = git.Git()
    auth_url = create_authenticated_url(url, token)
    yield git_cmd, auth_url


def validate_github_token(token: str) -> None:
    """Validate the format of a GitHub Personal Access Token.

    Parameters
    ----------
    token : str
        GitHub personal access token (PAT) for accessing private repositories.

    Raises
    ------
    InvalidGitHubTokenError
        If the token format is invalid.

    """
    if not re.fullmatch(_GITHUB_PAT_PATTERN, token):
        raise InvalidGitHubTokenError


async def checkout_partial_clone(config: CloneConfig, token: str | None) -> None:
    """Configure sparse-checkout for a partially cloned repository.

    Parameters
    ----------
    config : CloneConfig
        The configuration for cloning the repository, including subpath and blob flag.
    token : str | None
        GitHub personal access token (PAT) for accessing private repositories.

    Raises
    ------
    RuntimeError
        If the sparse-checkout configuration fails.

    """
    subpath = config.subpath.lstrip("/")
    if config.blob:
        # Remove the file name from the subpath when ingesting from a file url (e.g. blob/branch/path/file.txt)
        subpath = str(Path(subpath).parent.as_posix())

    try:
        repo = create_git_repo(config.local_path, config.url, token)
        repo.git.sparse_checkout("set", subpath)
    except git.GitCommandError as exc:
        msg = f"Failed to configure sparse-checkout: {exc}"
        raise RuntimeError(msg) from exc


async def resolve_commit(config: CloneConfig, token: str | None) -> str:
    """Resolve the commit to use for the clone.

    Parameters
    ----------
    config : CloneConfig
        The configuration for cloning the repository.
    token : str | None
        GitHub personal access token (PAT) for accessing private repositories.

    Returns
    -------
    str
        The commit SHA.

    """
    if config.commit:
        commit = config.commit
    elif config.tag:
        commit = await _resolve_ref_to_sha(config.url, pattern=f"refs/tags/{config.tag}*", token=token)
    elif config.branch:
        commit = await _resolve_ref_to_sha(config.url, pattern=f"refs/heads/{config.branch}", token=token)
    else:
        commit = await _resolve_ref_to_sha(config.url, pattern="HEAD", token=token)
    return commit


async def _resolve_ref_to_sha(url: str, pattern: str, token: str | None = None) -> str:
    """Return the commit SHA that <kind>/<ref> points to in <url>.

    * Branch → first line from ``git ls-remote``.
    * Tag    → if annotated, prefer the peeled ``^{}`` line (commit).

    Parameters
    ----------
    url : str
        The URL of the remote repository.
    pattern : str
        The pattern to use to resolve the commit SHA.
    token : str | None
        GitHub personal access token (PAT) for accessing private repositories.

    Returns
    -------
    str
        The commit SHA.

    Raises
    ------
    ValueError
        If the ref does not exist in the remote repository.

    """
    try:
        # Execute ls-remote command with proper authentication
        with git_auth_context(url, token) as (git_cmd, auth_url):
            output = git_cmd.ls_remote(auth_url, pattern)
        lines = output.splitlines()

        sha = _pick_commit_sha(lines)
        if not sha:
            msg = f"{pattern!r} not found in {url}"
            raise ValueError(msg)

    except git.GitCommandError as exc:
        msg = f"Failed to resolve {pattern} in {url}:\n{exc}"
        raise ValueError(msg) from exc

    return sha


def _pick_commit_sha(lines: Iterable[str]) -> str | None:
    """Return a commit SHA from ``git ls-remote`` output.

    • Annotated tag            →  prefer the peeled line (<sha> refs/tags/x^{})
    • Branch / lightweight tag →  first non-peeled line


    Parameters
    ----------
    lines : Iterable[str]
        The lines of a ``git ls-remote`` output.

    Returns
    -------
    str | None
        The commit SHA, or ``None`` if no commit SHA is found.

    """
    first_non_peeled: str | None = None

    for ln in lines:
        if not ln.strip():
            continue

        sha, ref = ln.split(maxsplit=1)

        if ref.endswith("^{}"):  # peeled commit of annotated tag
            return sha  # ← best match, done

        if first_non_peeled is None:  # remember the first ordinary line
            first_non_peeled = sha

    return first_non_peeled  # branch or lightweight tag (or None)



================================================
FILE: src/gitingest/utils/ignore_patterns.py
================================================
"""Default ignore patterns for Gitingest."""

from __future__ import annotations

from pathlib import Path

DEFAULT_IGNORE_PATTERNS: set[str] = {
    # Python
    "*.pyc",
    "*.pyo",
    "*.pyd",
    "__pycache__",
    ".pytest_cache",
    ".coverage",
    ".tox",
    ".nox",
    ".mypy_cache",
    ".ruff_cache",
    ".hypothesis",
    "poetry.lock",
    "Pipfile.lock",
    # JavaScript/FileSystemNode
    "node_modules",
    "bower_components",
    "package-lock.json",
    "yarn.lock",
    ".npm",
    ".yarn",
    ".pnpm-store",
    "bun.lock",
    "bun.lockb",
    # Java
    "*.class",
    "*.jar",
    "*.war",
    "*.ear",
    "*.nar",
    ".gradle/",
    "build/",
    ".settings/",
    ".classpath",
    "gradle-app.setting",
    "*.gradle",
    # IDEs and editors / Java
    ".project",
    # C/C++
    "*.o",
    "*.obj",
    "*.dll",
    "*.dylib",
    "*.exe",
    "*.lib",
    "*.out",
    "*.a",
    "*.pdb",
    # Binary
    "*.bin",
    # Swift/Xcode
    ".build/",
    "*.xcodeproj/",
    "*.xcworkspace/",
    "*.pbxuser",
    "*.mode1v3",
    "*.mode2v3",
    "*.perspectivev3",
    "*.xcuserstate",
    "xcuserdata/",
    ".swiftpm/",
    # Ruby
    "*.gem",
    ".bundle/",
    "vendor/bundle",
    "Gemfile.lock",
    ".ruby-version",
    ".ruby-gemset",
    ".rvmrc",
    # Rust
    "Cargo.lock",
    "**/*.rs.bk",
    # Java / Rust
    "target/",
    # Go
    "pkg/",
    # .NET/C#
    "obj/",
    "*.suo",
    "*.user",
    "*.userosscache",
    "*.sln.docstates",
    "*.nupkg",
    # Go / .NET / C#
    "bin/",
    # Version control
    ".git",
    ".svn",
    ".hg",
    ".gitignore",
    ".gitattributes",
    ".gitmodules",
    # Images and media
    "*.svg",
    "*.png",
    "*.jpg",
    "*.jpeg",
    "*.gif",
    "*.ico",
    "*.pdf",
    "*.mov",
    "*.mp4",
    "*.mp3",
    "*.wav",
    # Virtual environments
    "venv",
    ".venv",
    "env",
    ".env",
    "virtualenv",
    # IDEs and editors
    ".idea",
    ".vscode",
    ".vs",
    "*.swo",
    "*.swn",
    ".settings",
    "*.sublime-*",
    # Temporary and cache files
    "*.log",
    "*.bak",
    "*.swp",
    "*.tmp",
    "*.temp",
    ".cache",
    ".sass-cache",
    ".eslintcache",
    ".DS_Store",
    "Thumbs.db",
    "desktop.ini",
    # Build directories and artifacts
    "build",
    "dist",
    "target",
    "out",
    "*.egg-info",
    "*.egg",
    "*.whl",
    "*.so",
    # Documentation
    "site-packages",
    ".docusaurus",
    ".next",
    ".nuxt",
    # Database
    "*.db",
    "*.sqlite",
    "*.sqlite3",
    # Other common patterns
    ## Minified files
    "*.min.js",
    "*.min.css",
    ## Source maps
    "*.map",
    ## Terraform
    "*.tfstate*",
    ## Dependencies in various languages
    "vendor/",
    # Gitingest
    "digest.txt",
}


def load_ignore_patterns(root: Path, filename: str) -> set[str]:
    """Load ignore patterns from ``filename`` found under ``root``.

    The loader walks the directory tree, looks for the supplied ``filename``,
    and returns a unified set of patterns. It implements the same parsing rules
    we use for ``.gitignore`` and ``.gitingestignore`` (git-wildmatch syntax with
    support for negation and root-relative paths).

    Parameters
    ----------
    root : Path
        Directory to walk.
    filename : str
        The filename to look for in each directory.

    Returns
    -------
    set[str]
        A set of ignore patterns extracted from the ``filename`` file found under the ``root`` directory.

    """
    patterns: set[str] = set()

    for ignore_file in root.rglob(filename):
        if ignore_file.is_file():
            patterns.update(_parse_ignore_file(ignore_file, root))
    return patterns


def _parse_ignore_file(ignore_file: Path, root: Path) -> set[str]:
    """Parse an ignore file and return a set of ignore patterns.

    Parameters
    ----------
    ignore_file : Path
        The path to the ignore file.
    root : Path
        The root directory of the repository.

    Returns
    -------
    set[str]
        A set of ignore patterns.

    """
    patterns: set[str] = set()

    # Path of the ignore file relative to the repository root
    rel_dir = ignore_file.parent.relative_to(root)
    base_dir = Path() if rel_dir == Path() else rel_dir

    with ignore_file.open(encoding="utf-8") as fh:
        for raw in fh:
            line = raw.strip()
            if not line or line.startswith("#"):  # comments / blank lines
                continue

            # Handle negation ("!foobar")
            negated = line.startswith("!")
            if negated:
                line = line[1:]

            # Handle leading slash ("/foobar")
            if line.startswith("/"):
                line = line.lstrip("/")

            pattern_body = (base_dir / line).as_posix()
            patterns.add(f"!{pattern_body}" if negated else pattern_body)

    return patterns



================================================
FILE: src/gitingest/utils/ingestion_utils.py
================================================
"""Utility functions for the ingestion process."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pathspec import PathSpec

if TYPE_CHECKING:
    from pathlib import Path


def _should_include(path: Path, base_path: Path, include_patterns: set[str]) -> bool:
    """Return ``True`` if ``path`` matches any of ``include_patterns``.

    Parameters
    ----------
    path : Path
        The absolute path of the file or directory to check.

    base_path : Path
        The base directory from which the relative path is calculated.

    include_patterns : set[str]
        A set of patterns to check against the relative path.

    Returns
    -------
    bool
        ``True`` if the path matches any of the include patterns, ``False`` otherwise.

    """
    rel_path = _relative_or_none(path, base_path)
    if rel_path is None:  # outside repo → do *not* include
        return False
    if path.is_dir():  # keep directories so children are visited
        return True

    spec = PathSpec.from_lines("gitwildmatch", include_patterns)
    return spec.match_file(str(rel_path))


def _should_exclude(path: Path, base_path: Path, ignore_patterns: set[str]) -> bool:
    """Return ``True`` if ``path`` matches any of ``ignore_patterns``.

    Parameters
    ----------
    path : Path
        The absolute path of the file or directory to check.
    base_path : Path
        The base directory from which the relative path is calculated.
    ignore_patterns : set[str]
        A set of patterns to check against the relative path.

    Returns
    -------
    bool
        ``True`` if the path matches any of the ignore patterns, ``False`` otherwise.

    """
    rel_path = _relative_or_none(path, base_path)
    if rel_path is None:  # outside repo → already "excluded"
        return True

    spec = PathSpec.from_lines("gitwildmatch", ignore_patterns)
    return spec.match_file(str(rel_path))


def _relative_or_none(path: Path, base: Path) -> Path | None:
    """Return *path* relative to *base* or ``None`` if *path* is outside *base*.

    Parameters
    ----------
    path : Path
        The absolute path of the file or directory to check.
    base : Path
        The base directory from which the relative path is calculated.

    Returns
    -------
    Path | None
        The relative path of ``path`` to ``base``, or ``None`` if ``path`` is outside ``base``.

    """
    try:
        return path.relative_to(base)
    except ValueError:  # path is not a sub-path of base
        return None



================================================
FILE: src/gitingest/utils/logging_config.py
================================================
"""Logging configuration for gitingest using loguru.

This module provides structured JSON logging suitable for Kubernetes deployments
while also supporting human-readable logging for development.
"""

from __future__ import annotations

import json
import logging
import os
import sys
from typing import Any

from loguru import logger


def json_sink(message: Any) -> None:  # noqa: ANN401
    """Create JSON formatted log output.

    Parameters
    ----------
    message : Any
        The loguru message record

    """
    record = message.record

    log_entry = {
        "timestamp": record["time"].isoformat(),
        "level": record["level"].name.upper(),
        "logger": record["name"],
        "module": record["module"],
        "function": record["function"],
        "line": record["line"],
        "message": record["message"],
    }

    # Add exception info if present
    if record["exception"]:
        log_entry["exception"] = {
            "type": record["exception"].type.__name__,
            "value": str(record["exception"].value),
            "traceback": record["exception"].traceback,
        }

    # Add extra fields if present
    if record["extra"]:
        log_entry.update(record["extra"])

    sys.stdout.write(json.dumps(log_entry, ensure_ascii=False, separators=(",", ":")) + "\n")


def format_extra_fields(record: dict) -> str:
    """Format extra fields as JSON string.

    Parameters
    ----------
    record : dict
        The loguru record dictionary

    Returns
    -------
    str
        JSON formatted extra fields or empty string

    """
    if not record.get("extra"):
        return ""

    # Filter out loguru's internal extra fields
    filtered_extra = {k: v for k, v in record["extra"].items() if not k.startswith("_") and k not in ["name"]}

    # Handle nested extra structure - if there's an 'extra' key, use its contents
    if "extra" in filtered_extra and isinstance(filtered_extra["extra"], dict):
        filtered_extra = filtered_extra["extra"]

    if filtered_extra:
        extra_json = json.dumps(filtered_extra, ensure_ascii=False, separators=(",", ":"))
        return f" | {extra_json}"

    return ""


def extra_filter(record: dict) -> dict:
    """Filter function to add extra fields to the message.

    Parameters
    ----------
    record : dict
        The loguru record dictionary

    Returns
    -------
    dict
        Modified record with extra fields appended to message

    """
    extra_str = format_extra_fields(record)
    if extra_str:
        record["message"] = record["message"] + extra_str
    return record


class InterceptHandler(logging.Handler):
    """Intercept standard library logging and redirect to loguru."""

    def emit(self, record: logging.LogRecord) -> None:
        """Emit a record to loguru."""
        # Get corresponding loguru level
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level,
            record.getMessage(),
        )


def configure_logging() -> None:
    """Configure loguru for the application.

    Sets up JSON logging for production/Kubernetes environments
    or human-readable logging for development.
    Intercepts all standard library logging including uvicorn.
    """
    # Remove default handler
    logger.remove()

    # Check if we're in Kubernetes or production environment
    is_k8s = os.getenv("KUBERNETES_SERVICE_HOST") is not None
    log_format = os.getenv("LOG_FORMAT", "json" if is_k8s else "human")
    log_level = os.getenv("LOG_LEVEL", "INFO")

    if log_format.lower() == "json":
        # JSON format for structured logging (Kubernetes/production)
        logger.add(
            json_sink,
            level=log_level,
            enqueue=True,  # Async logging for better performance
            diagnose=False,  # Don't include variable values in exceptions (security)
            backtrace=True,  # Include full traceback
            serialize=True,  # Ensure proper serialization
        )
    else:
        # Human-readable format for development
        logger_format = (
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
            "<level>{level: <8}</level> | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
            "{message}"
        )
        logger.add(
            sys.stderr,
            format=logger_format,
            filter=extra_filter,
            level=log_level,
            enqueue=True,
            diagnose=True,  # Include variable values in development
            backtrace=True,
        )

    # Intercept all standard library logging
    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)

    # Intercept specific loggers that might bypass basicConfig
    for name in logging.root.manager.loggerDict:  # pylint: disable=no-member
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True


def get_logger(name: str | None = None) -> logger.__class__:
    """Get a configured logger instance.

    Parameters
    ----------
    name : str | None, optional
        Logger name, defaults to the calling module name

    Returns
    -------
    logger.__class__
        Configured logger instance

    """
    if name:
        return logger.bind(name=name)
    return logger


# Initialize logging when module is imported
configure_logging()



================================================
FILE: src/gitingest/utils/notebook.py
================================================
"""Utilities for processing Jupyter notebooks."""

from __future__ import annotations

import json
from itertools import chain
from typing import TYPE_CHECKING, Any

from gitingest.utils.exceptions import InvalidNotebookError
from gitingest.utils.logging_config import get_logger

if TYPE_CHECKING:
    from pathlib import Path

# Initialize logger for this module
logger = get_logger(__name__)


def process_notebook(file: Path, *, include_output: bool = True) -> str:
    """Process a Jupyter notebook file and return an executable Python script as a string.

    Parameters
    ----------
    file : Path
        The path to the Jupyter notebook file.
    include_output : bool
        Whether to include cell outputs in the generated script (default: ``True``).

    Returns
    -------
    str
        The executable Python script as a string.

    Raises
    ------
    InvalidNotebookError
        If the notebook file is invalid or cannot be processed.

    """
    try:
        with file.open(encoding="utf-8") as f:
            notebook: dict[str, Any] = json.load(f)
    except json.JSONDecodeError as exc:
        msg = f"Invalid JSON in notebook: {file}"
        raise InvalidNotebookError(msg) from exc

    # Check if the notebook contains worksheets
    worksheets = notebook.get("worksheets")
    if worksheets:
        logger.warning(
            "Worksheets are deprecated as of IPEP-17. Consider updating the notebook. "
            "(See: https://github.com/jupyter/nbformat and "
            "https://github.com/ipython/ipython/wiki/IPEP-17:-Notebook-Format-4#remove-multiple-worksheets "
            "for more information.)",
        )

        if len(worksheets) > 1:
            logger.warning(
                "Multiple worksheets detected. Combining all worksheets into a single script.",
            )

        cells = list(chain.from_iterable(ws["cells"] for ws in worksheets))

    else:
        cells = notebook["cells"]

    result = ["# Jupyter notebook converted to Python script."]

    for cell in cells:
        cell_str = _process_cell(cell, include_output=include_output)
        if cell_str:
            result.append(cell_str)

    return "\n\n".join(result) + "\n"


def _process_cell(cell: dict[str, Any], *, include_output: bool) -> str | None:
    """Process a Jupyter notebook cell and return the cell content as a string.

    Parameters
    ----------
    cell : dict[str, Any]
        The cell dictionary from a Jupyter notebook.
    include_output : bool
        Whether to include cell outputs in the generated script.

    Returns
    -------
    str | None
        The cell content as a string, or ``None`` if the cell is empty.

    Raises
    ------
    ValueError
        If an unexpected cell type is encountered.

    """
    cell_type = cell["cell_type"]

    # Validate cell type and handle unexpected types
    if cell_type not in ("markdown", "code", "raw"):
        msg = f"Unknown cell type: {cell_type}"
        raise ValueError(msg)

    cell_str = "".join(cell["source"])

    # Skip empty cells
    if not cell_str:
        return None

    # Convert Markdown and raw cells to multi-line comments
    if cell_type in ("markdown", "raw"):
        return f'"""\n{cell_str}\n"""'

    # Add cell output as comments
    outputs = cell.get("outputs")
    if include_output and outputs:
        # Include cell outputs as comments
        raw_lines: list[str] = []
        for output in outputs:
            raw_lines += _extract_output(output)

        cell_str += "\n# Output:\n#   " + "\n#   ".join(raw_lines)

    return cell_str


def _extract_output(output: dict[str, Any]) -> list[str]:
    """Extract the output from a Jupyter notebook cell.

    Parameters
    ----------
    output : dict[str, Any]
        The output dictionary from a Jupyter notebook cell.

    Returns
    -------
    list[str]
        The output as a list of strings.

    Raises
    ------
    ValueError
        If an unknown output type is encountered.

    """
    output_type = output["output_type"]

    if output_type == "stream":
        return output["text"]

    if output_type in ("execute_result", "display_data"):
        return output["data"]["text/plain"]

    if output_type == "error":
        return [f"Error: {output['ename']}: {output['evalue']}"]

    msg = f"Unknown output type: {output_type}"
    raise ValueError(msg)



================================================
FILE: src/gitingest/utils/os_utils.py
================================================
"""Utility functions for working with the operating system."""

from pathlib import Path


async def ensure_directory_exists_or_create(path: Path) -> None:
    """Ensure the directory exists, creating it if necessary.

    Parameters
    ----------
    path : Path
        The path to ensure exists.

    Raises
    ------
    OSError
        If the directory cannot be created.

    """
    try:
        path.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        msg = f"Failed to create directory {path}: {exc}"
        raise OSError(msg) from exc



================================================
FILE: src/gitingest/utils/pattern_utils.py
================================================
"""Pattern utilities for the Gitingest package."""

from __future__ import annotations

import re
from typing import Iterable

from gitingest.utils.ignore_patterns import DEFAULT_IGNORE_PATTERNS

_PATTERN_SPLIT_RE = re.compile(r"[,\s]+")


def process_patterns(
    exclude_patterns: str | set[str] | None = None,
    include_patterns: str | set[str] | None = None,
) -> tuple[set[str], set[str] | None]:
    """Process include and exclude patterns.

    Parameters
    ----------
    exclude_patterns : str | set[str] | None
        Exclude patterns to process.
    include_patterns : str | set[str] | None
        Include patterns to process.

    Returns
    -------
    tuple[set[str], set[str] | None]
        A tuple containing the processed ignore patterns and include patterns.

    """
    # Combine default ignore patterns + custom patterns
    ignore_patterns_set = DEFAULT_IGNORE_PATTERNS.copy()
    if exclude_patterns:
        ignore_patterns_set.update(_parse_patterns(exclude_patterns))

    # Process include patterns and override ignore patterns accordingly
    if include_patterns:
        parsed_include = _parse_patterns(include_patterns)
        # Override ignore patterns with include patterns
        ignore_patterns_set = set(ignore_patterns_set) - set(parsed_include)
    else:
        parsed_include = None

    return ignore_patterns_set, parsed_include


def _parse_patterns(patterns: str | Iterable[str]) -> set[str]:
    """Normalize a collection of file or directory patterns.

    Parameters
    ----------
    patterns : str | Iterable[str]
        One pattern string or an iterable of pattern strings. Each pattern may contain multiple comma- or
        whitespace-separated sub-patterns, e.g. "src/*, tests *.md".

    Returns
    -------
    set[str]
        Normalized patterns with Windows back-slashes converted to forward-slashes and duplicates removed.

    """
    # Treat a lone string as the iterable [string]
    if isinstance(patterns, str):
        patterns = [patterns]

    # Flatten, split on commas/whitespace, strip empties, normalise slashes
    return {
        part.replace("\\", "/")
        for pat in patterns
        for part in _PATTERN_SPLIT_RE.split(pat.strip())
        if part  # discard empty tokens
    }



================================================
FILE: src/gitingest/utils/query_parser_utils.py
================================================
"""Utility functions for parsing and validating query parameters."""

from __future__ import annotations

import string
from typing import TYPE_CHECKING, cast
from urllib.parse import ParseResult, unquote, urlparse

from gitingest.utils.compat_typing import StrEnum
from gitingest.utils.git_utils import _resolve_ref_to_sha, check_repo_exists
from gitingest.utils.logging_config import get_logger

if TYPE_CHECKING:
    from gitingest.schemas import IngestionQuery

# Initialize logger for this module
logger = get_logger(__name__)

HEX_DIGITS: set[str] = set(string.hexdigits)

KNOWN_GIT_HOSTS: list[str] = [
    "github.com",
    "gitlab.com",
    "bitbucket.org",
    "gitea.com",
    "codeberg.org",
    "gist.github.com",
]


class PathKind(StrEnum):
    """Path kind enum."""

    TREE = "tree"
    BLOB = "blob"
    ISSUES = "issues"
    PULL = "pull"


async def _fallback_to_root(query: IngestionQuery, token: str | None, warn_msg: str | None = None) -> IngestionQuery:
    """Fallback to the root of the repository if no extra path parts are provided.

    Parameters
    ----------
    query : IngestionQuery
        The query to fallback to the root of the repository.
    token : str | None
        The token to use to access the repository.
    warn_msg : str | None
        The message to warn.

    Returns
    -------
    IngestionQuery
        The query with the fallback to the root of the repository.

    """
    url = cast("str", query.url)
    query.commit = await _resolve_ref_to_sha(url, pattern="HEAD", token=token)
    if warn_msg:
        logger.warning(warn_msg)
    return query


async def _normalise_source(raw: str, token: str | None) -> ParseResult:
    """Return a fully-qualified ParseResult or raise.

    Parameters
    ----------
    raw : str
        The raw URL to parse.
    token : str | None
        The token to use to access the repository.

    Returns
    -------
    ParseResult
        The parsed URL.

    """
    raw = unquote(raw)
    parsed = urlparse(raw)

    if parsed.scheme:
        _validate_url_scheme(parsed.scheme)
        _validate_host(parsed.netloc)
        return parsed

    # no scheme ('host/user/repo' or 'user/repo')
    host = raw.split("/", 1)[0].lower()
    if "." in host:
        _validate_host(host)
        return urlparse(f"https://{raw}")

    # "user/repo" slug
    host = await _try_domains_for_user_and_repo(*_get_user_and_repo_from_path(raw), token=token)

    return urlparse(f"https://{host}/{raw}")


async def _try_domains_for_user_and_repo(user_name: str, repo_name: str, token: str | None = None) -> str:
    """Attempt to find a valid repository host for the given ``user_name`` and ``repo_name``.

    Parameters
    ----------
    user_name : str
        The username or owner of the repository.
    repo_name : str
        The name of the repository.
    token : str | None
        GitHub personal access token (PAT) for accessing private repositories.

    Returns
    -------
    str
        The domain of the valid repository host.

    Raises
    ------
    ValueError
        If no valid repository host is found for the given ``user_name`` and ``repo_name``.

    """
    for domain in KNOWN_GIT_HOSTS:
        candidate = f"https://{domain}/{user_name}/{repo_name}"
        if await check_repo_exists(candidate, token=token if domain.startswith("github.") else None):
            return domain

    msg = f"Could not find a valid repository host for '{user_name}/{repo_name}'."
    raise ValueError(msg)


def _is_valid_git_commit_hash(commit: str) -> bool:
    """Validate if the provided string is a valid Git commit hash.

    This function checks if the commit hash is a 40-character string consisting only
    of hexadecimal digits, which is the standard format for Git commit hashes.

    Parameters
    ----------
    commit : str
        The string to validate as a Git commit hash.

    Returns
    -------
    bool
        ``True`` if the string is a valid 40-character Git commit hash, otherwise ``False``.

    """
    sha_hex_length = 40
    return len(commit) == sha_hex_length and all(c in HEX_DIGITS for c in commit)


def _validate_host(host: str) -> None:
    """Validate a hostname.

    The host is accepted if it is either present in the hard-coded ``KNOWN_GIT_HOSTS`` list or if it satisfies the
    simple heuristics in ``_looks_like_git_host``, which try to recognise common self-hosted Git services (e.g. GitLab
    instances on sub-domains such as 'gitlab.example.com' or 'git.example.com').

    Parameters
    ----------
    host : str
        Hostname (case-insensitive).

    Raises
    ------
    ValueError
        If the host cannot be recognised as a probable Git hosting domain.

    """
    host = host.lower()
    if host not in KNOWN_GIT_HOSTS and not _looks_like_git_host(host):
        msg = f"Unknown domain '{host}' in URL"
        raise ValueError(msg)


def _looks_like_git_host(host: str) -> bool:
    """Check if the given host looks like a Git host.

    The current heuristic returns ``True`` when the host starts with ``git.`` (e.g. 'git.example.com'), starts with
    'gitlab.' (e.g. 'gitlab.company.com'), or starts with 'github.' (e.g. 'github.company.com' for GitHub Enterprise).

    Parameters
    ----------
    host : str
        Hostname (case-insensitive).

    Returns
    -------
    bool
        ``True`` if the host looks like a Git host, otherwise ``False``.

    """
    host = host.lower()
    return host.startswith(("git.", "gitlab.", "github."))


def _validate_url_scheme(scheme: str) -> None:
    """Validate the given scheme against the known schemes.

    Parameters
    ----------
    scheme : str
        The scheme to validate.

    Raises
    ------
    ValueError
        If the scheme is not 'http' or 'https'.

    """
    scheme = scheme.lower()
    if scheme not in ("https", "http"):
        msg = f"Invalid URL scheme '{scheme}' in URL"
        raise ValueError(msg)


def _get_user_and_repo_from_path(path: str) -> tuple[str, str]:
    """Extract the user and repository names from a given path.

    Parameters
    ----------
    path : str
        The path to extract the user and repository names from.

    Returns
    -------
    tuple[str, str]
        A tuple containing the user and repository names.

    Raises
    ------
    ValueError
        If the path does not contain at least two parts.

    """
    min_path_parts = 2
    path_parts = path.lower().strip("/").split("/")
    if len(path_parts) < min_path_parts:
        msg = f"Invalid repository URL '{path}'"
        raise ValueError(msg)
    return path_parts[0], path_parts[1]



================================================
FILE: src/gitingest/utils/timeout_wrapper.py
================================================
"""Utility functions for the Gitingest package."""

import asyncio
import functools
from typing import Awaitable, Callable, TypeVar

from gitingest.utils.compat_typing import ParamSpec
from gitingest.utils.exceptions import AsyncTimeoutError

T = TypeVar("T")
P = ParamSpec("P")


def async_timeout(seconds: int) -> Callable[[Callable[P, Awaitable[T]]], Callable[P, Awaitable[T]]]:
    """Async Timeout decorator.

    This decorator wraps an asynchronous function and ensures it does not run for
    longer than the specified number of seconds. If the function execution exceeds
    this limit, it raises an ``AsyncTimeoutError``.

    Parameters
    ----------
    seconds : int
        The maximum allowed time (in seconds) for the asynchronous function to complete.

    Returns
    -------
    Callable[[Callable[P, Awaitable[T]]], Callable[P, Awaitable[T]]]
        A decorator that, when applied to an async function, ensures the function
        completes within the specified time limit. If the function takes too long,
        an ``AsyncTimeoutError`` is raised.

    """

    def decorator(func: Callable[P, Awaitable[T]]) -> Callable[P, Awaitable[T]]:
        @functools.wraps(func)
        async def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            try:
                return await asyncio.wait_for(func(*args, **kwargs), timeout=seconds)
            except asyncio.TimeoutError as exc:
                msg = f"Operation timed out after {seconds} seconds"
                raise AsyncTimeoutError(msg) from exc

        return wrapper

    return decorator



================================================
FILE: src/server/__init__.py
================================================
"""Server module."""



================================================
FILE: src/server/__main__.py
================================================
"""Server module entry point for running with python -m server."""

import os

import uvicorn

# Import logging configuration first to intercept all logging
from gitingest.utils.logging_config import get_logger

logger = get_logger(__name__)

if __name__ == "__main__":
    # Get configuration from environment variables
    host = os.getenv("HOST", "0.0.0.0")  # noqa: S104
    port = int(os.getenv("PORT", "8000"))
    reload = os.getenv("RELOAD", "false").lower() == "true"

    logger.info(
        "Starting Gitingest server",
        extra={
            "host": host,
            "port": port,
        },
    )

    uvicorn.run(
        "server.main:app",
        host=host,
        port=port,
        reload=reload,
        log_config=None,  # Disable uvicorn's default logging config
    )



================================================
FILE: src/server/form_types.py
================================================
"""Reusable form type aliases for FastAPI form parameters."""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from fastapi import Form

from gitingest.utils.compat_typing import Annotated

if TYPE_CHECKING:
    from gitingest.utils.compat_typing import TypeAlias

StrForm: TypeAlias = Annotated[str, Form(...)]
IntForm: TypeAlias = Annotated[int, Form(...)]
OptStrForm: TypeAlias = Annotated[Optional[str], Form()]



================================================
FILE: src/server/main.py
================================================
"""Main module for the FastAPI application."""

from __future__ import annotations

import os
import threading
from pathlib import Path

import sentry_sdk
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from slowapi.errors import RateLimitExceeded
from starlette.middleware.trustedhost import TrustedHostMiddleware

# Import logging configuration first to intercept all logging
from gitingest.utils.logging_config import get_logger
from server.metrics_server import start_metrics_server
from server.routers import dynamic, index, ingest
from server.server_config import get_version_info, templates
from server.server_utils import limiter, rate_limit_exception_handler

# Load environment variables from .env file
load_dotenv()

# Initialize logger for this module
logger = get_logger(__name__)

# Initialize Sentry SDK if enabled
if os.getenv("GITINGEST_SENTRY_ENABLED") is not None:
    sentry_dsn = os.getenv("GITINGEST_SENTRY_DSN")

    # Only initialize Sentry if DSN is provided
    if sentry_dsn:
        # Configure Sentry options from environment variables
        traces_sample_rate = float(os.getenv("GITINGEST_SENTRY_TRACES_SAMPLE_RATE", "1.0"))
        profile_session_sample_rate = float(os.getenv("GITINGEST_SENTRY_PROFILE_SESSION_SAMPLE_RATE", "1.0"))
        profile_lifecycle_raw = os.getenv("GITINGEST_SENTRY_PROFILE_LIFECYCLE", "trace")
        profile_lifecycle = profile_lifecycle_raw if profile_lifecycle_raw in ("manual", "trace") else "trace"
        send_default_pii = os.getenv("GITINGEST_SENTRY_SEND_DEFAULT_PII", "true").lower() == "true"
        sentry_environment = os.getenv("GITINGEST_SENTRY_ENVIRONMENT", "")

        sentry_sdk.init(
            dsn=sentry_dsn,
            # Add data like request headers and IP for users
            send_default_pii=send_default_pii,
            # Set traces_sample_rate to capture transactions for tracing
            traces_sample_rate=traces_sample_rate,
            # Set profile_session_sample_rate to profile sessions
            profile_session_sample_rate=profile_session_sample_rate,
            # Set profile_lifecycle to automatically run the profiler
            profile_lifecycle=profile_lifecycle,
            # Set environment name
            environment=sentry_environment,
        )

# Initialize the FastAPI application
app = FastAPI(docs_url=None, redoc_url=None)
app.state.limiter = limiter

# Register the custom exception handler for rate limits
app.add_exception_handler(RateLimitExceeded, rate_limit_exception_handler)

# Start metrics server in a separate thread if enabled
if os.getenv("GITINGEST_METRICS_ENABLED") is not None:
    metrics_host = os.getenv("GITINGEST_METRICS_HOST", "127.0.0.1")
    metrics_port = int(os.getenv("GITINGEST_METRICS_PORT", "9090"))
    metrics_thread = threading.Thread(
        target=start_metrics_server,
        args=(metrics_host, metrics_port),
        daemon=True,
    )
    metrics_thread.start()


# Mount static files dynamically to serve CSS, JS, and other static assets
static_dir = Path(__file__).parent.parent / "static"
app.mount("/static", StaticFiles(directory=static_dir), name="static")


# Fetch allowed hosts from the environment or use the default values
allowed_hosts = os.getenv("ALLOWED_HOSTS")
if allowed_hosts:
    allowed_hosts = allowed_hosts.split(",")
else:
    # Define the default allowed hosts for the application
    default_allowed_hosts = ["gitingest.com", "*.gitingest.com", "localhost", "127.0.0.1"]
    allowed_hosts = default_allowed_hosts

# Add middleware to enforce allowed hosts
app.add_middleware(TrustedHostMiddleware, allowed_hosts=allowed_hosts)


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint to verify that the server is running.

    **Returns**

    - **dict[str, str]**: A JSON object with a "status" key indicating the server's health status.

    """
    return {"status": "healthy"}


@app.head("/", include_in_schema=False)
async def head_root() -> HTMLResponse:
    """Respond to HTTP HEAD requests for the root URL.

    **This endpoint mirrors the headers and status code of the index page**
    for HTTP HEAD requests, providing a lightweight way to check if the server
    is responding without downloading the full page content.

    **Returns**

    - **HTMLResponse**: An empty HTML response with appropriate headers

    """
    return HTMLResponse(content=None, headers={"content-type": "text/html; charset=utf-8"})


@app.get("/robots.txt", include_in_schema=False)
async def robots() -> FileResponse:
    """Serve the robots.txt file to guide search engine crawlers.

    **This endpoint serves the ``robots.txt`` file located in the static directory**
    to provide instructions to search engine crawlers about which parts of the site
    they should or should not index.

    **Returns**

    - **FileResponse**: The ``robots.txt`` file located in the static directory

    """
    return FileResponse("static/robots.txt")


@app.get("/llms.txt")
async def llm_txt() -> FileResponse:
    """Serve the llm.txt file to provide information about the site to LLMs.

    **This endpoint serves the ``llms.txt`` file located in the static directory**
    to provide information about the site to Large Language Models (LLMs)
    and other AI systems that may be crawling the site.

    **Returns**

    - **FileResponse**: The ``llms.txt`` file located in the static directory

    """
    return FileResponse("static/llms.txt")


@app.get("/docs", response_class=HTMLResponse, include_in_schema=False)
async def custom_swagger_ui(request: Request) -> HTMLResponse:
    """Serve custom Swagger UI documentation.

    **This endpoint serves a custom Swagger UI interface**
    for the API documentation, providing an interactive way to explore
    and test the available endpoints.

    **Parameters**

    - **request** (`Request`): The incoming HTTP request

    **Returns**

    - **HTMLResponse**: Custom Swagger UI documentation page

    """
    context = {"request": request}
    context.update(get_version_info())
    return templates.TemplateResponse("swagger_ui.jinja", context)


@app.get("/api", include_in_schema=True)
def openapi_json_get() -> JSONResponse:
    """Return the OpenAPI schema.

    **This endpoint returns the OpenAPI schema (openapi.json)**
    that describes the API structure, endpoints, and data models
    for documentation and client generation purposes.

    **Returns**

    - **JSONResponse**: The OpenAPI schema as JSON

    """
    return JSONResponse(app.openapi())


@app.api_route("/api", methods=["POST", "PUT", "DELETE", "OPTIONS", "HEAD"], include_in_schema=False)
@app.api_route("/api/", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD"], include_in_schema=False)
def openapi_json() -> JSONResponse:
    """Return the OpenAPI schema for various HTTP methods.

    **This endpoint returns the OpenAPI schema (openapi.json)**
    for multiple HTTP methods, providing API documentation
    for clients that may use different request methods.

    **Returns**

    - **JSONResponse**: The OpenAPI schema as JSON

    """
    return JSONResponse(app.openapi())


# Include routers for modular endpoints
app.include_router(index)
app.include_router(ingest)
app.include_router(dynamic)



================================================
FILE: src/server/metrics_server.py
================================================
"""Prometheus metrics server running on a separate port."""

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from prometheus_client import REGISTRY, generate_latest

from gitingest.utils.logging_config import get_logger

# Create a logger for this module
logger = get_logger(__name__)

# Create a separate FastAPI app for metrics
metrics_app = FastAPI(
    title="Gitingest Metrics",
    description="Prometheus metrics for Gitingest",
    docs_url=None,
    redoc_url=None,
)


@metrics_app.get("/metrics")
async def metrics() -> HTMLResponse:
    """Serve Prometheus metrics without authentication.

    This endpoint is only accessible from the local network.

    Returns
    -------
    HTMLResponse
        Prometheus metrics in text format

    """
    return HTMLResponse(
        content=generate_latest(REGISTRY),
        status_code=200,
        media_type="text/plain",
    )


def start_metrics_server(host: str = "127.0.0.1", port: int = 9090) -> None:
    """Start the metrics server on a separate port.

    Parameters
    ----------
    host : str
        The host to bind to (default: 127.0.0.1 for local network only)
    port : int
        The port to bind to (default: 9090)

    Returns
    -------
    None

    """
    logger.info("Starting metrics server", extra={"host": host, "port": port})

    # Configure uvicorn to suppress startup messages to avoid duplicates
    # since the main server already shows similar messages
    uvicorn.run(
        metrics_app,
        host=host,
        port=port,
        log_config=None,  # Disable uvicorn's default logging config
        access_log=False,  # Disable access logging for metrics server
        # Suppress uvicorn's startup messages by setting log level higher
        log_level="warning",
    )



================================================
FILE: src/server/models.py
================================================
"""Pydantic models for the query form."""

from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, Field, field_validator

from gitingest.utils.compat_func import removesuffix
from server.server_config import MAX_FILE_SIZE_KB

# needed for type checking (pydantic)
if TYPE_CHECKING:
    from server.form_types import IntForm, OptStrForm, StrForm


class PatternType(str, Enum):
    """Enumeration for pattern types used in file filtering."""

    INCLUDE = "include"
    EXCLUDE = "exclude"


class IngestRequest(BaseModel):
    """Request model for the /api/ingest endpoint.

    Attributes
    ----------
    input_text : str
        The Git repository URL or slug to ingest.
    max_file_size : int
        Maximum file size slider position (0-500) for filtering files.
    pattern_type : PatternType
        Type of pattern to use for file filtering (include or exclude).
    pattern : str
        Glob/regex pattern string for file filtering.
    token : str | None
        GitHub personal access token (PAT) for accessing private repositories.

    """

    input_text: str = Field(..., description="Git repository URL or slug to ingest")
    max_file_size: int = Field(..., ge=1, le=MAX_FILE_SIZE_KB, description="File size in KB")
    pattern_type: PatternType = Field(default=PatternType.EXCLUDE, description="Pattern type for file filtering")
    pattern: str = Field(default="", description="Glob/regex pattern for file filtering")
    token: str | None = Field(default=None, description="GitHub PAT for private repositories")

    @field_validator("input_text")
    @classmethod
    def validate_input_text(cls, v: str) -> str:
        """Validate that ``input_text`` is not empty."""
        if not v.strip():
            err = "input_text cannot be empty"
            raise ValueError(err)
        return removesuffix(v.strip(), ".git")

    @field_validator("pattern")
    @classmethod
    def validate_pattern(cls, v: str) -> str:
        """Validate ``pattern`` field."""
        return v.strip()


class IngestSuccessResponse(BaseModel):
    """Success response model for the /api/ingest endpoint.

    Attributes
    ----------
    repo_url : str
        The original repository URL that was processed.
    short_repo_url : str
        Short form of repository URL (user/repo).
    summary : str
        Summary of the ingestion process including token estimates.
    digest_url : str
        URL to download the full digest content (either S3 URL or local download endpoint).
    tree : str
        File tree structure of the repository.
    content : str
        Processed content from the repository files.
    default_max_file_size : int
        The file size slider position used.
    pattern_type : str
        The pattern type used for filtering.
    pattern : str
        The pattern used for filtering.

    """

    repo_url: str = Field(..., description="Original repository URL")
    short_repo_url: str = Field(..., description="Short repository URL (user/repo)")
    summary: str = Field(..., description="Ingestion summary with token estimates")
    digest_url: str = Field(..., description="URL to download the full digest content")
    tree: str = Field(..., description="File tree structure")
    content: str = Field(..., description="Processed file content")
    default_max_file_size: int = Field(..., description="File size slider position used")
    pattern_type: str = Field(..., description="Pattern type used")
    pattern: str = Field(..., description="Pattern used")


class IngestErrorResponse(BaseModel):
    """Error response model for the /api/ingest endpoint.

    Attributes
    ----------
    error : str
        Error message describing what went wrong.

    """

    error: str = Field(..., description="Error message")


# Union type for API responses
IngestResponse = Union[IngestSuccessResponse, IngestErrorResponse]


class S3Metadata(BaseModel):
    """Model for S3 metadata structure.

    Attributes
    ----------
    summary : str
        Summary of the ingestion process including token estimates.
    tree : str
        File tree structure of the repository.
    content : str
        Processed content from the repository files.

    """

    summary: str = Field(..., description="Ingestion summary with token estimates")
    tree: str = Field(..., description="File tree structure")
    content: str = Field(..., description="Processed file content")


class QueryForm(BaseModel):
    """Form data for the query.

    Attributes
    ----------
    input_text : str
        Text or URL supplied in the form.
    max_file_size : int
        The maximum allowed file size for the input, specified by the user.
    pattern_type : str
        The type of pattern used for the query (``include`` or ``exclude``).
    pattern : str
        Glob/regex pattern string.
    token : str | None
        GitHub personal access token (PAT) for accessing private repositories.

    """

    input_text: str
    max_file_size: int
    pattern_type: str
    pattern: str
    token: str | None = None

    @classmethod
    def as_form(
        cls,
        input_text: StrForm,
        max_file_size: IntForm,
        pattern_type: StrForm,
        pattern: StrForm,
        token: OptStrForm,
    ) -> QueryForm:
        """Create a QueryForm from FastAPI form parameters.

        Parameters
        ----------
        input_text : StrForm
            The input text provided by the user.
        max_file_size : IntForm
            The maximum allowed file size for the input.
        pattern_type : StrForm
            The type of pattern used for the query (``include`` or ``exclude``).
        pattern : StrForm
            Glob/regex pattern string.
        token : OptStrForm
            GitHub personal access token (PAT) for accessing private repositories.

        Returns
        -------
        QueryForm
            The QueryForm instance.

        """
        return cls(
            input_text=input_text,
            max_file_size=max_file_size,
            pattern_type=pattern_type,
            pattern=pattern,
            token=token,
        )



================================================
FILE: src/server/query_processor.py
================================================
"""Process a query by parsing input, cloning a repository, and generating a summary."""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import TYPE_CHECKING, cast

from gitingest.clone import clone_repo
from gitingest.ingestion import ingest_query
from gitingest.query_parser import parse_remote_repo
from gitingest.utils.git_utils import resolve_commit, validate_github_token
from gitingest.utils.logging_config import get_logger
from gitingest.utils.pattern_utils import process_patterns
from server.models import IngestErrorResponse, IngestResponse, IngestSuccessResponse, PatternType, S3Metadata
from server.s3_utils import (
    _build_s3_url,
    check_s3_object_exists,
    generate_s3_file_path,
    get_metadata_from_s3,
    is_s3_enabled,
    upload_metadata_to_s3,
    upload_to_s3,
)
from server.server_config import MAX_DISPLAY_SIZE

# Initialize logger for this module
logger = get_logger(__name__)

if TYPE_CHECKING:
    from gitingest.schemas.cloning import CloneConfig
    from gitingest.schemas.ingestion import IngestionQuery


def _cleanup_repository(clone_config: CloneConfig) -> None:
    """Clean up the cloned repository after processing."""
    try:
        local_path = Path(clone_config.local_path)
        if local_path.exists():
            shutil.rmtree(local_path)
            logger.info("Successfully cleaned up repository", extra={"local_path": str(local_path)})
    except (PermissionError, OSError):
        logger.exception("Could not delete repository", extra={"local_path": str(clone_config.local_path)})


async def _check_s3_cache(
    query: IngestionQuery,
    input_text: str,
    max_file_size: int,
    pattern_type: str,
    pattern: str,
    token: str | None,
) -> IngestSuccessResponse | None:
    """Check if digest already exists on S3 and return response if found.

    Parameters
    ----------
    query : IngestionQuery
        The parsed query object.
    input_text : str
        Original input text.
    max_file_size : int
        Maximum file size in KB.
    pattern_type : str
        Pattern type (include/exclude).
    pattern : str
        Pattern string.
    token : str | None
        GitHub token.

    Returns
    -------
    IngestSuccessResponse | None
        Response if file exists on S3, None otherwise.

    """
    if not is_s3_enabled():
        return None

    try:
        # Use git ls-remote to get commit SHA without cloning
        clone_config = query.extract_clone_config()
        logger.info("Resolving commit for S3 cache check", extra={"repo_url": query.url})
        query.commit = await resolve_commit(clone_config, token=token)
        logger.info("Commit resolved successfully", extra={"repo_url": query.url, "commit": query.commit})

        # Generate S3 file path using the resolved commit
        s3_file_path = generate_s3_file_path(
            source=query.url,
            user_name=cast("str", query.user_name),
            repo_name=cast("str", query.repo_name),
            commit=query.commit,
            subpath=query.subpath,
            include_patterns=query.include_patterns,
            ignore_patterns=query.ignore_patterns,
        )

        # Check if file exists on S3
        if check_s3_object_exists(s3_file_path):
            # File exists on S3, serve it directly without cloning
            s3_url = _build_s3_url(s3_file_path)
            query.s3_url = s3_url

            short_repo_url = f"{query.user_name}/{query.repo_name}"

            # Try to get cached metadata
            metadata = get_metadata_from_s3(s3_file_path)

            if metadata:
                # Use cached metadata if available
                summary = metadata.summary
                tree = metadata.tree
                content = metadata.content
            else:
                # Fallback to placeholder messages if metadata not available
                summary = "Digest served from cache (S3). Download the full digest to see content details."
                tree = "Digest served from cache. Download the full digest to see the file tree."
                content = "Digest served from cache. Download the full digest to see the content."

            return IngestSuccessResponse(
                repo_url=input_text,
                short_repo_url=short_repo_url,
                summary=summary,
                digest_url=s3_url,
                tree=tree,
                content=content,
                default_max_file_size=max_file_size,
                pattern_type=pattern_type,
                pattern=pattern,
            )
    except Exception as exc:
        # Log the exception but don't fail the entire request
        logger.warning("S3 cache check failed, falling back to normal cloning", extra={"error": str(exc)})

    logger.info("Digest not found in S3 cache, proceeding with normal cloning", extra={"repo_url": query.url})
    return None


def _store_digest_content(
    query: IngestionQuery,
    clone_config: CloneConfig,
    digest_content: str,
    summary: str,
    tree: str,
    content: str,
) -> None:
    """Store digest content either to S3 or locally based on configuration.

    Parameters
    ----------
    query : IngestionQuery
        The query object containing repository information.
    clone_config : CloneConfig
        The clone configuration object.
    digest_content : str
        The complete digest content to store.
    summary : str
        The summary content for metadata.
    tree : str
        The tree content for metadata.
    content : str
        The file content for metadata.

    """
    if is_s3_enabled():
        # Upload to S3 instead of storing locally
        s3_file_path = generate_s3_file_path(
            source=query.url,
            user_name=cast("str", query.user_name),
            repo_name=cast("str", query.repo_name),
            commit=query.commit,
            subpath=query.subpath,
            include_patterns=query.include_patterns,
            ignore_patterns=query.ignore_patterns,
        )
        s3_url = upload_to_s3(content=digest_content, s3_file_path=s3_file_path, ingest_id=query.id)

        # Also upload metadata JSON for caching
        metadata = S3Metadata(
            summary=summary,
            tree=tree,
            content=content,
        )
        try:
            upload_metadata_to_s3(metadata=metadata, s3_file_path=s3_file_path, ingest_id=query.id)
            logger.info("Successfully uploaded metadata to S3")
        except Exception as metadata_exc:
            # Log the error but don't fail the entire request
            logger.warning("Failed to upload metadata to S3", extra={"error": str(metadata_exc)})

        # Store S3 URL in query for later use
        query.s3_url = s3_url
    else:
        # Store locally
        local_txt_file = Path(clone_config.local_path).with_suffix(".txt")
        with local_txt_file.open("w", encoding="utf-8") as f:
            f.write(digest_content)


def _generate_digest_url(query: IngestionQuery) -> str:
    """Generate the digest URL based on S3 configuration.

    Parameters
    ----------
    query : IngestionQuery
        The query object containing repository information.

    Returns
    -------
    str
        The digest URL.

    Raises
    ------
    RuntimeError
        If S3 is enabled but no S3 URL was generated.

    """
    if is_s3_enabled():
        digest_url = getattr(query, "s3_url", None)
        if not digest_url:
            # This should not happen if S3 upload was successful
            msg = "S3 is enabled but no S3 URL was generated"
            raise RuntimeError(msg)
        return digest_url
    return f"/api/download/file/{query.id}"


async def process_query(
    input_text: str,
    max_file_size: int,
    pattern_type: PatternType,
    pattern: str,
    token: str | None = None,
) -> IngestResponse:
    """Process a query by parsing input, cloning a repository, and generating a summary.

    Handle user input, process Git repository data, and prepare
    a response for rendering a template with the processed results or an error message.

    Parameters
    ----------
    input_text : str
        Input text provided by the user, typically a Git repository URL or slug.
    max_file_size : int
        Max file size in KB to be include in the digest.
    pattern_type : PatternType
        Type of pattern to use (either "include" or "exclude")
    pattern : str
        Pattern to include or exclude in the query, depending on the pattern type.
    token : str | None
        GitHub personal access token (PAT) for accessing private repositories.

    Returns
    -------
    IngestResponse
        A union type, corresponding to IngestErrorResponse or IngestSuccessResponse

    Raises
    ------
    RuntimeError
        If the commit hash is not found (should never happen).

    """
    if token:
        validate_github_token(token)

    try:
        query = await parse_remote_repo(input_text, token=token)
    except Exception as exc:
        logger.warning("Failed to parse remote repository", extra={"input_text": input_text, "error": str(exc)})
        return IngestErrorResponse(error=str(exc))

    query.url = cast("str", query.url)
    query.max_file_size = max_file_size * 1024  # Convert to bytes since we currently use KB in higher levels
    query.ignore_patterns, query.include_patterns = process_patterns(
        exclude_patterns=pattern if pattern_type == PatternType.EXCLUDE else None,
        include_patterns=pattern if pattern_type == PatternType.INCLUDE else None,
    )

    # Check if digest already exists on S3 before cloning
    s3_response = await _check_s3_cache(
        query=query,
        input_text=input_text,
        max_file_size=max_file_size,
        pattern_type=pattern_type.value,
        pattern=pattern,
        token=token,
    )
    if s3_response:
        return s3_response

    clone_config = query.extract_clone_config()
    await clone_repo(clone_config, token=token)

    short_repo_url = f"{query.user_name}/{query.repo_name}"

    # The commit hash should always be available at this point
    if not query.commit:
        msg = "Unexpected error: no commit hash found"
        raise RuntimeError(msg)

    try:
        summary, tree, content = ingest_query(query)
        digest_content = tree + "\n" + content
        _store_digest_content(query, clone_config, digest_content, summary, tree, content)
    except Exception as exc:
        _print_error(query.url, exc, max_file_size, pattern_type, pattern)
        # Clean up repository even if processing failed
        _cleanup_repository(clone_config)
        return IngestErrorResponse(error=f"{exc!s}")

    if len(content) > MAX_DISPLAY_SIZE:
        content = (
            f"(Files content cropped to {int(MAX_DISPLAY_SIZE / 1_000)}k characters, "
            "download full ingest to see more)\n" + content[:MAX_DISPLAY_SIZE]
        )

    _print_success(
        url=query.url,
        max_file_size=max_file_size,
        pattern_type=pattern_type,
        pattern=pattern,
        summary=summary,
    )

    digest_url = _generate_digest_url(query)

    # Clean up the repository after successful processing
    _cleanup_repository(clone_config)

    return IngestSuccessResponse(
        repo_url=input_text,
        short_repo_url=short_repo_url,
        summary=summary,
        digest_url=digest_url,
        tree=tree,
        content=content,
        default_max_file_size=max_file_size,
        pattern_type=pattern_type,
        pattern=pattern,
    )


def _print_query(url: str, max_file_size: int, pattern_type: str, pattern: str) -> None:
    """Print a formatted summary of the query details for debugging.

    Parameters
    ----------
    url : str
        The URL associated with the query.
    max_file_size : int
        The maximum file size allowed for the query, in bytes.
    pattern_type : str
        Specifies the type of pattern to use, either "include" or "exclude".
    pattern : str
        The actual pattern string to include or exclude in the query.

    """
    default_max_file_kb = 50
    logger.info(
        "Processing query",
        extra={
            "url": url,
            "max_file_size_kb": int(max_file_size / 1024),
            "pattern_type": pattern_type,
            "pattern": pattern,
            "custom_size": int(max_file_size / 1024) != default_max_file_kb,
        },
    )


def _print_error(url: str, exc: Exception, max_file_size: int, pattern_type: str, pattern: str) -> None:
    """Print a formatted error message for debugging.

    Parameters
    ----------
    url : str
        The URL associated with the query that caused the error.
    exc : Exception
        The exception raised during the query or process.
    max_file_size : int
        The maximum file size allowed for the query, in bytes.
    pattern_type : str
        Specifies the type of pattern to use, either "include" or "exclude".
    pattern : str
        The actual pattern string to include or exclude in the query.

    """
    logger.error(
        "Query processing failed",
        extra={
            "url": url,
            "max_file_size_kb": int(max_file_size / 1024),
            "pattern_type": pattern_type,
            "pattern": pattern,
            "error": str(exc),
        },
    )


def _print_success(url: str, max_file_size: int, pattern_type: str, pattern: str, summary: str) -> None:
    """Print a formatted success message for debugging.

    Parameters
    ----------
    url : str
        The URL associated with the successful query.
    max_file_size : int
        The maximum file size allowed for the query, in bytes.
    pattern_type : str
        Specifies the type of pattern to use, either "include" or "exclude".
    pattern : str
        The actual pattern string to include or exclude in the query.
    summary : str
        A summary of the query result, including details like estimated tokens.

    """
    estimated_tokens = summary[summary.index("Estimated tokens:") + len("Estimated ") :]
    logger.info(
        "Query processing completed successfully",
        extra={
            "url": url,
            "max_file_size_kb": int(max_file_size / 1024),
            "pattern_type": pattern_type,
            "pattern": pattern,
            "estimated_tokens": estimated_tokens,
        },
    )



================================================
FILE: src/server/routers_utils.py
================================================
"""Utility functions for the ingest endpoints."""

from __future__ import annotations

from typing import Any

from fastapi import status
from fastapi.responses import JSONResponse

from server.models import IngestErrorResponse, IngestSuccessResponse, PatternType
from server.query_processor import process_query

COMMON_INGEST_RESPONSES: dict[int | str, dict[str, Any]] = {
    status.HTTP_200_OK: {"model": IngestSuccessResponse, "description": "Successful ingestion"},
    status.HTTP_400_BAD_REQUEST: {"model": IngestErrorResponse, "description": "Bad request or processing error"},
    status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": IngestErrorResponse, "description": "Internal server error"},
}


async def _perform_ingestion(
    input_text: str,
    max_file_size: int,
    pattern_type: str,
    pattern: str,
    token: str | None,
) -> JSONResponse:
    """Run ``process_query`` and wrap the result in a ``FastAPI`` ``JSONResponse``.

    Consolidates error handling shared by the ``POST`` and ``GET`` ingest endpoints.
    """
    try:
        pattern_type = PatternType(pattern_type)

        result = await process_query(
            input_text=input_text,
            max_file_size=max_file_size,
            pattern_type=pattern_type,
            pattern=pattern,
            token=token,
        )

        if isinstance(result, IngestErrorResponse):
            # Return structured error response with 400 status code
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=result.model_dump())

        # Return structured success response with 200 status code
        return JSONResponse(status_code=status.HTTP_200_OK, content=result.model_dump())

    except ValueError as ve:
        # Handle validation errors with 400 status code
        error_response = IngestErrorResponse(error=f"Validation error: {ve!s}")
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=error_response.model_dump())

    except Exception as exc:
        # Handle unexpected errors with 500 status code
        error_response = IngestErrorResponse(error=f"Internal server error: {exc!s}")
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=error_response.model_dump())



================================================
FILE: src/server/s3_utils.py
================================================
"""S3 utility functions for uploading and managing digest files."""

from __future__ import annotations

import hashlib
import os
from typing import TYPE_CHECKING
from urllib.parse import urlparse
from uuid import UUID  # noqa: TC003 (typing-only-standard-library-import) needed for type checking (pydantic)

import boto3
from botocore.exceptions import ClientError
from prometheus_client import Counter

from gitingest.utils.logging_config import get_logger
from server.models import S3Metadata

if TYPE_CHECKING:
    from botocore.client import BaseClient


# Initialize logger for this module
logger = get_logger(__name__)

_s3_ingest_lookup_counter = Counter("gitingest_s3_ingest_lookup", "Number of S3 ingest file lookups")
_s3_ingest_hit_counter = Counter("gitingest_s3_ingest_hit", "Number of S3 ingest file cache hits")
_s3_ingest_miss_counter = Counter("gitingest_s3_ingest_miss", "Number of S3 ingest file cache misses")


class S3UploadError(Exception):
    """Custom exception for S3 upload failures."""


def is_s3_enabled() -> bool:
    """Check if S3 is enabled via environment variables."""
    return os.getenv("S3_ENABLED", "false").lower() == "true"


def get_s3_config() -> dict[str, str | None]:
    """Get S3 configuration from environment variables."""
    config = {
        "endpoint_url": os.getenv("S3_ENDPOINT"),
        "aws_access_key_id": os.getenv("S3_ACCESS_KEY"),
        "aws_secret_access_key": os.getenv("S3_SECRET_KEY"),
        "region_name": os.getenv("S3_REGION") or os.getenv("AWS_REGION", "us-east-1"),
    }
    return {k: v for k, v in config.items() if v is not None}


def get_s3_bucket_name() -> str:
    """Get S3 bucket name from environment variables."""
    return os.getenv("S3_BUCKET_NAME", "gitingest-bucket")


def get_s3_alias_host() -> str | None:
    """Get S3 alias host for public URLs."""
    return os.getenv("S3_ALIAS_HOST")


def generate_s3_file_path(
    source: str,
    user_name: str,
    repo_name: str,
    commit: str,
    subpath: str,
    include_patterns: set[str] | None,
    ignore_patterns: set[str],
) -> str:
    """Generate S3 file path with proper naming convention.

    The file path is formatted as:
    [<S3_DIRECTORY_PREFIX>/]ingest/<provider>/<repo-owner>/<repo-name>/<branch>/<commit-ID>/
    <exclude&include hash>/<owner>-<repo-name>-<subpath-hash>.txt

    If S3_DIRECTORY_PREFIX environment variable is set, it will be prefixed to the path.
    The commit-ID is always included in the URL.
    If no specific commit is provided, the actual commit hash from the cloned repository is used.

    Parameters
    ----------
    source : str
        Git host (e.g., github, gitlab, bitbucket, etc.).
    user_name : str
        Repository owner or user.
    repo_name : str
        Repository name.
    commit : str
        Commit hash.
    subpath : str
        Subpath of the repository.
    include_patterns : set[str] | None
        Set of patterns specifying which files to include.
    ignore_patterns : set[str]
        Set of patterns specifying which files to exclude.

    Returns
    -------
    str
        S3 file path string.

    Raises
    ------
    ValueError
        If the source URL is invalid.

    """
    hostname = urlparse(source).hostname
    if hostname is None:
        msg = "Invalid source URL"
        logger.error(msg)
        raise ValueError(msg)

    # Create hash of exclude/include patterns for uniqueness
    patterns_str = f"include:{sorted(include_patterns) if include_patterns else []}"
    patterns_str += f"exclude:{sorted(ignore_patterns)}"
    patterns_hash = hashlib.sha256(patterns_str.encode()).hexdigest()[:16]
    subpath_hash = hashlib.sha256(subpath.encode()).hexdigest()[:16]

    file_name = f"{user_name}-{repo_name}-{subpath_hash}.txt"
    base_path = f"ingest/{hostname}/{user_name}/{repo_name}/{commit}/{patterns_hash}/{file_name}"

    # Check for S3_DIRECTORY_PREFIX environment variable
    s3_directory_prefix = os.getenv("S3_DIRECTORY_PREFIX")

    if not s3_directory_prefix:
        return base_path

    # Remove trailing slash if present and add the prefix
    s3_directory_prefix = s3_directory_prefix.rstrip("/")
    return f"{s3_directory_prefix}/{base_path}"


def create_s3_client() -> BaseClient:
    """Create and return an S3 client with configuration from environment."""
    config = get_s3_config()
    # Log S3 client creation (excluding sensitive info)
    log_config = config.copy()
    has_credentials = bool(log_config.pop("aws_access_key_id", None) or log_config.pop("aws_secret_access_key", None))
    logger.debug(
        "Creating S3 client",
        extra={
            "s3_config": log_config,
            "has_credentials": has_credentials,
        },
    )
    return boto3.client("s3", **config)


def upload_to_s3(content: str, s3_file_path: str, ingest_id: UUID) -> str:
    """Upload content to S3 and return the public URL.

    This function uploads the provided content to an S3 bucket and returns the public URL for the uploaded file.
    The ingest ID is stored as an S3 object tag.

    Parameters
    ----------
    content : str
        The digest content to upload.
    s3_file_path : str
        The S3 file path where the content will be stored.
    ingest_id : UUID
        The ingest ID to store as an S3 object tag.

    Returns
    -------
    str
        Public URL to access the uploaded file.

    Raises
    ------
    ValueError
        If S3 is not enabled.
    S3UploadError
        If the upload to S3 fails.

    """
    if not is_s3_enabled():
        msg = "S3 is not enabled"
        logger.error(msg)
        raise ValueError(msg)

    s3_client = create_s3_client()
    bucket_name = get_s3_bucket_name()

    extra_fields = {
        "bucket_name": bucket_name,
        "s3_file_path": s3_file_path,
        "ingest_id": str(ingest_id),
        "content_size": len(content),
    }

    # Log upload attempt
    logger.info("Starting S3 upload", extra=extra_fields)

    try:
        # Upload the content with ingest_id as tag
        s3_client.put_object(
            Bucket=bucket_name,
            Key=s3_file_path,
            Body=content.encode("utf-8"),
            ContentType="text/plain",
            Tagging=f"ingest_id={ingest_id!s}",
        )
    except ClientError as err:
        # Log upload failure
        logger.exception(
            "S3 upload failed",
            extra={
                "bucket_name": bucket_name,
                "s3_file_path": s3_file_path,
                "ingest_id": str(ingest_id),
                "error_code": err.response.get("Error", {}).get("Code"),
                "error_message": str(err),
            },
        )
        msg = f"Failed to upload to S3: {err}"
        raise S3UploadError(msg) from err

    # Generate public URL
    alias_host = get_s3_alias_host()
    if alias_host:
        # Use alias host if configured
        public_url = f"{alias_host.rstrip('/')}/{s3_file_path}"
    else:
        # Fallback to direct S3 URL
        endpoint = get_s3_config().get("endpoint_url")
        if endpoint:
            public_url = f"{endpoint.rstrip('/')}/{bucket_name}/{s3_file_path}"
        else:
            public_url = f"https://{bucket_name}.s3.{get_s3_config()['region_name']}.amazonaws.com/{s3_file_path}"

    # Log successful upload
    logger.info(
        "S3 upload completed successfully",
        extra={
            "bucket_name": bucket_name,
            "s3_file_path": s3_file_path,
            "ingest_id": str(ingest_id),
            "public_url": public_url,
        },
    )

    return public_url


def upload_metadata_to_s3(metadata: S3Metadata, s3_file_path: str, ingest_id: UUID) -> str:
    """Upload metadata JSON to S3 alongside the digest file.

    Parameters
    ----------
    metadata : S3Metadata
        The metadata struct containing summary, tree, and content.
    s3_file_path : str
        The S3 file path for the digest (metadata will use .json extension).
    ingest_id : UUID
        The ingest ID to store as an S3 object tag.

    Returns
    -------
    str
        Public URL to access the uploaded metadata file.

    Raises
    ------
    ValueError
        If S3 is not enabled.
    S3UploadError
        If the upload to S3 fails.

    """
    if not is_s3_enabled():
        msg = "S3 is not enabled"
        logger.error(msg)
        raise ValueError(msg)

    # Generate metadata file path by replacing .txt with .json
    metadata_file_path = s3_file_path.replace(".txt", ".json")

    s3_client = create_s3_client()
    bucket_name = get_s3_bucket_name()

    extra_fields = {
        "bucket_name": bucket_name,
        "metadata_file_path": metadata_file_path,
        "ingest_id": str(ingest_id),
        "metadata_size": len(metadata.model_dump_json()),
    }

    # Log upload attempt
    logger.info("Starting S3 metadata upload", extra=extra_fields)

    try:
        # Upload the metadata with ingest_id as tag
        s3_client.put_object(
            Bucket=bucket_name,
            Key=metadata_file_path,
            Body=metadata.model_dump_json(indent=2).encode("utf-8"),
            ContentType="application/json",
            Tagging=f"ingest_id={ingest_id!s}",
        )
    except ClientError as err:
        # Log upload failure
        logger.exception(
            "S3 metadata upload failed",
            extra={
                "bucket_name": bucket_name,
                "metadata_file_path": metadata_file_path,
                "ingest_id": str(ingest_id),
                "error_code": err.response.get("Error", {}).get("Code"),
                "error_message": str(err),
            },
        )
        msg = f"Failed to upload metadata to S3: {err}"
        raise S3UploadError(msg) from err

    # Generate public URL
    alias_host = get_s3_alias_host()
    if alias_host:
        # Use alias host if configured
        public_url = f"{alias_host.rstrip('/')}/{metadata_file_path}"
    else:
        # Fallback to direct S3 URL
        endpoint = get_s3_config().get("endpoint_url")
        if endpoint:
            public_url = f"{endpoint.rstrip('/')}/{bucket_name}/{metadata_file_path}"
        else:
            public_url = (
                f"https://{bucket_name}.s3.{get_s3_config()['region_name']}.amazonaws.com/{metadata_file_path}"
            )

    # Log successful upload
    logger.info(
        "S3 metadata upload completed successfully",
        extra={
            "bucket_name": bucket_name,
            "metadata_file_path": metadata_file_path,
            "ingest_id": str(ingest_id),
            "public_url": public_url,
        },
    )

    return public_url


def get_metadata_from_s3(s3_file_path: str) -> S3Metadata | None:
    """Retrieve metadata JSON from S3.

    Parameters
    ----------
    s3_file_path : str
        The S3 file path for the digest (metadata will use .json extension).

    Returns
    -------
    S3Metadata | None
        The metadata struct if found, None otherwise.

    """
    if not is_s3_enabled():
        return None

    # Generate metadata file path by replacing .txt with .json
    metadata_file_path = s3_file_path.replace(".txt", ".json")

    try:
        s3_client = create_s3_client()
        bucket_name = get_s3_bucket_name()

        # Get the metadata object
        response = s3_client.get_object(Bucket=bucket_name, Key=metadata_file_path)
        metadata_content = response["Body"].read().decode("utf-8")

        return S3Metadata.model_validate_json(metadata_content)
    except ClientError as err:
        # Object doesn't exist if we get a 404 error
        error_code = err.response.get("Error", {}).get("Code")
        if error_code == "404":
            logger.info("Metadata file not found", extra={"metadata_file_path": metadata_file_path})
            return None
        # Log other errors but don't fail
        logger.warning("Failed to retrieve metadata from S3", extra={"error": str(err)})
        return None
    except Exception as exc:
        # For any other exception, log and return None
        logger.warning("Unexpected error retrieving metadata from S3", extra={"error": str(exc)})
        return None


def _build_s3_url(key: str) -> str:
    """Build S3 URL for a given key."""
    alias_host = get_s3_alias_host()
    if alias_host:
        return f"{alias_host.rstrip('/')}/{key}"

    bucket_name = get_s3_bucket_name()
    config = get_s3_config()

    endpoint = config["endpoint_url"]
    if endpoint:
        return f"{endpoint.rstrip('/')}/{bucket_name}/{key}"

    return f"https://{bucket_name}.s3.{config['region_name']}.amazonaws.com/{key}"


def _check_object_tags(s3_client: BaseClient, bucket_name: str, key: str, target_ingest_id: UUID) -> bool:
    """Check if an S3 object has the matching ingest_id tag."""
    try:
        tags_response = s3_client.get_object_tagging(Bucket=bucket_name, Key=key)
        tags = {tag["Key"]: tag["Value"] for tag in tags_response.get("TagSet", [])}
        return tags.get("ingest_id") == str(target_ingest_id)
    except ClientError:
        return False


def check_s3_object_exists(s3_file_path: str) -> bool:
    """Check if an S3 object exists at the given path.

    Parameters
    ----------
    s3_file_path : str
        The S3 file path to check.

    Returns
    -------
    bool
        True if the object exists, False otherwise.

    Raises
    ------
    ClientError
        If there's an S3 error other than 404 (not found).

    """
    if not is_s3_enabled():
        logger.info("S3 not enabled, skipping object existence check", extra={"s3_file_path": s3_file_path})
        return False

    logger.info("Checking S3 object existence", extra={"s3_file_path": s3_file_path})
    _s3_ingest_lookup_counter.inc()
    try:
        s3_client = create_s3_client()
        bucket_name = get_s3_bucket_name()

        # Use head_object to check if the object exists without downloading it
        s3_client.head_object(Bucket=bucket_name, Key=s3_file_path)
    except ClientError as err:
        # Object doesn't exist if we get a 404 error
        error_code = err.response.get("Error", {}).get("Code")
        if error_code == "404":
            logger.info(
                "S3 object not found",
                extra={
                    "s3_file_path": s3_file_path,
                    "bucket_name": get_s3_bucket_name(),
                    "error_code": error_code,
                },
            )
            _s3_ingest_miss_counter.inc()
            return False
        # Re-raise other errors (permissions, etc.)
        raise
    except Exception as exc:
        # For any other exception, assume object doesn't exist
        logger.info(
            "S3 object check failed with exception, assuming not found",
            extra={
                "s3_file_path": s3_file_path,
                "bucket_name": get_s3_bucket_name(),
                "exception": str(exc),
            },
        )
        _s3_ingest_miss_counter.inc()
        return False
    else:
        logger.info(
            "S3 object found",
            extra={
                "s3_file_path": s3_file_path,
                "bucket_name": get_s3_bucket_name(),
            },
        )
        _s3_ingest_hit_counter.inc()
        return True


def get_s3_url_for_ingest_id(ingest_id: UUID) -> str | None:
    """Get S3 URL for a given ingest ID if it exists.

    Search for files in S3 using object tags to find the matching ingest_id and returns the S3 URL if found.
    Used by the download endpoint to redirect to S3 if available.

    Parameters
    ----------
    ingest_id : UUID
        The ingest ID to search for in S3 object tags.

    Returns
    -------
    str | None
        S3 URL if file exists, None otherwise.

    """
    if not is_s3_enabled():
        logger.debug("S3 not enabled, skipping URL lookup", extra={"ingest_id": str(ingest_id)})
        return None

    logger.info("Starting S3 URL lookup for ingest ID", extra={"ingest_id": str(ingest_id)})

    try:
        s3_client = create_s3_client()
        bucket_name = get_s3_bucket_name()

        # List all objects in the ingest/ prefix and check their tags
        paginator = s3_client.get_paginator("list_objects_v2")
        page_iterator = paginator.paginate(Bucket=bucket_name, Prefix="ingest/")

        objects_checked = 0
        for page in page_iterator:
            if "Contents" not in page:
                continue

            for obj in page["Contents"]:
                key = obj["Key"]
                objects_checked += 1
                if _check_object_tags(
                    s3_client=s3_client,
                    bucket_name=bucket_name,
                    key=key,
                    target_ingest_id=ingest_id,
                ):
                    s3_url = _build_s3_url(key)
                    logger.info(
                        "Found S3 object for ingest ID",
                        extra={
                            "ingest_id": str(ingest_id),
                            "s3_key": key,
                            "s3_url": s3_url,
                            "objects_checked": objects_checked,
                        },
                    )
                    return s3_url

        logger.info(
            "No S3 object found for ingest ID",
            extra={
                "ingest_id": str(ingest_id),
                "objects_checked": objects_checked,
            },
        )

    except ClientError as err:
        logger.exception(
            "Error during S3 URL lookup",
            extra={
                "ingest_id": str(ingest_id),
                "error_code": err.response.get("Error", {}).get("Code"),
                "error_message": str(err),
            },
        )

    return None



================================================
FILE: src/server/server_config.py
================================================
"""Configuration for the server."""

from __future__ import annotations

import os
from pathlib import Path

from fastapi.templating import Jinja2Templates

MAX_DISPLAY_SIZE: int = 300_000

# Slider configuration (if updated, update the logSliderToSize function in src/static/js/utils.js)
DEFAULT_FILE_SIZE_KB: int = 5 * 1024  # 5 mb
MAX_FILE_SIZE_KB: int = 100 * 1024  # 100 mb

EXAMPLE_REPOS: list[dict[str, str]] = [
    {"name": "Gitingest", "url": "https://github.com/coderamp-labs/gitingest"},
    {"name": "FastAPI", "url": "https://github.com/fastapi/fastapi"},
    {"name": "Flask", "url": "https://github.com/pallets/flask"},
    {"name": "Excalidraw", "url": "https://github.com/excalidraw/excalidraw"},
    {"name": "ApiAnalytics", "url": "https://github.com/tom-draper/api-analytics"},
]


# Version and repository configuration
APP_REPOSITORY = os.getenv("APP_REPOSITORY", "https://github.com/coderamp-labs/gitingest")
APP_VERSION = os.getenv("APP_VERSION", "unknown")
APP_VERSION_URL = os.getenv("APP_VERSION_URL", "https://github.com/coderamp-labs/gitingest")


def get_version_info() -> dict[str, str]:
    """Get version information including display version and link.

    Returns
    -------
    dict[str, str]
        Dictionary containing 'version' and 'version_link' keys.

    """
    # Use pre-computed values from GitHub Actions
    display_version = APP_VERSION
    version_link = APP_VERSION_URL

    # Fallback to repository root if no URL is provided
    if version_link == APP_REPOSITORY or not version_link:
        version_link = f"{APP_REPOSITORY.rstrip('/')}/tree/main"

    return {
        "version": display_version,
        "version_link": version_link,
    }


# Use absolute path to templates directory
templates_dir = Path(__file__).parent / "templates"
templates = Jinja2Templates(directory=templates_dir)



================================================
FILE: src/server/server_utils.py
================================================
"""Utility functions for the server."""

from fastapi import Request
from fastapi.responses import Response
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from gitingest.utils.logging_config import get_logger

# Initialize logger for this module
logger = get_logger(__name__)

# Initialize a rate limiter
limiter = Limiter(key_func=get_remote_address)


async def rate_limit_exception_handler(request: Request, exc: Exception) -> Response:
    """Handle rate-limiting errors with a custom exception handler.

    Parameters
    ----------
    request : Request
        The incoming HTTP request.
    exc : Exception
        The exception raised, expected to be RateLimitExceeded.

    Returns
    -------
    Response
        A response indicating that the rate limit has been exceeded.

    Raises
    ------
    exc
        If the exception is not a RateLimitExceeded error, it is re-raised.

    """
    if isinstance(exc, RateLimitExceeded):
        # Delegate to the default rate limit handler
        return _rate_limit_exceeded_handler(request, exc)
    # Re-raise other exceptions
    raise exc


## Color printing utility
class Colors:
    """ANSI color codes."""

    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"



================================================
FILE: src/server/routers/__init__.py
================================================
"""Module containing the routers for the FastAPI application."""

from server.routers.dynamic import router as dynamic
from server.routers.index import router as index
from server.routers.ingest import router as ingest

__all__ = ["dynamic", "index", "ingest"]



================================================
FILE: src/server/routers/dynamic.py
================================================
"""The dynamic router module defines handlers for dynamic path requests."""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from server.server_config import get_version_info, templates

router = APIRouter()


@router.get("/{full_path:path}", include_in_schema=False)
async def catch_all(request: Request, full_path: str) -> HTMLResponse:
    """Render a page with a Git URL based on the provided path.

    This endpoint catches all GET requests with a dynamic path, constructs a Git URL
    using the ``full_path`` parameter, and renders the ``git.jinja`` template with that URL.

    Parameters
    ----------
    request : Request
        The incoming request object, which provides context for rendering the response.
    full_path : str
        The full path extracted from the URL, which is used to build the Git URL.

    Returns
    -------
    HTMLResponse
        An HTML response containing the rendered template, with the Git URL
        and other default parameters such as file size.

    """
    context = {
        "request": request,
        "repo_url": full_path,
        "default_max_file_size": 243,
    }
    context.update(get_version_info())

    return templates.TemplateResponse("git.jinja", context)



================================================
FILE: src/server/routers/index.py
================================================
"""Module defining the FastAPI router for the home page of the application."""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from server.server_config import EXAMPLE_REPOS, get_version_info, templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse, include_in_schema=False)
async def home(request: Request) -> HTMLResponse:
    """Render the home page with example repositories and default parameters.

    This endpoint serves the home page of the application, rendering the ``index.jinja`` template
    and providing it with a list of example repositories and default file size values.

    Parameters
    ----------
    request : Request
        The incoming request object, which provides context for rendering the response.

    Returns
    -------
    HTMLResponse
        An HTML response containing the rendered home page template, with example repositories
        and other default parameters such as file size.

    """
    context = {
        "request": request,
        "examples": EXAMPLE_REPOS,
        "default_max_file_size": 243,
    }
    context.update(get_version_info())

    return templates.TemplateResponse("index.jinja", context)



================================================
FILE: src/server/routers/ingest.py
================================================
"""Ingest endpoint for the API."""

from typing import Union
from uuid import UUID

from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse
from prometheus_client import Counter

from gitingest.config import TMP_BASE_PATH
from server.models import IngestRequest
from server.routers_utils import COMMON_INGEST_RESPONSES, _perform_ingestion
from server.s3_utils import is_s3_enabled
from server.server_config import DEFAULT_FILE_SIZE_KB
from server.server_utils import limiter

ingest_counter = Counter("gitingest_ingest_total", "Number of ingests", ["status", "url"])

router = APIRouter()


@router.post("/api/ingest", responses=COMMON_INGEST_RESPONSES)
@limiter.limit("10/minute")
async def api_ingest(
    request: Request,  # noqa: ARG001 (unused-function-argument) # pylint: disable=unused-argument
    ingest_request: IngestRequest,
) -> JSONResponse:
    """Ingest a Git repository and return processed content.

    **This endpoint processes a Git repository by cloning it, analyzing its structure,**
    and returning a summary with the repository's content. The response includes
    file tree structure, processed content, and metadata about the ingestion.

    **Parameters**

    - **ingest_request** (`IngestRequest`): Pydantic model containing ingestion parameters

    **Returns**

    - **JSONResponse**: Success response with ingestion results or error response with appropriate HTTP status code

    """
    response = await _perform_ingestion(
        input_text=ingest_request.input_text,
        max_file_size=ingest_request.max_file_size,
        pattern_type=ingest_request.pattern_type.value,
        pattern=ingest_request.pattern,
        token=ingest_request.token,
    )
    # limit URL to 255 characters
    ingest_counter.labels(status=response.status_code, url=ingest_request.input_text[:255]).inc()
    return response


@router.get("/api/{user}/{repository}", responses=COMMON_INGEST_RESPONSES)
@limiter.limit("10/minute")
async def api_ingest_get(
    request: Request,  # noqa: ARG001 (unused-function-argument) # pylint: disable=unused-argument
    user: str,
    repository: str,
    max_file_size: int = DEFAULT_FILE_SIZE_KB,
    pattern_type: str = "exclude",
    pattern: str = "",
    token: str = "",
) -> JSONResponse:
    """Ingest a GitHub repository via GET and return processed content.

    **This endpoint processes a GitHub repository by analyzing its structure and returning a summary**
    with the repository's content. The response includes file tree structure, processed content, and
    metadata about the ingestion. All ingestion parameters are optional and can be provided as query parameters.

    **Path Parameters**
    - **user** (`str`): GitHub username or organization
    - **repository** (`str`): GitHub repository name

    **Query Parameters**
    - **max_file_size** (`int`, optional): Maximum file size in KB to include in the digest (default: 5120 KB)
    - **pattern_type** (`str`, optional): Type of pattern to use ("include" or "exclude", default: "exclude")
    - **pattern** (`str`, optional): Pattern to include or exclude in the query (default: "")
    - **token** (`str`, optional): GitHub personal access token for private repositories (default: "")

    **Returns**
    - **JSONResponse**: Success response with ingestion results or error response with appropriate HTTP status code
    """
    response = await _perform_ingestion(
        input_text=f"{user}/{repository}",
        max_file_size=max_file_size,
        pattern_type=pattern_type,
        pattern=pattern,
        token=token or None,
    )
    # limit URL to 255 characters
    ingest_counter.labels(status=response.status_code, url=f"{user}/{repository}"[:255]).inc()
    return response


@router.get("/api/download/file/{ingest_id}", response_model=None)
async def download_ingest(
    ingest_id: UUID,
) -> Union[RedirectResponse, FileResponse]:  # noqa: FA100 (future-rewritable-type-annotation) (pydantic)
    """Download the first text file produced for an ingest ID.

    **This endpoint retrieves the first ``*.txt`` file produced during the ingestion process**
    and returns it as a downloadable file. When S3 is enabled, this endpoint is disabled
    and clients should use the S3 URL provided in the ingest response instead.

    **Parameters**

    - **ingest_id** (`UUID`): Identifier that the ingest step emitted

    **Returns**

    - **FileResponse**: Streamed response with media type ``text/plain`` for local files

    **Raises**

    - **HTTPException**: **503** - endpoint is disabled when S3 is enabled
    - **HTTPException**: **404** - digest directory is missing or contains no ``*.txt`` file
    - **HTTPException**: **403** - the process lacks permission to read the directory or file

    """
    # Disable download endpoint when S3 is enabled
    if is_s3_enabled():
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Download endpoint is disabled when S3 is enabled. "
            "Use the S3 URL provided in the ingest response instead.",
        )

    # Fall back to local file serving
    # Normalize and validate the directory path
    directory = (TMP_BASE_PATH / str(ingest_id)).resolve()
    if not str(directory).startswith(str(TMP_BASE_PATH.resolve())):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid ingest ID: {ingest_id!r}")

    if not directory.is_dir():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Digest {ingest_id!r} not found")

    try:
        first_txt_file = next(directory.glob("*.txt"))
    except StopIteration as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No .txt file found for digest {ingest_id!r}",
        ) from exc

    try:
        return FileResponse(path=first_txt_file, media_type="text/plain", filename=first_txt_file.name)
    except PermissionError as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Permission denied for {first_txt_file}",
        ) from exc



================================================
FILE: src/server/templates/base.jinja
================================================
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        {# Favicons #}
        <link rel="icon" type="image/x-icon" href="/static/favicons/favicon.ico">
        <link rel="icon" type="image/svg+xml" href="/static/favicons/favicon.svg">
        <link rel="icon"
              type="image/png"
              href="/static/favicons/favicon-64.png"
              sizes="64x64">
        <link rel="apple-touch-icon"
              type="image/png"
              href="/static/favicons/apple-touch-icon.png"
              sizes="180x180">
        {# Search Engine Meta Tags #}
        <meta name="title"       content="Gitingest">
        <meta name="description"
              content="Replace 'hub' with 'ingest' in any GitHub URL for a prompt-friendly text.">
        <meta name="keywords"
              content="Gitingest, AI tools, LLM integration, Ingest, Digest, Context, Prompt, Git workflow, codebase extraction, Git repository, Git automation, Summarize, prompt-friendly">
        <meta name="robots"      content="index, follow">
        {# Open Graph Meta Tags #}
        <meta property="og:title"       content="Gitingest">
        <meta property="og:description"
              content="Replace 'hub' with 'ingest' in any GitHub URL for a prompt-friendly text.">
        <meta property="og:type"        content="website">
        <meta property="og:url"         content="{{ request.url }}">
        <meta property="og:image"       content="/static/og-image.png">
        {# Web App Meta #}
        <meta name="apple-mobile-web-app-title"            content="Gitingest">
        <meta name="application-name"                      content="Gitingest">
        <meta name="theme-color"                           content="#FCA847">
        <meta name="mobile-web-app-capable"                content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="default">
        {# Twitter card #}
        <meta name="twitter:card"        content="summary_large_image">
        <meta name="twitter:title"       content="Gitingest">
        <meta name="twitter:description"
              content="Replace 'hub' with 'ingest' in any GitHub URL for a prompt-friendly text.">
        <meta name="twitter:image"       content="/static/og-image.png">
        {# Title #}
        <title>
            {% block title %}
                {% if short_repo_url %}
                    Gitingest - {{ short_repo_url }}
                {% else %}
                    Gitingest
                {% endif %}
            {% endblock %}
        </title>
        <script src="https://cdn.tailwindcss.com"></script>
        {% include 'components/tailwind_components.html' %}
    </head>
    <body class="bg-[#FFFDF8] min-h-screen flex flex-col">
        {% include 'components/navbar.jinja' %}
        {# Main content wrapper #}
        <main class="flex-1 w-full">
            <div class="max-w-4xl mx-auto px-4 py-8">
                {% block content %}{% endblock %}
            </div>
        </main>
        {# Footer #}
        {% include 'components/footer.jinja' %}
        {# Scripts #}
        <script defer src="/static/js/index.js"></script>
        <script defer src="/static/js/utils.js"></script>
        <script defer src="/static/js/posthog.js"></script>
    </body>
</html>



================================================
FILE: src/server/templates/git.jinja
================================================
{% extends "base.jinja" %}
{% block content %}
    {% if error_message %}
        <div class="mb-6 p-4 bg-red-50 border border-red-200 rounded-lg text-red-700"
             id="error-message"
             data-message="{{ error_message }}">{{ error_message }}</div>
    {% endif %}
    {% with show_examples=false %}
        {% include 'components/git_form.jinja' %}
    {% endwith %}
    {% include 'components/result.jinja' %}
{% endblock content %}



================================================
FILE: src/server/templates/index.jinja
================================================
{% extends "base.jinja" %}
{% block content %}
    <div class="mb-8">
        <div class="relative w-full flex sm:flex-row flex-col justify-center sm:items-center">
            {# Title & Sparkles #}
            <h1 class="landing-page-title">
                Prompt-friendly
                <br>
                codebase&nbsp;
            </h1>
            <img src="/static/svg/sparkle-red.svg" class="sparkle-red no-drag">
            <img src="/static/svg/sparkle-green.svg" class="sparkle-green no-drag">
        </div>
        <p class="intro-text mt-8">Turn any Git repository into a simple text digest of its codebase.</p>
        <p class="intro-text mt-0">This is useful for feeding a codebase into any LLM.</p>
    </div>
    {% if error_message %}
        <div class="mb-6 p-4 bg-red-50 border border-red-200 rounded-lg text-red-700"
             id="error-message"
             data-message="{{ error_message }}">{{ error_message }}</div>
    {% endif %}
    {% with show_examples=true %}
        {% include 'components/git_form.jinja' %}
    {% endwith %}
    <p class="text-gray-600 text-sm max-w-2xl mx-auto text-center mt-4">
        You can also replace 'hub' with 'ingest' in any GitHub URL.
    </p>
    {% include 'components/result.jinja' %}
{% endblock %}



================================================
FILE: src/server/templates/swagger_ui.jinja
================================================
{% extends "base.jinja" %}
{% block title %}GitIngest API{% endblock %}
{% block content %}
    <div class="mb-8">
        <div class="relative w-full flex sm:flex-row flex-col justify-center sm:items-center">
            {# Title & Sparkles #}
            <h1 class="landing-page-title">
                GitIngest
                <br>
                API&nbsp;
            </h1>
            <img src="/static/svg/sparkle-red.svg" class="sparkle-red no-drag">
            <img src="/static/svg/sparkle-green.svg" class="sparkle-green no-drag">
        </div>
        <p class="intro-text mt-8">Turn any Git repository into a simple text digest of its codebase.</p>
        <p class="intro-text mt-0">This is useful for feeding a codebase into any LLM.</p>
    </div>
    <div class="bg-[#fff4da] rounded-xl border-[3px] border-gray-900 p-4 md:p-8 relative z-20">
        <div id="swagger-ui"></div>
    </div>
    <link rel="stylesheet"
          href="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css">
    <script src="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
    <script>
  window.onload = function() {
    SwaggerUIBundle({
      url: "/openapi.json",
      dom_id: '#swagger-ui',
      presets: [
        SwaggerUIBundle.presets.apis,
        SwaggerUIBundle.SwaggerUIStandalonePreset
      ],
      layout: "BaseLayout",
      deepLinking: true,
    });
  }
    </script>
{% endblock %}



================================================
FILE: src/server/templates/components/_macros.jinja
================================================
{# Icon link #}
{% macro footer_icon_link(href, icon, label) -%}
    <a href="{{ href }}"
       target="_blank"
       rel="noopener noreferrer"
       class="hover:underline flex items-center">
        <img src="/static/{{ icon }}" alt="{{ label }} logo" class="w-4 h-4 mr-1">
        {{ label }}
    </a>
{%- endmacro %}



================================================
FILE: src/server/templates/components/footer.jinja
================================================
{% from 'components/_macros.jinja' import footer_icon_link %}
<footer class="w-full border-t-[3px] border-gray-900 mt-auto">
    <div class="max-w-4xl mx-auto px-4 py-4">
        <div class="grid grid-cols-3 items-center text-gray-900 text-sm">
            {# Left column — Chrome + PyPI #}
            <div class="flex items-center space-x-4">
                {{ footer_icon_link('https://chromewebstore.google.com/detail/adfjahbijlkjfoicpjkhjicpjpjfaood',
                                'icons/chrome.svg',
                                'Chrome Extension') }}
                {{ footer_icon_link('https://pypi.org/project/gitingest',
                                'icons/python.svg',
                                'Python Package') }}
            </div>
            {# Middle column - Version information #}
            <div class="flex justify-center">
                <span>Version:&nbsp;</span>
                {% if version != "unknown" %}
                    <a href="{{ version_link }}"
                       target="_blank"
                       rel="noopener noreferrer"
                       class="text-blue-600 hover:text-blue-800 underline">{{ version }}</a>
                {% else %}
                    <span>{{ version }}</span>
                {% endif %}
            </div>
            {# Right column - Discord #}
            <div class="flex justify-end">
                {{ footer_icon_link('https://discord.gg/zerRaGK9EC',
                                'icons/discord.svg',
                                'Discord') }}
            </div>
        </div>
    </div>
</footer>



================================================
FILE: src/server/templates/components/git_form.jinja
================================================
<div class="relative">
    <div class="w-full h-full absolute inset-0 bg-gray-900 rounded-xl translate-y-2 translate-x-2"></div>
    <div class="rounded-xl relative z-20 p-8 sm:p-10 border-[3px] border-gray-900 bg-[#fff4da]">
        <img src="https://cdn.devdojo.com/images/january2023/shape-1.png"
             class="absolute md:block hidden left-0 h-[4.5rem] w-[4.5rem] bottom-0 -translate-x-full ml-3">
        <!-- Ingest Form -->
        <form id="ingestForm" method="post" onsubmit="handleSubmit(event, true)">
            <!-- Top row: repo URL + Ingest button -->
            <div class="flex md:flex-row flex-col w-full h-full justify-center items-stretch space-y-5 md:space-y-0 md:space-x-5">
                <!-- Repository URL Input -->
                <div class="relative w-full h-full">
                    <div class="w-full h-full rounded bg-gray-900 translate-y-1 translate-x-1 absolute inset-0 z-10"></div>
                    <input type="text"
                           name="input_text"
                           id="input_text"
                           placeholder="https://github.com/..."
                           value="{{ repo_url if repo_url else '' }}"
                           required
                           class="border-[3px] w-full relative z-20 border-gray-900 placeholder-gray-600 text-lg font-medium focus:outline-none py-3.5 px-6 rounded bg-[#E8F0FE]">
                </div>
                <!-- Ingest button -->
                <div class="relative w-auto flex-shrink-0 h-full group">
                    <div class="w-full h-full rounded bg-gray-800 translate-y-1 translate-x-1 absolute inset-0 z-10"></div>
                    <button type="submit"
                            class="py-3.5 rounded px-6 group-hover:-translate-y-px group-hover:-translate-x-px ease-out duration-300 z-20 relative w-full border-[3px] border-gray-900 font-medium bg-[#ffc480] tracking-wide text-lg flex-shrink-0 text-gray-900">
                        Ingest
                    </button>
                </div>
            </div>
            <!-- Hidden fields -->
            <input type="hidden" name="pattern_type" value="exclude">
            <input type="hidden" name="pattern" value="">
            <!-- Controls row: pattern selector, file size slider, PAT checkbox with PAT field below -->
            <div id="controlsRow"
                 class="mt-7 grid gap-6 grid-cols-1 sm:grid-cols-[3fr_2fr] md:gap-x-10 lg:grid-cols-[5fr_4fr_4fr] lg:gap-y-0">
                <!-- Pattern selector -->
                <div class="w-full relative self-center">
                    <div class="w-full h-full rounded bg-gray-900 translate-y-1 translate-x-1 absolute inset-0 z-10"></div>
                    <div class="flex relative z-20 border-[3px] border-gray-900 rounded bg-white">
                        <!-- Pattern type selector -->
                        <div class="relative flex items-center">
                            <select id="pattern_type"
                                    name="pattern_type"
                                    onchange="changePattern()"
                                    class="pattern-select">
                                <option value="exclude"
                                        {% if pattern_type == 'exclude' or not pattern_type %}selected{% endif %}>
                                    Exclude
                                </option>
                                <option value="include" {% if pattern_type == 'include' %}selected{% endif %}>Include</option>
                            </select>
                            <svg class="absolute right-2 w-4 h-4 pointer-events-none"
                                 xmlns="http://www.w3.org/2000/svg"
                                 viewBox="0 0 24 24"
                                 fill="none"
                                 stroke="currentColor"
                                 stroke-width="2"
                                 stroke-linecap="round"
                                 stroke-linejoin="round">
                                <polyline points="6 9 12 15 18 9" />
                            </svg>
                        </div>
                        <!-- Pattern input field -->
                        <input type="text"
                               id="pattern"
                               name="pattern"
                               placeholder="*.md, src/ "
                               value="{{ pattern if pattern else '' }}"
                               class=" py-2 px-2 bg-[#E8F0FE] focus:outline-none w-full">
                    </div>
                </div>
                <!-- File size selector -->
                <div class="w-full self-center">
                    <label for="file_size" class="block text-gray-700 mb-1">
                        Include files under: <span id="size_value" class="font-bold">50kB</span>
                    </label>
                    <input type="range"
                           id="file_size"
                           min="1"
                           max="500"
                           required
                           value="{{ default_max_file_size }}"
                           class="w-full h-3 bg-[#FAFAFA] bg-no-repeat bg-[length:50%_100%] bg-[#ebdbb7] appearance-none border-[3px] border-gray-900 rounded-sm focus:outline-none bg-gradient-to-r from-[#FE4A60] to-[#FE4A60] [&::-webkit-slider-thumb]:w-5 [&::-webkit-slider-thumb]:h-7 [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:bg-white [&::-webkit-slider-thumb]:rounded-sm [&::-webkit-slider-thumb]:cursor-pointer [&::-webkit-slider-thumb]:border-solid [&::-webkit-slider-thumb]:border-[3px] [&::-webkit-slider-thumb]:border-gray-900 [&::-webkit-slider-thumb]:shadow-[3px_3px_0_#000]">
                    <input type="hidden" id="max_file_size_kb" name="max_file_size" value="">
                </div>
                <!-- PAT checkbox with PAT field below -->
                <div class="flex flex-col items-start w-full sm:col-span-2 lg:col-span-1 lg:row-span-2 lg:pt-3.5">
                    <!-- PAT checkbox -->
                    <div class="flex items-center space-x-2">
                        <label for="showAccessSettings"
                               class="flex gap-2 text-gray-900 cursor-pointer">
                            <div class="relative w-6 h-6">
                                <input type="checkbox"
                                       id="showAccessSettings"
                                       onchange="toggleAccessSettings()"
                                       {% if token %}checked{% endif %}
                                       class="cursor-pointer peer appearance-none w-full h-full rounded-sm border-[3px] border-current bg-white m-0 text-current shadow-[3px_3px_0_currentColor]" />
                                <span class="absolute inset-0 w-3 h-3 m-auto scale-0 transition-transform duration-150 ease-in-out shadow-[inset_1rem_1rem_#FE4A60] bg-[CanvasText] origin-bottom-left peer-checked:scale-100"
                                      style="clip-path: polygon(14% 44%, 0 65%, 50% 100%, 100% 16%, 80% 0%, 43% 62%)"></span>
                            </div>
                            Private Repository
                        </label>
                        <span class="badge-new">NEW</span>
                    </div>
                    <!-- PAT field -->
                    <div id="accessSettingsContainer"
                         class="{% if not token %}hidden {% endif %}mt-3 w-full">
                        <div class="relative w-full">
                            <div class="w-full h-full rounded bg-gray-900 translate-y-1 translate-x-1 absolute inset-0 z-10"></div>
                            <div class="flex relative z-20 border-[3px] border-gray-900 rounded bg-white">
                                <input id="token"
                                       type="password"
                                       name="token"
                                       placeholder="Personal Access Token"
                                       value="{{ token if token else '' }}"
                                       class="py-2 pl-2 pr-8 bg-[#E8F0FE] focus:outline-none w-full rounded">
                                <!-- Info icon with tooltip -->
                                <span class="absolute right-3 top-1/2 -translate-y-1/2">
                                    <!-- Icon -->
                                    <svg class="w-4 h-4 text-gray-600 cursor-pointer peer"
                                         xmlns="http://www.w3.org/2000/svg"
                                         fill="none"
                                         viewBox="0 0 24 24"
                                         stroke="currentColor"
                                         stroke-width="2">
                                        <circle cx="12" cy="12" r="10" />
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M12 16v-4m0-4h.01" />
                                    </svg>
                                    <!-- Tooltip (tooltip listens to peer-hover) -->
                                    <div class="absolute bottom-full mb-2 left-1/2 -translate-x-1/2 bg-gray-900 text-white text-xs leading-tight py-1 px-2 rounded shadow-lg opacity-0 pointer-events-none peer-hover:opacity-100 peer-hover:pointer-events-auto transition-opacity duration-200 whitespace-nowrap">
                                        <ul class="list-disc pl-4">
                                            <li>PAT is never stored in the backend</li>
                                            <li>Used once for cloning, then discarded from memory</li>
                                            <li>No browser caching</li>
                                            <li>Cloned repos are deleted after processing</li>
                                        </ul>
                                    </div>
                                </span>
                            </div>
                        </div>
                        <!-- Help section -->
                        <div class="mt-2 flex items-center space-x-1">
                            <a href="https://github.com/settings/tokens/new?description=gitingest&scopes=repo"
                               target="_blank"
                               rel="noopener noreferrer"
                               class="text-sm text-gray-600 hover:text-gray-800 flex items-center space-x-1 underline">
                                <span>Get your token</span>
                                <svg class="w-3 h-3"
                                     fill="none"
                                     stroke="currentColor"
                                     viewBox="0 0 24 24"
                                     xmlns="http://www.w3.org/2000/svg">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                                </svg>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </form>
        <!-- Example repositories section -->
        {% if show_examples %}
            <div id="exampleRepositories"
                 class="{% if token %}lg:mt-0 {% endif %} mt-4">
                <p class="opacity-70 mb-1">Try these example repositories:</p>
                <div class="flex flex-wrap gap-2">
                    {% for example in examples %}
                        <button onclick="submitExample('{{ example.url }}')"
                                class="px-4 py-1 bg-[#EBDBB7] hover:bg-[#FFC480] text-gray-900 rounded transition-colors duration-200 border-[3px] border-gray-900 relative hover:-translate-y-px hover:-translate-x-px">
                            {{ example.name }}
                        </button>
                    {% endfor %}
                </div>
            </div>
        {% endif %}
    </div>
</div>
<script defer src="/static/js/git.js"></script>
<script defer src="/static/js/git_form.js"></script>



================================================
FILE: src/server/templates/components/navbar.jinja
================================================
<header class="sticky top-0 bg-[#FFFDF8] border-b-[3px] border-gray-900 z-50">
    <div class="max-w-4xl mx-auto px-4">
        <div class="flex justify-between items-center h-16">
            {# Logo #}
            <div class="flex items-center gap-4">
                <h1 class="text-2xl font-bold tracking-tight">
                    <a href="/" class="hover:opacity-80 transition-opacity">
                        <span class="text-gray-900">Git</span><span class="text-[#FE4A60]">ingest</span>
                    </a>
                </h1>
            </div>
            {# Navigation with updated styling #}
            <nav class="flex items-center space-x-6">
                <a href="/llms.txt" class="link-bounce flex items-center text-gray-900">
                    <span class="badge-new">NEW</span>
                    /llms.txt
                </a>
                {# GitHub link #}
                <div class="flex items-center gap-2">
                    <a href="https://github.com/coderamp-labs/gitingest"
                       target="_blank"
                       rel="noopener noreferrer"
                       class="link-bounce flex items-center gap-1.5 text-gray-900">
                        <img src="/static/icons/github.svg" class="w-4 h-4" alt="GitHub logo">
                        GitHub
                    </a>
                    {# Star counter #}
                    <div class="no-drag flex items-center text-sm text-gray-600">
                        <img src="/static/svg/github-star.svg"
                             class="w-4 h-4 mr-1"
                             alt="GitHub star icon">
                        <span id="github-stars">0</span>
                    </div>
                </div>
            </nav>
        </div>
    </div>
</header>
{# Load GitHub stars script #}
<script defer src="/static/js/navbar.js"></script>



================================================
FILE: src/server/templates/components/result.jinja
================================================
<div class="mt-10">
    <!-- Error Message (hidden by default) -->
    <div id="results-error" style="display:none"></div>
    <!-- Loading Spinner (hidden by default) -->
    <div id="results-loading" style="display:none">
        <div class="relative mt-10">
            <div class="w-full h-full absolute inset-0 bg-black rounded-xl translate-y-2 translate-x-2"></div>
            <div class="bg-[#fafafa] rounded-xl border-[3px] border-gray-900 p-6 relative z-20 flex flex-col items-center space-y-4">
                <div class="loader border-8 border-[#fff4da] border-t-8 border-t-[#ffc480] rounded-full w-16 h-16 animate-spin"></div>
                <p class="text-lg font-bold text-gray-900">Loading...</p>
            </div>
        </div>
    </div>
    <!-- Results Section (hidden by default) -->
    <div id="results-section" style="display:none">
        <div class="relative">
            <div class="w-full h-full absolute inset-0 bg-gray-900 rounded-xl translate-y-2 translate-x-2"></div>
            <div class="bg-[#fafafa] rounded-xl border-[3px] border-gray-900 p-6 relative z-20 space-y-6">
                <div class="grid grid-cols-1 md:grid-cols-12 gap-6">
                    <div class="md:col-span-5">
                        <div class="flex justify-between items-center mb-4 py-2">
                            <h3 class="text-lg font-bold text-gray-900">Summary</h3>
                        </div>
                        <div class="relative">
                            <div class="w-full h-full rounded bg-gray-900 translate-y-1 translate-x-1 absolute inset-0"></div>
                            <textarea id="result-summary"
                                      class="w-full h-[160px] p-4 bg-[#fff4da] border-[3px] border-gray-900 rounded font-mono text-sm resize-none focus:outline-none relative z-10"
                                      readonly></textarea>
                        </div>
                        <div class="relative mt-4 inline-block group ml-4">
                            <div class="w-full h-full rounded bg-gray-900 translate-y-1 translate-x-1 absolute inset-0"></div>
                            <button onclick="copyFullDigest()"
                                    class="inline-flex items-center px-4 py-2 bg-[#ffc480] border-[3px] border-gray-900 text-gray-900 rounded group-hover:-translate-y-px group-hover:-translate-x-px transition-transform relative z-10">
                                <svg class="w-4 h-4 mr-2"
                                     fill="none"
                                     stroke="currentColor"
                                     viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" />
                                </svg>
                                Copy all
                            </button>
                        </div>
                        <div class="relative mt-4 inline-block group ml-4">
                            <div class="w-full h-full rounded bg-gray-900 translate-y-1 translate-x-1 absolute inset-0"></div>
                            <button onclick="downloadFullDigest()"
                                    class="inline-flex items-center px-4 py-2 bg-[#ffc480] border-[3px] border-gray-900 text-gray-900 rounded group-hover:-translate-y-px group-hover:-translate-x-px transition-transform relative z-10">
                                <svg class="w-4 h-4 mr-2"
                                     fill="none"
                                     stroke="currentColor"
                                     viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                                </svg>
                                Download
                            </button>
                        </div>
                    </div>
                    <div class="md:col-span-7">
                        <div class="flex justify-between items-center mb-4">
                            <h3 class="text-lg font-bold text-gray-900">Directory Structure</h3>
                            <div class="relative group">
                                <div class="w-full h-full rounded bg-gray-900 translate-y-1 translate-x-1 absolute inset-0"></div>
                                <button onclick="copyText('directory-structure')"
                                        class="px-4 py-2 bg-[#ffc480] border-[3px] border-gray-900 text-gray-900 rounded group-hover:-translate-y-px group-hover:-translate-x-px transition-transform relative z-10 flex items-center gap-2">
                                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" />
                                    </svg>
                                    Copy
                                </button>
                            </div>
                        </div>
                        <div class="relative">
                            <div class="w-full h-full rounded bg-gray-900 translate-y-1 translate-x-1 absolute inset-0"></div>
                            <div class="directory-structure w-full p-4 bg-[#fff4da] border-[3px] border-gray-900 rounded font-mono text-sm resize-y focus:outline-none relative z-10 h-[215px] overflow-auto"
                                 id="directory-structure-container"
                                 readonly>
                                <input type="hidden" id="directory-structure-content" value="" />
                                <pre id="directory-structure-pre"></pre>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="text-lg font-bold text-gray-900">Files Content</h3>
                        <div class="relative group">
                            <div class="w-full h-full rounded bg-gray-900 translate-y-1 translate-x-1 absolute inset-0"></div>
                            <button onclick="copyText('result-text')"
                                    class="px-4 py-2 bg-[#ffc480] border-[3px] border-gray-900 text-gray-900 rounded group-hover:-translate-y-px group-hover:-translate-x-px transition-transform relative z-10 flex items-center gap-2">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" />
                                </svg>
                                Copy
                            </button>
                        </div>
                    </div>
                    <div class="relative">
                        <div class="w-full h-full rounded bg-gray-900 translate-y-1 translate-x-1 absolute inset-0"></div>
                        <textarea id="result-content"
                                  class="result-text w-full p-4 bg-[#fff4da] border-[3px] border-gray-900 rounded font-mono text-sm resize-y focus:outline-none relative z-10"
                                  style="min-height: 600px"
                                  readonly></textarea>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>



================================================
FILE: src/server/templates/components/tailwind_components.html
================================================
<style type="text/tailwindcss">
  @layer components {
    .badge-new {
      @apply inline-block -rotate-6 -translate-y-1 mx-1 px-1 bg-[#FE4A60] border border-gray-900 text-white text-[10px] font-bold shadow-[2px_2px_0_0_rgba(0,0,0,1)];
    }
    .landing-page-title {
      @apply inline-block w-full relative text-center text-4xl sm:text-5xl md:text-6xl lg:text-7xl sm:pt-20 lg:pt-5 font-bold tracking-tighter;
    }
    .intro-text {
      @apply text-center text-gray-600 text-lg max-w-2xl mx-auto;
    }
    .sparkle-red {
      @apply absolute flex-shrink-0 h-auto w-14 sm:w-20 md:w-24 p-2 left-0 lg:ml-32 -translate-x-2 md:translate-x-10 lg:-translate-x-full -translate-y-4 sm:-translate-y-8 md:-translate-y-0 lg:-translate-y-10;
    }
    .sparkle-green {
      @apply absolute flex-shrink-0 right-0 bottom-0 w-10 sm:w-16 lg:w-20 -translate-x-10 lg:-translate-x-12 translate-y-4 sm:translate-y-10 md:translate-y-2 lg:translate-y-4;
    }
    .pattern-select {
      @apply min-w-max appearance-none pr-6 pl-2 py-2 bg-[#e6e8eb] border-r-[3px] border-gray-900 cursor-pointer focus:outline-none;
    }
  }

  @layer utilities {
    .no-drag {
      @apply pointer-events-none select-none;
      -webkit-user-drag: none;
    }
    .link-bounce {
      @apply transition-transform hover:-translate-y-0.5;
    }
  }
</style>



================================================
FILE: src/static/llms.txt
================================================
# GitIngest – **AI Agent Integration Guide**

Turn any Git repository into a prompt-ready text digest. GitIngest fetches, cleans, and formats source code so AI agents and Large Language Models can reason over complete projects programmatically.

**🤖 For AI Agents**: Use CLI or Python package for automated integration. Web UI is designed for human interaction only.

---
## 1. Installation

### 1.1 CLI Installation (Recommended for Scripts & Automation)
```bash
# Best practice: Use pipx for CLI tools (isolated environment)
pipx install gitingest

# Alternative: Use pip (may conflict with other packages)
pip install gitingest

# Verify installation
gitingest --help
```

### 1.2 Python Package Installation (For Code Integration)
```bash
# For projects/notebooks: Use pip in virtual environment
python -m venv gitingest-env
source gitingest-env/bin/activate  # On Windows: gitingest-env\Scripts\activate
pip install gitingest

# Or add to requirements.txt
echo "gitingest" >> requirements.txt
pip install -r requirements.txt

# For self-hosting: Install with server dependencies
pip install gitingest[server]

# For development: Install with dev dependencies
pip install gitingest[dev,server]
```

### 1.3 Installation Verification
```bash
# Test CLI installation
gitingest --version

# Test Python package
python -c "from gitingest import ingest; print('GitIngest installed successfully')"

# Quick functionality test
gitingest https://github.com/octocat/Hello-World -o test_output.txt
```

---
## 2. Quick-Start for AI Agents
| Method | Best for | One-liner |
|--------|----------|-----------|
| **CLI** | Scripts, automation, pipelines | `gitingest https://github.com/user/repo -o - \| your-llm` |
| **Python** | Code integration, notebooks, async tasks | `from gitingest import ingest; s,t,c = ingest('repo-url'); process(c)` |
| **URL Hack** | Quick web scraping (limited) | Replace `github.com` → `gitingest.com` in any GitHub URL |
| **Web UI** | **Human use only** | ~~Not recommended for AI agents~~ |

---
## 3. Output Format for AI Processing
GitIngest returns **structured plain-text** optimized for LLM consumption with three distinct sections:

### 3.1 Repository Summary
```
Repository: owner/repo-name
Files analyzed: 42
Estimated tokens: 15.2k
```
Contains basic metadata: repository name, file count, and token estimation for LLM planning.

### 3.2 Directory Structure
```
Directory structure:
└── project-name/
    ├── src/
    │   ├── main.py
    │   └── utils.py
    ├── tests/
    │   └── test_main.py
    └── README.md
```
Hierarchical tree view showing the complete project structure for context and navigation.

### 3.3 File Contents
Each file is wrapped with clear delimiters:
```
================================================
FILE: src/main.py
================================================
def hello_world():
    print("Hello, World!")

if __name__ == "__main__":
    hello_world()


================================================
FILE: README.md
================================================
# Project Title

This is a sample project...
```

### 3.4 Usage Example
```python
# Python package usage
from gitingest import ingest

summary, tree, content = ingest("https://github.com/octocat/Hello-World")

# Returns exactly:
# summary = "Repository: octocat/hello-world\nFiles analyzed: 1\nEstimated tokens: 29"
# tree = "Directory structure:\n└── octocat-hello-world/\n    └── README"
# content = "================================================\nFILE: README\n================================================\nHello World!\n\n\n"

# For AI processing, combine all sections:
full_context = f"{summary}\n\n{tree}\n\n{content}"
```

```bash
# CLI usage - pipe directly to your AI system
gitingest https://github.com/octocat/Hello-World -o - | your_llm_processor

# Output streams the complete formatted text:
# Repository: octocat/hello-world
# Files analyzed: 1
# Estimated tokens: 29
#
# Directory structure:
# └── octocat-hello-world/
#     └── README
#
# ================================================
# FILE: README
# ================================================
# Hello World!
```



---
## 4. AI Agent Integration Methods

### 4.1 CLI Integration (Recommended for Automation)
```bash
# Basic usage - pipe directly to your AI system
gitingest https://github.com/user/repo -o - | your_ai_processor

# Advanced filtering for focused analysis (long flags)
gitingest https://github.com/user/repo \
  --include-pattern "*.py" --include-pattern "*.js" --include-pattern "*.md" \
  --max-size 102400 \
  -o - | python your_analyzer.py

# Same command with short flags (more concise)
gitingest https://github.com/user/repo \
  -i "*.py" -i "*.js" -i "*.md" \
  -s 102400 \
  -o - | python your_analyzer.py

# Exclude unwanted files and directories (long flags)
gitingest https://github.com/user/repo \
  --exclude-pattern "node_modules/*" --exclude-pattern "*.log" \
  --exclude-pattern "dist/*" \
  -o - | your_analyzer

# Same with short flags
gitingest https://github.com/user/repo \
  -e "node_modules/*" -e "*.log" -e "dist/*" \
  -o - | your_analyzer

# Private repositories with token (short flag)
export GITHUB_TOKEN="ghp_your_token_here"
gitingest https://github.com/user/private-repo -t $GITHUB_TOKEN -o -

# Specific branch analysis (short flag)
gitingest https://github.com/user/repo -b main -o -

# Save to file (default: digest.txt in current directory)
gitingest https://github.com/user/repo -o my_analysis.txt

# Ultra-concise example for small files only
gitingest https://github.com/user/repo -i "*.py" -s 51200 -o -
```

**Key Parameters for AI Agents**:
- `-s` / `--max-size`: Maximum file size in bytes to process (default: no limit)
- `-i` / `--include-pattern`: Include files matching Unix shell-style wildcards
- `-e` / `--exclude-pattern`: Exclude files matching Unix shell-style wildcards
- `-b` / `--branch`: Specify branch to analyze (defaults to repository's default branch)
- `-t` / `--token`: GitHub personal access token for private repositories
- `-o` / `--output`: Stream to STDOUT with `-` (default saves to `digest.txt`)

### 4.2 Python Package (Best for Code Integration)
```python
from gitingest import ingest, ingest_async
import asyncio

# Synchronous processing
def analyze_repository(repo_url: str):
    summary, tree, content = ingest(repo_url)

    # Process metadata
    repo_info = parse_summary(summary)

    # Analyze structure
    file_structure = parse_tree(tree)

    # Process code content
    return analyze_code(content)

# Asynchronous processing (recommended for AI services)
async def batch_analyze_repos(repo_urls: list):
    tasks = [ingest_async(url) for url in repo_urls]
    results = await asyncio.gather(*tasks)
    return [process_repo_data(*result) for result in results]

# Memory-efficient processing for large repos
def stream_process_repo(repo_url: str):
    summary, tree, content = ingest(
        repo_url,
        max_file_size=51200,  # 50KB max per file
        include_patterns=["*.py", "*.js"],  # Focus on code files
    )

    # Process in chunks to manage memory
    for file_content in split_content(content):
        yield analyze_file(file_content)

# Filtering with exclude patterns
def analyze_without_deps(repo_url: str):
    summary, tree, content = ingest(
        repo_url,
        exclude_patterns=[
            "node_modules/*", "*.lock", "dist/*",
            "build/*", "*.min.js", "*.log"
        ]
    )
    return analyze_code(content)
```

**Python Integration Patterns**:
- **Batch Processing**: Use `ingest_async` for multiple repositories
- **Memory Management**: Use `max_file_size` and pattern filtering for large repos
- **Error Handling**: Wrap in try-catch for network/auth issues
- **Caching**: Store results to avoid repeated API calls
- **Pattern Filtering**: Use `include_patterns` and `exclude_patterns` lists

### 4.3 Web UI (❌ Not for AI Agents)
The web interface at `https://gitingest.com` is designed for **human interaction only**.

**Why AI agents should avoid the web UI**:
- Requires manual interaction and browser automation
- No programmatic access to results
- Rate limiting and CAPTCHA protection
- Inefficient for automated workflows

**Use CLI or Python package instead** for all AI agent integrations.

---
## 5. AI Agent Best Practices

### 5.1 Repository Analysis Workflows
```python
# Pattern 1: Full repository analysis
def full_repo_analysis(repo_url: str):
    summary, tree, content = ingest(repo_url)
    return {
        'metadata': extract_metadata(summary),
        'structure': analyze_structure(tree),
        'code_analysis': analyze_all_files(content),
        'insights': generate_insights(summary, tree, content)
    }

# Pattern 2: Selective file processing
def selective_analysis(repo_url: str, file_patterns: list):
    summary, tree, content = ingest(
        repo_url,
        include_patterns=file_patterns
    )
    return focused_analysis(content)

# Pattern 3: Streaming for large repos
def stream_analysis(repo_url: str):
    # First pass: get structure and metadata only
    summary, tree, _ = ingest(
        repo_url,
        include_patterns=["*.md", "*.txt"],
        max_file_size=10240  # 10KB limit for docs
    )

    # Then process code files selectively by language
    for pattern in ["*.py", "*.js", "*.go", "*.rs"]:
        _, _, content = ingest(
            repo_url,
            include_patterns=[pattern],
            max_file_size=51200  # 50KB limit for code
        )
        yield process_language_specific(content, pattern)
```

### 5.2 Error Handling for AI Agents
```python
from gitingest import ingest
from gitingest.utils.exceptions import GitIngestError
import time

def robust_ingest(repo_url: str, retries: int = 3):
    for attempt in range(retries):
        try:
            return ingest(repo_url)
        except GitIngestError as e:
            if attempt == retries - 1:
                return None, None, f"Failed to ingest: {e}"
            time.sleep(2 ** attempt)  # Exponential backoff
```

### 5.3 Private Repository Access
```python
import os
from gitingest import ingest

# Method 1: Environment variable
def ingest_private_repo(repo_url: str):
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        raise ValueError("GITHUB_TOKEN environment variable required")
    return ingest(repo_url, token=token)

# Method 2: Secure token management
def ingest_with_token_rotation(repo_url: str, token_manager):
    token = token_manager.get_active_token()
    try:
        return ingest(repo_url, token=token)
    except AuthenticationError:
        token = token_manager.rotate_token()
        return ingest(repo_url, token=token)
```

---
## 6. Integration Scenarios for AI Agents

| Use Case | Recommended Method | Example Implementation |
|----------|-------------------|----------------------|
| **Code Review Bot** | Python async | `await ingest_async(pr_repo)` → analyze changes |
| **Documentation Generator** | CLI with filtering | `gitingest repo -i "*.py" -i "*.md" -o -` |
| **Vulnerability Scanner** | Python with error handling | Batch process multiple repos |
| **Code Search Engine** | CLI → Vector DB | `gitingest repo -o - \| embed \| store` |
| **AI Coding Assistant** | Python integration | Load repo context into conversation |
| **CI/CD Analysis** | CLI integration | `gitingest repo -o - \| analyze_pipeline` |
| **Repository Summarization** | Python with streaming | Process large repos in chunks |
| **Dependency Analysis** | CLI exclude patterns | `gitingest repo -e "node_modules/*" -e "*.lock" -o -` |
| **Security Audit** | CLI with size limits | `gitingest repo -i "*.py" -i "*.js" -s 204800 -o -` |

---
## 7. Support & Resources for AI Developers
* **Web UI official instance**: https://gitingest.com
* **GitHub Repository**: https://github.com/coderamp-labs/gitingest
* **Python Package**: https://pypi.org/project/gitingest/
* **Community Support**: https://discord.gg/zerRaGK9EC

_GitIngest – Purpose-built for AI agents to understand entire codebases programmatically._



================================================
FILE: src/static/robots.txt
================================================
User-agent: *
Allow: /
Allow: /api/
Allow: /coderamp-labs/gitingest/



================================================
FILE: src/static/js/git.js
================================================
function waitForStars() {
    return new Promise((resolve) => {
        const check = () => {
            const stars = document.getElementById('github-stars');

            if (stars && stars.textContent !== '0') {resolve();}
            else {setTimeout(check, 10);}
        };

        check();
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const urlInput = document.getElementById('input_text');
    const form = document.getElementById('ingestForm');

    if (urlInput && urlInput.value.trim() && form) {
    // Wait for stars to be loaded before submitting
        waitForStars().then(() => {
            const submitEvent = new SubmitEvent('submit', {
                cancelable: true,
                bubbles: true
            });

            Object.defineProperty(submitEvent, 'target', {
                value: form,
                enumerable: true
            });
            handleSubmit(submitEvent, true);
        });
    }
});



================================================
FILE: src/static/js/git_form.js
================================================
// Strike-through / un-strike file lines when the pattern-type menu flips.
function changePattern() {
    const dirPre = document.getElementById('directory-structure-pre');

    if (!dirPre) {return;}

    const treeLineElements = Array.from(dirPre.querySelectorAll('pre[name="tree-line"]'));

    // Skip the first tree line element
    treeLineElements.slice(2).forEach((element) => {
        element.classList.remove('line-through');
        element.classList.remove('text-gray-500');
    });

    // Reset the pattern input field
    const patternInput = document.getElementById('pattern');

    if (patternInput) {
        patternInput.value = '';
    }
}

// Show/hide the Personal-Access-Token section when the "Private repository" checkbox is toggled.
function toggleAccessSettings() {
    const container = document.getElementById('accessSettingsContainer');
    const examples = document.getElementById('exampleRepositories');
    const show = document.getElementById('showAccessSettings')?.checked;

    container?.classList.toggle('hidden', !show);
    examples?.classList.toggle('lg:mt-0', show);
}



document.addEventListener('DOMContentLoaded', () => {
    toggleAccessSettings();
    changePattern();
});


// Make them available to existing inline attributes
window.changePattern = changePattern;
window.toggleAccessSettings = toggleAccessSettings;



================================================
FILE: src/static/js/index.js
================================================
function submitExample(repoName) {
    const input = document.getElementById('input_text');

    if (input) {
        input.value = repoName;
        input.focus();
    }
}

// Make it visible to inline onclick handlers
window.submitExample = submitExample;



================================================
FILE: src/static/js/navbar.js
================================================
// Fetch GitHub stars
function formatStarCount(count) {
    if (count >= 1000) {return `${ (count / 1000).toFixed(1) }k`;}

    return count.toString();
}

async function fetchGitHubStars() {
    try {
        const res = await fetch('https://api.github.com/repos/coderamp-labs/gitingest');

        if (!res.ok) {throw new Error(`${res.status} ${res.statusText}`);}
        const data = await res.json();

        document.getElementById('github-stars').textContent =
        formatStarCount(data.stargazers_count);
    } catch (err) {
        console.error('Error fetching GitHub stars:', err);
        const el = document.getElementById('github-stars').parentElement;

        if (el) {el.style.display = 'none';}
    }
}

// auto-run when script loads
fetchGitHubStars();



================================================
FILE: src/static/js/posthog.js
================================================
/* eslint-disable */
!function (t, e) {
    let o, n, p, r;
    if (e.__SV) {return;}                 // already loaded

    window.posthog = e;
    e._i = [];
    e.init = function (i, s, a) {
        function g(t, e) {
            const o = e.split(".");
            if (o.length === 2) {
                t = t[o[0]];
                e = o[1];
            }
            t[e] = function () {
                t.push([e].concat(Array.prototype.slice.call(arguments, 0)));
            };
        }

        p = t.createElement("script");
        p.type = "text/javascript";
        p.crossOrigin = "anonymous";
        p.async = true;
        p.src = `${ s.api_host.replace(".i.posthog.com", "-assets.i.posthog.com") }/static/array.js`;

        r = t.getElementsByTagName("script")[0];
        r.parentNode.insertBefore(p, r);

        let u = e;
        if (a !== undefined) {
            u = e[a] = [];
        } else {
            a = "posthog";
        }

        u.people = u.people || [];
        u.toString = function (t) {
            let e = "posthog";
            if (a !== "posthog") {e += `.${ a }`;}
            if (!t) {e += " (stub)";}
            return e;
        };
        u.people.toString = function () {
            return `${ u.toString(1) }.people (stub)`;
        };


        o = [
            "init", "capture", "register", "register_once", "register_for_session", "unregister",
            "unregister_for_session", "getFeatureFlag", "getFeatureFlagPayload", "isFeatureEnabled",
            "reloadFeatureFlags", "updateEarlyAccessFeatureEnrollment", "getEarlyAccessFeatures",
            "on", "onFeatureFlags", "onSessionId", "getSurveys", "getActiveMatchingSurveys",
            "renderSurvey", "canRenderSurvey", "getNextSurveyStep", "identify", "setPersonProperties",
            "group", "resetGroups", "setPersonPropertiesForFlags", "resetPersonPropertiesForFlags",
            "setGroupPropertiesForFlags", "resetGroupPropertiesForFlags", "reset", "get_distinct_id",
            "getGroups", "get_session_id", "get_session_replay_url", "alias", "set_config",
            "startSessionRecording", "stopSessionRecording", "sessionRecordingStarted",
            "captureException", "loadToolbar", "get_property", "getSessionProperty",
            "createPersonProfile", "opt_in_capturing", "opt_out_capturing",
            "has_opted_in_capturing", "has_opted_out_capturing", "clear_opt_in_out_capturing",
            "debug", "getPageViewId"
        ];

        for (n = 0; n < o.length; n++) {g(u, o[n]);}
        e._i.push([i, s, a]);
    };

    e.__SV = 1;
}(document, window.posthog || []);

/* Initialise PostHog */
posthog.init('phc_9aNpiIVH2zfTWeY84vdTWxvrJRCQQhP5kcVDXUvcdou', {
    api_host: 'https://eu.i.posthog.com',
    person_profiles: 'always',
});



================================================
FILE: src/static/js/utils.js
================================================
function getFileName(element) {
    const indentSize = 4;
    let path = '';
    let prevIndentLevel = null;

    while (element) {
        const line = element.textContent;
        const index = line.search(/[a-zA-Z0-9_.-]/);
        const indentLevel = index / indentSize;

        // Stop when we reach or go above the top-level directory
        if (indentLevel <= 1) {
            break;
        }

        // Only include directories that are one level above the previous
        if (prevIndentLevel === null || indentLevel === prevIndentLevel - 1) {
            const fileName = line.substring(index).trim();

            path = fileName + path;
            prevIndentLevel = indentLevel;
        }

        element = element.previousElementSibling;
    }

    return path;
}

function toggleFile(element) {
    const patternInput = document.getElementById('pattern');
    const patternFiles = patternInput.value ? patternInput.value.split(',').map((item) => item.trim()) : [];

    const directoryContainer = document.getElementById('directory-structure-container');
    const treeLineElements = Array.from(directoryContainer.children).filter((child) => child.tagName === 'PRE');

    // Skip the first two tree lines (header and repository name)
    if (treeLineElements[0] === element || treeLineElements[1] === element) {
        return;
    }

    element.classList.toggle('line-through');
    element.classList.toggle('text-gray-500');

    const fileName = getFileName(element);
    const fileIndex = patternFiles.indexOf(fileName);

    if (fileIndex !== -1) {
        patternFiles.splice(fileIndex, 1);
    } else {
        patternFiles.push(fileName);
    }

    patternInput.value = patternFiles.join(', ');
}

// Copy functionality
function copyText(className) {
    let textToCopy;

    if (className === 'directory-structure') {
    // For directory structure, get the hidden input value
        const hiddenInput = document.getElementById('directory-structure-content');

        if (!hiddenInput) {return;}
        textToCopy = hiddenInput.value;
    } else {
    // For other elements, get the textarea value
        const textarea = document.querySelector(`.${ className }`);

        if (!textarea) {return;}
        textToCopy = textarea.value;
    }

    const button = document.querySelector(`button[onclick="copyText('${className}')"]`);

    if (!button) {return;}

    // Copy text
    navigator.clipboard.writeText(textToCopy)
        .then(() => {
            // Store original content
            const originalContent = button.innerHTML;

            // Change button content
            button.innerHTML = 'Copied!';

            // Reset after 1 second
            setTimeout(() => {
                button.innerHTML = originalContent;
            }, 1000);
        })
        .catch((err) => {
            console.error('Failed to copy text:', err);
            const originalContent = button.innerHTML;

            button.innerHTML = 'Failed to copy';
            setTimeout(() => {
                button.innerHTML = originalContent;
            }, 1000);
        });
}

// Helper functions for toggling result blocks
function showLoading() {
    document.getElementById('results-loading').style.display = 'block';
    document.getElementById('results-section').style.display = 'none';
    document.getElementById('results-error').style.display = 'none';
}
function showResults() {
    document.getElementById('results-loading').style.display = 'none';
    document.getElementById('results-section').style.display = 'block';
    document.getElementById('results-error').style.display = 'none';
}
function showError(msg) {
    document.getElementById('results-loading').style.display = 'none';
    document.getElementById('results-section').style.display = 'none';
    const errorDiv = document.getElementById('results-error');

    errorDiv.innerHTML = msg;
    errorDiv.style.display = 'block';
}

// Helper function to collect form data
function collectFormData(form) {
    const json_data = {};
    const inputText = form.querySelector('[name="input_text"]');
    const token = form.querySelector('[name="token"]');
    const hiddenInput = document.getElementById('max_file_size_kb');
    const patternType = document.getElementById('pattern_type');
    const pattern = document.getElementById('pattern');

    if (inputText) {json_data.input_text = inputText.value;}
    if (token) {json_data.token = token.value;}
    if (hiddenInput) {json_data.max_file_size = hiddenInput.value;}
    if (patternType) {json_data.pattern_type = patternType.value;}
    if (pattern) {json_data.pattern = pattern.value;}

    return json_data;
}

// Helper function to manage button loading state
function setButtonLoadingState(submitButton, isLoading) {
    if (!isLoading) {
        submitButton.disabled = false;
        submitButton.innerHTML = submitButton.getAttribute('data-original-content') || 'Submit';
        submitButton.classList.remove('bg-[#ffb14d]');

        return;
    }

    // Store original content if not already stored
    if (!submitButton.getAttribute('data-original-content')) {
        submitButton.setAttribute('data-original-content', submitButton.innerHTML);
    }

    submitButton.disabled = true;
    submitButton.innerHTML = `
        <div class="flex items-center justify-center">
            <svg class="animate-spin h-5 w-5 text-gray-900" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            <span class="ml-2">Processing...</span>
        </div>
    `;
    submitButton.classList.add('bg-[#ffb14d]');
}

// Helper function to handle successful response
function handleSuccessfulResponse(data) {
    // Show results section
    showResults();

    // Store the digest_url for download functionality
    window.currentDigestUrl = data.digest_url;

    // Set plain text content for summary, tree, and content
    document.getElementById('result-summary').value = data.summary || '';
    document.getElementById('directory-structure-content').value = data.tree || '';
    document.getElementById('result-content').value = data.content || '';

    // Populate directory structure lines as clickable <pre> elements
    const dirPre = document.getElementById('directory-structure-pre');

    if (dirPre && data.tree) {
        dirPre.innerHTML = '';
        data.tree.split('\n').forEach((line) => {
            const pre = document.createElement('pre');

            pre.setAttribute('name', 'tree-line');
            pre.className = 'cursor-pointer hover:line-through hover:text-gray-500';
            pre.textContent = line;
            pre.onclick = function () { toggleFile(this); };
            dirPre.appendChild(pre);
        });
    }

    // Scroll to results
    document.getElementById('results-section').scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function handleSubmit(event, showLoadingSpinner = false) {
    event.preventDefault();
    const form = event.target || document.getElementById('ingestForm');

    if (!form) {return;}

    // Ensure hidden input is updated before collecting form data
    const slider = document.getElementById('file_size');
    const hiddenInput = document.getElementById('max_file_size_kb');

    if (slider && hiddenInput) {
        hiddenInput.value = logSliderToSize(slider.value);
    }

    if (showLoadingSpinner) {
        showLoading();
    }

    const submitButton = form.querySelector('button[type="submit"]');

    if (!submitButton) {return;}

    const json_data = collectFormData(form);

    if (showLoadingSpinner) {
        setButtonLoadingState(submitButton, true);
    }

    // Submit the form to /api/ingest as JSON
    fetch('/api/ingest', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(json_data)
    })
        .then(async (response) => {
            let data;

            try {
                data = await response.json();
            } catch {
                data = {};
            }
            setButtonLoadingState(submitButton, false);

            if (!response.ok) {
                // Show all error details if present
                if (Array.isArray(data.detail)) {
                    const details = data.detail.map((d) => `<li>${d.msg || JSON.stringify(d)}</li>`).join('');

                    showError(`<div class='mb-6 p-4 bg-red-50 border border-red-200 rounded-lg text-red-700'><b>Error(s):</b><ul>${details}</ul></div>`);

                    return;
                }
                // Other errors
                showError(`<div class='mb-6 p-4 bg-red-50 border border-red-200 rounded-lg text-red-700'>${data.error || JSON.stringify(data) || 'An error occurred.'}</div>`);

                return;
            }

            // Handle error in data
            if (data.error) {
                showError(`<div class='mb-6 p-4 bg-red-50 border border-red-200 rounded-lg text-red-700'>${data.error}</div>`);

                return;
            }

            handleSuccessfulResponse(data);
        })
        .catch((error) => {
            setButtonLoadingState(submitButton, false);
            showError(`<div class='mb-6 p-4 bg-red-50 border border-red-200 rounded-lg text-red-700'>${error}</div>`);
        });
}

function copyFullDigest() {
    const directoryStructure = document.getElementById('directory-structure-content').value;
    const filesContent = document.querySelector('.result-text').value;
    const fullDigest = `${directoryStructure}\n\nFiles Content:\n\n${filesContent}`;
    const button = document.querySelector('[onclick="copyFullDigest()"]');
    const originalText = button.innerHTML;

    navigator.clipboard.writeText(fullDigest).then(() => {
        button.innerHTML = `
            <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
            </svg>
            Copied!
        `;

        setTimeout(() => {
            button.innerHTML = originalText;
        }, 2000);
    })
        .catch((err) => {
            console.error('Failed to copy text: ', err);
        });
}

function downloadFullDigest() {
    // Check if we have a digest_url
    if (!window.currentDigestUrl) {
        console.error('No digest_url available for download');

        return;
    }

    // Show feedback on the button
    const button = document.querySelector('[onclick="downloadFullDigest()"]');
    const originalText = button.innerHTML;

    button.innerHTML = `
        <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path>
        </svg>
        Downloading...
    `;

    // Create a download link using the digest_url
    const a = document.createElement('a');

    a.href = window.currentDigestUrl;
    a.download = 'digest.txt';
    document.body.appendChild(a);
    a.click();

    // Clean up
    document.body.removeChild(a);

    // Update button to show success
    button.innerHTML = `
        <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
        </svg>
        Downloaded!
    `;

    setTimeout(() => {
        button.innerHTML = originalText;
    }, 2000);
}

// Add the logSliderToSize helper function
function logSliderToSize(position) {
    const maxPosition = 500;
    const maxValue = Math.log(102400); // 100 MB

    const value = Math.exp(maxValue * (position / maxPosition)**1.5);

    return Math.round(value);
}

// Move slider initialization to a separate function
function initializeSlider() {
    const slider = document.getElementById('file_size');
    const sizeValue = document.getElementById('size_value');
    const hiddenInput = document.getElementById('max_file_size_kb');

    if (!slider || !sizeValue || !hiddenInput) {return;}

    function updateSlider() {
        const value = logSliderToSize(slider.value);

        sizeValue.textContent = formatSize(value);
        slider.style.backgroundSize = `${(slider.value / slider.max) * 100}% 100%`;
        hiddenInput.value = value; // Set hidden input to KB value
    }

    // Update on slider change
    slider.addEventListener('input', updateSlider);

    // Initialize slider position
    updateSlider();
}

// Add helper function for formatting size
function formatSize(sizeInKB) {
    if (sizeInKB >= 1024) {
        return `${ Math.round(sizeInKB / 1024) }MB`;
    }

    return `${ Math.round(sizeInKB) }kB`;
}

// Add this new function
function setupGlobalEnterHandler() {
    document.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' && !event.target.matches('textarea')) {
            const form = document.getElementById('ingestForm');

            if (form) {
                handleSubmit(new Event('submit'), true);
            }
        }
    });
}

// Add to the DOMContentLoaded event listener
document.addEventListener('DOMContentLoaded', () => {
    initializeSlider();
    setupGlobalEnterHandler();
});


// Make sure these are available globally
window.handleSubmit = handleSubmit;
window.toggleFile = toggleFile;
window.copyText = copyText;
window.copyFullDigest = copyFullDigest;
window.downloadFullDigest = downloadFullDigest;



================================================
FILE: tests/__init__.py
================================================
"""Tests for the gitingest package."""



================================================
FILE: tests/conftest.py
================================================
"""Fixtures for tests.

This file provides shared fixtures for creating sample queries, a temporary directory structure, and a helper function
to write ``.ipynb`` notebooks for testing notebook utilities.
"""

from __future__ import annotations

import json
import sys
import uuid
from pathlib import Path
from typing import TYPE_CHECKING, Any, Callable, Dict
from unittest.mock import AsyncMock, MagicMock

import pytest

from gitingest.query_parser import IngestionQuery

if TYPE_CHECKING:
    from pytest_mock import MockerFixture

WriteNotebookFunc = Callable[[str, Dict[str, Any]], Path]

DEMO_URL = "https://github.com/user/repo"
LOCAL_REPO_PATH = "/tmp/repo"
DEMO_COMMIT = "deadbeefdeadbeefdeadbeefdeadbeefdeadbeef"


def get_ensure_git_installed_call_count() -> int:
    """Get the number of calls made by ensure_git_installed based on platform.

    On Windows, ensure_git_installed makes 2 calls:
    1. git --version
    2. git config core.longpaths

    On other platforms, it makes 1 call:
    1. git --version

    Returns
    -------
    int
        The number of calls made by ensure_git_installed

    """
    return 2 if sys.platform == "win32" else 1


@pytest.fixture
def sample_query() -> IngestionQuery:
    """Provide a default ``IngestionQuery`` object for use in tests.

    This fixture returns a ``IngestionQuery`` pre-populated with typical fields and some default ignore patterns.

    Returns
    -------
    IngestionQuery
        The sample ``IngestionQuery`` object.

    """
    return IngestionQuery(
        user_name="test_user",
        repo_name="test_repo",
        local_path=Path("/tmp/test_repo").resolve(),
        slug="test_user/test_repo",
        id=uuid.uuid4(),
        branch="main",
        max_file_size=1_000_000,
        ignore_patterns={"*.pyc", "__pycache__", ".git"},
    )


@pytest.fixture
def temp_directory(tmp_path: Path) -> Path:
    """Create a temporary directory structure for testing repository scanning.

    The structure includes:
    test_repo/
    ├── file1.txt
    ├── file2.py
    ├── src/
    │   ├── subfile1.txt
    │   ├── subfile2.py
    │   └── subdir/
    │       ├── file_subdir.txt
    │       └── file_subdir.py
    ├── dir1/
    │   └── file_dir1.txt
    └── dir2/
        └── file_dir2.txt

    Parameters
    ----------
    tmp_path : Path
        The temporary directory path provided by the ``tmp_path`` fixture.

    Returns
    -------
    Path
        The path to the created ``test_repo`` directory.

    """
    test_dir = tmp_path / "test_repo"
    test_dir.mkdir()

    # Root files
    (test_dir / "file1.txt").write_text("Hello World")
    (test_dir / "file2.py").write_text("print('Hello')")

    # src directory and its files
    src_dir = test_dir / "src"
    src_dir.mkdir()
    (src_dir / "subfile1.txt").write_text("Hello from src")
    (src_dir / "subfile2.py").write_text("print('Hello from src')")

    # src/subdir and its files
    subdir = src_dir / "subdir"
    subdir.mkdir()
    (subdir / "file_subdir.txt").write_text("Hello from subdir")
    (subdir / "file_subdir.py").write_text("print('Hello from subdir')")

    # dir1 and its file
    dir1 = test_dir / "dir1"
    dir1.mkdir()
    (dir1 / "file_dir1.txt").write_text("Hello from dir1")

    # dir2 and its file
    dir2 = test_dir / "dir2"
    dir2.mkdir()
    (dir2 / "file_dir2.txt").write_text("Hello from dir2")

    return test_dir


@pytest.fixture
def write_notebook(tmp_path: Path) -> WriteNotebookFunc:
    """Provide a helper function to write a ``.ipynb`` notebook file with the given content.

    Parameters
    ----------
    tmp_path : Path
        The temporary directory path provided by the ``tmp_path`` fixture.

    Returns
    -------
    WriteNotebookFunc
        A callable that accepts a filename and a dictionary (representing JSON notebook data), writes it to a
        ``.ipynb`` file, and returns the path to the file.

    """

    def _write_notebook(name: str, content: dict[str, Any]) -> Path:
        notebook_path = tmp_path / name
        with notebook_path.open(mode="w", encoding="utf-8") as f:
            json.dump(content, f)
        return notebook_path

    return _write_notebook


@pytest.fixture
def stub_resolve_sha(mocker: MockerFixture) -> dict[str, AsyncMock]:
    """Patch *both* async helpers that hit the network.

    Include this fixture *only* in tests that should stay offline.
    """
    head_mock = mocker.patch(
        "gitingest.utils.query_parser_utils._resolve_ref_to_sha",
        new_callable=mocker.AsyncMock,
        return_value=DEMO_COMMIT,
    )
    ref_mock = mocker.patch(
        "gitingest.utils.git_utils._resolve_ref_to_sha",
        new_callable=mocker.AsyncMock,
        return_value=DEMO_COMMIT,
    )
    # return whichever you want to assert on; here we return the dict
    return {"head": head_mock, "ref": ref_mock}


@pytest.fixture
def stub_branches(mocker: MockerFixture) -> Callable[[list[str]], None]:
    """Return a function that stubs git branch discovery to *branches*."""

    def _factory(branches: list[str]) -> None:
        # Patch the GitPython fetch function
        mocker.patch(
            "gitingest.utils.git_utils.fetch_remote_branches_or_tags",
            new_callable=AsyncMock,
            return_value=branches,
        )

        # Patch GitPython's ls_remote method to return the mocked output
        ls_remote_output = "\n".join(f"{DEMO_COMMIT[:12]}{i:02d}\trefs/heads/{b}" for i, b in enumerate(branches))
        mock_git_cmd = mocker.patch("git.Git")
        mock_git_cmd.return_value.ls_remote.return_value = ls_remote_output

        # Also patch the git module imports in our utils
        mocker.patch("gitingest.utils.git_utils.git.Git", return_value=mock_git_cmd.return_value)

    return _factory


@pytest.fixture
def repo_exists_true(mocker: MockerFixture) -> AsyncMock:
    """Patch ``gitingest.clone.check_repo_exists`` to always return ``True``."""
    return mocker.patch("gitingest.clone.check_repo_exists", return_value=True)


@pytest.fixture
def run_command_mock(mocker: MockerFixture) -> AsyncMock:
    """Patch ``gitingest.clone.run_command`` with an ``AsyncMock``.

    The mocked function returns a dummy process whose ``communicate`` method yields generic
    ``stdout`` / ``stderr`` bytes. Tests can still access / tweak the mock via the fixture argument.
    """
    mock = AsyncMock(side_effect=_fake_run_command)
    mocker.patch("gitingest.utils.git_utils.run_command", mock)

    # Mock GitPython components
    _setup_gitpython_mocks(mocker)

    return mock


@pytest.fixture
def gitpython_mocks(mocker: MockerFixture) -> dict[str, MagicMock]:
    """Provide comprehensive GitPython mocks for testing."""
    return _setup_gitpython_mocks(mocker)


def _setup_gitpython_mocks(mocker: MockerFixture) -> dict[str, MagicMock]:
    """Set up comprehensive GitPython mocks."""
    # Mock git.Git class
    mock_git_cmd = MagicMock()
    mock_git_cmd.version.return_value = "git version 2.34.1"
    mock_git_cmd.config.return_value = "true"
    mock_git_cmd.execute.return_value = f"{DEMO_COMMIT}\trefs/heads/main\n"
    mock_git_cmd.ls_remote.return_value = f"{DEMO_COMMIT}\trefs/heads/main\n"
    mock_git_cmd.clone.return_value = ""

    # Mock git.Repo class
    mock_repo = MagicMock()
    mock_repo.git = MagicMock()
    mock_repo.git.fetch = MagicMock()
    mock_repo.git.checkout = MagicMock()
    mock_repo.git.submodule = MagicMock()
    mock_repo.git.execute = MagicMock()
    mock_repo.git.config = MagicMock()
    mock_repo.git.sparse_checkout = MagicMock()

    # Mock git.Repo.clone_from
    mock_clone_from = MagicMock(return_value=mock_repo)

    git_git_mock = mocker.patch("git.Git", return_value=mock_git_cmd)
    git_repo_mock = mocker.patch("git.Repo", return_value=mock_repo)
    mocker.patch("git.Repo.clone_from", mock_clone_from)

    # Patch imports in our modules
    mocker.patch("gitingest.utils.git_utils.git.Git", return_value=mock_git_cmd)
    mocker.patch("gitingest.utils.git_utils.git.Repo", return_value=mock_repo)
    mocker.patch("gitingest.clone.git.Git", return_value=mock_git_cmd)
    mocker.patch("gitingest.clone.git.Repo", return_value=mock_repo)
    mocker.patch("gitingest.clone.git.Repo.clone_from", mock_clone_from)

    return {
        "git_cmd": mock_git_cmd,
        "repo": mock_repo,
        "clone_from": mock_clone_from,
        "git_git_mock": git_git_mock,
        "git_repo_mock": git_repo_mock,
    }


async def _fake_run_command(*args: str) -> tuple[bytes, bytes]:
    if "ls-remote" in args:
        # single match: <sha> <tab>refs/heads/main
        return (f"{DEMO_COMMIT}\trefs/heads/main\n".encode(), b"")
    return (b"output", b"error")



================================================
FILE: tests/test_cli.py
================================================
"""Tests for the Gitingest CLI."""

from __future__ import annotations

from inspect import signature
from pathlib import Path

import pytest
from click.testing import CliRunner, Result

from gitingest.__main__ import main
from gitingest.config import MAX_FILE_SIZE, OUTPUT_FILE_NAME


@pytest.mark.parametrize(
    ("cli_args", "expect_file"),
    [
        pytest.param(["./"], True, id="default-options"),
        pytest.param(
            [
                "./",
                "--output",
                str(OUTPUT_FILE_NAME),
                "--max-size",
                str(MAX_FILE_SIZE),
                "--exclude-pattern",
                "tests/",
                "--include-pattern",
                "src/",
                "--include-submodules",
            ],
            True,
            id="custom-options",
        ),
    ],
)
def test_cli_writes_file(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    *,
    cli_args: list[str],
    expect_file: bool,
) -> None:
    """Run the CLI and verify that the SARIF file is created (or not)."""
    expectes_exit_code = 0
    # Work inside an isolated temp directory
    monkeypatch.chdir(tmp_path)

    result = _invoke_isolated_cli_runner(cli_args)

    assert result.exit_code == expectes_exit_code, result.stderr

    # Summary line should be on STDOUT
    stdout_lines = result.stdout.splitlines()
    assert f"Analysis complete! Output written to: {OUTPUT_FILE_NAME}" in stdout_lines

    # File side-effect
    sarif_file = tmp_path / OUTPUT_FILE_NAME
    assert sarif_file.exists() is expect_file, f"{OUTPUT_FILE_NAME} existence did not match expectation"


def test_cli_with_stdout_output() -> None:
    """Test CLI invocation with output directed to STDOUT."""
    output_file = Path(OUTPUT_FILE_NAME)
    # Clean up any existing digest.txt file before test
    if output_file.exists():
        output_file.unlink()

    try:
        result = _invoke_isolated_cli_runner(["./", "--output", "-", "--exclude-pattern", "tests/"])

        # ─── core expectations (stdout) ────────────────────────────────────-
        assert result.exit_code == 0, f"CLI exited with code {result.exit_code}, stderr: {result.stderr}"
        assert "---" in result.stdout, "Expected file separator '---' not found in STDOUT"
        assert "src/gitingest/__main__.py" in result.stdout, (
            "Expected content (e.g., src/gitingest/__main__.py) not found in STDOUT"
        )
        assert not output_file.exists(), f"Output file {output_file} was unexpectedly created."

        # ─── the summary must *not* pollute STDOUT, must appear on STDERR ───
        summary = "Analysis complete! Output sent to stdout."
        stdout_lines = result.stdout.splitlines()
        stderr_lines = result.stderr.splitlines()
        assert summary not in stdout_lines, "Unexpected summary message found in STDOUT"
        assert summary in stderr_lines, "Expected summary message not found in STDERR"
        assert f"Output written to: {output_file.name}" not in stderr_lines
    finally:
        # Clean up any digest.txt file that might have been created during test
        if output_file.exists():
            output_file.unlink()


def _invoke_isolated_cli_runner(args: list[str]) -> Result:
    """Return a ``CliRunner`` that keeps ``stderr`` separate on Click 8.0-8.1."""
    kwargs = {}
    if "mix_stderr" in signature(CliRunner.__init__).parameters:
        kwargs["mix_stderr"] = False  # Click 8.0-8.1
    runner = CliRunner(**kwargs)
    return runner.invoke(main, args)



================================================
FILE: tests/test_clone.py
================================================
"""Tests for the ``clone`` module.

These tests cover various scenarios for cloning repositories, verifying that the appropriate Git commands are invoked
and handling edge cases such as nonexistent URLs, timeouts, redirects, and specific commits or branches.
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

import pytest

from gitingest.clone import clone_repo
from gitingest.schemas import CloneConfig
from gitingest.utils.git_utils import check_repo_exists
from tests.conftest import DEMO_URL, LOCAL_REPO_PATH

if TYPE_CHECKING:
    from pathlib import Path
    from unittest.mock import AsyncMock

    from pytest_mock import MockerFixture


# All cloning-related tests assume (unless explicitly overridden) that the repository exists.
# Apply the check-repo patch automatically so individual tests don't need to repeat it.
pytestmark = pytest.mark.usefixtures("repo_exists_true")

GIT_INSTALLED_CALLS = 2 if sys.platform == "win32" else 1


@pytest.mark.asyncio
async def test_clone_with_commit(repo_exists_true: AsyncMock, gitpython_mocks: dict) -> None:
    """Test cloning a repository with a specific commit hash.

    Given a valid URL and a commit hash:
    When ``clone_repo`` is called,
    Then the repository should be cloned and checked out at that commit.
    """
    commit_hash = "a" * 40  # Simulating a valid commit hash
    clone_config = CloneConfig(
        url=DEMO_URL,
        local_path=LOCAL_REPO_PATH,
        commit=commit_hash,
        branch="main",
    )

    await clone_repo(clone_config)

    repo_exists_true.assert_any_call(clone_config.url, token=None)

    # Verify GitPython calls were made
    mock_git_cmd = gitpython_mocks["git_cmd"]
    mock_repo = gitpython_mocks["repo"]
    mock_clone_from = gitpython_mocks["clone_from"]

    # Should have called version (for ensure_git_installed)
    mock_git_cmd.version.assert_called()

    # Should have called clone_from (since partial_clone=False)
    mock_clone_from.assert_called_once()

    # Should have called fetch and checkout on the repo
    mock_repo.git.fetch.assert_called()
    mock_repo.git.checkout.assert_called_with(commit_hash)


@pytest.mark.asyncio
async def test_clone_nonexistent_repository(repo_exists_true: AsyncMock) -> None:
    """Test cloning a nonexistent repository URL.

    Given an invalid or nonexistent URL:
    When ``clone_repo`` is called,
    Then a ValueError should be raised with an appropriate error message.
    """
    clone_config = CloneConfig(
        url="https://github.com/user/nonexistent-repo",
        local_path=LOCAL_REPO_PATH,
        commit=None,
        branch="main",
    )
    # Override the default fixture behaviour for this test
    repo_exists_true.return_value = False

    with pytest.raises(ValueError, match="Repository not found"):
        await clone_repo(clone_config)

    repo_exists_true.assert_any_call(clone_config.url, token=None)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("git_command_succeeds", "expected"),
    [
        (True, True),  # git ls-remote succeeds -> repo exists
        (False, False),  # git ls-remote fails -> repo doesn't exist or no access
    ],
)
async def test_check_repo_exists(
    git_command_succeeds: bool,  # noqa: FBT001
    *,
    expected: bool,
    mocker: MockerFixture,
) -> None:
    """Verify that ``check_repo_exists`` works by using _resolve_ref_to_sha."""
    mock_resolve = mocker.patch("gitingest.utils.git_utils._resolve_ref_to_sha")

    if git_command_succeeds:
        mock_resolve.return_value = "abc123def456"  # Mock SHA
    else:
        mock_resolve.side_effect = ValueError("Repository not found")

    result = await check_repo_exists(DEMO_URL)

    assert result is expected
    mock_resolve.assert_called_once_with(DEMO_URL, "HEAD", token=None)


@pytest.mark.asyncio
async def test_clone_without_commit(repo_exists_true: AsyncMock, gitpython_mocks: dict) -> None:
    """Test cloning a repository when no commit hash is provided.

    Given a valid URL and no commit hash:
    When ``clone_repo`` is called,
    Then the repository should be cloned and checked out at the resolved commit.
    """
    clone_config = CloneConfig(url=DEMO_URL, local_path=LOCAL_REPO_PATH, commit=None, branch="main")

    await clone_repo(clone_config)

    repo_exists_true.assert_any_call(clone_config.url, token=None)

    # Verify GitPython calls were made
    mock_git_cmd = gitpython_mocks["git_cmd"]
    mock_repo = gitpython_mocks["repo"]
    mock_clone_from = gitpython_mocks["clone_from"]

    # Should have resolved the commit via ls_remote
    mock_git_cmd.ls_remote.assert_called()
    # Should have cloned the repo
    mock_clone_from.assert_called_once()
    # Should have fetched and checked out
    mock_repo.git.fetch.assert_called()
    mock_repo.git.checkout.assert_called()


@pytest.mark.asyncio
async def test_clone_creates_parent_directory(tmp_path: Path, gitpython_mocks: dict) -> None:
    """Test that ``clone_repo`` creates parent directories if they don't exist.

    Given a local path with non-existent parent directories:
    When ``clone_repo`` is called,
    Then it should create the parent directories before attempting to clone.
    """
    nested_path = tmp_path / "deep" / "nested" / "path" / "repo"
    clone_config = CloneConfig(url=DEMO_URL, local_path=str(nested_path))

    await clone_repo(clone_config)

    # Verify parent directories were created
    assert nested_path.parent.exists()

    # Verify clone operation happened
    mock_clone_from = gitpython_mocks["clone_from"]
    mock_clone_from.assert_called_once()


@pytest.mark.asyncio
async def test_clone_with_specific_subpath(gitpython_mocks: dict) -> None:
    """Test cloning a repository with a specific subpath.

    Given a valid repository URL and a specific subpath:
    When ``clone_repo`` is called,
    Then the repository should be cloned with sparse checkout enabled.
    """
    subpath = "src/docs"
    clone_config = CloneConfig(url=DEMO_URL, local_path=LOCAL_REPO_PATH, subpath=subpath)

    await clone_repo(clone_config)

    # Verify partial clone (using git.clone instead of Repo.clone_from)
    mock_git_cmd = gitpython_mocks["git_cmd"]
    mock_git_cmd.clone.assert_called()

    # Verify sparse checkout was configured
    mock_repo = gitpython_mocks["repo"]
    mock_repo.git.sparse_checkout.assert_called()


@pytest.mark.asyncio
async def test_clone_with_include_submodules(gitpython_mocks: dict) -> None:
    """Test cloning a repository with submodules included.

    Given a valid URL and ``include_submodules=True``:
    When ``clone_repo`` is called,
    Then the repository should update submodules after cloning.
    """
    clone_config = CloneConfig(url=DEMO_URL, local_path=LOCAL_REPO_PATH, branch="main", include_submodules=True)

    await clone_repo(clone_config)

    # Verify submodule update was called
    mock_repo = gitpython_mocks["repo"]
    mock_repo.git.submodule.assert_called_with("update", "--init", "--recursive", "--depth=1")


@pytest.mark.asyncio
async def test_check_repo_exists_with_auth_token(mocker: MockerFixture) -> None:
    """Test ``check_repo_exists`` with authentication token.

    Given a GitHub URL and a token:
    When ``check_repo_exists`` is called,
    Then it should pass the token to _resolve_ref_to_sha.
    """
    mock_resolve = mocker.patch("gitingest.utils.git_utils._resolve_ref_to_sha")
    mock_resolve.return_value = "abc123def456"  # Mock SHA

    test_token = "token123"  # noqa: S105
    result = await check_repo_exists("https://github.com/test/repo", token=test_token)

    assert result is True
    mock_resolve.assert_called_once_with("https://github.com/test/repo", "HEAD", token=test_token)



================================================
FILE: tests/test_git_utils.py
================================================
"""Tests for the ``git_utils`` module.

These tests validate the ``validate_github_token`` function, which ensures that
GitHub personal access tokens (PATs) are properly formatted.
"""

from __future__ import annotations

import base64
from typing import TYPE_CHECKING

import pytest

from gitingest.utils.exceptions import InvalidGitHubTokenError
from gitingest.utils.git_utils import create_git_auth_header, create_git_repo, is_github_host, validate_github_token

if TYPE_CHECKING:
    from pathlib import Path

    from pytest_mock import MockerFixture


@pytest.mark.parametrize(
    "token",
    [
        # Valid tokens: correct prefixes and at least 36 allowed characters afterwards
        "github_pat_" + "a" * 22 + "_" + "b" * 59,
        "ghp_" + "A" * 36,
        "ghu_" + "B" * 36,
        "ghs_" + "C" * 36,
        "ghr_" + "D" * 36,
        "gho_" + "E" * 36,
    ],
)
def test_validate_github_token_valid(token: str) -> None:
    """validate_github_token should accept properly-formatted tokens."""
    # Should not raise any exception
    validate_github_token(token)


@pytest.mark.parametrize(
    "token",
    [
        "github_pat_short",  # Too short after prefix
        "ghp_" + "b" * 35,  # one character short
        "invalidprefix_" + "c" * 36,  # Wrong prefix
        "github_pat_" + "!" * 36,  # Disallowed characters
        "github_pat_" + "a" * 36,  # Too short after 'github_pat_' prefix
        "",  # Empty string
    ],
)
def test_validate_github_token_invalid(token: str) -> None:
    """Test that ``validate_github_token`` raises ``InvalidGitHubTokenError`` on malformed tokens."""
    with pytest.raises(InvalidGitHubTokenError):
        validate_github_token(token)


@pytest.mark.parametrize(
    ("local_path", "url", "token", "should_configure_auth"),
    [
        (
            "/some/path",
            "https://github.com/owner/repo.git",
            None,
            False,  # No auth configuration expected when token is None
        ),
        (
            "/some/path",
            "https://github.com/owner/repo.git",
            "ghp_" + "d" * 36,
            True,  # Auth configuration expected for GitHub URL + token
        ),
        (
            "/some/path",
            "https://gitlab.com/owner/repo.git",
            "ghp_" + "e" * 36,
            False,  # No auth configuration for non-GitHub URL even if token provided
        ),
    ],
)
def test_create_git_repo(
    local_path: str,
    url: str,
    token: str | None,
    should_configure_auth: bool,  # noqa: FBT001
    mocker: MockerFixture,
) -> None:
    """Test that ``create_git_repo`` creates a proper Git repo object."""
    # Mock git.Repo to avoid actual filesystem operations
    mock_repo = mocker.MagicMock()
    mock_repo_class = mocker.patch("git.Repo", return_value=mock_repo)

    repo = create_git_repo(local_path, url, token)

    # Should create repo with correct path
    mock_repo_class.assert_called_once_with(local_path)
    assert repo == mock_repo

    # Check auth configuration
    if should_configure_auth:
        mock_repo.git.config.assert_called_once()
    else:
        mock_repo.git.config.assert_not_called()


@pytest.mark.parametrize(
    "token",
    [
        "ghp_abcdefghijklmnopqrstuvwxyz012345",  # typical ghp_ token
        "github_pat_1234567890abcdef1234567890abcdef1234",
    ],
)
def test_create_git_auth_header(token: str) -> None:
    """Test that ``create_git_auth_header`` produces correct base64-encoded header."""
    header = create_git_auth_header(token)
    expected_basic = base64.b64encode(f"x-oauth-basic:{token}".encode()).decode()
    expected = f"http.https://github.com/.extraheader=Authorization: Basic {expected_basic}"
    assert header == expected


@pytest.mark.parametrize(
    ("url", "token", "should_call"),
    [
        ("https://github.com/foo/bar.git", "ghp_" + "f" * 36, True),
        ("https://github.com/foo/bar.git", None, False),
        ("https://gitlab.com/foo/bar.git", "ghp_" + "g" * 36, False),
    ],
)
def test_create_git_repo_helper_calls(
    mocker: MockerFixture,
    tmp_path: Path,
    *,
    url: str,
    token: str | None,
    should_call: bool,
) -> None:
    """Test that ``create_git_auth_header`` is invoked only when appropriate."""
    work_dir = tmp_path / "repo"
    header_mock = mocker.patch("gitingest.utils.git_utils.create_git_auth_header", return_value="key=value")
    mock_repo = mocker.MagicMock()
    mocker.patch("git.Repo", return_value=mock_repo)

    create_git_repo(str(work_dir), url, token)

    if should_call:
        header_mock.assert_called_once_with(token, url=url)
        mock_repo.git.config.assert_called_once_with("key", "value")
    else:
        header_mock.assert_not_called()
        mock_repo.git.config.assert_not_called()


@pytest.mark.parametrize(
    ("url", "expected"),
    [
        # GitHub.com URLs
        ("https://github.com/owner/repo.git", True),
        ("http://github.com/owner/repo.git", True),
        ("https://github.com/owner/repo", True),
        # GitHub Enterprise URLs
        ("https://github.company.com/owner/repo.git", True),
        ("https://github.enterprise.org/owner/repo.git", True),
        ("http://github.internal/owner/repo.git", True),
        ("https://github.example.co.uk/owner/repo.git", True),
        # Non-GitHub URLs
        ("https://gitlab.com/owner/repo.git", False),
        ("https://bitbucket.org/owner/repo.git", False),
        ("https://git.example.com/owner/repo.git", False),
        ("https://mygithub.com/owner/repo.git", False),  # doesn't start with "github."
        ("https://subgithub.com/owner/repo.git", False),
        ("https://example.com/github/repo.git", False),
        # Edge cases
        ("", False),
        ("not-a-url", False),
        ("ftp://github.com/owner/repo.git", True),  # Different protocol but still github.com
    ],
)
def test_is_github_host(url: str, *, expected: bool) -> None:
    """Test that ``is_github_host`` correctly identifies GitHub and GitHub Enterprise URLs."""
    assert is_github_host(url) == expected


@pytest.mark.parametrize(
    ("token", "url", "expected_hostname"),
    [
        # GitHub.com URLs (default)
        ("ghp_" + "a" * 36, "https://github.com", "github.com"),
        ("ghp_" + "a" * 36, "https://github.com/owner/repo.git", "github.com"),
        # GitHub Enterprise URLs
        ("ghp_" + "b" * 36, "https://github.company.com", "github.company.com"),
        ("ghp_" + "c" * 36, "https://github.enterprise.org/owner/repo.git", "github.enterprise.org"),
        ("ghp_" + "d" * 36, "http://github.internal", "github.internal"),
    ],
)
def test_create_git_auth_header_with_ghe_url(token: str, url: str, expected_hostname: str) -> None:
    """Test that ``create_git_auth_header`` handles GitHub Enterprise URLs correctly."""
    header = create_git_auth_header(token, url=url)
    expected_basic = base64.b64encode(f"x-oauth-basic:{token}".encode()).decode()
    expected = f"http.https://{expected_hostname}/.extraheader=Authorization: Basic {expected_basic}"
    assert header == expected


@pytest.mark.parametrize(
    ("local_path", "url", "token", "expected_auth_hostname"),
    [
        # GitHub.com URLs - should use default hostname
        (
            "/some/path",
            "https://github.com/owner/repo.git",
            "ghp_" + "a" * 36,
            "github.com",
        ),
        # GitHub Enterprise URLs - should use custom hostname
        (
            "/some/path",
            "https://github.company.com/owner/repo.git",
            "ghp_" + "b" * 36,
            "github.company.com",
        ),
        (
            "/some/path",
            "https://github.enterprise.org/owner/repo.git",
            "ghp_" + "c" * 36,
            "github.enterprise.org",
        ),
        (
            "/some/path",
            "http://github.internal/owner/repo.git",
            "ghp_" + "d" * 36,
            "github.internal",
        ),
    ],
)
def test_create_git_repo_with_ghe_urls(
    local_path: str,
    url: str,
    token: str,
    expected_auth_hostname: str,
    mocker: MockerFixture,
) -> None:
    """Test that ``create_git_repo`` handles GitHub Enterprise URLs correctly."""
    mock_repo = mocker.MagicMock()
    mocker.patch("git.Repo", return_value=mock_repo)

    create_git_repo(local_path, url, token)

    # Should configure auth with the correct hostname
    mock_repo.git.config.assert_called_once()
    auth_config_call = mock_repo.git.config.call_args[0]

    # The first argument should contain the hostname
    assert expected_auth_hostname in auth_config_call[0]


@pytest.mark.parametrize(
    ("local_path", "url", "token"),
    [
        # Should NOT configure auth for non-GitHub URLs
        ("/some/path", "https://gitlab.com/owner/repo.git", "ghp_" + "a" * 36),
        ("/some/path", "https://bitbucket.org/owner/repo.git", "ghp_" + "b" * 36),
        ("/some/path", "https://git.example.com/owner/repo.git", "ghp_" + "c" * 36),
    ],
)
def test_create_git_repo_ignores_non_github_urls(
    local_path: str,
    url: str,
    token: str,
    mocker: MockerFixture,
) -> None:
    """Test that ``create_git_repo`` does not configure auth for non-GitHub URLs."""
    mock_repo = mocker.MagicMock()
    mocker.patch("git.Repo", return_value=mock_repo)

    create_git_repo(local_path, url, token)

    # Should not configure auth for non-GitHub URLs
    mock_repo.git.config.assert_not_called()



================================================
FILE: tests/test_gitignore_feature.py
================================================
"""Tests for the gitignore functionality in Gitingest."""

from pathlib import Path

import pytest

from gitingest.entrypoint import ingest_async
from gitingest.utils.ignore_patterns import load_ignore_patterns


@pytest.fixture(name="repo_path")
def repo_fixture(tmp_path: Path) -> Path:
    """Create a temporary repository structure.

    The repository structure includes:
    - A ``.gitignore`` that excludes ``exclude.txt``
    - ``include.txt`` (should be processed)
    - ``exclude.txt`` (should be skipped when gitignore rules are respected)
    """
    # Create a .gitignore file that excludes 'exclude.txt'
    gitignore_file = tmp_path / ".gitignore"
    gitignore_file.write_text("exclude.txt\n")

    # Create a file that should be included
    include_file = tmp_path / "include.txt"
    include_file.write_text("This file should be included.")

    # Create a file that should be excluded
    exclude_file = tmp_path / "exclude.txt"
    exclude_file.write_text("This file should be excluded.")

    return tmp_path


def test_load_gitignore_patterns(tmp_path: Path) -> None:
    """Test that ``load_ignore_patterns()`` correctly loads patterns from a ``.gitignore`` file."""
    gitignore = tmp_path / ".gitignore"
    # Write some sample patterns with a comment line included
    gitignore.write_text("exclude.txt\n*.log\n# a comment\n")

    patterns = load_ignore_patterns(tmp_path, filename=".gitignore")

    # Check that the expected patterns are loaded
    assert "exclude.txt" in patterns
    assert "*.log" in patterns
    # Ensure that comment lines are not added
    for pattern in patterns:
        assert not pattern.startswith("#")


@pytest.mark.asyncio
async def test_ingest_with_gitignore(repo_path: Path) -> None:
    """Integration test for ``ingest_async()`` respecting ``.gitignore`` rules.

    When ``include_gitignored`` is ``False`` (default), the content of ``exclude.txt`` should be omitted.
    When ``include_gitignored`` is ``True``, both files should be present.
    """
    # Run ingestion with the gitignore functionality enabled.
    _, _, content_with_ignore = await ingest_async(source=str(repo_path))
    # 'exclude.txt' should be skipped.
    assert "This file should be excluded." not in content_with_ignore
    # 'include.txt' should be processed.
    assert "This file should be included." in content_with_ignore

    # Run ingestion with the gitignore functionality disabled.
    _, _, content_without_ignore = await ingest_async(source=str(repo_path), include_gitignored=True)
    # Now both files should be present.
    assert "This file should be excluded." in content_without_ignore
    assert "This file should be included." in content_without_ignore



================================================
FILE: tests/test_ingestion.py
================================================
"""Tests for the ``query_ingestion`` module.

These tests validate directory scanning, file content extraction, notebook handling, and the overall ingestion logic,
including filtering patterns and subpaths.
"""

from __future__ import annotations

import re
from typing import TYPE_CHECKING, TypedDict

import pytest

from gitingest.ingestion import ingest_query

if TYPE_CHECKING:
    from pathlib import Path

    from gitingest.query_parser import IngestionQuery


def test_run_ingest_query(temp_directory: Path, sample_query: IngestionQuery) -> None:
    """Test ``ingest_query`` to ensure it processes the directory and returns expected results.

    Given a directory with ``.txt`` and ``.py`` files:
    When ``ingest_query`` is invoked,
    Then it should produce a summary string listing the files analyzed and a combined content string.
    """
    sample_query.local_path = temp_directory
    sample_query.subpath = "/"
    sample_query.type = None

    summary, _, content = ingest_query(sample_query)

    assert "Repository: test_user/test_repo" in summary
    assert "Files analyzed: 8" in summary

    # Check presence of key files in the content
    assert "src/subfile1.txt" in content
    assert "src/subfile2.py" in content
    assert "src/subdir/file_subdir.txt" in content
    assert "src/subdir/file_subdir.py" in content
    assert "file1.txt" in content
    assert "file2.py" in content
    assert "dir1/file_dir1.txt" in content
    assert "dir2/file_dir2.txt" in content


# TODO: Additional tests:
# - Multiple include patterns, e.g. ["*.txt", "*.py"] or ["/src/*", "*.txt"].
# - Edge cases with weird file names or deep subdirectory structures.
# TODO : def test_include_nonexistent_extension


class PatternScenario(TypedDict):
    """A scenario for testing the ingestion of a set of patterns."""

    include_patterns: set[str]
    ignore_patterns: set[str]
    expected_num_files: int
    expected_content: set[str]
    expected_structure: set[str]
    expected_not_structure: set[str]


@pytest.mark.parametrize(
    "pattern_scenario",
    [
        pytest.param(
            PatternScenario(
                {
                    "include_patterns": {"file2.py", "dir2/file_dir2.txt"},
                    "ignore_patterns": {*()},
                    "expected_num_files": 2,
                    "expected_content": {"file2.py", "dir2/file_dir2.txt"},
                    "expected_structure": {"test_repo/", "dir2/"},
                    "expected_not_structure": {"src/", "subdir/", "dir1/"},
                },
            ),
            id="include-explicit-files",
        ),
        pytest.param(
            PatternScenario(
                {
                    "include_patterns": {
                        "file1.txt",
                        "file2.py",
                        "file_dir1.txt",
                        "*/file_dir2.txt",
                    },
                    "ignore_patterns": {*()},
                    "expected_num_files": 4,
                    "expected_content": {"file1.txt", "file2.py", "dir1/file_dir1.txt", "dir2/file_dir2.txt"},
                    "expected_structure": {"test_repo/", "dir1/", "dir2/"},
                    "expected_not_structure": {"src/", "subdir/"},
                },
            ),
            id="include-wildcard-directory",
        ),
        pytest.param(
            PatternScenario(
                {
                    "include_patterns": {"*.py"},
                    "ignore_patterns": {*()},
                    "expected_num_files": 3,
                    "expected_content": {
                        "file2.py",
                        "src/subfile2.py",
                        "src/subdir/file_subdir.py",
                    },
                    "expected_structure": {"test_repo/", "src/", "subdir/"},
                    "expected_not_structure": {"dir1/", "dir2/"},
                },
            ),
            id="include-wildcard-files",
        ),
        pytest.param(
            PatternScenario(
                {
                    "include_patterns": {"**/file_dir2.txt", "src/**/*.py"},
                    "ignore_patterns": {*()},
                    "expected_num_files": 3,
                    "expected_content": {
                        "dir2/file_dir2.txt",
                        "src/subfile2.py",
                        "src/subdir/file_subdir.py",
                    },
                    "expected_structure": {"test_repo/", "dir2/", "src/", "subdir/"},
                    "expected_not_structure": {"dir1/"},
                },
            ),
            id="include-recursive-wildcard",
        ),
        pytest.param(
            PatternScenario(
                {
                    "include_patterns": {*()},
                    "ignore_patterns": {"file2.py", "dir2/file_dir2.txt"},
                    "expected_num_files": 6,
                    "expected_content": {
                        "file1.txt",
                        "src/subfile1.txt",
                        "src/subfile2.py",
                        "src/subdir/file_subdir.txt",
                        "src/subdir/file_subdir.py",
                        "dir1/file_dir1.txt",
                    },
                    "expected_structure": {"test_repo/", "src/", "subdir/", "dir1/"},
                    "expected_not_structure": {"dir2/"},
                },
            ),
            id="exclude-explicit-files",
        ),
        pytest.param(
            PatternScenario(
                {
                    "include_patterns": {*()},
                    "ignore_patterns": {"file1.txt", "file2.py", "*/file_dir1.txt"},
                    "expected_num_files": 5,
                    "expected_content": {
                        "src/subfile1.txt",
                        "src/subfile2.py",
                        "src/subdir/file_subdir.txt",
                        "src/subdir/file_subdir.py",
                        "dir2/file_dir2.txt",
                    },
                    "expected_structure": {"test_repo/", "src/", "subdir/", "dir2/"},
                    "expected_not_structure": {"dir1/"},
                },
            ),
            id="exclude-wildcard-directory",
        ),
        pytest.param(
            PatternScenario(
                {
                    "include_patterns": {*()},
                    "ignore_patterns": {"src/**/*.py"},
                    "expected_num_files": 6,
                    "expected_content": {
                        "file1.txt",
                        "file2.py",
                        "src/subfile1.txt",
                        "src/subdir/file_subdir.txt",
                        "dir1/file_dir1.txt",
                        "dir2/file_dir2.txt",
                    },
                    "expected_structure": {
                        "test_repo/",
                        "dir1/",
                        "dir2/",
                        "src/",
                        "subdir/",
                    },
                    "expected_not_structure": {*()},
                },
            ),
            id="exclude-recursive-wildcard",
        ),
    ],
)
def test_include_ignore_patterns(
    temp_directory: Path,
    sample_query: IngestionQuery,
    pattern_scenario: PatternScenario,
) -> None:
    """Test ``ingest_query`` to ensure included and ignored paths are included and ignored respectively.

    Given a directory with ``.txt`` and ``.py`` files, and a set of include patterns or a set of ignore patterns:
    When ``ingest_query`` is invoked,
    Then it should produce a summary string listing the files analyzed and a combined content string.
    """
    sample_query.local_path = temp_directory
    sample_query.subpath = "/"
    sample_query.type = None
    sample_query.include_patterns = pattern_scenario["include_patterns"]
    sample_query.ignore_patterns = pattern_scenario["ignore_patterns"]

    summary, structure, content = ingest_query(sample_query)

    assert "Repository: test_user/test_repo" in summary
    num_files_regex = re.compile(r"^Files analyzed: (\d+)$", re.MULTILINE)
    assert (num_files_match := num_files_regex.search(summary)) is not None
    assert int(num_files_match.group(1)) == pattern_scenario["expected_num_files"]

    # Check presence of key files in the content
    for expected_content_item in pattern_scenario["expected_content"]:
        assert expected_content_item in content

    # check presence of included directories in structure
    for expected_structure_item in pattern_scenario["expected_structure"]:
        assert expected_structure_item in structure

    # check non-presence of non-included directories in structure
    for expected_not_structure_item in pattern_scenario["expected_not_structure"]:
        assert expected_not_structure_item not in structure



================================================
FILE: tests/test_notebook_utils.py
================================================
"""Tests for the ``notebook`` utils module.

These tests validate how notebooks are processed into Python-like output, ensuring that markdown/raw cells are
converted to triple-quoted blocks, code cells remain executable code, and various edge cases (multiple worksheets,
empty cells, outputs, etc.) are handled appropriately.
"""

import pytest

from gitingest.utils.notebook import process_notebook
from tests.conftest import WriteNotebookFunc


def test_process_notebook_all_cells(write_notebook: WriteNotebookFunc) -> None:
    """Test processing a notebook containing markdown, code, and raw cells.

    Given a notebook with:
      - One markdown cell
      - One code cell
      - One raw cell
    When ``process_notebook`` is invoked,
    Then markdown and raw cells should appear in triple-quoted blocks, and code cells remain as normal code.
    """
    expected_count = 4
    notebook_content = {
        "cells": [
            {"cell_type": "markdown", "source": ["# Markdown cell"]},
            {"cell_type": "code", "source": ['print("Hello Code")']},
            {"cell_type": "raw", "source": ["<raw content>"]},
        ],
    }
    nb_path = write_notebook("all_cells.ipynb", notebook_content)
    result = process_notebook(nb_path)

    assert result.count('"""') == expected_count, (
        "Two non-code cells => 2 triple-quoted blocks => 4 total triple quotes."
    )

    # Ensure markdown and raw cells are in triple quotes
    assert "# Markdown cell" in result
    assert "<raw content>" in result

    # Ensure code cell is not in triple quotes
    assert 'print("Hello Code")' in result
    assert '"""\nprint("Hello Code")\n"""' not in result


def test_process_notebook_with_worksheets(write_notebook: WriteNotebookFunc) -> None:
    """Test a notebook containing the (as of IPEP-17 deprecated) ``worksheets`` key.

    Given a notebook that uses the ``worksheets`` key with a single worksheet,
    When ``process_notebook`` is called,
    Then a ``DeprecationWarning`` should be raised, and the content should match an equivalent notebook
    that has top-level ``cells``.
    """
    with_worksheets = {
        "worksheets": [
            {
                "cells": [
                    {"cell_type": "markdown", "source": ["# Markdown cell"]},
                    {"cell_type": "code", "source": ['print("Hello Code")']},
                    {"cell_type": "raw", "source": ["<raw content>"]},
                ],
            },
        ],
    }
    without_worksheets = with_worksheets["worksheets"][0]  # same, but no 'worksheets' key

    nb_with = write_notebook("with_worksheets.ipynb", with_worksheets)
    nb_without = write_notebook("without_worksheets.ipynb", without_worksheets)

    result_with = process_notebook(nb_with)

    # Should not raise a warning
    result_without = process_notebook(nb_without)

    assert result_with == result_without, "Content from the single worksheet should match the top-level equivalent."


def test_process_notebook_multiple_worksheets(write_notebook: WriteNotebookFunc) -> None:
    """Test a notebook containing multiple ``worksheets``.

    Given a notebook with two worksheets:
      - First with a markdown cell
      - Second with a code cell
    When ``process_notebook`` is called,
    Then a warning about multiple worksheets should be raised, and the second worksheet's content should appear
    in the final output.
    """
    multi_worksheets = {
        "worksheets": [
            {"cells": [{"cell_type": "markdown", "source": ["# First Worksheet"]}]},
            {"cells": [{"cell_type": "code", "source": ["# Second Worksheet"]}]},
        ],
    }

    single_worksheet = {
        "worksheets": [
            {"cells": [{"cell_type": "markdown", "source": ["# First Worksheet"]}]},
        ],
    }

    nb_multi = write_notebook("multiple_worksheets.ipynb", multi_worksheets)
    nb_single = write_notebook("single_worksheet.ipynb", single_worksheet)

    result_multi = process_notebook(nb_multi)

    result_single = process_notebook(nb_single)

    assert result_multi != result_single, "Two worksheets should produce more content than one."
    assert len(result_multi) > len(result_single), "The multi-worksheet notebook should have extra code content."
    assert "# First Worksheet" in result_single
    assert "# Second Worksheet" not in result_single
    assert "# First Worksheet" in result_multi
    assert "# Second Worksheet" in result_multi


def test_process_notebook_code_only(write_notebook: WriteNotebookFunc) -> None:
    """Test a notebook containing only code cells.

    Given a notebook with code cells only:
    When ``process_notebook`` is called,
    Then no triple quotes should appear in the output.
    """
    notebook_content = {
        "cells": [
            {"cell_type": "code", "source": ["print('Code Cell 1')"]},
            {"cell_type": "code", "source": ["x = 42"]},
        ],
    }
    nb_path = write_notebook("code_only.ipynb", notebook_content)
    result = process_notebook(nb_path)

    assert '"""' not in result, "No triple quotes expected when there are only code cells."
    assert "print('Code Cell 1')" in result
    assert "x = 42" in result


def test_process_notebook_markdown_only(write_notebook: WriteNotebookFunc) -> None:
    """Test a notebook with only markdown cells.

    Given a notebook with two markdown cells:
    When ``process_notebook`` is called,
    Then each markdown cell should become a triple-quoted block (2 blocks => 4 triple quotes total).
    """
    expected_count = 4
    notebook_content = {
        "cells": [
            {"cell_type": "markdown", "source": ["# Markdown Header"]},
            {"cell_type": "markdown", "source": ["Some more markdown."]},
        ],
    }
    nb_path = write_notebook("markdown_only.ipynb", notebook_content)
    result = process_notebook(nb_path)

    assert result.count('"""') == expected_count, "Two markdown cells => 2 blocks => 4 triple quotes total."
    assert "# Markdown Header" in result
    assert "Some more markdown." in result


def test_process_notebook_raw_only(write_notebook: WriteNotebookFunc) -> None:
    """Test a notebook with only raw cells.

    Given two raw cells:
    When ``process_notebook`` is called,
    Then each raw cell should become a triple-quoted block (2 blocks => 4 triple quotes total).
    """
    expected_count = 4
    notebook_content = {
        "cells": [
            {"cell_type": "raw", "source": ["Raw content line 1"]},
            {"cell_type": "raw", "source": ["Raw content line 2"]},
        ],
    }
    nb_path = write_notebook("raw_only.ipynb", notebook_content)
    result = process_notebook(nb_path)

    assert result.count('"""') == expected_count, "Two raw cells => 2 blocks => 4 triple quotes."
    assert "Raw content line 1" in result
    assert "Raw content line 2" in result


def test_process_notebook_empty_cells(write_notebook: WriteNotebookFunc) -> None:
    """Test that cells with an empty ``source`` are skipped.

    Given a notebook with 4 cells, 3 of which have empty ``source``:
    When ``process_notebook`` is called,
    Then only the non-empty cell should appear in the output (1 block => 2 triple quotes).
    """
    expected_count = 2
    notebook_content = {
        "cells": [
            {"cell_type": "markdown", "source": []},
            {"cell_type": "code", "source": []},
            {"cell_type": "raw", "source": []},
            {"cell_type": "markdown", "source": ["# Non-empty markdown"]},
        ],
    }
    nb_path = write_notebook("empty_cells.ipynb", notebook_content)
    result = process_notebook(nb_path)

    assert result.count('"""') == expected_count, "Only one non-empty cell => 1 block => 2 triple quotes"
    assert "# Non-empty markdown" in result


def test_process_notebook_invalid_cell_type(write_notebook: WriteNotebookFunc) -> None:
    """Test a notebook with an unknown cell type.

    Given a notebook cell whose ``cell_type`` is unrecognized:
    When ``process_notebook`` is called,
    Then a ValueError should be raised.
    """
    notebook_content = {
        "cells": [
            {"cell_type": "markdown", "source": ["# Valid markdown"]},
            {"cell_type": "unknown", "source": ["Unrecognized cell type"]},
        ],
    }
    nb_path = write_notebook("invalid_cell_type.ipynb", notebook_content)

    with pytest.raises(ValueError, match="Unknown cell type: unknown"):
        process_notebook(nb_path)


def test_process_notebook_with_output(write_notebook: WriteNotebookFunc) -> None:
    """Test a notebook that has code cells with outputs.

    Given a code cell and multiple output objects:
    When ``process_notebook`` is called with ``include_output=True``,
    Then the outputs should be appended as commented lines under the code.
    """
    notebook_content = {
        "cells": [
            {
                "cell_type": "code",
                "source": [
                    "import matplotlib.pyplot as plt\n",
                    "print('my_data')\n",
                    "my_data = [1, 2, 3, 4, 5]\n",
                    "plt.plot(my_data)\n",
                    "my_data",
                ],
                "outputs": [
                    {"output_type": "stream", "text": ["my_data"]},
                    {"output_type": "execute_result", "data": {"text/plain": ["[1, 2, 3, 4, 5]"]}},
                    {"output_type": "display_data", "data": {"text/plain": ["<Figure size 640x480 with 1 Axes>"]}},
                ],
            },
        ],
    }

    nb_path = write_notebook("with_output.ipynb", notebook_content)
    with_output = process_notebook(nb_path, include_output=True)
    without_output = process_notebook(nb_path, include_output=False)

    expected_source = (
        "# Jupyter notebook converted to Python script.\n\n"
        "import matplotlib.pyplot as plt\n"
        "print('my_data')\n"
        "my_data = [1, 2, 3, 4, 5]\n"
        "plt.plot(my_data)\n"
        "my_data\n"
    )

    expected_output = "# Output:\n#   my_data\n#   [1, 2, 3, 4, 5]\n#   <Figure size 640x480 with 1 Axes>\n"

    expected_combined = expected_source + expected_output

    assert with_output == expected_combined, "Should include source code and comment-ified output."
    assert without_output == expected_source, "Should include only the source code without output."



================================================
FILE: tests/test_pattern_utils.py
================================================
"""Test pattern utilities."""

from gitingest.utils.ignore_patterns import DEFAULT_IGNORE_PATTERNS
from gitingest.utils.pattern_utils import _parse_patterns, process_patterns


def test_process_patterns_empty_patterns() -> None:
    """Test ``process_patterns`` with empty patterns.

    Given empty ``include_patterns`` and ``exclude_patterns``:
    When ``process_patterns`` is called,
    Then ``include_patterns`` becomes ``None`` and ``DEFAULT_IGNORE_PATTERNS`` apply.
    """
    exclude_patterns, include_patterns = process_patterns(exclude_patterns="", include_patterns="")

    assert include_patterns is None
    assert exclude_patterns == DEFAULT_IGNORE_PATTERNS


def test_parse_patterns_valid() -> None:
    """Test ``_parse_patterns`` with valid comma-separated patterns.

    Given patterns like "*.py, *.md, docs/*":
    When ``_parse_patterns`` is called,
    Then it should return a set of parsed strings.
    """
    patterns = "*.py, *.md, docs/*"
    parsed_patterns = _parse_patterns(patterns)

    assert parsed_patterns == {"*.py", "*.md", "docs/*"}


def test_process_patterns_include_and_ignore_overlap() -> None:
    """Test ``process_patterns`` with overlapping patterns.

    Given include="*.py" and ignore={"*.py", "*.txt"}:
    When ``process_patterns`` is called,
    Then "*.py" should be removed from ignore patterns.
    """
    exclude_patterns, include_patterns = process_patterns(exclude_patterns={"*.py", "*.txt"}, include_patterns="*.py")

    assert include_patterns == {"*.py"}
    assert exclude_patterns is not None
    assert "*.py" not in exclude_patterns
    assert "*.txt" in exclude_patterns



================================================
FILE: tests/test_summary.py
================================================
"""Test that ``gitingest.ingest()`` emits a concise, 5-or-6-line summary."""

import re
from pathlib import Path

import pytest

from gitingest import ingest

REPO = "pallets/flask"

PATH_CASES = [
    ("tree", "/examples/celery"),
    ("blob", "/examples/celery/make_celery.py"),
    ("blob", "/.gitignore"),
]

REF_CASES = [
    ("Branch", "main"),
    ("Branch", "stable"),
    ("Tag", "3.0.3"),
    ("Commit", "e9741288637e0d9abe95311247b4842a017f7d5c"),
]


@pytest.mark.parametrize(("path_type", "path"), PATH_CASES)
@pytest.mark.parametrize(("ref_type", "ref"), REF_CASES)
def test_ingest_summary(path_type: str, path: str, ref_type: str, ref: str) -> None:
    """Assert that ``gitingest.ingest()`` emits a concise, 5-or-6-line summary.

    - Non-'main” refs → 5 key/value pairs + blank line (6 total).
    - 'main” branch   → ref line omitted (5 total).
    - Required keys:
        - Repository
        - ``ref_type`` (absent on 'main”)
        - File│Subpath (chosen by ``path_type``)
        - Lines│Files analyzed (chosen by ``path_type``)
        - Estimated tokens (positive integer)

    Any missing key, wrong value, or incorrect line count should fail.

    Parameters
    ----------
    path_type : {"tree", "blob"}
        GitHub object type under test.
    path : str
        The repository sub-path or file path to feed into the URL.
    ref_type : {"Branch", "Tag", "Commit"}
        Label expected on line 2 of the summary (absent if `ref` is "main").
    ref : str
        Actual branch name, tag, or commit hash.

    """
    is_main_branch = ref == "main"
    is_blob = path_type == "blob"
    expected_lines = _calculate_expected_lines(ref_type, is_main_branch=is_main_branch)
    expected_non_empty_lines = expected_lines - 1

    summary, _, _ = ingest(f"https://github.com/{REPO}/{path_type}/{ref}{path}")
    lines = summary.splitlines()
    parsed_lines = dict(line.split(": ", 1) for line in lines if ": " in line)

    assert parsed_lines["Repository"] == REPO

    if is_main_branch:
        # We omit the 'Branch' line for 'main' branches.
        assert ref_type not in parsed_lines
    else:
        assert parsed_lines[ref_type] == ref

    if is_blob:
        assert parsed_lines["File"] == Path(path).name
        assert "Lines" in parsed_lines
    else:  # 'tree'
        assert parsed_lines["Subpath"] == path
        assert "Files analyzed" in parsed_lines

    token_match = re.search(r"\d+", parsed_lines["Estimated tokens"])
    assert token_match, "'Estimated tokens' should contain a number"
    assert int(token_match.group()) > 0

    assert len(lines) == expected_lines
    assert len(parsed_lines) == expected_non_empty_lines


def _calculate_expected_lines(ref_type: str, *, is_main_branch: bool) -> int:
    """Calculate the expected number of lines in the summary.

    The total number of lines depends on the following:
    - Commit type does not include the 'Branch'/'Tag' line, reducing the count by 1.
    - The "main" branch omits the 'Branch' line, reducing the count by 1.

    Parameters
    ----------
    ref_type : str
        The type of reference, e.g., "Branch", "Tag", or "Commit".
    is_main_branch : bool
        True if the reference is the "main" branch, False otherwise.

    Returns
    -------
    int
        The expected number of lines in the summary.

    """
    base_lines = 7
    if is_main_branch:
        base_lines -= 1
    if ref_type == "Commit":
        base_lines -= 1
    return base_lines



================================================
FILE: tests/.pylintrc
================================================
[MASTER]
init-hook=
    import sys
    sys.path.append('./src')

[MESSAGES CONTROL]
disable=missing-class-docstring,missing-function-docstring,protected-access,fixme

[FORMAT]
max-line-length=119



================================================
FILE: tests/query_parser/__init__.py
================================================
"""Tests for the query parser."""



================================================
FILE: tests/query_parser/test_git_host_agnostic.py
================================================
"""Tests to verify that the query parser is Git host agnostic.

These tests confirm that ``parse_query`` correctly identifies user/repo pairs and canonical URLs for GitHub, GitLab,
Bitbucket, Gitea, and Codeberg, even if the host is omitted.
"""

from __future__ import annotations

import pytest

from gitingest.config import MAX_FILE_SIZE
from gitingest.query_parser import parse_remote_repo
from gitingest.utils.query_parser_utils import KNOWN_GIT_HOSTS, _is_valid_git_commit_hash

# Repository matrix: (host, user, repo)
_REPOS: list[tuple[str, str, str]] = [
    ("github.com", "fastapi", "fastapi"),
    ("gitlab.com", "gitlab-org", "gitlab-runner"),
    ("bitbucket.org", "na-dna", "llm-knowledge-share"),
    ("gitea.com", "xorm", "xorm"),
    ("codeberg.org", "forgejo", "forgejo"),
    ("git.rwth-aachen.de", "medialab", "19squared"),
    ("gitlab.alpinelinux.org", "alpine", "apk-tools"),
]


# Generate cartesian product of repository tuples with URL variants.
@pytest.mark.parametrize(("host", "user", "repo"), _REPOS, ids=[f"{h}:{u}/{r}" for h, u, r in _REPOS])
@pytest.mark.parametrize("variant", ["full", "noscheme", "slug"])
@pytest.mark.asyncio
async def test_parse_query_without_host(
    host: str,
    user: str,
    repo: str,
    variant: str,
) -> None:
    """Verify that ``parse_remote_repo`` handles URLs, host-omitted URLs and raw slugs."""
    # Build the input URL based on the selected variant
    if variant == "full":
        url = f"https://{host}/{user}/{repo}"
    elif variant == "noscheme":
        url = f"{host}/{user}/{repo}"
    else:  # "slug"
        url = f"{user}/{repo}"

    expected_url = f"https://{host}/{user}/{repo}"

    # For slug form with a custom host (not in KNOWN_GIT_HOSTS) we expect a failure,
    # because the parser cannot guess which domain to use.
    if variant == "slug" and host not in KNOWN_GIT_HOSTS:
        with pytest.raises(ValueError, match="Could not find a valid repository host"):
            await parse_remote_repo(url)
        return

    query = await parse_remote_repo(url)

    # Compare against the canonical dict while ignoring unpredictable fields.
    actual = query.model_dump(exclude={"id", "local_path", "ignore_patterns", "s3_url"})

    assert "commit" in actual
    assert _is_valid_git_commit_hash(actual["commit"])
    del actual["commit"]

    expected = {
        "host": host,
        "user_name": user,
        "repo_name": repo,
        "url": expected_url,
        "slug": f"{user}-{repo}",
        "subpath": "/",
        "type": None,
        "branch": None,
        "tag": None,
        "max_file_size": MAX_FILE_SIZE,
        "include_patterns": None,
        "include_submodules": False,
    }

    assert actual == expected



================================================
FILE: tests/query_parser/test_query_parser.py
================================================
"""Tests for the ``query_parser`` module.

These tests cover URL parsing, pattern parsing, and handling of branches/subpaths for HTTP(S) repositories and local
paths.
"""

# pylint: disable=too-many-arguments, too-many-positional-arguments
from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Callable

import pytest

from gitingest.query_parser import parse_local_dir_path, parse_remote_repo
from gitingest.utils.query_parser_utils import _is_valid_git_commit_hash
from tests.conftest import DEMO_URL

if TYPE_CHECKING:
    from unittest.mock import AsyncMock

    from gitingest.schemas import IngestionQuery


URLS_HTTPS: list[str] = [
    DEMO_URL,
    "https://gitlab.com/user/repo",
    "https://bitbucket.org/user/repo",
    "https://gitea.com/user/repo",
    "https://codeberg.org/user/repo",
    "https://gist.github.com/user/repo",
    "https://git.example.com/user/repo",
    "https://gitlab.example.com/user/repo",
    "https://gitlab.example.se/user/repo",
]

URLS_HTTP: list[str] = [url.replace("https://", "http://") for url in URLS_HTTPS]


@pytest.mark.parametrize("url", URLS_HTTPS, ids=lambda u: u)
@pytest.mark.asyncio
async def test_parse_url_valid_https(url: str, stub_resolve_sha: dict[str, AsyncMock]) -> None:
    """Valid HTTPS URLs parse correctly and ``query.url`` equals the input."""
    query = await _assert_basic_repo_fields(url, stub_resolve_sha["head"])

    assert query.url == url  # HTTPS: canonical URL should equal input


@pytest.mark.parametrize("url", URLS_HTTP, ids=lambda u: u)
@pytest.mark.asyncio
async def test_parse_url_valid_http(url: str, stub_resolve_sha: dict[str, AsyncMock]) -> None:
    """Valid HTTP URLs parse correctly (slug check only)."""
    await _assert_basic_repo_fields(url, stub_resolve_sha["head"])


@pytest.mark.asyncio
async def test_parse_url_invalid(stub_resolve_sha: dict[str, AsyncMock]) -> None:
    """Test ``parse_remote_repo`` with an invalid URL.

    Given an HTTPS URL lacking a repository structure (e.g., "https://github.com"),
    When ``parse_remote_repo`` is called,
    Then a ValueError should be raised indicating an invalid repository URL.
    """
    url = "https://github.com"

    with pytest.raises(ValueError, match="Invalid repository URL"):
        await parse_remote_repo(url)

    stub_resolve_sha["head"].assert_not_awaited()


@pytest.mark.asyncio
@pytest.mark.parametrize("url", [DEMO_URL, "https://gitlab.com/user/repo"])
async def test_parse_query_basic(url: str, stub_resolve_sha: dict[str, AsyncMock]) -> None:
    """Test ``parse_remote_repo`` with a basic valid repository URL.

    Given an HTTPS URL:
    When ``parse_remote_repo`` is called,
    Then user/repo, URL should be parsed correctly.
    """
    query = await parse_remote_repo(url)

    stub_resolve_sha["head"].assert_awaited_once()
    assert query.user_name == "user"
    assert query.repo_name == "repo"
    assert query.url == url


@pytest.mark.asyncio
async def test_parse_query_mixed_case(stub_resolve_sha: dict[str, AsyncMock]) -> None:
    """Test ``parse_remote_repo`` with mixed-case URLs.

    Given a URL with mixed-case parts (e.g. "Https://GitHub.COM/UsEr/rEpO"):
    When ``parse_remote_repo`` is called,
    Then the user and repo names should be normalized to lowercase.
    """
    url = "Https://GitHub.COM/UsEr/rEpO"
    query = await parse_remote_repo(url)

    stub_resolve_sha["head"].assert_awaited_once()
    assert query.user_name == "user"
    assert query.repo_name == "repo"


@pytest.mark.asyncio
async def test_parse_url_with_subpaths(
    stub_branches: Callable[[list[str]], None],
    stub_resolve_sha: dict[str, AsyncMock],
) -> None:
    """Test ``parse_remote_repo`` with a URL containing branch and subpath.

    Given a URL referencing a branch ("main") and a subdir ("subdir/file"):
    When ``parse_remote_repo`` is called with remote branch fetching,
    Then user, repo, branch, and subpath should be identified correctly.
    """
    url = DEMO_URL + "/tree/main/subdir/file"

    stub_branches(["main", "dev", "feature-branch"])

    query = await _assert_basic_repo_fields(url, stub_resolve_sha["ref"])

    assert query.user_name == "user"
    assert query.repo_name == "repo"
    assert query.branch == "main"
    assert query.subpath == "/subdir/file"


@pytest.mark.asyncio
async def test_parse_url_invalid_repo_structure(stub_resolve_sha: dict[str, AsyncMock]) -> None:
    """Test ``parse_remote_repo`` with a URL missing a repository name.

    Given a URL like "https://github.com/user":
    When ``parse_remote_repo`` is called,
    Then a ValueError should be raised indicating an invalid repository URL.
    """
    url = "https://github.com/user"

    with pytest.raises(ValueError, match="Invalid repository URL"):
        await parse_remote_repo(url)

    stub_resolve_sha["head"].assert_not_awaited()


async def test_parse_local_dir_path_local_path() -> None:
    """Test ``parse_local_dir_path``.

    Given "/home/user/project":
    When ``parse_local_dir_path`` is called,
    Then the local path should be set, id generated, and slug formed accordingly.
    """
    path = "/home/user/project"
    query = parse_local_dir_path(path)
    tail = Path("home/user/project")

    assert query.local_path.parts[-len(tail.parts) :] == tail.parts
    assert query.id is not None
    assert query.slug == "home/user/project"


async def test_parse_local_dir_path_relative_path() -> None:
    """Test ``parse_local_dir_path`` with a relative path.

    Given "./project":
    When ``parse_local_dir_path`` is called,
    Then ``local_path`` resolves relatively, and ``slug`` ends with "project".
    """
    path = "./project"
    query = parse_local_dir_path(path)
    tail = Path("project")

    assert query.local_path.parts[-len(tail.parts) :] == tail.parts
    assert query.slug.endswith("project")


@pytest.mark.asyncio
async def test_parse_remote_repo_empty_source(stub_resolve_sha: dict[str, AsyncMock]) -> None:
    """Test ``parse_remote_repo`` with an empty string.

    Given an empty source string:
    When ``parse_remote_repo`` is called,
    Then a ValueError should be raised indicating an invalid repository URL.
    """
    url = ""

    with pytest.raises(ValueError, match="Invalid repository URL"):
        await parse_remote_repo(url)

    stub_resolve_sha["head"].assert_not_awaited()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("path", "expected_branch", "mock_name"),
    [
        ("/tree/main", "main", "ref"),
        ("/tree/abcd1234abcd1234abcd1234abcd1234abcd1234", None, "ref"),
    ],
)
async def test_parse_url_branch_and_commit_distinction(
    path: str,
    expected_branch: str,
    stub_branches: Callable[[list[str]], None],
    stub_resolve_sha: dict[str, AsyncMock],
    mock_name: str,
) -> None:
    """Test ``parse_remote_repo`` distinguishing branch vs. commit hash.

    Given either a branch URL (e.g., ".../tree/main") or a 40-character commit URL:
    When ``parse_remote_repo`` is called with branch fetching,
    Then the function should correctly set ``branch`` or ``commit`` based on the URL content.
    """
    stub_branches(["main", "dev", "feature-branch"])

    url = DEMO_URL + path
    query = await _assert_basic_repo_fields(url, stub_resolve_sha[mock_name])

    assert query.branch == expected_branch
    assert query.commit is not None
    assert _is_valid_git_commit_hash(query.commit)


async def test_parse_local_dir_path_uuid_uniqueness() -> None:
    """Test ``parse_local_dir_path`` for unique UUID generation.

    Given the same path twice:
    When ``parse_local_dir_path`` is called repeatedly,
    Then each call should produce a different query id.
    """
    path = "/home/user/project"
    query_1 = parse_local_dir_path(path)
    query_2 = parse_local_dir_path(path)

    assert query_1.id != query_2.id


@pytest.mark.asyncio
async def test_parse_url_with_query_and_fragment(stub_resolve_sha: dict[str, AsyncMock]) -> None:
    """Test ``parse_remote_repo`` with query parameters and a fragment.

    Given a URL like "https://github.com/user/repo?arg=value#fragment":
    When ``parse_remote_repo`` is called,
    Then those parts should be stripped, leaving a clean user/repo URL.
    """
    url = DEMO_URL + "?arg=value#fragment"
    query = await parse_remote_repo(url)

    stub_resolve_sha["head"].assert_awaited_once()
    assert query.user_name == "user"
    assert query.repo_name == "repo"
    assert query.url == DEMO_URL  # URL should be cleaned


@pytest.mark.asyncio
async def test_parse_url_unsupported_host(stub_resolve_sha: dict[str, AsyncMock]) -> None:
    """Test ``parse_remote_repo`` with an unsupported host.

    Given "https://only-domain.com":
    When ``parse_remote_repo`` is called,
    Then a ValueError should be raised for the unknown domain.
    """
    url = "https://only-domain.com"

    with pytest.raises(ValueError, match="Unknown domain 'only-domain.com' in URL"):
        await parse_remote_repo(url)

    stub_resolve_sha["head"].assert_not_awaited()


@pytest.mark.asyncio
async def test_parse_query_with_branch() -> None:
    """Test ``parse_remote_repo`` when a branch is specified in a blob path.

    Given "https://github.com/pandas-dev/pandas/blob/2.2.x/...":
    When ``parse_remote_repo`` is called,
    Then the branch should be identified, subpath set, and commit remain None.
    """
    url = "https://github.com/pandas-dev/pandas/blob/2.2.x/.github/ISSUE_TEMPLATE/documentation_improvement.yaml"
    query = await parse_remote_repo(url)

    assert query.user_name == "pandas-dev"
    assert query.repo_name == "pandas"
    assert query.url == "https://github.com/pandas-dev/pandas"
    assert query.slug == "pandas-dev-pandas"
    assert query.id is not None
    assert query.subpath == "/.github/ISSUE_TEMPLATE/documentation_improvement.yaml"
    assert query.branch == "2.2.x"
    assert query.commit is not None
    assert _is_valid_git_commit_hash(query.commit)
    assert query.type == "blob"


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("path", "expected_branch", "expected_subpath", "mock_name"),
    [
        ("/tree/feature/fix1/src", "feature/fix1", "/src", "ref"),
        ("/tree/main/src", "main", "/src", "ref"),
        ("", None, "/", "head"),
        ("/tree/nonexistent-branch/src", None, "/", "ref"),
        ("/tree/fix", "fix", "/", "ref"),
        ("/blob/fix/page.html", "fix", "/page.html", "ref"),
    ],
)
async def test_parse_repo_source_with_various_url_patterns(
    path: str,
    expected_branch: str | None,
    expected_subpath: str,
    stub_branches: Callable[[list[str]], None],
    stub_resolve_sha: dict[str, AsyncMock],
    mock_name: str,
) -> None:
    """Test ``parse_remote_repo`` with various GitHub-style URL permutations.

    Given various GitHub-style URL permutations:
    When ``parse_remote_repo`` is called,
    Then it should detect (or reject) a branch and resolve the sub-path.

    Branch discovery is stubbed so that only names passed to ``stub_branches`` are considered "remote".
    """
    stub_branches(["feature/fix1", "main", "feature-branch", "fix"])

    url = DEMO_URL + path
    query = await _assert_basic_repo_fields(url, stub_resolve_sha[mock_name])

    assert query.branch == expected_branch
    assert query.subpath == expected_subpath


@pytest.mark.asyncio
async def _assert_basic_repo_fields(url: str, sha_mock: AsyncMock) -> IngestionQuery:
    """Run ``parse_remote_repo`` and assert user, repo and slug are parsed."""
    query = await parse_remote_repo(url)

    assert query.commit is not None
    assert _is_valid_git_commit_hash(query.commit)

    if query.commit in url:
        sha_mock.assert_not_awaited()
    else:
        sha_mock.assert_awaited_once()

    assert query.user_name == "user"
    assert query.repo_name == "repo"
    assert query.slug == "user-repo"

    return query



================================================
FILE: tests/server/__init__.py
================================================
"""Tests for the server."""



================================================
FILE: tests/server/test_flow_integration.py
================================================
"""Integration tests covering core functionalities, edge cases, and concurrency handling."""

import shutil
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Generator

import pytest
from fastapi import status
from fastapi.testclient import TestClient
from pytest_mock import MockerFixture

from src.server.main import app

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / "src" / "templates"


@pytest.fixture(scope="module")
def test_client() -> Generator[TestClient, None, None]:
    """Create a test client fixture."""
    with TestClient(app) as client_instance:
        client_instance.headers.update({"Host": "localhost"})
        yield client_instance


@pytest.fixture(autouse=True)
def mock_static_files(mocker: MockerFixture) -> None:
    """Mock the static file mount to avoid directory errors."""
    mock_static = mocker.patch("src.server.main.StaticFiles", autospec=True)
    mock_static.return_value = None
    return mock_static


@pytest.fixture(scope="module", autouse=True)
def cleanup_tmp_dir() -> Generator[None, None, None]:
    """Remove ``/tmp/gitingest`` after this test-module is done."""
    yield  # run tests
    temp_dir = Path("/tmp/gitingest")
    if temp_dir.exists():
        try:
            shutil.rmtree(temp_dir)
        except PermissionError as exc:
            sys.stderr.write(f"Error cleaning up {temp_dir}: {exc}\n")


@pytest.mark.asyncio
async def test_remote_repository_analysis(request: pytest.FixtureRequest) -> None:
    """Test the complete flow of analyzing a remote repository."""
    client = request.getfixturevalue("test_client")
    form_data = {
        "input_text": "https://github.com/octocat/Hello-World",
        "max_file_size": 243,
        "pattern_type": "exclude",
        "pattern": "",
        "token": "",
    }

    response = client.post("/api/ingest", json=form_data)
    assert response.status_code == status.HTTP_200_OK, f"Form submission failed: {response.text}"

    # Check that response is JSON
    response_data = response.json()
    assert "content" in response_data
    assert response_data["content"]
    assert "repo_url" in response_data
    assert "summary" in response_data
    assert "tree" in response_data
    assert "content" in response_data


@pytest.mark.asyncio
async def test_invalid_repository_url(request: pytest.FixtureRequest) -> None:
    """Test handling of an invalid repository URL."""
    client = request.getfixturevalue("test_client")
    form_data = {
        "input_text": "https://github.com/nonexistent/repo",
        "max_file_size": 243,
        "pattern_type": "exclude",
        "pattern": "",
        "token": "",
    }

    response = client.post("/api/ingest", json=form_data)
    # Should return 400 for invalid repository
    assert response.status_code == status.HTTP_400_BAD_REQUEST, f"Request failed: {response.text}"

    # Check that response is JSON error
    response_data = response.json()
    assert "error" in response_data


@pytest.mark.asyncio
async def test_large_repository(request: pytest.FixtureRequest) -> None:
    """Simulate analysis of a large repository with nested folders."""
    client = request.getfixturevalue("test_client")
    # TODO: ingesting a large repo take too much time (eg: godotengine/godot repository)
    form_data = {
        "input_text": "https://github.com/octocat/hello-world",
        "max_file_size": 10,
        "pattern_type": "exclude",
        "pattern": "",
        "token": "",
    }

    response = client.post("/api/ingest", json=form_data)
    assert response.status_code == status.HTTP_200_OK, f"Request failed: {response.text}"

    response_data = response.json()
    if response.status_code == status.HTTP_200_OK:
        assert "content" in response_data
        assert response_data["content"]
    else:
        assert "error" in response_data


@pytest.mark.asyncio
async def test_concurrent_requests(request: pytest.FixtureRequest) -> None:
    """Test handling of multiple concurrent requests."""
    client = request.getfixturevalue("test_client")

    def make_request() -> None:
        form_data = {
            "input_text": "https://github.com/octocat/hello-world",
            "max_file_size": 243,
            "pattern_type": "exclude",
            "pattern": "",
            "token": "",
        }
        response = client.post("/api/ingest", json=form_data)
        assert response.status_code == status.HTTP_200_OK, f"Request failed: {response.text}"

        response_data = response.json()
        if response.status_code == status.HTTP_200_OK:
            assert "content" in response_data
            assert response_data["content"]
        else:
            assert "error" in response_data

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(make_request) for _ in range(5)]
        for future in futures:
            future.result()


@pytest.mark.asyncio
async def test_large_file_handling(request: pytest.FixtureRequest) -> None:
    """Test handling of repositories with large files."""
    client = request.getfixturevalue("test_client")
    form_data = {
        "input_text": "https://github.com/octocat/Hello-World",
        "max_file_size": 1,
        "pattern_type": "exclude",
        "pattern": "",
        "token": "",
    }

    response = client.post("/api/ingest", json=form_data)
    assert response.status_code == status.HTTP_200_OK, f"Request failed: {response.text}"

    response_data = response.json()
    if response.status_code == status.HTTP_200_OK:
        assert "content" in response_data
        assert response_data["content"]
    else:
        assert "error" in response_data


@pytest.mark.asyncio
async def test_repository_with_patterns(request: pytest.FixtureRequest) -> None:
    """Test repository analysis with include/exclude patterns."""
    client = request.getfixturevalue("test_client")
    form_data = {
        "input_text": "https://github.com/octocat/Hello-World",
        "max_file_size": 243,
        "pattern_type": "include",
        "pattern": "*.md",
        "token": "",
    }

    response = client.post("/api/ingest", json=form_data)
    assert response.status_code == status.HTTP_200_OK, f"Request failed: {response.text}"

    response_data = response.json()
    if response.status_code == status.HTTP_200_OK:
        assert "content" in response_data
        assert "pattern_type" in response_data
        assert response_data["pattern_type"] == "include"
        assert "pattern" in response_data
        assert response_data["pattern"] == "*.md"
    else:
        assert "error" in response_data



================================================
FILE: .docker/minio/setup.sh
================================================
#!/bin/sh

# Simple script to set up MinIO bucket and user
# Based on example from MinIO issues

# Format bucket name to ensure compatibility
BUCKET_NAME=$(echo "${S3_BUCKET_NAME}" | tr '[:upper:]' '[:lower:]' | tr '_' '-')

# Configure MinIO client
mc alias set myminio http://minio:9000 ${MINIO_ROOT_USER} ${MINIO_ROOT_PASSWORD}

# Remove bucket if it exists (for clean setup)
mc rm -r --force myminio/${BUCKET_NAME} || true

# Create bucket
mc mb myminio/${BUCKET_NAME}

# Set bucket policy to allow downloads
mc anonymous set download myminio/${BUCKET_NAME}

# Create user with access and secret keys
mc admin user add myminio ${S3_ACCESS_KEY} ${S3_SECRET_KEY} || echo "User already exists"

# Create policy for the bucket
echo '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Action":["s3:*"],"Resource":["arn:aws:s3:::'${BUCKET_NAME}'/*","arn:aws:s3:::'${BUCKET_NAME}'"]}]}' > /tmp/policy.json

# Apply policy
mc admin policy create myminio gitingest-policy /tmp/policy.json || echo "Policy already exists"
mc admin policy attach myminio gitingest-policy --user ${S3_ACCESS_KEY}

echo "MinIO setup completed successfully"
echo "Bucket: ${BUCKET_NAME}"
echo "Access via console: http://localhost:9001"



================================================
FILE: .github/ISSUE_TEMPLATE/bug_report.yml
================================================
name: Bug report 🐞
description: Report a bug or internal server error when using Gitingest
title: "(bug): "
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to report a bug! :lady_beetle:

        Please fill out the following details to help us reproduce and fix the issue. :point_down:

  - type: dropdown
    id: interface
    attributes:
      label: Which interface did you use?
      default: 0
      options:
        - "Select one..."
        - Web UI
        - CLI
        - PyPI package
    validations:
      required: true

  - type: input
    id: repo_url
    attributes:
      label: Repository URL (if public)
      placeholder: e.g., https://github.com/<username>/<repo>/commit_branch_or_tag/blob_or_tree/subdir

  - type: dropdown
    id: git_host
    attributes:
      label: Git host
      description: The Git host of the repository.
      default: 0
      options:
        - "Select one..."
        - GitHub (github.com)
        - GitLab (gitlab.com)
        - Bitbucket (bitbucket.org)
        - Gitea (gitea.com)
        - Codeberg (codeberg.org)
        - Gist (gist.github.com)
        - Kaggle (kaggle.com)
        - GitHub Enterprise (github.company.com)
        - Other (specify below)
    validations:
      required: true

  - type: input
    id: git_host_other
    attributes:
      label: Other Git host
      placeholder: If you selected "Other", please specify the Git host here.

  - type: dropdown
    id: repo_visibility
    attributes:
      label: Repository visibility
      default: 0
      options:
        - "Select one..."
        - public
        - private
    validations:
      required: true

  - type: dropdown
    id: revision
    attributes:
      label: Commit, branch, or tag
      default: 0
      options:
        - "Select one..."
        - default branch
        - commit
        - branch
        - tag
    validations:
      required: true

  - type: dropdown
    id: ingest_scope
    attributes:
      label: Did you ingest the full repository or a subdirectory?
      default: 0
      options:
        - "Select one..."
        - full repository
        - subdirectory
    validations:
      required: true

  - type: dropdown
    id: os
    attributes:
      label: Operating system
      default: 0
      options:
        - "Select one..."
        - Not relevant (Web UI)
        - macOS
        - Windows
        - Linux
    validations:
      required: true

  - type: dropdown
    id: browser
    attributes:
      label: Browser (Web UI only)
      default: 0
      options:
        - "Select one..."
        - Not relevant (CLI / PyPI)
        - Chrome
        - Firefox
        - Safari
        - Edge
        - Other (specify below)
    validations:
      required: true

  - type: input
    id: browser_other
    attributes:
      label: Other browser
      placeholder: If you selected "Other", please specify the browser here.

  - type: input
    id: gitingest_version
    attributes:
      label: Gitingest version
      placeholder: e.g., v0.1.5
      description: Not required if you used the Web UI.

  - type: input
    id: python_version
    attributes:
      label: Python version
      placeholder: e.g., 3.11.5
      description: Not required if you used the Web UI.

  - type: textarea
    id: bug_description
    attributes:
      label: Bug description
      placeholder: Describe the bug here.
      description: A detailed but concise description of the bug.
    validations:
      required: true


  - type: textarea
    id: steps_to_reproduce
    attributes:
      label: Steps to reproduce
      placeholder: Include the exact commands or actions that led to the error.
      description: Include the exact commands or actions that led to the error *(if relevant)*.
      render: shell

  - type: textarea
    id: expected_behavior
    attributes:
      label: Expected behavior
      placeholder: Describe what you expected to happen.
      description: Describe what you expected to happen *(if relevant)*.

  - type: textarea
    id: actual_behavior
    attributes:
      label: Actual behavior
      description: Paste the full error message or stack trace here.

  - type: textarea
    id: additional_context
    attributes:
      label: Additional context, logs, or screenshots
      placeholder: Add any other context, links, or screenshots about the issue here.



================================================
FILE: .github/ISSUE_TEMPLATE/feature_request.yml
================================================
name: Feature request 💡
description: Suggest a new feature or improvement for Gitingest
title: "(feat): "
labels: ["enhancement"]
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to help us improve **Gitingest**! :sparkles:

        Please fill in the sections below to describe your idea. The more detail you provide, the easier it is for us to evaluate and plan the work. :point_down:

  - type: input
    id: summary
    attributes:
      label: Feature summary
      placeholder: One-sentence description of the feature.
    validations:
      required: true

  - type: textarea
    id: problem
    attributes:
      label: Problem / motivation
      description: What problem does this feature solve? How does it affect your workflow?
      placeholder: Why is this feature important? Describe the pain point or limitation you're facing.
    validations:
      required: true

  - type: textarea
    id: proposal
    attributes:
      label: Proposed solution
      placeholder: Describe what you would like to see happen.
      description: Outline the feature as you imagine it. *(optional)*


  - type: textarea
    id: alternatives
    attributes:
      label: Alternatives considered
      placeholder: List other approaches you've considered or work-arounds you use today.
      description: Feel free to mention why those alternatives don't fully solve the problem.

  - type: dropdown
    id: interface
    attributes:
      label: Which interface would this affect?
      default: 0
      options:
        - "Select one..."
        - Web UI
        - CLI
        - PyPI package
        - CLI + PyPI package
        - All
    validations:
      required: true

  - type: dropdown
    id: priority
    attributes:
      label: How important is this to you?
      default: 0
      options:
        - "Select one..."
        - Nice to have
        - Important
        - Critical
    validations:
      required: true

  - type: dropdown
    id: willingness
    attributes:
      label: Would you like to work on this feature yourself?
      default: 0
      options:
        - "Select one..."
        - Yes, I'd like to implement it
        - Maybe, if I get some guidance
        - No, just requesting (absolutely fine!)
    validations:
      required: true

  - type: dropdown
    id: support_needed
    attributes:
      label: Would you need support from the maintainers (if you're implementing it yourself)?
      default: 0
      options:
        - "Select one..."
        - No, I can handle it solo
        - Yes, I'd need some guidance
        - Not sure yet
        - This is just a suggestion, I'm not planning to implement it myself (absolutely fine!)

  - type: textarea
    id: additional_context
    attributes:
      label: Additional context, screenshots, or examples
      placeholder: Add links, sketches, or any other context that would help us understand and implement the feature.



================================================
FILE: .github/workflows/ci.yml
================================================
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

permissions:
  contents: read

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        python-version: ["3.8", "3.13"]
        include:
          - os: ubuntu-latest
            python-version: "3.13"
            coverage: true

    steps:
      - name: Harden the runner (Audit all outbound calls)
        uses: step-security/harden-runner@ec9f2d5744a09debf3a187a3f4f675c53b671911 # v2.13.0
        with:
          egress-policy: audit

      - uses: actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8 # v5.0.0

      - name: Set up Python
        uses: actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065 # v5.6.0
        with:
          python-version: ${{ matrix.python-version }}
          cache: 'pip'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          python -m pip install ".[dev,server]"

      - name: Cache pytest results
        uses: actions/cache@v4
        with:
          path: .pytest_cache
          key: ${{ runner.os }}-pytest-${{ matrix.python-version }}-${{ hashFiles('**/pytest.ini') }}
          restore-keys: |
            ${{ runner.os }}-pytest-${{ matrix.python-version }}-

      - name: Run tests
        if: ${{ matrix.coverage != true }}
        run: pytest

      - name: Run tests
        if: ${{ matrix.coverage == true }}
        run: pytest



      - name: Run pre-commit hooks
        uses: pre-commit/action@2c7b3805fd2a0fd8c1884dcaebf91fc102a13ecd # v3.0.1
        if: ${{ matrix.python-version == '3.13' && matrix.os == 'ubuntu-latest' }}



================================================
FILE: .github/workflows/codeql.yml
================================================
# For most projects, this workflow file will not need changing; you simply need
# to commit it to your repository.
#
# You may wish to alter this file to override the set of languages analyzed,
# or to provide custom queries or build logic.
#
# ******** NOTE ********
# We have attempted to detect the languages in your repository. Please check
# the `language` matrix defined below to confirm you have the correct set of
# supported CodeQL languages.
#
name: "CodeQL"

on:
  push:
    branches: ["main"]
  pull_request:
    # The branches below must be a subset of the branches above
    branches: ["main"]
  schedule:
    - cron: "0 0 * * 1"

permissions:
  contents: read

jobs:
  analyze:
    name: Analyze
    runs-on: ubuntu-latest
    permissions:
      actions: read
      contents: read
      security-events: write

    strategy:
      fail-fast: false
      matrix:
        language: ["javascript", "python"]
        # CodeQL supports [ $supported-codeql-languages ]
        # Learn more about CodeQL language support at https://aka.ms/codeql-docs/language-support

    steps:
      - name: Harden the runner (Audit all outbound calls)
        uses: step-security/harden-runner@ec9f2d5744a09debf3a187a3f4f675c53b671911 # v2.13.0
        with:
          egress-policy: audit

      - name: Checkout repository
        uses: actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8 # v5.0.0

      # Initializes the CodeQL tools for scanning.
      - name: Initialize CodeQL
        uses: github/codeql-action/init@df559355d593797519d70b90fc8edd5db049e7a2 # v3.29.9
        with:
          languages: ${{ matrix.language }}
          # If you wish to specify custom queries, you can do so here or in a config file.
          # By default, queries listed here will override any specified in a config file.
          # Prefix the list here with "+" to use these queries and those in the config file.

      # Autobuild attempts to build any compiled languages  (C/C++, C#, or Java).
      # If this step fails, then you should remove it and run the build manually (see below)
      - name: Autobuild
        uses: github/codeql-action/autobuild@df559355d593797519d70b90fc8edd5db049e7a2 # v3.29.9

      # ℹ️ Command-line programs to run using the OS shell.
      # 📚 See https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepsrun

      #   If the Autobuild fails above, remove it and uncomment the following three lines.
      #   modify them (or add more) to build your code if your project, please refer to the EXAMPLE below for guidance.

      # - run: |
      #   echo "Run, Build Application using script"
      #   ./location_of_script_within_repo/buildscript.sh

      - name: Perform CodeQL Analysis
        uses: github/codeql-action/analyze@df559355d593797519d70b90fc8edd5db049e7a2 # v3.29.9
        with:
          category: "/language:${{matrix.language}}"



================================================
FILE: .github/workflows/dependency-review.yml
================================================
# Dependency Review Action
#
# This Action will scan dependency manifest files that change as part of a Pull Request,
# surfacing known-vulnerable versions of the packages declared or updated in the PR.
# Once installed, if the workflow run is marked as required,
# PRs introducing known-vulnerable packages will be blocked from merging.
#
# Source repository: https://github.com/actions/dependency-review-action
name: 'Dependency Review'
on: [pull_request]

permissions:
  contents: read

jobs:
  dependency-review:
    runs-on: ubuntu-latest
    steps:
      - name: Harden the runner (Audit all outbound calls)
        uses: step-security/harden-runner@ec9f2d5744a09debf3a187a3f4f675c53b671911 # v2.13.0
        with:
          egress-policy: audit

      - name: 'Checkout Repository'
        uses: actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8 # v5.0.0
      - name: 'Dependency Review'
        uses: actions/dependency-review-action@da24556b548a50705dd671f47852072ea4c105d9 # v4.7.1



================================================
FILE: .github/workflows/deploy-pr.yml
================================================
name: Manage PR Temp Envs
'on':
  pull_request:
    types:
      - labeled
      - unlabeled
      - closed

permissions:
  contents: read
  pull-requests: write

env:
  APP_NAME: gitingest
  FLUX_OWNER: '${{ github.repository_owner }}'
  FLUX_REPO: '${{ secrets.CR_FLUX_REPO }}'

jobs:
  deploy-pr-env:
    if: >-
      ${{ github.event.action == 'labeled' && github.event.label.name ==
      'deploy-pr-temp-env' }}
    runs-on: ubuntu-latest
    steps:
      - name: Create GitHub App token
        uses: actions/create-github-app-token@v2
        id: app-token
        with:
          app-id: '${{ secrets.CR_APP_CI_APP_ID }}'
          private-key: '${{ secrets.CR_APP_CI_PRIVATE_KEY }}'
          owner: '${{ env.FLUX_OWNER }}'
          repositories: '${{ env.FLUX_REPO }}'

      - name: Checkout Flux repo
        uses: actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8 # v5.0.0
        with:
          repository: '${{ env.FLUX_OWNER }}/${{ env.FLUX_REPO }}'
          token: '${{ steps.app-token.outputs.token }}'
          path: flux-repo
          persist-credentials: false

      - name: Export PR ID
        shell: bash
        run: 'echo "PR_ID=${{ github.event.pull_request.number }}" >> $GITHUB_ENV'

      - name: Ensure template exists
        shell: bash
        run: >
          T="flux-repo/pr-template/${APP_NAME}"

          [[ -d "$T" ]] || { echo "Missing $T"; exit 1; }

          [[ $(find "$T" -type f | wc -l) -gt 0 ]] || { echo "No files in $T";
          exit 1; }

      - name: Render & copy template
        shell: bash
        run: |
          SRC="flux-repo/pr-template/${APP_NAME}"
          DST="flux-repo/deployments/prs-${APP_NAME}/${PR_ID}"
          mkdir -p "$DST"
          cp -r "$SRC/." "$DST/"
          find "$DST" -type f -print0 \
            | xargs -0 -n1 sed -i "s|@PR-ID@|${PR_ID}|g"

      - name: Sanity‑check rendered output
        shell: bash
        run: >
          E=$(find "flux-repo/pr-template/${APP_NAME}" -type f | wc -l)

          G=$(find "flux-repo/deployments/prs-${APP_NAME}/${PR_ID}" -type f | wc
          -l)

          (( G == E )) || { echo "Expected $E files, got $G"; exit 1; }

      - name: Commit & push creation
        shell: bash
        run: >
          cd flux-repo

          git config user.name  "${{ steps.app-token.outputs.app-slug }}[bot]"

          git config user.email "${{ steps.app-token.outputs.app-slug
          }}[bot]@users.noreply.github.com"

          git add .

          git commit -m "chore(prs-${APP_NAME}): create temp env for PR #${{
          env.PR_ID }} [skip ci]" || echo "Nothing to commit"

          git remote set-url origin \
            https://x-access-token:${{ steps.app-token.outputs.token }}@github.com/${{ env.FLUX_OWNER }}/${{ env.FLUX_REPO }}.git
          git push origin HEAD:main

      - name: Comment preview URL on PR
        uses: thollander/actions-comment-pull-request@v3
        with:
          github-token: '${{ secrets.GITHUB_TOKEN }}'
          pr-number: '${{ github.event.pull_request.number }}'
          comment-tag: 'pr-preview'
          create-if-not-exists: 'true'
          message: |
            🌐 [Preview environment](https://pr-${{ env.PR_ID }}.${{ env.APP_NAME }}.coderamp.dev/) for PR #${{ env.PR_ID }}

            📊 [Log viewer](https://app.datadoghq.eu/logs?query=kube_namespace%3Aprs-gitingest%20version%3Apr-${{ env.PR_ID }})

  remove-pr-env:
    if: >-
      (github.event.action == 'unlabeled' && github.event.label.name ==
      'deploy-pr-temp-env') || (github.event.action == 'closed')
    runs-on: ubuntu-latest
    steps:
      - name: Create GitHub App token
        uses: actions/create-github-app-token@v2
        id: app-token
        with:
          app-id: '${{ secrets.CR_APP_CI_APP_ID }}'
          private-key: '${{ secrets.CR_APP_CI_PRIVATE_KEY }}'
          owner: '${{ env.FLUX_OWNER }}'
          repositories: '${{ env.FLUX_REPO }}'

      - name: Checkout Flux repo
        uses: actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8 # v5.0.0
        with:
          repository: '${{ env.FLUX_OWNER }}/${{ env.FLUX_REPO }}'
          token: '${{ steps.app-token.outputs.token }}'
          path: flux-repo
          persist-credentials: false

      - name: Export PR ID
        shell: bash
        run: 'echo "PR_ID=${{ github.event.pull_request.number }}" >> $GITHUB_ENV'

      - name: Remove deployed directory
        shell: bash
        run: |
          DST="flux-repo/deployments/prs-${APP_NAME}/${PR_ID}"
          if [[ -d "$DST" ]]; then
            rm -rf "$DST"
            echo "✅ Deleted $DST"
          else
            echo "⏭️ Nothing to delete at $DST"
          fi

      - name: Commit & push deletion
        shell: bash
        run: >
          cd flux-repo

          git config user.name  "${{ steps.app-token.outputs.app-slug }}[bot]"

          git config user.email "${{ steps.app-token.outputs.app-slug
          }}[bot]@users.noreply.github.com"

          git add -A

          git commit -m "chore(prs-${APP_NAME}): remove temp env for PR #${{
          env.PR_ID }} [skip ci]" || echo "Nothing to commit"

          git remote set-url origin \
            https://x-access-token:${{ steps.app-token.outputs.token }}@github.com/${{ env.FLUX_OWNER }}/${{ env.FLUX_REPO }}.git
          git push origin HEAD:main

      - name: Comment preview URL on PR
        uses: thollander/actions-comment-pull-request@v3
        with:
          github-token: '${{ secrets.GITHUB_TOKEN }}'
          pr-number: '${{ github.event.pull_request.number }}'
          comment-tag: 'pr-preview'
          create-if-not-exists: 'true'
          message: |
            ⚙️ Preview environment was undeployed.



================================================
FILE: .github/workflows/docker-build.ecr.yml
================================================
name: Build & Push Container

on:
  push:
    branches:
      - 'main'
    tags:
      - '*'
  merge_group:
  pull_request:
    types: [labeled, synchronize, reopened, ready_for_review, opened]

env:
  PUSH_FROM_PR: >-
    ${{ github.event_name == 'pull_request' &&
       (
         contains(github.event.pull_request.labels.*.name, 'push-container') ||
         contains(github.event.pull_request.labels.*.name, 'deploy-pr-temp-env')
       )
    }}

jobs:
  terraform:
    name: "ECR"
    runs-on: ubuntu-latest
    if: github.repository == 'coderamp-labs/gitingest'

    permissions:
      id-token: write
      contents: read
      pull-requests: write

    steps:
      - name: Checkout
        uses: actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8 # v5.0.0
        with:
          ref: ${{ github.event_name == 'pull_request' && github.event.pull_request.head.sha || github.sha }}

      - name: configure aws credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: ${{ secrets.CODERAMP_AWS_ECR_REGISTRY_PUSH_ROLE_ARN }}
          role-session-name: GitHub_to_AWS_via_FederatedOIDC
          aws-region: eu-west-1

      - name: Set current timestamp
        id: vars
        run: |
          echo "timestamp=$(date +%s)" >> $GITHUB_OUTPUT
          echo "sha_short=$(git rev-parse --short HEAD)" >> $GITHUB_OUTPUT
          echo "sha_full=$(git rev-parse HEAD)" >> $GITHUB_OUTPUT

      - name: Determine version and deployment context
        id: version
        run: |
          REPO_URL="https://github.com/${{ github.repository }}"

          if [[ "${{ github.ref_type }}" == "tag" ]]; then
            # Tag deployment - display version, link to release
            echo "version=${{ github.ref_name }}" >> $GITHUB_OUTPUT
            echo "app_version=${{ github.ref_name }}" >> $GITHUB_OUTPUT
            echo "app_version_url=${REPO_URL}/releases/tag/${{ github.ref_name }}" >> $GITHUB_OUTPUT
          elif [[ "${{ github.event_name }}" == "pull_request" ]]; then
            # PR deployment - display pr-XXX, link to PR commit
            PR_NUMBER="${{ github.event.pull_request.number }}"
            COMMIT_HASH="${{ steps.vars.outputs.sha_full }}"
            echo "version=${PR_NUMBER}/merge-${COMMIT_HASH}" >> $GITHUB_OUTPUT
            echo "app_version=pr-${PR_NUMBER}" >> $GITHUB_OUTPUT
            echo "app_version_url=${REPO_URL}/pull/${PR_NUMBER}/commits/${COMMIT_HASH}" >> $GITHUB_OUTPUT
          else
            # Branch deployment - display branch name, link to commit
            BRANCH_NAME="${{ github.ref_name }}"
            COMMIT_HASH="${{ steps.vars.outputs.sha_full }}"
            echo "app_version=${BRANCH_NAME}" >> $GITHUB_OUTPUT
            echo "app_version_url=${REPO_URL}/commit/${COMMIT_HASH}" >> $GITHUB_OUTPUT
          fi

      - name: Login to Amazon ECR
        id: login-ecr
        uses: aws-actions/amazon-ecr-login@v2

      - name: Docker Meta
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: |
            ${{ secrets.ECR_REGISTRY_URL }}
          flavor: |
            latest=false
          tags: |
            type=ref,event=branch,branch=main,suffix=-${{ steps.vars.outputs.sha_short }}-${{ steps.vars.outputs.timestamp }}
            type=ref,event=pr,suffix=-${{ steps.vars.outputs.sha_short }}-${{ steps.vars.outputs.timestamp }}
            type=pep440,pattern={{raw}}

      - name: Set up QEMU
        uses: docker/setup-qemu-action@v3

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Build and push
        uses: docker/build-push-action@v6
        with:
          context: .
          platforms: linux/amd64, linux/arm64
          push: ${{ github.event_name != 'pull_request' || env.PUSH_FROM_PR == 'true' }}
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          build-args: |
            APP_REPOSITORY=https://github.com/${{ github.repository }}
            APP_VERSION=${{ steps.version.outputs.app_version }}
            APP_VERSION_URL=${{ steps.version.outputs.app_version_url }}
          cache-from: type=gha
          cache-to: type=gha,mode=max



================================================
FILE: .github/workflows/docker-build.ghcr.yml
================================================
name: Build & Push Container

on:
  push:
    branches:
      - 'main'
    tags:
      - '*'
  merge_group:
  pull_request:
    types: [labeled, synchronize, reopened, ready_for_review, opened]

concurrency:
  group: ${{ github.workflow }}-${{ github.head_ref || github.ref }}
  cancel-in-progress: true

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}
  PUSH_FROM_PR: >-
    ${{ github.event_name == 'pull_request' &&
       (
         contains(github.event.pull_request.labels.*.name, 'push-container') ||
         contains(github.event.pull_request.labels.*.name, 'deploy-pr-temp-env')
       )
    }}

permissions:
  contents: read

jobs:
  docker-build:
    name: "GHCR"
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
      attestations: write
      id-token: write
    steps:
      - name: Harden the runner (Audit all outbound calls)
        uses: step-security/harden-runner@ec9f2d5744a09debf3a187a3f4f675c53b671911 # v2.13.0
        with:
          egress-policy: audit

      - uses: actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8 # v5.0.0
        with:
          ref: ${{ github.event_name == 'pull_request' && github.event.pull_request.head.sha || github.sha }}

      - name: Set current timestamp
        id: vars
        run: |
          echo "timestamp=$(date +%s)" >> $GITHUB_OUTPUT
          echo "sha_short=$(git rev-parse --short HEAD)" >> $GITHUB_OUTPUT
          echo "sha_full=$(git rev-parse HEAD)" >> $GITHUB_OUTPUT

      - name: Determine version and deployment context
        id: version
        run: |
          REPO_URL="https://github.com/${{ github.repository }}"

          if [[ "${{ github.ref_type }}" == "tag" ]]; then
            # Tag deployment - display version, link to release
            echo "version=${{ github.ref_name }}" >> $GITHUB_OUTPUT
            echo "app_version=${{ github.ref_name }}" >> $GITHUB_OUTPUT
            echo "app_version_url=${REPO_URL}/releases/tag/${{ github.ref_name }}" >> $GITHUB_OUTPUT
          elif [[ "${{ github.event_name }}" == "pull_request" ]]; then
            # PR deployment - display pr-XXX, link to PR commit
            PR_NUMBER="${{ github.event.pull_request.number }}"
            COMMIT_HASH="${{ steps.vars.outputs.sha_full }}"
            echo "version=${PR_NUMBER}/merge-${COMMIT_HASH}" >> $GITHUB_OUTPUT
            echo "app_version=pr-${PR_NUMBER}" >> $GITHUB_OUTPUT
            echo "app_version_url=${REPO_URL}/pull/${PR_NUMBER}/commits/${COMMIT_HASH}" >> $GITHUB_OUTPUT
          else
            # Branch deployment - display branch name, link to commit
            BRANCH_NAME="${{ github.ref_name }}"
            COMMIT_HASH="${{ steps.vars.outputs.sha_full }}"
            echo "app_version=${BRANCH_NAME}" >> $GITHUB_OUTPUT
            echo "app_version_url=${REPO_URL}/commit/${COMMIT_HASH}" >> $GITHUB_OUTPUT
          fi

      - name: Log in to the Container registry
        uses: docker/login-action@184bdaa0721073962dff0199f1fb9940f07167d1 # v3.5.0
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Docker Meta
        id: meta
        uses: docker/metadata-action@c1e51972afc2121e065aed6d45c65596fe445f3f # v5.8.0
        with:
          images: |
            ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          flavor: |
            latest=false
          tags: |
            type=ref,event=branch,branch=main
            type=ref,event=branch,branch=main,suffix=-${{ steps.vars.outputs.sha_short }}-${{ steps.vars.outputs.timestamp }}
            type=pep440,pattern={{raw}}
            type=ref,event=pr,suffix=-${{ steps.vars.outputs.sha_short }}-${{ steps.vars.outputs.timestamp }}

      - name: Set up QEMU
        uses: docker/setup-qemu-action@29109295f81e9208d7d86ff1c6c12d2833863392 # v3.6.0

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@e468171a9de216ec08956ac3ada2f0791b6bd435 # v3.11.1

      - name: Build and push
        uses: docker/build-push-action@263435318d21b8e681c14492fe198d362a7d2c83 # v6.18.0
        id: push
        with:
          context: .
          platforms: linux/amd64, linux/arm64
          push: ${{ github.event_name != 'pull_request' || env.PUSH_FROM_PR == 'true' }}
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          build-args: |
            APP_REPOSITORY=https://github.com/${{ github.repository }}
            APP_VERSION=${{ steps.version.outputs.app_version }}
            APP_VERSION_URL=${{ steps.version.outputs.app_version_url }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

      - name: Generate artifact attestation
        if: github.event_name != 'pull_request' || env.PUSH_FROM_PR == 'true'
        uses: actions/attest-build-provenance@e8998f949152b193b063cb0ec769d69d929409be # v2.4.0
        with:
          subject-name: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME}}
          subject-digest: ${{ steps.push.outputs.digest }}
          push-to-registry: true



================================================
FILE: .github/workflows/pr-title-check.yml
================================================
name: PR Conventional Commit Validation

on:
  pull_request:
    types: [opened, synchronize, reopened, edited]

jobs:
  validate-pr-title:
    runs-on: ubuntu-latest
    steps:
      - name: Harden the runner (Audit all outbound calls)
        uses: step-security/harden-runner@ec9f2d5744a09debf3a187a3f4f675c53b671911 # v2.13.0
        with:
          egress-policy: audit

      - name: PR Conventional Commit Validation
        uses:  ytanikin/pr-conventional-commits@b72758283dcbee706975950e96bc4bf323a8d8c0 # 1.4.2
        with:
          task_types: '["feat","fix","docs","test","ci","refactor","perf","chore","revert"]'
          add_label: 'false'



================================================
FILE: .github/workflows/publish_to_pypi.yml
================================================
name: Publish to PyPI

on:
  release:
    types: [created] # Run when you click "Publish release"
  workflow_dispatch: # ... or run it manually from the Actions tab

permissions:
  contents: read

jobs:
  release-build:
    runs-on: ubuntu-latest

    steps:
      - name: Harden the runner (Audit all outbound calls)
        uses: step-security/harden-runner@ec9f2d5744a09debf3a187a3f4f675c53b671911 # v2.13.0
        with:
          egress-policy: audit

      - uses: actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8 # v5.0.0

      - name: Set up Python 3.13
        uses: actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065 # v5.6.0
        with:
          python-version: "3.13"
          cache: pip
          cache-dependency-path: pyproject.toml

      - name: Build package
        run: |
          python -m pip install --upgrade pip
          python -m pip install build twine
          python -m build
          twine check dist/*
      - name: Upload dist artefact
        uses: actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 # v4.6.2
        with:
          name: dist
          path: dist/

# Publish to PyPI (only if "dist/" succeeded)
  pypi-publish:
    needs: release-build
    runs-on: ubuntu-latest
    environment: pypi

    permissions:
      id-token: write # OIDC token for trusted publishing

    steps:
      - name: Harden the runner (Audit all outbound calls)
        uses: step-security/harden-runner@ec9f2d5744a09debf3a187a3f4f675c53b671911 # v2.13.0
        with:
          egress-policy: audit

      - uses: actions/download-artifact@634f93cb2916e3fdff6788551b99b062d0335ce0 # v5.0.0
        with:
          name: dist
          path: dist/

      - uses: pypa/gh-action-pypi-publish@76f52bc884231f62b9a034ebfe128415bbaabdfc # release/v1
        with:
          verbose: true



================================================
FILE: .github/workflows/rebase-needed.yml
================================================
name: PR Needs Rebase

on:
  workflow_dispatch: {}
  schedule:
    - cron: '0 * * * *'

permissions:
  pull-requests: write

jobs:
  label-rebase-needed:
    runs-on: ubuntu-latest
    if: github.repository == 'coderamp-labs/gitingest'

    concurrency:
      group: ${{ github.workflow }}-${{ github.ref }}
      cancel-in-progress: true

    steps:
      - name: Check for merge conflicts
        uses: eps1lon/actions-label-merge-conflict@v3
        with:
          dirtyLabel: 'rebase needed :construction:'
          repoToken: '${{ secrets.GITHUB_TOKEN }}'
          commentOnClean: This pull request has resolved merge conflicts and is ready for review.
          commentOnDirty: This pull request has merge conflicts that must be resolved before it can be merged.
          retryMax: 30
          continueOnMissingPermissions: false



================================================
FILE: .github/workflows/release-please.yml
================================================
name: release-please
on:
  push:
    branches:
      - main

permissions:
  contents: write
  pull-requests: write

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8 # v5.0.0

      - name: Create GitHub App token
        uses: actions/create-github-app-token@v2
        id: app-token
        with:
          app-id: '${{ secrets.CR_APP_CI_APP_ID }}'
          private-key: '${{ secrets.CR_APP_CI_PRIVATE_KEY }}'
          owner: '${{ env.FLUX_OWNER }}'
          repositories: '${{ env.FLUX_REPO }}'

      - name: Release Please
        uses: googleapis/release-please-action@v4
        with:
          token: '${{ steps.app-token.outputs.token }}'



================================================
FILE: .github/workflows/scorecard.yml
================================================
name: OSSF Scorecard
on:
  branch_protection_rule:
  schedule:
    - cron: '33 11 * * 2'  # Every Tuesday at 11:33 AM UTC
  push:
    branches: [ main ]

permissions: read-all

concurrency: # avoid overlapping runs
  group: scorecard-${{ github.ref }}
  cancel-in-progress: true

jobs:
  analysis:
    name: Scorecard analysis
    runs-on: ubuntu-latest
    permissions:
      security-events: write # upload SARIF to code-scanning
      id-token: write # publish results for the badge

    steps:
      - name: Harden the runner (Audit all outbound calls)
        uses: step-security/harden-runner@ec9f2d5744a09debf3a187a3f4f675c53b671911 # v2.13.0
        with:
          egress-policy: audit

      - name: Checkout
        uses: actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8 # v5.0.0
        with:
          persist-credentials: false

      - name: Run Scorecard
        uses: ossf/scorecard-action@f35c64557cf912815708bb1126d9948f3e459487
        with:
          results_file: results.sarif
          results_format: sarif
          publish_results: true  # enables the public badge

      - name: Upload to code-scanning
        uses: github/codeql-action/upload-sarif@df559355d593797519d70b90fc8edd5db049e7a2 # v3.29.9
        with:
          sarif_file: results.sarif



================================================
FILE: .github/workflows/stale.yml
================================================
name: "Close stale issues and PRs"

on:
  schedule:
    - cron: "0 6 * * *"
  workflow_dispatch: {}

permissions:
  issues: write
  pull-requests: write

jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v9
        with:
          repo-token: ${{ secrets.GITHUB_TOKEN }}
          days-before-stale: 45
          days-before-close: 10
          stale-issue-label: stale
          stale-pr-label: stale
          stale-issue-message: |
            Hi there! We haven’t seen activity here for 45 days, so I’m marking this issue as stale.
            If you’d like to keep it open, please leave a comment within 10 days. Thanks!
          stale-pr-message: |
            Hi there! We haven’t seen activity on this pull request for 45 days, so I’m marking it as stale.
            If you’d like to keep it open, please leave a comment within 10 days. Thanks!
          close-issue-message: |
            Hi there! We haven’t heard anything for 10 days, so I’m closing this issue. Feel free to reopen if you’d like to continue the discussion. Thanks!
          close-pr-message: |
            Hi there! We haven’t heard anything for 10 days, so I’m closing this pull request. Feel free to reopen if you’d like to continue working on it. Thanks!


