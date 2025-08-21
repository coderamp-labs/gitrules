/**
 * File Tree Management
 */

// Generate file tree structure dynamically from workspace state
function generateFileTreeData() {
    const tree = {};
    const state = window.workspaceManager?.getState();
    if (!state) return [];
    
    const files = Object.keys(state.files);
    
    // Build nested tree structure
    files.forEach(filePath => {
        const parts = filePath.split('/');
        let current = tree;
        
        // Create folder nodes
        for (let i = 0; i < parts.length - 1; i++) {
            const folderName = parts[i];
            const folderPath = parts.slice(0, i + 1).join('/');
            
            if (!current[folderName]) {
                current[folderName] = {
                    type: 'folder',
                    path: folderPath,
                    name: folderName,
                    children: {}
                };
            }
            current = current[folderName].children;
        }
        
        // Add file node
        const fileName = parts[parts.length - 1];
        current[fileName] = {
            type: 'file',
            path: filePath,
            name: fileName
        };
    });
    
    // Convert to array format expected by renderer
    function convertToArray(obj) {
        return Object.values(obj).map(node => {
            if (node.type === 'folder') {
                return {
                    ...node,
                    children: convertToArray(node.children)
                };
            }
            return node;
        });
    }
    
    return convertToArray(tree);
}

// Render file tree
function renderFileTree() {
    const treeContainer = document.getElementById('file-tree');
    const emptyStateEl = document.getElementById('files-empty-state');
    if (!treeContainer) return;
    
    treeContainer.innerHTML = '';
    
    const state = window.workspaceManager?.getState();
    const hasFiles = state && Object.keys(state.files).length > 0;
    
    if (!hasFiles) {
        if (emptyStateEl) {
            emptyStateEl.classList.remove('hidden');
        }
        return;
    } else {
        if (emptyStateEl) {
            emptyStateEl.classList.add('hidden');
        }
    }
    
    function renderNode(node, level = 0) {
        const div = document.createElement('div');
        div.style.paddingLeft = `${level * 16}px`;
        
        if (node.type === 'folder') {
            const state = window.workspaceManager?.getState();
            // Default to expanded - only collapsed if explicitly marked
            let isExpanded = true;
            if (state && state.expandedFolders.has(node.path + ':collapsed')) {
                isExpanded = false;
            }
            const folderIcon = isExpanded ? 'mdi-folder-open' : 'mdi-folder';
            div.innerHTML = `
                <div class="flex items-center gap-1 p-1 hover:bg-gray-100 cursor-pointer folder-toggle" data-path="${node.path}">
                    <svg class="w-3 h-3 transition-transform ${isExpanded ? 'rotate-90' : ''}" fill="currentColor" viewBox="0 0 20 20">
                        <path d="M7 7l3 3 3-3" stroke="currentColor" stroke-width="2" fill="none"/>
                    </svg>
                    <span class="mdi ${folderIcon} text-blue-600 text-base"></span>
                    <span class="font-medium">${node.name}</span>
                </div>
            `;
            
            treeContainer.appendChild(div);
            
            if (isExpanded && node.children) {
                node.children.forEach(child => renderNode(child, level + 1));
            }
        } else {
            // File node
            const state = window.workspaceManager?.getState();
            const isSelected = state && state.selectedFile === node.path;
            div.innerHTML = `
                <div class="flex items-center justify-between p-1 hover:bg-gray-100 cursor-pointer file-item ${isSelected ? 'bg-cyan-100 font-medium' : ''}" data-path="${node.path}">
                    <div class="flex items-center gap-1">
                        <span class="w-3"></span>
                        <span class="mdi mdi-file-document-outline text-gray-600 text-sm"></span>
                        <span>${node.name}</span>
                        <span class="text-xs text-blue-600 ml-1">✓</span>
                    </div>
                    <button class="delete-file opacity-0 group-hover:opacity-100 hover:opacity-100 text-red-600 hover:text-red-800 p-1" data-path="${node.path}" title="Delete file">
                        <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                            <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd"/>
                        </svg>
                    </button>
                </div>
            `;
            
            const fileDiv = div.querySelector('.file-item');
            fileDiv.classList.add('group');
            treeContainer.appendChild(div);
        }
    }
    
    // Generate and render dynamic tree
    const fileTreeData = generateFileTreeData();
    fileTreeData.forEach(node => renderNode(node));
    
    // Add event listeners
    treeContainer.addEventListener('click', handleTreeClick);
}

