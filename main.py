from popcorntime import PopcornTime
import json
popAPI = PopcornTime()

data = popAPI.get_movie('tt4116284')
json_data = json.dumps(data, indent=4)
# print(json_data)
print(f"{data['torrents']['en']['720p']['source']}\n\n{data['torrents']['en']['720p']['url']}\n\n{data['exist_translations']}")
