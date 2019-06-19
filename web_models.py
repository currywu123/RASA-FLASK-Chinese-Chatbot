import rasa
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
import asyncio
from rasa.utils.endpoints import EndpointConfig

model_dir = './models'
action_endpoint = EndpointConfig(url='http://localhost:5055/webhook')

agent = Agent.load(model_dir, action_endpoint = action_endpoint)

def handle_saying(saying):
	res = asyncio.run(agent.handle_text(saying))
	#print(res)
	#print(type(res))
	if res == []:
		return res
	else:
		return res[0]['text'] 