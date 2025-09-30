import asyncio
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from dotenv import load_dotenv

load_dotenv()

from browser_use import Agent, ChatGoogle

file_name = 'Juice-shop.txt'

# Check this one for security issues: https://github.com/juice-shop/juice-shop?tab=readme-ov-file
with open(f'../Instructions/{file_name}', 'r') as file:
	task_input = file.read().strip()

task = f"{task_input}"

agent = Agent(task=task, llm=ChatGoogle(model='gemini-2.5-flash'))


async def main():
	await agent.run()
	input('Press Enter to close the browser...')


if __name__ == '__main__':
	asyncio.run(main())