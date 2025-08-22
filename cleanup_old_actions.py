#!/usr/bin/env python3
"""Clean up old individual action files after consolidation"""

from pathlib import Path
import shutil

def cleanup_old_files():
    """Remove old individual action files"""
    actions_dir = Path(__file__).parent / "app" / "actions"
    
    # Remove agents and rules directories
    agents_dir = actions_dir / "agents"
    rules_dir = actions_dir / "rules"
    
    removed_count = 0
    
    if agents_dir.exists():
        file_count = len(list(agents_dir.glob("*")))
        print(f"Removing agents directory with {file_count} files...")
        shutil.rmtree(agents_dir)
        removed_count += file_count
    
    if rules_dir.exists():
        file_count = len(list(rules_dir.glob("*")))
        print(f"Removing rules directory with {file_count} files...")
        shutil.rmtree(rules_dir)
        removed_count += file_count
    
    # Remove old mcps.json
    mcps_json = actions_dir / "mcps.json"
    if mcps_json.exists():
        print("Removing mcps.json...")
        mcps_json.unlink()
        removed_count += 1
    
    print(f"\nCleanup complete! Removed {removed_count} files/directories.")
    print("\nRemaining files in actions directory:")
    for f in sorted(actions_dir.glob("*.yaml")):
        print(f"  - {f.name}")

if __name__ == "__main__":
    response = input("This will remove all old individual action files. Continue? (y/n): ")
    if response.lower() == 'y':
        cleanup_old_files()
    else:
        print("Cleanup cancelled.")