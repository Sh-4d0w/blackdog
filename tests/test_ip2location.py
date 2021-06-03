from blackdog.osint.IP_Address.Geolocation.My_IP_Address import *

def test_isJson():
	ip = My_IP_Address()
	ip.setIP('8.8.8.8')
	r = ip.makeRequest()
	
