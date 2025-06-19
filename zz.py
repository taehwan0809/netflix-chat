import urllib3
import json
import os

http = urllib3.PoolManager()

def lambda_handler(event, context):
    # API 키
    api_key = os.getenv('OPENAI_API_KEY')
    
    body = json.loads(event['body'])
    
    print(type(body))
    
    # 요청 데이터
    data = {
        "model": "gpt-4o-mini",
        "input": f"""캐릭터 {body['char']}를 연기하는 봇 역할. 
        방금 {body['msg']}라는 채팅을 받았다. 
        이에 대해 캐릭터 연기에 맞게 답변을 도출하기."""
    }
    
    # 헤더
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    
    # API 호출
    response = http.request(
        'POST',
        'https://api.openai.com/v1/responses',
        body=json.dumps(data),
        headers=headers
    )
    
    res_data = json.loads(response.data.decode('utf-8'))
    # 응답 반환
    return {
        'statusCode': response.status,
        'body': res_data['output'][0]['content'][0]['text']
    }