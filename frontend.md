Directory structure:
└── coderamp-labs-gitingest/
    └── src/
        └── server/
            └── templates/
                ├── base.jinja
                ├── git.jinja
                ├── index.jinja
                ├── swagger_ui.jinja
                └── components/
                    ├── _macros.jinja
                    ├── footer.jinja
                    ├── git_form.jinja
                    ├── navbar.jinja
                    ├── result.jinja
                    └── tailwind_components.html


Files Content:

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


