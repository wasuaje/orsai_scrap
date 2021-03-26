import urllib
import urllib2



url = 'http://orsai.bitacoras.com/wp-comments-post.php'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = dict(author="Wuelfhis Asuaje", email="wasuaje@hotmail.com",comment="Saludos desde Venezuela",comment_post_ID=2497,comment_parent=0)
headers = { 'User-Agent' : user_agent }

submitVars={}
submitVars['author'] = "Wuelfhis Asuaje"
submitVars['email'] = "wasuaje@hotmail.com"
submitVars['comment'] = "Saludos !"
submitVars['comment_post_ID'] = "2497"
submitVars['comment_parent'] = "0"

submitUrl = url
referer = "http://orsai.bitacoras.com/"

submitVarsUrlencoded = urllib.urlencode(submitVars)
req = urllib2.Request(submitUrl, submitVarsUrlencoded)
req.add_header('Referer', referer)
req.add_header('User-Agent', user_agent)

response = urllib2.urlopen(req)
thePage = response.read()

