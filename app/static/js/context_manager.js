/**
 * Context Management UI
 */

// Initialize context UI
function initializeContextUI() {
    const contextSwitcher = document.getElementById('context-switcher');
    const newContextBtn = document.getElementById('new-context-btn');
    const deleteContextBtn = document.getElementById('delete-context-btn');
    
    if (!contextSwitcher) return;
    
    // Handle context switching
    if (!contextSwitcher.hasAttribute('data-initialized')) {
        contextSwitcher.addEventListener('change', function() {
            const newContext = this.value;
            if (newContext && newContext !== window.workspaceManager?.currentContextId) {
                window.workspaceManager?.switchContext(newContext);
            }
        });
        contextSwitcher.setAttribute('data-initialized', 'true');
    }
    
    // Handle new context creation
    if (newContextBtn && !newContextBtn.hasAttribute('data-initialized')) {
        newContextBtn.addEventListener('click', async function() {
            const name = await openContextModal();
            if (name && name.trim()) {
                const id = name.toLowerCase().replace(/[^a-z0-9]/g, '-');
                if (window.workspaceManager?.createContext(id, name.trim())) {
                    window.workspaceManager?.switchContext(id);
                } else {
                    // Silently handle existing context
                    // Could show error in modal but for now just skip
                }
            }
        });
        newContextBtn.setAttribute('data-initialized', 'true');
    }
    
    // Handle context deletion
    if (deleteContextBtn && !deleteContextBtn.hasAttribute('data-initialized')) {
        deleteContextBtn.addEventListener('click', function() {
            if (window.workspaceManager?.currentContextId === 'default') {
                // Silently return without deleting default context
                return;
            }
            
            // Delete context without confirmation
            window.workspaceManager?.deleteContext(window.workspaceManager?.currentContextId);
        });
        deleteContextBtn.setAttribute('data-initialized', 'true');
    }
}

// Update workspace contents based on selected tab
function updateWorkspaceContents(tabId) {
    updateWorkspaceFileSystem(tabId);
    if (window.updateWorkspaceEditor) {
        window.updateWorkspaceEditor(tabId);
    }
}

function updateWorkspaceFileSystem(tabId) {
    // File system now uses the persistent file tree
    // This function can be used to filter visible files based on tab context
    if (window.renderFileTree) {
        window.renderFileTree();
    }
}

// Export functions for global use
window.initializeContextUI = initializeContextUI;
window.updateWorkspaceContents = updateWorkspaceContents;
window.updateWorkspaceFileSystem = updateWorkspaceFileSystem;