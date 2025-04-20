# Browser Automation Examples

This repository contains examples of browser automation using Playwright and Python. The examples demonstrate how to automate common web tasks with human-like behavior to avoid bot detection.

## Current Examples

### Grocery Shopping Automation
Demonstrates automated grocery shopping with features like:
- Human-like typing and delays
- Bot detection avoidance
- Error handling
- Progress tracking

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/browser-automation-examples.git
cd browser-automation-examples
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Playwright browsers:
```bash
playwright install chromium
```

## Usage

Run the grocery shopping example:
```bash
python grocery_shopping.py
```

## Features

- Random delays between actions to simulate human behavior
- Stealth browser settings to avoid bot detection
- Configurable item lists
- Progress tracking and error handling
- Visible browser automation for debugging

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 