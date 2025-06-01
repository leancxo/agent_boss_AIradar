"""
Agent Boss Configuration

This file contains all configurable settings for Agent Boss.
Modify these settings to customize your Agent Boss instance.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class AgentBossConfig:
    """Configuration settings for Agent Boss"""
    
    # Email for Gemini login (CHANGE THIS FOR NEW INSTANCES)
    GEMINI_EMAIL = os.getenv('AGENT_BOSS_EMAIL', 'pkp121@gmail.com')
    
    # LLM Configuration
    LLM_MODEL = os.getenv('LLM_MODEL', 'gpt-4o')
    LLM_TEMPERATURE = float(os.getenv('LLM_TEMPERATURE', '0.1'))
    
    # Task Execution Settings
    MAX_RETRIES = int(os.getenv('AGENT_BOSS_MAX_RETRIES', '3'))
    TASK_TIMEOUT = int(os.getenv('AGENT_BOSS_TIMEOUT', '300'))  # seconds
    
    # Browser Settings
    BROWSER_HEADLESS = os.getenv('BROWSER_HEADLESS', 'false').lower() == 'true'
    BROWSER_TIMEOUT = int(os.getenv('BROWSER_TIMEOUT', '30000'))  # milliseconds
    
    # Validation Settings
    ENABLE_CODE_VALIDATION = os.getenv('ENABLE_CODE_VALIDATION', 'true').lower() == 'true'
    ENABLE_CODE_TESTING = os.getenv('ENABLE_CODE_TESTING', 'true').lower() == 'true'
    
    # Logging Configuration
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    # Report Settings
    SAVE_REPORTS = os.getenv('SAVE_REPORTS', 'true').lower() == 'true'
    REPORTS_DIR = os.getenv('REPORTS_DIR', 'reports')
    
    @classmethod
    def get_llm_config(cls):
        """Get LLM configuration dictionary"""
        return {
            'model': cls.LLM_MODEL,
            'temperature': cls.LLM_TEMPERATURE
        }
    
    @classmethod
    def get_task_config(cls):
        """Get task execution configuration"""
        return {
            'max_retries': cls.MAX_RETRIES,
            'timeout': cls.TASK_TIMEOUT,
            'validate': cls.ENABLE_CODE_VALIDATION,
            'test': cls.ENABLE_CODE_TESTING
        }
    
    @classmethod
    def validate_config(cls):
        """Validate configuration settings"""
        required_env_vars = ['OPENAI_API_KEY']
        missing_vars = []
        
        for var in required_env_vars:
            if not os.getenv(var):
                missing_vars.append(var)
        
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
        
        return True

# Quick access to common configurations
DEFAULT_CONFIG = AgentBossConfig.get_llm_config()
TASK_CONFIG = AgentBossConfig.get_task_config() 