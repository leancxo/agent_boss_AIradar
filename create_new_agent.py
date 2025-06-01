#!/usr/bin/env python3
"""
Agent Boss Template Creator

This script helps you create a new Agent Boss instance from the template.
It will copy the template files and help you configure them for your specific use case.
"""

import os
import shutil
import sys
from pathlib import Path

def create_new_agent_boss(project_name: str, email: str, target_dir: str = None):
    """Create a new Agent Boss instance"""
    
    if target_dir is None:
        target_dir = project_name
    
    # Create target directory
    target_path = Path(target_dir)
    if target_path.exists():
        print(f"❌ Directory {target_dir} already exists!")
        return False
    
    print(f"🚀 Creating new Agent Boss instance: {project_name}")
    print(f"📁 Target directory: {target_dir}")
    print(f"📧 Email: {email}")
    
    try:
        # Create directory structure
        target_path.mkdir(parents=True)
        
        # Copy template files
        template_files = [
            'agent_boss.py',
            'config.py',
            'requirements.txt',
            'README.md',
            'SETUP.md',
            'LICENSE',
            '.gitignore'
        ]
        
        template_dirs = [
            'tasks',
            'ai_platforms',
            'validators',
            'reports'
        ]
        
        # Copy files
        for file in template_files:
            if os.path.exists(file):
                shutil.copy2(file, target_path / file)
                print(f"✅ Copied {file}")
        
        # Copy directories
        for dir_name in template_dirs:
            if os.path.exists(dir_name):
                shutil.copytree(dir_name, target_path / dir_name)
                print(f"✅ Copied {dir_name}/")
        
        # Create .env file with user's email
        env_content = f"""# Agent Boss Environment Configuration
# Generated for: {project_name}

# Required: OpenAI API Key for GPT-4o model
OPENAI_API_KEY=your_openai_api_key_here

# Agent Boss Configuration
AGENT_BOSS_EMAIL={email}
AGENT_BOSS_TIMEOUT=300
AGENT_BOSS_MAX_RETRIES=3

# Optional: Additional AI platform keys
ANTHROPIC_API_KEY=your_anthropic_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
"""
        
        with open(target_path / '.env', 'w') as f:
            f.write(env_content)
        print(f"✅ Created .env with email: {email}")
        
        # Create project-specific README
        readme_content = f"""# {project_name} - Agent Boss Instance

This is a customized Agent Boss instance for {project_name}.

## Quick Start

1. **Install dependencies:**
```bash
pip install -r requirements.txt
playwright install
```

2. **Configure your OpenAI API key:**
```bash
# Edit .env file and add your OpenAI API key
nano .env
```

3. **Run your first task:**
```bash
python agent_boss.py --task "Create a hello world HTML page" --ai gemini --validate --test
```

## Configuration

- **Email:** {email}
- **Project:** {project_name}

## Customization

Edit `config.py` to modify settings for this specific Agent Boss instance.

See `SETUP.md` for detailed configuration options.
"""
        
        with open(target_path / 'PROJECT_README.md', 'w') as f:
            f.write(readme_content)
        print(f"✅ Created PROJECT_README.md")
        
        print(f"\n🎉 Successfully created Agent Boss instance: {project_name}")
        print(f"\n📋 Next steps:")
        print(f"1. cd {target_dir}")
        print(f"2. Edit .env and add your OpenAI API key")
        print(f"3. pip install -r requirements.txt")
        print(f"4. playwright install")
        print(f"5. python agent_boss.py --task 'your first task' --ai gemini --validate --test")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating Agent Boss instance: {str(e)}")
        return False

def main():
    """Main CLI interface"""
    print("🤖 Agent Boss Template Creator")
    print("=" * 40)
    
    if len(sys.argv) < 3:
        print("Usage: python create_new_agent.py <project_name> <email> [target_directory]")
        print("\nExample:")
        print("  python create_new_agent.py my-project user@example.com")
        print("  python create_new_agent.py my-project user@example.com /path/to/project")
        sys.exit(1)
    
    project_name = sys.argv[1]
    email = sys.argv[2]
    target_dir = sys.argv[3] if len(sys.argv) > 3 else None
    
    success = create_new_agent_boss(project_name, email, target_dir)
    
    if success:
        print("\n✨ Happy supervising! 🤖👔")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main() 