// Handle tree clicks
async function handleTreeClick(event) {
    const deleteButton = event.target.closest('.delete-file');
    const folderToggle = event.target.closest('.folder-toggle');
    const fileItem = event.target.closest('.file-item');
    
    if (deleteButton) {
        event.stopPropagation();
        const path = deleteButton.dataset.path;
        window.workspaceManager?.deleteFile(path);
    } else if (folderToggle) {
        const path = folderToggle.dataset.path;
        const state = window.workspaceManager?.getState();
        if (state) {
            // Track collapsed state instead of expanded state (default is expanded)
            const collapsedKey = path + ':collapsed';
            if (state.expandedFolders.has(collapsedKey)) {
                state.expandedFolders.delete(collapsedKey);
            } else {
                state.expandedFolders.add(collapsedKey);
            }
            window.workspaceManager.saveState(window.workspaceManager.currentContextId);
            renderFileTree();
        }
    } else if (fileItem) {
        const path = fileItem.dataset.path;
        await openFile(path);
    }
}

// Open file in editor
async function openFile(path) {
    if (!window.workspaceMonacoEditor) return;
    
    const state = window.workspaceManager?.getState();
    if (!state || !state.files[path]) {
        console.error('File not found:', path);
        window.workspaceMonacoEditor.setValue(`⚠️ File not found: "${path}"`);
        return;
    }
    
    // Update selected file
    state.selectedFile = path;
    window.workspaceManager.saveState(window.workspaceManager.currentContextId);
    
    // Show content
    const content = state.files[path];
    window.workspaceMonacoEditor.setValue(content);
    
    // Update file path label
    updateFilePathLabel(path);
    
    // Refresh tree to show selection
    renderFileTree();
}

// Update file path label
function updateFilePathLabel(path) {
    const filePathElement = document.getElementById('current-file-path');
    if (!filePathElement) return;
    
    if (path) {
        filePathElement.textContent = path;
        filePathElement.className = 'text-xs text-gray-600 bg-gray-50 px-2 py-1 border border-gray-300 rounded';
        filePathElement.style.fontFamily = "'Courier New', monospace";
    } else {
        filePathElement.textContent = 'No file selected';
        filePathElement.className = 'text-xs text-gray-400 bg-gray-50 px-2 py-1 border border-gray-300 rounded';
        filePathElement.style.fontFamily = "'Courier New', monospace";
    }
}

// Create new file
async function createNewFile() {
    const fileName = prompt('Enter file name (with extension):');
    if (!fileName || fileName.trim() === '') {
        return;
    }
    
    const filePath = fileName.trim();
    
    // Create file with default content
    const defaultContent = filePath.endsWith('.md') ? 
        `# ${filePath.replace('.md', '').replace(/[_-]/g, ' ')}\n\nYour content here...` :
        filePath.endsWith('.json') ?
        '{\n  "name": "new-file",\n  "version": "1.0.0"\n}' :
        filePath.endsWith('.yaml') || filePath.endsWith('.yml') ?
        'name: new-file\nversion: 1.0.0\n' :
        '# New file\n\nContent goes here...';
    
    return await includeFile(filePath, defaultContent);
}

// Include a file with given path and content
async function includeFile(filePath, content) {
    return window.workspaceManager?.includeFile(filePath, content);
}

// Delete file
async function deleteFile(path) {
    return window.workspaceManager?.deleteFile(path);
}

