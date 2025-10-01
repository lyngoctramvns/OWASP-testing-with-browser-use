## Automation & OWASP Top 10 testing with Browser-use

Tools:
Browser-use: https://github.com/browser-use/browser-use

Websites tested on:
Sauce Lab Demo: https://www.saucedemo.com/
OWASP Juice Shop: https://github.com/juice-shop/juice-shop

### Setup
1. First, run Juice Shop from local computer
2. install browser-use and dotenv
3. Change file name in main.py to the instruction file which is in Instructions folder

### Environmental Variable

```bash
    GEMINI_API_KEY="YOUR GOOGLE API KEY"
    FILE_PATH="FILE PATH OF YOUR INSTRUCTIONS"
```

### Run Test
Run the program with:
```bash
    python main.py
```

**The outputs and results can be seen in result folder**