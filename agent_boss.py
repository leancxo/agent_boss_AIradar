"""
Agent Boss - AI Development Tool Supervisor

This is the main controller that manages and supervises AI development tools
to ensure they complete tasks correctly and efficiently.
"""

from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
import logging
import json
from datetime import datetime
from typing import Dict, List, Optional, Any
import argparse
from config import AgentBossConfig, DEFAULT_CONFIG

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(
    level=getattr(logging, AgentBossConfig.LOG_LEVEL),
    format=AgentBossConfig.LOG_FORMAT
)
logger = logging.getLogger(__name__)

class TaskResult:
    """Represents the result of a task execution"""
    def __init__(self, success: bool, message: str, output: Any = None, errors: List[str] = None):
        self.success = success
        self.message = message
        self.output = output
        self.errors = errors or []
        self.timestamp = datetime.now()

class AgentBoss:
    """
    The main Agent Boss class that supervises AI development tools
    """
    
    def __init__(self, config: Dict = None):
        # Validate configuration
        AgentBossConfig.validate_config()
        
        self.config = config or DEFAULT_CONFIG
        self.llm = ChatOpenAI(
            model=self.config.get('model', AgentBossConfig.LLM_MODEL),
            temperature=self.config.get('temperature', AgentBossConfig.LLM_TEMPERATURE)
        )
        self.task_history = []
        
        logger.info(f"🤖 Agent Boss initialized with model: {self.llm.model_name}")
        
    async def assign_task(self, ai_platform: str, task: str, validate: bool = True, test: bool = True) -> TaskResult:
        """
        Assign a task to a specific AI platform and supervise its completion
        
        Args:
            ai_platform: The AI platform to use (e.g., 'gemini', 'chatgpt')
            task: The task description
            validate: Whether to validate the output
            test: Whether to test the generated code
            
        Returns:
            TaskResult: The result of the task execution
        """
        logger.info(f"🎯 Agent Boss assigning task to {ai_platform}: {task}")
        
        try:
            if ai_platform.lower() == 'gemini':
                result = await self._execute_gemini_task(task, validate, test)
            elif ai_platform.lower() == 'chatgpt':
                result = await self._execute_chatgpt_task(task, validate, test)
            else:
                result = TaskResult(False, f"Unsupported AI platform: {ai_platform}")
            
            self.task_history.append({
                'platform': ai_platform,
                'task': task,
                'result': result,
                'timestamp': datetime.now()
            })
            
            # Save report if enabled
            if AgentBossConfig.SAVE_REPORTS:
                self._save_task_report(ai_platform, task, result)
            
            return result
            
        except Exception as e:
            logger.error(f"❌ Error executing task: {str(e)}")
            return TaskResult(False, f"Task execution failed: {str(e)}", errors=[str(e)])
    
    async def _execute_gemini_task(self, task: str, validate: bool, test: bool) -> TaskResult:
        """Execute a task using Google Gemini"""
        
        # Create the browser automation task using configured email
        browser_task = f"""1. Open a new browser window
2. Navigate to https://gemini.google.com
3. Wait for the page to fully load
4. Look for a 'Sign In' or 'Get started' button and click it
5. Wait for the Google login page to load
6. Enter the email address: {AgentBossConfig.GEMINI_EMAIL}
7. Click 'Next' or submit the email
8. Complete the login process (handle any verification steps)
9. Once logged into Gemini, find the chat input area
10. Type this message: "{task}"
11. Send the message and wait for Gemini's response
12. Wait for the complete response to be generated"""
        
        if validate and test:
            browser_task += """
13. If the response contains code, copy the code
14. Open a new tab and test the code to ensure it works
15. If the code works, go back to Gemini and send: "✅ Agent Boss: Task completed successfully. Code tested and validated."
16. If the code doesn't work, send: "❌ Agent Boss: Code has issues. Please fix and provide working code."
17. Wait for any fixes and retest if needed
18. Close the browser once task is confirmed complete"""
        else:
            browser_task += """
13. Send a follow-up message: "✅ Agent Boss: Task received and completed."
14. Close the browser"""
        
        try:
            agent = Agent(
                task=browser_task,
                llm=self.llm
            )
            
            logger.info("🤖 Agent Boss supervising Gemini task execution...")
            await agent.run()
            
            return TaskResult(True, "Task completed successfully via Gemini")
            
        except Exception as e:
            logger.error(f"❌ Gemini task execution failed: {str(e)}")
            return TaskResult(False, f"Gemini task failed: {str(e)}", errors=[str(e)])
    
    async def _execute_chatgpt_task(self, task: str, validate: bool, test: bool) -> TaskResult:
        """Execute a task using ChatGPT (placeholder for future implementation)"""
        return TaskResult(False, "ChatGPT integration not yet implemented")
    
    def create_workflow(self, steps: List[Dict]) -> Dict:
        """Create a multi-step workflow"""
        return {
            'id': f"workflow_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            'steps': steps,
            'created_at': datetime.now()
        }
    
    async def execute_workflow(self, workflow: Dict) -> List[TaskResult]:
        """Execute a multi-step workflow"""
        logger.info(f"🔄 Agent Boss executing workflow: {workflow['id']}")
        results = []
        
        for i, step in enumerate(workflow['steps']):
            logger.info(f"📋 Executing step {i+1}/{len(workflow['steps'])}")
            
            if 'ai' in step and 'task' in step:
                result = await self.assign_task(
                    ai_platform=step['ai'],
                    task=step['task'],
                    validate=step.get('validate', False),
                    test=step.get('test', False)
                )
                results.append(result)
                
                if not result.success:
                    logger.error(f"❌ Workflow step {i+1} failed, stopping execution")
                    break
            
        return results
    
    def generate_report(self) -> Dict:
        """Generate a report of all completed tasks"""
        successful_tasks = [t for t in self.task_history if t['result'].success]
        failed_tasks = [t for t in self.task_history if not t['result'].success]
        
        return {
            'total_tasks': len(self.task_history),
            'successful_tasks': len(successful_tasks),
            'failed_tasks': len(failed_tasks),
            'success_rate': len(successful_tasks) / len(self.task_history) if self.task_history else 0,
            'task_history': self.task_history,
            'config': {
                'email': AgentBossConfig.GEMINI_EMAIL,
                'model': self.llm.model_name,
                'validation_enabled': AgentBossConfig.ENABLE_CODE_VALIDATION,
                'testing_enabled': AgentBossConfig.ENABLE_CODE_TESTING
            }
        }
    
    def _save_task_report(self, platform: str, task: str, result: TaskResult):
        """Save individual task report to file"""
        import os
        
        # Create reports directory if it doesn't exist
        os.makedirs(AgentBossConfig.REPORTS_DIR, exist_ok=True)
        
        # Generate report filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{AgentBossConfig.REPORTS_DIR}/task_{platform}_{timestamp}.json"
        
        # Create report data
        report_data = {
            'platform': platform,
            'task': task,
            'success': result.success,
            'message': result.message,
            'errors': result.errors,
            'timestamp': result.timestamp.isoformat(),
            'config': {
                'email': AgentBossConfig.GEMINI_EMAIL,
                'model': self.llm.model_name
            }
        }
        
        # Save to file
        try:
            with open(filename, 'w') as f:
                json.dump(report_data, f, indent=2, default=str)
            logger.info(f"📄 Task report saved to: {filename}")
        except Exception as e:
            logger.warning(f"⚠️ Failed to save task report: {str(e)}")

