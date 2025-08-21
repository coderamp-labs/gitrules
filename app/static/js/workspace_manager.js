/**
 * WorkspaceState - Manages all state for a single workspace context
 */
class WorkspaceState {
    constructor(contextId) {
        this.contextId = contextId;
        this.files = {};  // File path -> content mapping
        this.selectedFile = null;
        this.expandedFolders = new Set();
        this.history = {
            past: [],
            present: null,
            future: [],
            maxSize: 50
        };
    }

    // Initialize empty state
    initEmpty() {
        this.files = {};
        this.selectedFile = null;
        this.expandedFolders = new Set();
        this.history.present = this.snapshot();
        this.history.past = [];
        this.history.future = [];
    }

    // Create a snapshot of current state
    snapshot() {
        return {
            files: { ...this.files },
            selectedFile: this.selectedFile,
            expandedFolders: Array.from(this.expandedFolders),
            timestamp: new Date().toISOString()
        };
    }

    // Add a file (Include action)
    addFile(path, content) {
        this.pushHistory();
        this.files[path] = content;
        this.selectedFile = path;
        this.history.present = this.snapshot();
        // Dispatch event for auto-share
        window.dispatchEvent(new CustomEvent('workspace-file-added'));
    }

    // Delete a file
    deleteFile(path) {
        this.pushHistory();
        delete this.files[path];
        if (this.selectedFile === path) {
            this.selectedFile = null;
        }
        this.history.present = this.snapshot();
        // Dispatch event for auto-share
        window.dispatchEvent(new CustomEvent('workspace-file-deleted'));
    }

    // Push current state to history
    pushHistory() {
        if (this.history.present) {
            this.history.past.push(this.history.present);
            if (this.history.past.length > this.history.maxSize) {
                this.history.past.shift();
            }
            this.history.future = [];
        }
    }

    // Go to previous state
    undo() {
        if (this.history.past.length === 0) return false;
        
        const previousState = this.history.past.pop();
        this.history.future.unshift(this.history.present);
        this.history.present = previousState;
        this.restoreFromSnapshot(previousState);
        return true;
    }

    // Go to next state
    redo() {
        if (this.history.future.length === 0) return false;
        
        const nextState = this.history.future.shift();
        this.history.past.push(this.history.present);
        this.history.present = nextState;
        this.restoreFromSnapshot(nextState);
        return true;
    }

    // Restore state from snapshot
    restoreFromSnapshot(snapshot) {
        this.files = { ...snapshot.files };
        this.selectedFile = snapshot.selectedFile;
        this.expandedFolders = new Set(snapshot.expandedFolders || []);
    }

    // Reset to empty state
    reset() {
        this.pushHistory();
        this.files = {};
        this.selectedFile = null;
        this.expandedFolders = new Set();
        this.history.present = this.snapshot();
    }

    // Check if we can undo/redo
    canUndo() {
        return this.history.past.length > 0;
    }

    canRedo() {
        return this.history.future.length > 0;
    }

    // Serialize state for localStorage
    serialize() {
        return JSON.stringify({
            contextId: this.contextId,
            files: this.files,
            selectedFile: this.selectedFile,
            expandedFolders: Array.from(this.expandedFolders),
            history: {
                past: this.history.past,
                present: this.history.present,
                future: this.history.future
            }
        });
    }

    // Deserialize state from localStorage
    static deserialize(contextId, data) {
        const state = new WorkspaceState(contextId);
        if (data) {
            try {
                const parsed = typeof data === 'string' ? JSON.parse(data) : data;
                state.files = parsed.files || {};
                state.selectedFile = parsed.selectedFile || null;
                state.expandedFolders = new Set(parsed.expandedFolders || []);
                
                if (parsed.history) {
                    state.history.past = parsed.history.past || [];
                    state.history.present = parsed.history.present || state.snapshot();
                    state.history.future = parsed.history.future || [];
                } else {
                    state.history.present = state.snapshot();
                }
            } catch (e) {
                console.error('Failed to deserialize state:', e);
                state.initEmpty();
            }
        } else {
            state.initEmpty();
        }
        return state;
    }
}

/**
 * WorkspaceManager - Manages multiple workspace contexts
 */
class WorkspaceManager {
    constructor() {
        this.contexts = {};
        this.currentContextId = null;
        this.currentState = null;
    }

    // Initialize the manager
    init() {
        this.contexts = this.loadContextsList();
        
        if (!this.contexts['default']) {
            this.createContext('default', 'Default Workspace');
        }
        
        const lastContext = localStorage.getItem('app:currentContext');
        
        if (lastContext && this.contexts[lastContext]) {
            this.switchContext(lastContext);
        } else {
            this.switchContext('default');
        }
    }

    // Load contexts list from localStorage
    loadContextsList() {
        try {
            const data = localStorage.getItem('app:contexts');
            return data ? JSON.parse(data) : {};
        } catch {
            return {};
        }
    }

    // Save contexts list to localStorage
    saveContextsList() {
        localStorage.setItem('app:contexts', JSON.stringify(this.contexts));
    }

