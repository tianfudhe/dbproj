import urllib
import urllib2
import json

query_type={0:'qavg',1:'qmax',2:'qmin',3:'qseq'}

query_dict={'qmax':'select max(value) from {0} where uid=\'{1}\'',
		'qmin':'select min(value) from {0} where uid=\'{1}\'',
		'qseq':'select value from {0} where uid=\'{1}\'',
		
		}

parse_dict={0:'pmax',1:'pmax',2:'pmax',3:'pmax'}

def pmax(res):
	try:
		res=res['results'][0]['series'][0]['values']
	except:
		res='res null'
	return res

def query_data(user_id, query_id, value_type,scene_id=None,time_range=None,ip='localhost',port='8086',data_type='test'):
	query_url = 'http://{0}:{1}/query'.format(ip,port)
	cmd = query_dict[query_type[query_id]].format(value_type,user_id)
	if not scene_id is None:
		scene_condition = ' or region=\'{}\''*len(scene_id)
		scene_condition = scene_condition.format(*scene_id)[3:]
		cmd +=' and ({})'.format(scene_condition)
	if time_range:
		cmd +=' and time<{}'.format(time_range[1])
		cmd +=' and time>{}'.format(time_range[0])
	print cmd
	params={'db':value_type,'q':cmd}

	data = urllib.urlencode(params)
	res = urllib2.urlopen(query_url+'?'+data)
	jres = json.loads(res.read())
	#return jres
	return eval(parse_dict[query_id])(jres)
if __name__=='__main__':
	#print query_data(user_id=1,query_id=1,value_type='test',scene_id=(0,1),time_range=(14959500600000000000,1495950070000000000))
	print query_data(user_id=1,query_id=3,value_type='test',scene_id=(0,1),time_range=(0,1495950070000000000))
