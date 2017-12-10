########### Python 3.6 #############
import requests, json
import os

###############################################
#### Update or verify the following values. ###
###############################################

# Replace the subscription_key string value with your valid subscription key.
subscription_key = os.environ['COMPUTER_VISION_API_KEY']

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
uri_base = 'https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/analyze' ##### <1> #####

headers = {
    # Request headers.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

params = { ##### <2> #####
    # Request parameters. All of them are optional.
    'visualFeatures': 'Description',
    'language': 'en',
}

# Replace the three dots below with the URL of a JPEG image of a celebrity.
body = "{'url': 'https://emotionwebsto.blob.core.windows.net/handson/emotionweb_happiness.jpg'}" ##### <3> #####

try:
    # Execute the REST API call and get the response.
    response = requests.post(uri_base, params=params, data=body, headers=headers) ##### <4> #####
    data = response.text

    # 'data' contains the JSON data. The following formats the JSON data for display.
    parsed = json.loads(data)
    print ("Response:")
    print (json.dumps(parsed, sort_keys=True, indent=2))

except Exception as e:
    print('Error:')
    print(e)

####################################
