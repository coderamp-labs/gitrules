#!/usr/bin/env python3
"""Convert existing .md action files to .yaml format with metadata"""

import yaml
from pathlib import Path
import re

def convert_md_to_yaml(md_file_path: Path, output_dir: Path):
    """Convert a single MD file to YAML format"""
    
    # Read the MD content
    with open(md_file_path, 'r') as f:
        content = f.read()
    
    # Generate display name and slug from filename
    slug = md_file_path.stem
    display_name = slug.replace('-', ' ').title()
    
    # Special handling for agents with frontmatter
    if '---' in content and content.startswith('---'):
        # Extract frontmatter if it exists
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1])
                # Use name from frontmatter if available
                if 'name' in frontmatter:
                    slug = frontmatter['name']
                    display_name = slug.replace('-', ' ').title()
            except:
                pass  # If frontmatter parsing fails, use defaults
    
    # Create YAML structure
    yaml_data = {
        'display_name': display_name,
        'slug': slug,
        'content': content
    }
    
    # Write YAML file
    yaml_file_path = output_dir / f"{md_file_path.stem}.yaml"
    with open(yaml_file_path, 'w') as f:
        yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    print(f"Converted: {md_file_path.name} -> {yaml_file_path.name}")
    return yaml_file_path

def main():
    """Convert all MD files in actions directory to YAML format"""
    
    actions_dir = Path(__file__).parent / "app" / "actions"
    
    # Convert agents
    agents_dir = actions_dir / "agents"
    if agents_dir.exists():
        print("\nConverting agents...")
        for md_file in agents_dir.glob("*.md"):
            # Skip if YAML already exists
            yaml_file = agents_dir / f"{md_file.stem}.yaml"
            if not yaml_file.exists():
                convert_md_to_yaml(md_file, agents_dir)
            else:
                print(f"Skipping {md_file.name} - YAML already exists")
    
    # Convert rules
    rules_dir = actions_dir / "rules"
    if rules_dir.exists():
        print("\nConverting rules...")
        for md_file in rules_dir.glob("*.md"):
            # Skip if YAML already exists
            yaml_file = rules_dir / f"{md_file.stem}.yaml"
            if not yaml_file.exists():
                convert_md_to_yaml(md_file, rules_dir)
            else:
                print(f"Skipping {md_file.name} - YAML already exists")
    
    print("\nConversion complete!")
    print("\nNote: The original .md files have been preserved.")
    print("The backend will prioritize .yaml files when both exist.")
    print("You can safely delete the .md files once you've verified the conversion.")

if __name__ == "__main__":
    main()