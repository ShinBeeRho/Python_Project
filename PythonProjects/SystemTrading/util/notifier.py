# 메세지 기능 사용X
# import requests

# TARGET_URL = 'http://notify-api.line.me/api/notify'


# def send_message(message, token=None):
#     try:
#         response = requests.post(
#             TARGET_URL,
#             headers={
#                 'Authorization': 'Bearer' + token
#             },
#             data={
#                 'message': message
#             }
#         )
#         status = response.json()['status']

#         if status != 200:
#             raise Exception('Fail need to check. Status is %s' % status)

#     except Exception as e:
#         print("Exception occured")
#         # raise Exception(e)
