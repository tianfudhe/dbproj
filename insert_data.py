import urllib
import urllib2
import json


def insert_data(user_id, scene_id, value, ip='localhost',port='8086',data_type='test'):
	write_url = r'http://{0}:{1}/write?db={2}'.format(ip,port,data_type)
	print write_url	
	data = '{0},uid={1},region={2} value={3}'.format(data_type,user_id,scene_id,value)
	data = data.encode()
	#postdata = urllib.urlencode(data)
	request = urllib2.Request(write_url, data)
	response = urllib2.urlopen(request)

	return response

if __name__=='__main__':
	for uid in range(3):
		for region in range(2):
			for value in range(40,120,10):
				insert_data(uid,region,value)
