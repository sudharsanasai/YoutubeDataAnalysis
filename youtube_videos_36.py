from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import pandas as pd	

DEVELOPER_KEY = "YOUR_DEVELOPER_KEY_HERE"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

import pandas as pd	


def youtube_search(q, max_results=50,order="relevance", token=None, location=None, location_radius=None):

  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=q,
    type="video",
    pageToken=token,
    order = order,
    part="id,snippet", # Part signifies the different types of data you want 
    maxResults=max_results,
    location=location,
    locationRadius=location_radius).execute()
	


  videos,channelId,channelTitle,categoryId,title,videoId,viewCount,likeCount,dislikeCount,commentCount,favoriteCount,category,tags  = []

  for search_result in search_response.get("items", []):
  
  
  
    if search_result["id"]["kind"] == "youtube#video":
	  	
	  title.append(search_result['snippet']['title']) 
	  videoId.append(search_result['id']['videoId'])
	  
	  
	  response = youtube.videos().list(
		part='statistics, snippet',
		id=videoId_temp).execute()
	  
	  
	  
	  channelId.append(response['items'][0]['snippet']['channelId'])
	  channelTitle.append(response['items'][0]['snippet']['channelTitle'])
	  categoryId.append(response['items'][0]['snippet']['categoryId'])
	  favoriteCount.append(response['items'][0]['statistics']['favoriteCount'])
	  viewCount.append(response['items'][0]['statistics']['viewCount'])
	  likeCount.append(response['items'][0]['statistics']['likeCount'])
	  dislikeCount.append(response['items'][0]['statistics']['dislikeCount'])
	  
	  if 'commentCount' in response['items'][0]['statistics'].keys():
		commentCount.append(response['items'][0]['statistics']['commentCount'])
	  else:
	    commentCount.append([])
	  
	  if 'tags' in response['items'][0]['snippet'].keys():
		tags.append(response['items'][0]['snippet']['tags'])
	  else:
		tags.append([])
		
	  youtube_dict = {'tags':tags,'channelId': channelId,'channelTitle': channelTitle,'categoryId':categoryId,'title':title,'videoId':videoId,'viewCount':viewCount,'likeCount':likeCount,'dislikeCount':dislikeCount,'commentCount':commentCount,'favoriteCount':favoriteCount}

	  return youtube_dict


def geo_query(video_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    video_response = youtube.videos().list(
        id=video_id,
        part='snippet, recordingDetails, statistics'

    ).execute()

    return video_response