// Include predefined content templates
async function includeTemplate(templateName) {
    const templates = {
        'Supabase MCP': {
            path: 'mcps/supabase_mcp.json',
            content: `{
  "name": "supabase-mcp",
  "version": "1.0.0",
  "description": "Model Context Protocol for Supabase integration",
  "tools": [
    {
      "name": "query_database",
      "description": "Execute SQL queries on Supabase database"
    }
  ]
}`
        },
        'Github MCP': {
            path: 'mcps/github_mcp.json',
            content: `{
  "name": "github-mcp",
  "version": "1.0.0",
  "description": "Model Context Protocol for GitHub integration",
  "tools": [
    {
      "name": "create_issue",
      "description": "Create a new GitHub issue"
    }
  ]
}`
        },
        'Python': {
            path: 'guidelines/python_style.md',
            content: `# Python Style Guidelines

## Code Formatting
- Use PEP 8 style guide
- Line length: 88 characters (Black formatter)
- Use type hints for all functions

## Best Practices
- Use meaningful variable names
- Add docstrings to all functions and classes
- Prefer list comprehensions over loops when appropriate`
        },
        'TypeScript': {
            path: 'guidelines/typescript_rules.md',
            content: `# TypeScript Coding Rules

## Type Safety
- Always use strict mode
- No \`any\` type unless absolutely necessary
- Define interfaces for all data structures

## Code Style
- Use Prettier for formatting
- Prefer const over let
- Use arrow functions for callbacks`
        },
        'Researcher': {
            path: 'subagents/researcher.md',
            content: `# Researcher Agent

A specialized subagent for information gathering and analysis.

## Capabilities
- Web search and analysis
- Document research
- Data compilation and synthesis

## Usage
\`\`\`
@researcher find information about [topic]
\`\`\``
        },
        'Memory Manager': {
            path: 'subagents/memory_manager.md',
            content: `# Memory Manager Agent

Handles context and conversation history management.

## Features
- Long-term context preservation
- Conversation summarization
- Knowledge base integration

## Usage
\`\`\`
@memory store this information about [topic]
@memory recall information about [topic]
\`\`\``
        },
        'Code Reviewer': {
            path: 'subagents/code_reviewer.md',
            content: `# Code Reviewer Agent

Specialized agent for code review and quality assessment.

## Capabilities
- Code quality analysis
- Security vulnerability detection
- Best practices compliance
- Performance optimization suggestions

## Usage
\`\`\`
@reviewer analyze this code for issues
@reviewer check security vulnerabilities
\`\`\``
        },
        'React Guidelines': {
            path: 'guidelines/react_rules.md',
            content: `# React Development Guidelines

## Component Structure
- Use functional components with hooks
- Prefer composition over inheritance
- Keep components small and focused

## State Management
- Use useState for local state
- Use useContext for shared state
- Consider useReducer for complex state logic

## Performance
- Use React.memo for expensive components
- Optimize re-renders with useMemo and useCallback
- Lazy load components when appropriate`
        },
        'API Design Guidelines': {
            path: 'guidelines/api_design.md',
            content: `# API Design Guidelines

## RESTful Principles
- Use HTTP methods correctly (GET, POST, PUT, DELETE)
- Use meaningful resource URLs
- Return appropriate HTTP status codes

## Request/Response Format
- Use JSON for request and response bodies
- Include proper Content-Type headers
- Implement consistent error response format

## Security
- Use HTTPS for all endpoints
- Implement proper authentication/authorization
- Validate all input parameters`
        },
        'Database MCP': {
            path: 'mcps/database_mcp.json',
            content: `{
  "name": "database-mcp",
  "version": "1.0.0",
  "description": "Model Context Protocol for database operations",
  "tools": [
    {
      "name": "query_database",
      "description": "Execute SQL queries on database"
    },
    {
      "name": "create_table",
      "description": "Create new database tables"
    },
    {
      "name": "migrate_schema",
      "description": "Run database migrations"
    }
  ]
}`
        }
    };
    
    const template = templates[templateName];
    if (template) {
        return await includeFile(template.path, template.content);
    } else {
        console.error('Unknown template:', templateName);
        return false;
    }
}

// Initialize file tree system
function initializeFileTree() {
    // Wire up history buttons
    const prevBtn = document.getElementById('files-prev-btn');
    const nextBtn = document.getElementById('files-next-btn');
    const resetBtn = document.getElementById('files-reset-btn');
    
    if (prevBtn && !prevBtn.hasAttribute('data-initialized')) {
        prevBtn.addEventListener('click', () => window.workspaceManager?.undo());
        prevBtn.setAttribute('data-initialized', 'true');
    }
    if (nextBtn && !nextBtn.hasAttribute('data-initialized')) {
        nextBtn.addEventListener('click', () => window.workspaceManager?.redo());
        nextBtn.setAttribute('data-initialized', 'true');
    }
    if (resetBtn && !resetBtn.hasAttribute('data-initialized')) {
        resetBtn.addEventListener('click', () => window.workspaceManager?.reset());
        resetBtn.setAttribute('data-initialized', 'true');
    }
    
    // Wire up New File button
    const newFileButton = document.getElementById('new-file-button');
    if (newFileButton && !newFileButton.hasAttribute('data-initialized')) {
        newFileButton.addEventListener('click', createNewFile);
        newFileButton.setAttribute('data-initialized', 'true');
    }
    
    // Wire up Quick Action buttons (use delegation to avoid duplicates)
    if (!document.body.hasAttribute('data-qa-initialized')) {
        document.addEventListener('click', async function(e) {
            const button = e.target.closest('.action-button[data-template]');
            if (button) {
                const templateName = button.dataset.template;
                if (templateName) {
                    await includeTemplate(templateName);
                }
            }
        });
        document.body.setAttribute('data-qa-initialized', 'true');
    }
}

// Export functions for global use
window.generateFileTreeData = generateFileTreeData;
window.renderFileTree = renderFileTree;
window.handleTreeClick = handleTreeClick;
window.openFile = openFile;
window.updateFilePathLabel = updateFilePathLabel;
window.createNewFile = createNewFile;
window.includeFile = includeFile;
window.deleteFile = deleteFile;
window.includeTemplate = includeTemplate;
window.initializeFileTree = initializeFileTree;