/**
 * AutoShare Manager - Handles automatic sharing with debounced saves
 */
class AutoShareManager {
    constructor() {
        this.state = 'synced'; // hidden, synced, syncing, error
        this.dirty = false;
        this.currentShareUrl = null;
        this.currentShareId = null;
        this.debounceTimer = null;
        this.pendingSync = false;
        this.lastPayloadHash = null;
        
        // UI elements
        this.panel = null;
        this.linkInput = null;
        this.copyButton = null;
        
        this.init();
    }
    
    init() {
        this.panel = document.getElementById('auto-share-panel');
        this.linkInput = document.getElementById('share-link-input');
        this.copyButton = document.getElementById('copy-share-link');
        
        if (this.copyButton) {
            this.copyButton.addEventListener('click', () => this.copyLink());
        }
        
        // Listen for workspace changes
        this.attachListeners();
        
        // Trigger initial sync if there's content
        setTimeout(() => {
            const data = this.collectWorkspaceData();
            if (Object.keys(data).length > 0) {
                this.markDirty();
            }
        }, 500);
    }
    
    attachListeners() {
        // Listen for file content changes
        window.addEventListener('workspace-content-changed', () => {
            this.markDirty();
        });
        
        // Listen for file additions/deletions
        window.addEventListener('workspace-file-added', () => {
            this.markDirty();
        });
        
        window.addEventListener('workspace-file-deleted', () => {
            this.markDirty();
        });
    }
    
    markDirty() {
        this.dirty = true;
        
        // Clear existing timer
        if (this.debounceTimer) {
            clearTimeout(this.debounceTimer);
        }
        
        // Set new timer for 500ms
        this.debounceTimer = setTimeout(() => {
            this.sync();
        }, 500);
    }
    
    async sync() {
        // Skip if already syncing
        if (this.state === 'syncing') {
            this.pendingSync = true;
            return;
        }
        
        // Collect current workspace data
        const payload = this.collectWorkspaceData();
        
        // If no files, don't sync
        if (Object.keys(payload).length === 0) {
            this.dirty = false;
            this.setState('synced');
            if (this.linkInput) {
                this.linkInput.value = 'Add files to generate install link';
            }
            return;
        }
        
        // Check if payload has changed
        const payloadHash = this.hashPayload(payload);
        if (payloadHash === this.lastPayloadHash) {
            this.dirty = false;
            return;
        }
        
        // Update UI to syncing state
        this.setState('syncing');
        
        try {
            // Send to API
            const response = await fetch('/api/install', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ files: payload })
            });
            
            if (!response.ok) {
                throw new Error('Failed to sync');
            }
            
            const data = await response.json();
            
            // Update state with new share URL
            this.currentShareId = data.hash;
            this.currentShareUrl = `sh -c "$(curl -fsSL ${window.location.origin}/api/install/${data.hash}.sh)"`;
            this.lastPayloadHash = payloadHash;
            this.dirty = false;
            
            // Update UI to synced state
            this.setState('synced');
            
            // Check if we need another sync
            if (this.pendingSync || this.dirty) {
                this.pendingSync = false;
                setTimeout(() => this.sync(), 100);
            }
            
        } catch (error) {
            console.error('Auto-share sync failed:', error);
            this.setState('error');
            
            // Retry after a delay if still dirty
            if (this.dirty) {
                setTimeout(() => this.sync(), 2000);
            }
        }
    }
    
    collectWorkspaceData() {
        const allFiles = {};
        
        // Get files directly from workspace manager state
        const state = window.workspaceManager?.getState();
        if (state?.files) {
            return { ...state.files };
        }
        
        // Fallback: collect files from tree structure
        function collectFilesFromTree(nodes, collected) {
            nodes.forEach(node => {
                if (node.type === 'file') {
                    const state = window.workspaceManager?.getState();
                    if (state?.files[node.path]) {
                        collected[node.path] = state.files[node.path];
                    }
                } else if (node.type === 'folder' && node.children) {
                    collectFilesFromTree(node.children, collected);
                }
            });
        }
        
        // Collect files from dynamic tree if available
        if (window.generateFileTreeData) {
            const fileTreeData = window.generateFileTreeData();
            collectFilesFromTree(fileTreeData, allFiles);
        }
        
        return allFiles;
    }
    
    hashPayload(payload) {
        // Simple hash for change detection
        return JSON.stringify(payload);
    }
    
    setState(newState) {
        this.state = newState;
        
        switch (newState) {
            case 'hidden':
                if (this.panel) this.panel.style.display = 'none';
                break;
                
            case 'synced':
                if (this.panel) this.panel.style.display = 'flex';
                if (this.linkInput) {
                    this.linkInput.value = this.currentShareUrl || 'Add files to generate install link';
                    this.linkInput.classList.remove('opacity-50');
                    this.linkInput.disabled = false;
                }
                if (this.copyButton) {
                    this.copyButton.disabled = !this.currentShareUrl;
                    if (this.currentShareUrl) {
                        this.copyButton.classList.remove('opacity-50');
                    } else {
                        this.copyButton.classList.add('opacity-50');
                    }
                }
                break;
                
            case 'syncing':
                if (this.panel) this.panel.style.display = 'flex';
                if (this.linkInput) {
                    this.linkInput.classList.add('opacity-50');
                    this.linkInput.disabled = true;
                }
                if (this.copyButton) {
                    this.copyButton.disabled = true;
                    this.copyButton.classList.add('opacity-50');
                }
                break;
                
            case 'error':
                if (this.panel) this.panel.style.display = 'flex';
                // Keep last good link visible but indicate error somehow
                if (this.linkInput && this.currentShareUrl) {
                    this.linkInput.value = this.currentShareUrl;
                    this.linkInput.classList.remove('opacity-50');
                    this.linkInput.disabled = false;
                }
                if (this.copyButton && this.currentShareUrl) {
                    this.copyButton.disabled = false;
                    this.copyButton.classList.remove('opacity-50');
                }
                break;
        }
    }
    
    async copyLink() {
        if (!this.currentShareUrl) return;
        
        try {
            await navigator.clipboard.writeText(this.currentShareUrl);
            
            // Show feedback
            const originalText = this.copyButton.textContent;
            this.copyButton.textContent = 'Copied!';
            this.copyButton.classList.remove('bg-cyan-400');
            this.copyButton.classList.add('bg-green-400');
            
            setTimeout(() => {
                this.copyButton.textContent = originalText;
                this.copyButton.classList.remove('bg-green-400');
                this.copyButton.classList.add('bg-cyan-400');
            }, 2000);
        } catch (error) {
            console.error('Failed to copy:', error);
        }
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    // Wait a bit for workspace to be ready
    setTimeout(() => {
        window.autoShareManager = new AutoShareManager();
    }, 200);
});