    // Create a new context
    createContext(id, name) {
        if (this.contexts[id]) {
            console.warn(`Context ${id} already exists`);
            return false;
        }
        
        this.contexts[id] = {
            id,
            name,
            createdAt: Date.now()
        };
        
        this.saveContextsList();
        return true;
    }

    // Switch to a different context
    switchContext(contextId) {
        if (!this.contexts[contextId] && contextId !== 'default') {
            const saved = this.loadContextsList();
            if (!saved[contextId]) {
                console.error(`Context ${contextId} not found`);
                return false;
            }
            this.contexts = saved;
        }
        
        if (this.currentState) {
            this.saveState(this.currentContextId);
        }
        
        this.currentContextId = contextId;
        this.currentState = this.loadState(contextId);
        localStorage.setItem('app:currentContext', contextId);
        this.render();
        
        return true;
    }

    // Delete a context
    deleteContext(contextId) {
        if (contextId === 'default') {
            console.warn('Cannot delete default context');
            return false;
        }
        
        delete this.contexts[contextId];
        localStorage.removeItem(`app:workspace:${contextId}`);
        this.saveContextsList();
        
        if (this.currentContextId === contextId) {
            this.switchContext('default');
        }
        
        return true;
    }

    // Save state to localStorage
    saveState(contextId) {
        if (!this.currentState) return;
        
        const key = `app:workspace:${contextId}`;
        localStorage.setItem(key, this.currentState.serialize());
    }

    // Load state from localStorage
    loadState(contextId) {
        const key = `app:workspace:${contextId}`;
        const data = localStorage.getItem(key);
        return WorkspaceState.deserialize(contextId, data);
    }

    // Get current state
    getState() {
        return this.currentState;
    }

    // Render the UI based on current state
    render() {
        if (!this.currentState) return;
        
        // Update file tree
        if (window.renderFileTree) {
            window.renderFileTree();
        }
        
        // Update editor
        if (this.currentState.selectedFile && this.currentState.files[this.currentState.selectedFile]) {
            // Selected file exists - load it
            if (window.openFile) {
                window.openFile(this.currentState.selectedFile);
            }
        } else {
            // No selected file - check if we have any files to auto-select
            const fileKeys = Object.keys(this.currentState.files);
            if (fileKeys.length > 0 && !this.currentState.selectedFile) {
                // Auto-select first file
                const firstFile = fileKeys[0];
                this.currentState.selectedFile = firstFile;
                this.saveState(this.currentContextId);
                
                if (window.openFile) {
                    window.openFile(firstFile);
                }
            } else {
                // No files available - show placeholder
                if (window.workspaceMonacoEditor) {
                    window.workspaceMonacoEditor.setValue('Select a file from the left to view its content.');
                }
                if (window.updateFilePathLabel) {
                    window.updateFilePathLabel(null);
                }
            }
        }
        
        this.updateHistoryButtons();
        this.updateContextDropdown();
    }

    // Update history button states
    updateHistoryButtons() {
        const prevBtn = document.getElementById('files-prev-btn');
        const nextBtn = document.getElementById('files-next-btn');
        
        if (prevBtn) {
            prevBtn.disabled = !this.currentState.canUndo();
        }
        if (nextBtn) {
            nextBtn.disabled = !this.currentState.canRedo();
        }
    }

    // Update context dropdown
    updateContextDropdown() {
        const contextSwitcher = document.getElementById('context-switcher');
        if (!contextSwitcher) return;
        
        contextSwitcher.innerHTML = '';
        Object.values(this.contexts).forEach(ctx => {
            const option = document.createElement('option');
            option.value = ctx.id;
            // Truncate long names to fit the dropdown
            let displayName = ctx.name;
            if (displayName.length > 25) {
                displayName = displayName.substring(0, 22) + '...';
            }
            option.textContent = displayName;
            option.title = ctx.name; // Show full name on hover
            option.selected = ctx.id === this.currentContextId;
            contextSwitcher.appendChild(option);
        });
    }

    // Include a file (main action for adding files)
    includeFile(path, content) {
        if (!this.currentState) return false;
        
        if (this.currentState.files[path]) {
            if (!confirm(`File "${path}" already exists. Overwrite?`)) {
                return false;
            }
        }
        
        this.currentState.addFile(path, content);
        this.saveState(this.currentContextId);
        this.render();
        return true;
    }

    // Delete a file
    deleteFile(path) {
        if (!this.currentState) return false;
        
        if (!confirm(`Delete "${path}"?`)) {
            return false;
        }
        
        this.currentState.deleteFile(path);
        this.saveState(this.currentContextId);
        this.render();
        return true;
    }

    // Undo action
    undo() {
        if (!this.currentState) return;
        
        if (this.currentState.undo()) {
            this.saveState(this.currentContextId);
            this.render();
        }
    }

    // Redo action
    redo() {
        if (!this.currentState) return;
        
        if (this.currentState.redo()) {
            this.saveState(this.currentContextId);
            this.render();
        }
    }

    // Reset current workspace
    reset() {
        if (!this.currentState) return;
        
        if (confirm('Reset will clear all files. Are you sure?')) {
            this.currentState.reset();
            this.saveState(this.currentContextId);
            this.render();
        }
    }
}

// Export for global use
window.WorkspaceState = WorkspaceState;
window.WorkspaceManager = WorkspaceManager;