import requests, json
from flask import Flask, request, jsonify, abort
import sys

application = Flask(__name__)


def createReponse(user_key):
    data = {
        'event': 'send',
        'user': user_key,
        'textContent': {'text': '네, 알려드리겠습니다.'}
    }
    return data


# 네이버 톡톡 챗봇 연결
@application.route("/bera", methods=['POST'])
def aaa():
    print(request.get_json())
    authKey = "KVmHa+NKS5uxicV5V57t"
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Authorization': authKey
    }
    user_key = request.get_json()['user']
    msg = request.get_json()

    if msg['textContent']['text'] == '웹개발자 책 하나 추천해줄래?' or msg['textContent']['text'] == '웹개발책' or msg['textContent'][
        'text'] == '웹 도서':
        data = createReponse(user_key)
        message = json.dumps(data)
        response = requests.post('https://gw.talk.naver.com/chatbot/v1/event', headers=headers, data=message)
        data = {
            'event': 'send',
            'user': user_key,
            'compositeContent': {
                'compositeList': [
                    {
                        'image': {
                            'imageUrl': 'https://contents.kyobobook.co.kr/sih/fit-in/200x0/pdt/9791191905298.jpg'},
                        'buttonList': [
                            {
                                'type': 'LINK',
                                'data': {
                                    'title': '이런 책은 어떠세요? "스프링 부트"',
                                    'url': 'https://buly.kr/9BS8a4o'
                                }
                            }
                        ]
                    }

                ]
            }
        }
    elif msg['textContent']['text'] == '데이터 책 추천' or msg['textContent']['text'] == '데이터책' or msg['textContent'][
        'text'] == '데이터 도서':
        data = createReponse(user_key)
        message = json.dumps(data)
        response = requests.post('https://gw.talk.naver.com/chatbot/v1/event', headers=headers, data=message)
        data = {
            'event': 'send',
            'user': user_key,
            'compositeContent': {
                'compositeList': [
                    {
                        'image': {
                            'imageUrl': 'https://contents.kyobobook.co.kr/sih/fit-in/200x0/pdt/9791169210287.jpg'},
                        'buttonList': [
                            {
                                'type': 'LINK',
                                'data': {
                                    'title': '교보문고로 이동하기',
                                    'url': 'https://search.kyobobook.co.kr/search?keyword=%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B6%84%EC%84%9D&target=total&gbCode=TOT&ra=qntt'
                                }
                            }
                        ]
                    }
                ]
            }
        }
    elif msg['textContent']['text'] == '요즘 웹 개발이 핫 하던데 어떻게 시작하면 좋을까?' or msg['textContent']['text'] == '진로고민상담':
        data = createReponse(user_key)
        message = json.dumps(data)
        response = requests.post('https://gw.talk.naver.com/chatbot/v1/event', headers=headers, data=message)
        data = {
            'event': 'send',
            'user': user_key,
            'compositeContent': {
                'compositeList': [
                    {
                        'image': {'imageUrl': 'https://zrr.kr/jdDc'},
                        'buttonList': [
                            {
                                'type': 'LINK',
                                'data': {
                                    'title': '베라31스푼 홈페이지로 이동하기',
                                    'url': 'http://localhost:8181/web'
                                }
                            }
                        ]
                    }
                ]
            }
        }
    elif msg['textContent']['text'] == '웹 말고 더 핫한 AI는 어떻게 준비해야 되니?':
        data = createReponse(user_key)
        message = json.dumps(data)
        response = requests.post('https://gw.talk.naver.com/chatbot/v1/event', headers=headers, data=message)
        data = {
            'event': 'send',
            'user': user_key,
            'compositeContent': {
                'compositeList': [
                    {
                        'image': {'imageUrl': 'https://zrr.kr/jdDc'},
                        'buttonList': [
                            {
                                'type': 'LINK',
                                'data': {
                                    'title': '베라31스푼 홈페이지로 이동하기',
                                    'url': 'http://localhost:8181/ai'
                                }
                            }
                        ]
                    }
                ]
            }
        }
    elif msg['textContent']['text'] == '안녕하세요':
        data = {
            'event': 'send',
            'user': user_key,
            'textContent': {'text': '네, 무엇을 도와드릴까요?'},
        }
    elif msg['textContent']['text'] == '궁금한게 있는데 현직자들한테 질문 할 수 있는 곳이 있어?':
        data = createReponse(user_key)
        message = json.dumps(data)
        response = requests.post('https://gw.talk.naver.com/chatbot/v1/event', headers=headers, data=message)
        data = {
            'event': 'send',
            'user': user_key,
            'compositeContent': {
                'compositeList': [
                    {
                        'image': {'imageUrl': 'https://zrr.kr/jdDc'},
                        'buttonList': [
                            {
                                'type': 'LINK',
                                'data': {
                                    'title': '베라31스푼 Q&A게시판 이동하기',
                                    'url': 'http://localhost:8181/qna'
                                }
                            }
                        ]
                    }
                ]
            }
        }
    elif msg['textContent']['text'] == '웹개발 채용이 궁금해':
        data = createReponse(user_key)
        message = json.dumps(data)
        response = requests.post('https://gw.talk.naver.com/chatbot/v1/event', headers=headers, data=message)
        data = {
            'event': 'send',
            'user': user_key,
            'compositeContent': {
                'compositeList': [
                    {
                        'image': {'imageUrl': 'https://zrr.kr/nkuo'},
                        'buttonList': [
                            {
                                'type': 'LINK',
                                'data': {
                                    'title': '사람인 채용정보로 이동하기',
                                    'url': 'https://www.saramin.co.kr/zf_user/jobs/list/job-category?cat_kewd=87&panel_type=&search_optional_item=n&search_done=y&panel_count=y&preview=y'
                                }
                            }
                        ]
                    }
                ]
            }
        }
    elif msg['textContent']['text'] == '데이터 채용이 궁금해':
        data = createReponse(user_key)
        message = json.dumps(data)
        response = requests.post('https://gw.talk.naver.com/chatbot/v1/event', headers=headers, data=message)
        data = {
            'event': 'send',
            'user': user_key,
            'compositeContent': {
                'compositeList': [
                    {
                        'image': {'imageUrl': 'https://zrr.kr/nkuo'},
                        'buttonList': [
                            {
                                'type': 'LINK',
                                'data': {
                                    'title': '사람인 채용정보로 이동하기',
                                    'url': 'https://www.saramin.co.kr/zf_user/jobs/list/job-category?cat_kewd=82&panel_type=&search_optional_item=n&search_done=y&panel_count=y&preview=y'
                                }
                            }
                        ]
                    }
                ]
            }
        }
    else:
        data = {
            'event': 'send',
            'user': user_key,
            'textContent': {'text': '조금만 기다려주세요. 서비스 준비중입니다.'}
        }

    message = json.dumps(data)
    response = requests.post('https://gw.talk.naver.com/chatbot/v1/event', headers=headers, data=message)
    """
    if msg['textContent']['text'] == '데이터 책 추천' or msg['textContent']['text'] == '데이터책' or msg['textContent']['text'] == '데이터':
        data = {
            'event' : 'send',
            'user' : user_key,
            'compositeContent': {
                'compositeList': [
                    {
                        'image': {'imageUrl': 'https://contents.kyobobook.co.kr/sih/fit-in/200x0/pdt/9791191905298.jpg'},
                        'buttonList': [
                            {
                                'type': 'LINK',                             
                                'data': {
                                    'title': '베라31스푼 사이트로 이동하기',
                                    'url': 'https://search.kyobobook.co.kr/search?keyword=%EC%8A%A4%ED%94%84%EB%A7%81%EB%B6%80%ED%8A%B8&gbCode=TOT&target=total'
                                }
                            }
                        ]
                    }

                ]
            }
        }
    else:
         data = {
             'event': 'send',
             'user': user_key,
             'textContent': {'text': '네, 이용자님이 찾으시는 정보입니다.'}
        }

    message = json.dumps(data)
    response = requests.post('https://gw.talk.naver.com/chatbot/v1/event', headers=headers, data=message)

    """
    return 'a'


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, debug=True)
