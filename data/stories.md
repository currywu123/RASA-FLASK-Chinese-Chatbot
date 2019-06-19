## happy path 1
* greet
  - utter_greet
* inform
  - utter_ask
* recommend_spot
  - action_provide_spots
* introduce_spot
  - action_introduce_spots
  - slot{"spot": null}
* introduce_food
  - action_introduce_food
* thankyou
  - action_noworries
* oppo:
  - utter_oppo
* goodbye
  - utter_goodbye

## happy path 2
* inform
  - utter_ask
* introduce_spot
  - action_introduce_spots
  - slot{"spot": null}
* thankyou
  - action_noworries
* goodbye
  - utter_goodbye

## happy path 3
* inform
  - utter_ask
* introduce_spot
  - action_introduce_spots
  - slot{"spot": null}
* introduce_food
  - action_introduce_food
* goodbye
  - utter_goodbye

## happy path 4
* greet
  - utter_greet
* inform
  - utter_ask
* introduce_spot
  - action_introduce_spots
  - slot{"spot": null}
* introduce_food
  - action_introduce_food
* thankyou
  - action_noworries
* goodbye
  - utter_goodbye

## sad path 1
* greet
  - utter_greet
* inform
  - utter_ask
* recommend_spot
  - action_provide_spots
* introduce_spot
  - action_introduce_spots
  - slot{"spot": null}
* introduce_food
  - action_introduce_food
* insult
  - action_sad

## sad path 2
* greet
  - utter_greet
* inform
  - utter_ask
* recommend_spot
  - action_provide_spots
* insult
  - action_sad

## sad path 3
* greet
  - utter_greet
* introduce_spot
  - action_introduce_spots
  - slot{"spot": null}
* insult
  - action_sad
* whatcanyoudo
  - action_icando

## greet
* greet
  - utter_greet

## goodbye
* goodbye
  - utter_goodbye

## inform
* inform
  - utter_ask

## inform + introduce
* inform
  - utter_ask
* introduce_spot
  - action_introduce_spots
  - slot{"spot": null}

## inform + introduce_food
* inform
  - utter_ask
* introduce_food
  - action_introduce_food

## inform + providing_spot
* inform
  - utter_ask
* recommend_spot
  - action_provide_spots

## Generated Story 7266279435303393504
* greet
    - utter_greet
* inform{"province": "天津"}
    - slot{"province": "天津"}
    - utter_ask
* insult
    - action_sad
* thankyou
    - action_noworries
* insult
    - action_sad
    - rewind
* whatcanyoudo
    - action_icando
    - rewind
* unknown
    - action_unknown
* insult
    - action_sad
    - rewind
* whatcanyoudo
    - action_icando
    - rewind
* whatcanyoudo
    - action_icando
    - rewind
* recommend_spot
    - action_provide_spots
* introduce_spot{"spot": "天津古文化街"}
    - slot{"spot": "天津古文化街"}
    - action_introduce_spots
    - slot{"spot": null}
* inform{"province": "北京"}
    - slot{"province": "北京"}
    - utter_ask
* recommend_spot
    - action_provide_spots
* inform{"province": "北京"}
    - slot{"province": "北京"}
    - utter_ask
* recommend_spot
    - action_provide_spots

## Generated Story 8535577808949347764
* greet
    - utter_greet
* inform{"province": "广东"}
    - slot{"province": "广东"}
    - utter_ask
* recommend_spot
    - action_provide_spots
* introduce_spot{"spot": "罗浮山"}
    - slot{"spot": "罗浮山"}
    - action_introduce_spots
    - slot{"spot": null}
* introduce_food
    - action_introduce_food
* thankyou
    - action_noworries
* goodbye
    - utter_goodbye

## Generated Story 2764035252642486678
* greet
    - utter_greet
* inform{"province": "北京"}
    - slot{"province": "北京"}
    - utter_ask
* recommend_spot
    - action_provide_spots
* introduce_spot{"spot": "颐和园"}
    - slot{"spot": "颐和园"}
    - action_introduce_spots
* unknown
    - action_unknown
    - rewind
* thankyou
    - action_noworries
    - rewind
* introduce_spot{"spot": "故宫博物院"}
    - slot{"spot": "故宫博物院"}
    - action_introduce_spots
* thankyou
    - action_noworries
    - rewind
* goodbye
    - utter_goodbye

## Generated Story 976488237529756992
* greet
    - utter_greet
* inform{"province": "北京"}
    - slot{"province": "北京"}
    - utter_ask
* introduce_food
    - action_introduce_food
* recommend_spot
    - action_provide_spots
* introduce_spot{"spot": "故宫博物院"}
    - slot{"spot": "故宫博物院"}
    - action_introduce_spots
* thankyou
    - action_noworries
    - rewind
* whatcanyoudo
    - action_icando
    - rewind
* thankyou
    - action_noworries
    - rewind
* goodbye
    - utter_goodbye

## chat
* chat
    - action_chat

## Generated Story -6990716699631921705
* greet
    - utter_greet
* inform{"province": "北京"}
    - slot{"province": "北京"}
    - utter_ask
* recommend_spot
    - action_provide_spots
* introduce_spot{"spot": "天坛公园"}
    - slot{"spot": "天坛公园"}
    - action_introduce_spots
* introduce_food
    - action_introduce_food
* chat{"name": "徐曳恺"}
    - slot{"name": "徐曳恺"}
    - action_chat
    - action_chat
    - rewind
* chat{"name": "孙王斌"}
    - slot{"name": "孙王斌"}
    - action_chat
    - rewind

## Generated Story -231057281917837298
* greet
    - utter_greet
* inform{"province": "安徽"}
    - slot{"province": "安徽"}
    - utter_ask
* recommend_spot
    - action_provide_spots
* introduce_spot{"spot": "西递宏村"}
    - slot{"spot": "西递宏村"}
    - action_introduce_spots
* introduce_food
    - action_introduce_food
* chat{"name": "徐曳恺"}
    - slot{"name": "徐曳恺"}
    - action_chat
    - rewind
* thankyou
    - action_noworries
    - rewind

## oppo
* oppo:
    - utter_oppo
## Generated Story 2482138980461769590
* greet
    - utter_greet
* unknown{"other": "天气"}
    - action_unknown
    - rewind
* unknown
    - action_unknown
    - rewind
* oppo
    - utter_oppo
* inform{"province": "福建"}
    - slot{"province": "福建"}
    - utter_ask
* recommend_spot
    - action_provide_spots
* introduce_spot{"spot": "三坊七巷"}
    - slot{"spot": "三坊七巷"}
    - action_introduce_spots
* introduce_food
    - action_introduce_food
* introduce_food
    - action_introduce_food
* whatcanyoudo
    - action_icando
    - rewind
* unknown{"other": "携程"}
    - action_unknown
    - rewind
* whatcanyoudo
    - action_icando
    - rewind
* goodbye
    - utter_goodbye
