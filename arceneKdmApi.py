#  Exemple d'utilisation de l'api ARCENe.
#  Copyright (C) 2016 http://www.cst.fr 
#  @author <Sebastien Bodin>
#  @version 1.0 (2016-07-01)
#
#  The MIT License (MIT)
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
#  TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH 
#  THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



#!/usr/bin/python


#Les modules a importer
import requests
from xml.dom.minidom import parseString
import ConfigParser


#Recuperation parametres du fichier config
config = ConfigParser.RawConfigParser() 
config.read('config')
username 				= config.get('USER','username')
password 				= config.get('USER','password')
client 					= config.get('USER','client')
client_secret 				= config.get('USER','client_secret')
siteUrl 				= config.get('USER','siteUrl')
ca					= config.get('USER','atosCa')


#Mise en place de l'url
tokenEndPoint 				= "/oauth/token"
url 					= siteUrl + tokenEndPoint



#Mise en place de la requete
payload = {
'grant_type':		'password',
'client_id':		client,
'client_secret':	client_secret,
'username':		username,
'password':		password
}

r = requests.post(url, data=payload, verify=ca)
print r.content



#Recuperation du token
dataContent = r.content
dom = parseString(dataContent)
tokenDom = dom.getElementsByTagName('value')
access_token = tokenDom[0].firstChild.nodeValue
print ("\n\n\nRecuperation du token")
print (access_token)
print ("\n\n\n")



##########



#Mise en place de l'url de recuperation des KDM du cinema : 1000001
cinemaUrl 				= "/kdm/cinema/urn:x-facilityID:cnc.fr:"
cinemaCode 				= "1000001"                       #code sur 9 digits
accessTokenEndPoint 			= "/?access_token=" + access_token
url 					= siteUrl + cinemaUrl + cinemaCode + accessTokenEndPoint


#Mise en place de la requete
security_token 				= access_token
payload = {
'grant_type':		'Bearer',
'client_id':		client,
'client_secret':	client_secret,
'username':		username,
'password':		password + security_token
}
r = requests.get(url, data=payload, verify=ca)



#Recuperation des donnees
dataContent = r.content
print ("\n\n\nRecuperation des kdms du cinema : 1000001")
print (dataContent)
print ("\n\n\n")



##########



#Mise en place de l'url de recuperation des KDM de la salle :1000001 du cinema : 1000001
cinemaUrl 				= "/kdm/cinema/urn:x-facilityID:cnc.fr:"
cinemaCode 				= "1000001"
roomUrl 				= "/room/urn:x-facilityID:cnc.fr:"            
roomCode 				= "1000001"
accessTokenEndPoint 			= "/?access_token=" + access_token
url 					= siteUrl + cinemaUrl + cinemaCode + roomUrl + roomCode + accessTokenEndPoint


#Mise en place de la requete
security_token 				= access_token
payload = {
'grant_type':		'Bearer',
'client_id':		client,
'client_secret':	client_secret,
'username':		username,
'password':		password + security_token
}
r = requests.get(url, data=payload, verify=ca)


#Recuperation des donnees
dataContent = r.content
print ("\n\n\nRecuperation des kdms de la salle :1000001 du cinema : 1000001")
print (dataContent)
print ("\n\n\n")



############



#Recuperation des donnees
dom=parseString(dataContent)



#Recuperation de l'ID du premier KDM
kdmListDom = dom.getElementsByTagName('uuid')
kdm1Uuid = kdmListDom[0].firstChild.nodeValue
print ("\n\n\nRecuperation de l'ID du premier KDM")
print (kdm1Uuid)



#Mise en place de l'url de recupertaion du KDM
kdmEndPoint 				= "/kdm/"
accessTokenEndPoint 			= "/?access_token=" + access_token
url 					= siteUrl + kdmEndPoint + kdm1Uuid + accessTokenEndPoint



#Mise en place de la requete
security_token 				= access_token
payload = {
'grant_type':		'Bearer',
'client_id':		client,
'client_secret':	client_secret,
'username':		username,
'password':		password + security_token
}
r = requests.get(url, data=payload, verify=ca)



#Affichage du KDM recupere
print ("\n\n\nRecuperation du KDM")
print (r.content)