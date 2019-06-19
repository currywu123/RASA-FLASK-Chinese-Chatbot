# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormAction
from rasa_sdk.events import UserUtteranceReverted

import time
import codecs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import numpy as np
import urllib.request
import gzip
import json

driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

def getInfoBox(spotname):
	try:
		 
		driver.get("http://baike.baidu.com/")
		elem_input = driver.find_element_by_xpath("//form[@id='searchForm']/input")
		time.sleep(2)
		
		elem_input.send_keys(spotname)
		elem_input.send_keys(Keys.RETURN)
		
		elem_value = driver.find_elements_by_xpath("//div[@class='lemma-summary']/div")
		values = []
		for value in elem_value:
			values.append(value.text.strip('\n'))
		result = ' '.join(values)
		time.sleep(2)
		return result

	except Exception as e:  
		print ("Error: ", e)
		return []
	finally:
		pass
'''
def get_weather(cityname):
	url = 'http://wthrcdn.etouch.cn/weather_mini?city='+urllib.parse.quote(cityname)
	weather_data = urllib.request.urlopen(url).read()
	weather_data = gzip.decompress(weather_data).decode('utf-8')
	weather_dict = json.loads(weather_data)
	if weather_dict.get('desc') == 'invilad-citykey':
		return None
	elif weather_dict.get('desc') =='OK' :
		forecast = weather_dict.get('data').get('forecast')
		result = []
		for i in range(7):
			result.append('日期：'+forecast[1].get('date')+'\n' \
				   +'天气：'+forecast[1].get('type')+'\n'\
				   +'高温：'+forecast[1].get('high')+'\n'\
				   +'低温：'+forecast[1].get('low')+'\n'\
				   +'风向：'+forecast[1].get('fengxiang')+'\n'\
				   +'风力：'+forecast[1].get('fengli')+'\n')
		return result
'''
class ProvideSpots(Action):

	def name(self) -> Text:
		return 'action_provide_spots'

	def run(self, dispatcher:CollectingDispatcher, tracker: Tracker, domain:Dict[Text, Any]) -> List:
		buttons = []
		province = tracker.get_slot('province')
		if province==None:
			dispatcher.utter_message("请主人告诉我想查看的省份哦")
		else:
			spots = []
			#buttons = []
			with codecs.open('./data/5A_province/'+ province + '.txt', 'r', encoding = 'utf-8') as f:
				for line in f.readlines():
					if line != '\n':
						spot = line.rstrip('\n')
						spots.append(spot)
						#payload = "/inform{\"spot\":\"" + spot + "\"}"
						#buttons.append({"title": "{}".format(spot), "payload": payload})
				spots = "\n".join(spots)
				text = "{}的5A级旅游景点主要有\n{}".format(province, spots)
				#dispatcher.utter_button_message(text, buttons)
				dispatcher.utter_message(text)
		return []


class IntroduceSpots(Action):
	def name(self) -> Text:
		return 'action_introduce_spots'

	def run(self, dispatcher:CollectingDispatcher, tracker:Tracker, domain:Dict[Text, Any]) -> List[Dict]:
		spot = tracker.get_slot('spot')
		if spot==None:
			dispatcher.utter_message("请主人告诉我要查询的景点名称哦")
		else:
			result = getInfoBox(spot)
			if len(result)>0:
				dispatcher.utter_message(result)
			else:
				dispatcher.utter_message('对不起，笨笨找不到{}的介绍'.format(spot))

		return []


class IntroduceFood(Action):
	def name(self) -> Text:
		return "action_introduce_food"

	def run(self, dispatcher:CollectingDispatcher, tracker:Tracker, domain:Dict[Text, Any]) -> List:
		province = tracker.get_slot('province')
		if province==None:
			dispatcher.utter_message("主人要告诉我想要查询的省份哦")
		else:
			df = pd.read_excel('./data/food.xlsx')
			food = df[df['province']==province]['food'].tolist()
			kind = len(food)
			if kind==0:
				dispatcher.utter_message('对不起主人，笨笨暂时还不知道{}有哪些好吃的'.format(province))
			else:
				if kind > 5:
					#select_food = np.random.choice(food, 5).tolist()
					select_food = food[:5]
				else:
					select_food = food
				dispatcher.utter_message("{}的特色美食主要有\n{}".format(province, '\n'.join(select_food)))
		return []

'''
class ReportWeather(Action):
	def name(self) -> Text:
		return 'action_report_weather'

	def run(self, dispatcher:CollectingDispatcher, tracker: Tracker, domain:Dict[Text, Any]) -> List:
		city = input('主人请输入你想要查询的城市：\n') # 这个是在action端输出 不能返回robot界面
		if city ==None:
			dispatcher.utter_message("主人要告诉我查询的城市哦")
		else:
			result = get_weather(city)
			if result == None:
				dispatcher.utter_message('输入的城市名有误，主人请验证后重新输入哦')
			else:
				dispatcher.utter_message('{}最近一星期的天气如下：\n{}'.format(city, '\n'.join(result)))

		return []
'''
'''
class FacilityForm(FormAction):

	def name(self) -> Text:
		return 'facility_form'

	@staticmethod:
	def required_slots(tracker:Tracker) -> List[Text]:
		return ['province', 'spot']

	def slot_mappings(self) -> Dict[Text, Any]:
		return {'province': self.from_entity(entity='province', intent=['inform']),
				'spot': self.from_entity(entity='spot', intent=['introduce'])}

	def submit(self, dispatcher:CollectingDispatcher, tracker:Tracker, domain:Dict[Text, Any]) -> List[Dict]:
		province = tracker.get_slot('province')
		spot = tracker.get_slot('spot')

'''
class ActionUnknown(Action):
	def name(self) -> Text:
		return 'action_unknown'
	def run(self, dispatcher:CollectingDispatcher, tracker:Tracker, domain:Dict[Text, Any]) -> List:
		dispatcher.utter_template('utter_unknown', tracker)
		return [UserUtteranceReverted()]


class ActionIcando(Action):
	def name(self) -> Text:
		return 'action_icando'
	def run(self, dispatcher:CollectingDispatcher, tracker:Tracker, domain:Dict[Text, Any]) -> List:
		dispatcher.utter_template('utter_icando', tracker)
		return [UserUtteranceReverted()]

class ActionSad(Action):
	def name(self) -> Text:
		return 'action_sad'
	def run(self, dispatcher:CollectingDispatcher, tracker:Tracker, domain:Dict[Text, Any]) -> List:
		dispatcher.utter_template('utter_sad', tracker)
		return [UserUtteranceReverted()]


class ActionFallback(Action):
	def name(self) -> Text:
		return 'action_my_fallback'
	def run(self, dispatcher:CollectingDispatcher, tracker:Tracker, domain:Dict[Text, Any]) -> List:
		dispatcher.utter_message('笨笨没有听懂，麻烦主人重新表述一遍')
		return []


class ActionNoworries(Action):
	def name(self) -> Text:
		return 'action_noworries'
	def run(self, dispatcher:CollectingDispatcher, tracker:Tracker, domain:Dict[Text, Any]) -> List:
		dispatcher.utter_template('utter_noworries', tracker)
		return [UserUtteranceReverted()]

class ActionChat(Action):
	def name(self) -> Text:
		return 'action_chat'
	def run(self, dispatcher:CollectingDispatcher, tracker:Tracker, domain:Dict[Text, Any]) -> List:
		dispatcher.utter_template('utter_chat', tracker)
		return [UserUtteranceReverted()]




