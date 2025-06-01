# Agent Boss Setup Guide

This guide will help you set up a new Agent Boss instance for supervising AI development tools.

## 🚀 Quick Start

### 1. Clone or Download Template
```bash
# If using as a template, create a new directory
mkdir my-agent-boss
cd my-agent-boss

# Copy all files from this template
```

### 2. Environment Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

### 3. Configure Environment Variables
```bash
# Copy the environment template
cp .env.example .env

# Edit .env with your API keys
nano .env  # or use your preferred editor
```

Required environment variables:
```bash
# OpenAI API Key (required for GPT-4o model)
OPENAI_API_KEY=your_openai_api_key_here

# Optional: Other AI platform keys for future integrations
ANTHROPIC_API_KEY=your_anthropic_key_here
GOOGLE_API_KEY=your_google_key_here
```

### 4. Test Your Setup
```bash
# Run a simple test task
python agent_boss.py --task "Create a simple hello world HTML page" --ai gemini --validate --test
```

## 🔧 Configuration Options

### Agent Boss Configuration
You can customize Agent Boss behavior by modifying the config in `agent_boss.py`:

```python
boss = AgentBoss({
    'model': 'gpt-4o',           # LLM model to use
    'temperature': 0.1,          # Response creativity (0.0-1.0)
    'max_retries': 3,           # Max retry attempts
    'timeout': 300,             # Task timeout in seconds
})
```

### Email Configuration
Update the email address in `agent_boss.py` for Gemini login:
```python
# Line ~77 in agent_boss.py
6. Enter the email address: YOUR_EMAIL@gmail.com
```

## 📁 Project Structure Explained

```
agent-boss/
├── agent_boss.py          # Main controller - START HERE
├── tasks/                 # Task templates and definitions
│   └── code_generation.py # Pre-built task templates
├── ai_platforms/          # Future: AI platform integrations
├── validators/            # Future: Code validation modules
├── reports/              # Generated task reports
├── .env.example          # Environment variables template
├── requirements.txt      # Python dependencies
├── SETUP.md             # This setup guide
└── README.md            # Project documentation
```

## 🎯 Usage Examples

### Basic Task Assignment
```bash
python agent_boss.py --task "Create a tic-tac-toe game" --ai gemini --validate --test
```

### Using Pre-built Templates
```python
from tasks.code_generation import COMMON_TASKS

# Use a pre-built task
task = COMMON_TASKS["calculator"]
python agent_boss.py --task "$task" --ai gemini --validate --test
```

### Custom Task Creation
```python
from agent_boss import AgentBoss

boss = AgentBoss()
result = await boss.assign_task(
    ai_platform="gemini",
    task="Create a weather app with API integration",
    validate=True,
    test=True
)
```

## 🔄 Creating New Agent Boss Instances

### For New Projects
1. Copy this entire directory
2. Update the email in `agent_boss.py`
3. Modify task templates in `tasks/`
4. Add your API keys to `.env`
5. Customize configuration as needed

### For Team Use
1. Create a shared template repository
2. Each team member clones and configures
3. Share task templates via the `tasks/` directory
4. Use version control for task definitions

## 🛠️ Customization

### Adding New Task Types
1. Edit `tasks/code_generation.py`
2. Add new methods to `CodeGenerationTasks`
3. Update `COMMON_TASKS` dictionary

### Adding New AI Platforms
1. Create new file in `ai_platforms/`
2. Implement platform-specific logic
3. Update `agent_boss.py` to support new platform

### Custom Validation
1. Create validators in `validators/`
2. Integrate with task execution flow
3. Add validation rules as needed

## 🐛 Troubleshooting

### Common Issues
1. **Browser not opening**: Check Playwright installation
2. **Login failures**: Verify email/credentials
3. **API errors**: Check API keys in `.env`
4. **Task timeouts**: Increase timeout in config

### Debug Mode
```bash
# Run with verbose logging
python agent_boss.py --task "your task" --ai gemini --validate --test --debug
```

## 📊 Monitoring and Reports

Agent Boss automatically generates reports. Access them via:
```bash
python agent_boss.py --task "your task" --ai gemini --report
```

Reports include:
- Task success/failure rates
- Execution times
- Error logs
- Performance metrics

## 🔒 Security Notes

- Keep API keys secure in `.env` files
- Don't commit `.env` to version control
- Use environment-specific configurations
- Regularly rotate API keys

## 🚀 Next Steps

1. Run your first task
2. Explore pre-built templates
3. Create custom task definitions
4. Set up monitoring and reporting
5. Scale to multiple AI platforms

Happy supervising! 🤖👔 