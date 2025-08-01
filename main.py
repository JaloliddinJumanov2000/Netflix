# # import requests
# #
# #
# # def time_split(seconds):
# #     hours = seconds // 3600
# #     minute = (seconds % 3600) // 60
# #     second = seconds % 60
# #     return f"{hours}:{minute}:{second}"
# #
# #
# # def define_genere(ids):
# #     url2 = "http://localhost:8000"
# #     response = requests.get(url2).json()
# #     genres = []
# #     for datas in response:
# #         if datas['id'] in ids:
# #             genres.append(datas['name'])
# #     return genres
# #
# #
# # url = "http://localhost:8000/contents/"
# #
# # response = requests.get(url).json()
# # for datas in response:
# #     print(f'FILM: {datas.get("title")}')
# #     for key, value in datas.items():
# #         if key == 'duration':
# #             print(f"{key}: {time_split(value)}")
# #         elif key == 'genre':
# #             print(f"{key}: {define_genere(value)}")
# #         else:
# #
# # print(f"{key}: {value}")
# #
# # print(response.json())
#
#
# # import requests
# #
# # url = "http://localhost:8000/1/"
# #
# # response = requests.delete(url)
# #
# # print(response.status_code)
#
# import requests
#
# url = "https://twitter154.p.rapidapi.com/tweet/replies/continuation"
#
# querystring = {"tweet_id":"1924684020107116709","continuation_token":"ZAAAAPBVHBmm-Iawof7U97U19Me0obLCjbc19oe2-Z3e8rU1xIXYkai08rU1wIa7vd2j_7Y1kILTkeeGo7Y1-IXYqdGO0uM0qIfY6YSE7rU16oLY-aqw9LU1sMe8id6277U1JQISFQQAAA"}
#
# headers = {
# 	"x-rapidapi-key": "325fa23ccbmsh56633734b8ec183p1ee096jsn274ca6c3ef2e",
# 	"x-rapidapi-host": "twitter154.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())