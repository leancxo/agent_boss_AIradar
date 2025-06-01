"""
Code Generation Task Templates for Agent Boss

This module contains predefined task templates for common code generation requests.
"""

class CodeGenerationTasks:
    """Predefined code generation tasks"""
    
    @staticmethod
    def web_app(app_type: str, features: list = None) -> str:
        """Generate a web application"""
        features_str = ", ".join(features) if features else "basic functionality"
        return f"""Create a complete {app_type} web application with {features_str}. 
        Include HTML, CSS, and JavaScript. Make it responsive and modern-looking. 
        Ensure all functionality works properly and add comments to explain the code."""
    
    @staticmethod
    def game(game_type: str, difficulty: str = "medium") -> str:
        """Generate a game"""
        return f"""Create a complete {game_type} game in HTML, CSS, and JavaScript. 
        Difficulty level: {difficulty}. Include game logic, scoring, win/lose conditions, 
        and a reset function. Make it visually appealing and user-friendly."""
    
    @staticmethod
    def utility_script(language: str, purpose: str) -> str:
        """Generate a utility script"""
        return f"""Create a {language} script that {purpose}. 
        Include proper error handling, comments, and documentation. 
        Make it production-ready with input validation."""
    
    @staticmethod
    def api_integration(service: str, functionality: str) -> str:
        """Generate API integration code"""
        return f"""Create code to integrate with {service} API for {functionality}. 
        Include proper authentication, error handling, and response parsing. 
        Provide examples of usage and handle rate limiting."""
    
    @staticmethod
    def data_processor(input_format: str, output_format: str, processing: str) -> str:
        """Generate data processing code"""
        return f"""Create a data processor that takes {input_format} input, 
        performs {processing}, and outputs {output_format}. 
        Include validation, error handling, and progress tracking."""

# Common task examples
COMMON_TASKS = {
    "tic_tac_toe": CodeGenerationTasks.game("tic-tac-toe", "easy"),
    "calculator": CodeGenerationTasks.web_app("calculator", ["basic arithmetic", "memory functions", "history"]),
    "todo_app": CodeGenerationTasks.web_app("todo list", ["add/remove tasks", "mark complete", "local storage"]),
    "weather_app": CodeGenerationTasks.api_integration("weather", "current weather and forecast display"),
    "file_organizer": CodeGenerationTasks.utility_script("Python", "organizes files by type and date"),
    "password_generator": CodeGenerationTasks.web_app("password generator", ["customizable length", "character sets", "strength indicator"]),
    "quiz_game": CodeGenerationTasks.game("quiz", "medium"),
    "expense_tracker": CodeGenerationTasks.web_app("expense tracker", ["add expenses", "categories", "monthly reports"]),
    "url_shortener": CodeGenerationTasks.web_app("URL shortener", ["shorten URLs", "click tracking", "custom aliases"]),
    "markdown_converter": CodeGenerationTasks.data_processor("Markdown", "HTML", "markdown to HTML conversion")
} 