#!/usr/bin/env python3
"""Consolidate all action files into single YAML files per category"""

import yaml
from pathlib import Path
import json

def consolidate_agents():
    """Consolidate all agent YAML files into a single agents.yaml"""
    agents_dir = Path(__file__).parent / "app" / "actions" / "agents"
    agents_data = []
    
    # Read all YAML files
    for yaml_file in sorted(agents_dir.glob("*.yaml")):
        with open(yaml_file, 'r') as f:
            data = yaml.safe_load(f)
            agents_data.append(data)
    
    # Read remaining MD files that don't have YAML versions
    for md_file in sorted(agents_dir.glob("*.md")):
        yaml_file = agents_dir / f"{md_file.stem}.yaml"
        if not yaml_file.exists():
            with open(md_file, 'r') as f:
                content = f.read()
                slug = md_file.stem
                display_name = slug.replace('-', ' ').title()
                agents_data.append({
                    'display_name': display_name,
                    'slug': slug,
                    'content': content
                })
    
    # Write consolidated file
    output_file = Path(__file__).parent / "app" / "actions" / "agents.yaml"
    with open(output_file, 'w') as f:
        yaml.dump({'agents': agents_data}, f, default_flow_style=False, 
                  allow_unicode=True, sort_keys=False)
    
    print(f"Consolidated {len(agents_data)} agents into agents.yaml")
    return len(agents_data)

def consolidate_rules():
    """Consolidate all rule YAML files into a single rules.yaml"""
    rules_dir = Path(__file__).parent / "app" / "actions" / "rules"
    rules_data = []
    
    # Read all YAML files
    for yaml_file in sorted(rules_dir.glob("*.yaml")):
        with open(yaml_file, 'r') as f:
            data = yaml.safe_load(f)
            rules_data.append(data)
    
    # Read remaining MD files that don't have YAML versions
    for md_file in sorted(rules_dir.glob("*.md")):
        yaml_file = rules_dir / f"{md_file.stem}.yaml"
        if not yaml_file.exists():
            with open(md_file, 'r') as f:
                content = f.read()
                slug = md_file.stem
                display_name = slug.replace('-', ' ').title()
                rules_data.append({
                    'display_name': display_name,
                    'slug': slug,
                    'content': content
                })
    
    # Write consolidated file
    output_file = Path(__file__).parent / "app" / "actions" / "rules.yaml"
    with open(output_file, 'w') as f:
        yaml.dump({'rules': rules_data}, f, default_flow_style=False, 
                  allow_unicode=True, sort_keys=False)
    
    print(f"Consolidated {len(rules_data)} rules into rules.yaml")
    return len(rules_data)

def consolidate_mcps():
    """Convert mcps.json to mcps.yaml with consistent structure"""
    mcps_file = Path(__file__).parent / "app" / "actions" / "mcps.json"
    
    if mcps_file.exists():
        with open(mcps_file, 'r') as f:
            mcps_json = json.load(f)
        
        # Transform to list format with display_name and slug
        mcps_data = []
        for name, config in mcps_json.items():
            mcps_data.append({
                'display_name': name.replace('-', ' ').title(),
                'slug': name,
                'config': config
            })
        
        # Write consolidated file
        output_file = Path(__file__).parent / "app" / "actions" / "mcps.yaml"
        with open(output_file, 'w') as f:
            yaml.dump({'mcps': mcps_data}, f, default_flow_style=False, 
                      allow_unicode=True, sort_keys=False)
        
        print(f"Consolidated {len(mcps_data)} MCPs into mcps.yaml")
        return len(mcps_data)
    return 0

def main():
    """Consolidate all actions into category files"""
    print("Starting consolidation...")
    
    agents_count = consolidate_agents()
    rules_count = consolidate_rules()
    mcps_count = consolidate_mcps()
    
    print(f"\nConsolidation complete!")
    print(f"Total: {agents_count} agents, {rules_count} rules, {mcps_count} MCPs")
    print("\nCreated files:")
    print("  - app/actions/agents.yaml")
    print("  - app/actions/rules.yaml")
    print("  - app/actions/mcps.yaml")
    print("\nNote: Original files have been preserved.")
    print("You can delete the individual files once the new system is verified.")

if __name__ == "__main__":
    main()