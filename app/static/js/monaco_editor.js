/**
 * Monaco Editor Integration
 */

let workspaceMonacoEditor;

function initializeWorkspaceEditor() {
    require.config({ paths: { vs: 'https://unpkg.com/monaco-editor@0.44.0/min/vs' } });
    
    require(['vs/editor/editor.main'], function () {
        workspaceMonacoEditor = monaco.editor.create(document.getElementById('workspace-monaco-editor'), {
            value: '',
            language: 'markdown',
            theme: 'vs',
            fontSize: 12,
            lineNumbers: 'on',
            minimap: { enabled: false },
            scrollBeyondLastLine: false,
            automaticLayout: true,
            wordWrap: 'on'
        });
        
        // Listen for content changes and update workspace state
        workspaceMonacoEditor.onDidChangeModelContent(function() {
            const state = window.workspaceManager?.getState();
            if (state && state.selectedFile) {
                // Update the file content in workspace state
                state.files[state.selectedFile] = workspaceMonacoEditor.getValue();
                // Save to localStorage
                if (window.workspaceManager) {
                    window.workspaceManager.saveState(window.workspaceManager.currentContextId);
                }
                // Dispatch event for auto-share
                window.dispatchEvent(new CustomEvent('workspace-content-changed'));
            }
        });
        
        // Expose globally for access from other components
        window.workspaceMonacoEditor = workspaceMonacoEditor;
        
        // Copy functionality
        document.getElementById('copy-workspace-editor').addEventListener('click', function() {
            const content = workspaceMonacoEditor.getValue();
            navigator.clipboard.writeText(content);
        });
        
        // Initialize QuickAction button handlers after editor is ready
        setTimeout(initializeQuickActionHandlers, 100);
    });
}

function insertTextAtCursor(text) {
    if (!workspaceMonacoEditor) return;
    
    const selection = workspaceMonacoEditor.getSelection();
    const position = selection.getStartPosition();
    
    workspaceMonacoEditor.executeEdits('quickaction-insert', [{
        range: new monaco.Range(position.lineNumber, position.column, position.lineNumber, position.column),
        text: text
    }]);
    
    // Move cursor to end of inserted text
    const newPosition = new monaco.Position(position.lineNumber, position.column + text.length);
    workspaceMonacoEditor.setPosition(newPosition);
    workspaceMonacoEditor.focus();
}

function initializeQuickActionHandlers() {
    // Helper function to extract button label
    function getButtonLabel(button) {
        const labelSpan = button.querySelector('span.font-bold');
        return labelSpan ? labelSpan.textContent.trim() : 'Unknown';
    }
    
    // Add handlers for main QuickAction buttons (above workspace)
    const mainQuickActionButtons = document.querySelectorAll('#quick-actions-section button');
    mainQuickActionButtons.forEach(button => {
        // Skip "See all..." buttons
        if (button.textContent.includes('See all')) return;
        
        button.addEventListener('click', function() {
            const label = getButtonLabel(this);
            insertTextAtCursor(label);
        });
    });
    
    // Add handlers for workspace panel QuickAction buttons
    const workspaceActionButtons = document.querySelectorAll('.qa-tab-content button');
    workspaceActionButtons.forEach(button => {
        button.addEventListener('click', function() {
            const label = getButtonLabel(this);
            insertTextAtCursor(label);
        });
    });
}

function updateWorkspaceEditor(tabId) {
    if (!workspaceMonacoEditor) return;
    
    const editorContent = {
        'tab-claude': {
            content: `# Claude Configuration

## Subagents
- Researcher: Information gathering specialist
- Memory Manager: Context and history management

## Guidelines
- Python: PEP 8 compliance, type hints
- Code quality: Clean, documented, tested

## MCPs (Model Context Protocols)
- Database integration
- File system access
- API connections`,
            language: 'markdown'
        },
        'tab-cursor': {
            content: `// Cursor/VS Code Configuration

{
  "rules": [
    "Always use TypeScript for new files",
    "Prefer functional components in React",
    "Use meaningful variable names",
    "Add JSDoc comments for functions"
  ],
  "preferences": {
    "tabSize": 2,
    "insertSpaces": true,
    "trimTrailingWhitespace": true
  },
  "extensions": [
    "Prettier",
    "ESLint",
    "GitLens",
    "Auto Rename Tag"
  ]
}`,
            language: 'json'
        }
    };
    
    const config = editorContent[tabId];
    if (config) {
        workspaceMonacoEditor.setValue(config.content);
        monaco.editor.setModelLanguage(workspaceMonacoEditor.getModel(), config.language);
        const languageSelect = document.getElementById('workspace-language-select');
        if (languageSelect) {
            languageSelect.value = config.language;
        }
    }
}

// Export functions for global use
window.workspaceMonacoEditor = workspaceMonacoEditor;
window.initializeWorkspaceEditor = initializeWorkspaceEditor;
window.insertTextAtCursor = insertTextAtCursor;
window.initializeQuickActionHandlers = initializeQuickActionHandlers;
window.updateWorkspaceEditor = updateWorkspaceEditor;