async def main():
    """Main CLI interface for Agent Boss"""
    parser = argparse.ArgumentParser(description='Agent Boss - AI Development Tool Supervisor')
    parser.add_argument('--task', required=True, help='The task to assign to the AI')
    parser.add_argument('--ai', default='gemini', choices=['gemini', 'chatgpt'], help='AI platform to use')
    parser.add_argument('--validate', action='store_true', help='Validate the output')
    parser.add_argument('--test', action='store_true', help='Test the generated code')
    parser.add_argument('--report', action='store_true', help='Generate a report after completion')
    parser.add_argument('--config', help='Path to custom config file')
    
    args = parser.parse_args()
    
    # Initialize Agent Boss
    boss = AgentBoss()
    
    # Execute the task
    logger.info("🚀 Agent Boss starting up...")
    logger.info(f"📧 Using email: {AgentBossConfig.GEMINI_EMAIL}")
    
    result = await boss.assign_task(
        ai_platform=args.ai,
        task=args.task,
        validate=args.validate,
        test=args.test
    )
    
    # Print results
    if result.success:
        logger.info(f"✅ Task completed successfully: {result.message}")
    else:
        logger.error(f"❌ Task failed: {result.message}")
        if result.errors:
            for error in result.errors:
                logger.error(f"   Error: {error}")
    
    # Generate report if requested
    if args.report:
        report = boss.generate_report()
        logger.info(f"📊 Report: {json.dumps(report, indent=2, default=str)}")

if __name__ == "__main__":
    asyncio.run(main()) 