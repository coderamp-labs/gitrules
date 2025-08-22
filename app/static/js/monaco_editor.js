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
    console.log("Inserted text:", text);

    // Move cursor to end of inserted text
    const newPosition = new monaco.Position(position.lineNumber, position.column + text.length);
    workspaceMonacoEditor.setPosition(newPosition);
    workspaceMonacoEditor.focus();
}

function initializeQuickActionHandlers() {
    // Helper function to extract button label

}

function updateWorkspaceEditor(tabId) {
    // This function is no longer needed as we're using file-based content
    // Kept for compatibility but does nothing
    return;
}

// Export functions for global use
window.workspaceMonacoEditor = workspaceMonacoEditor;
window.initializeWorkspaceEditor = initializeWorkspaceEditor;
window.insertTextAtCursor = insertTextAtCursor;
window.initializeQuickActionHandlers = initializeQuickActionHandlers;
window.updateWorkspaceEditor = updateWorkspaceEditor;