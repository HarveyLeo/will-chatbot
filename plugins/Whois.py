from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings
import requests
import re
import json
class Whois(WillPlugin):

    @hear("~whois (?P<text>.*)")
    def check_whois(self, message, text):

        #ip address
        if text.count(".")==3:

            result_text = requests.get("https://who.is/whois-ip/ip-address/"+ip,headers= {"User-Agent": "Mozilla/5.0"}).text
            whois_text = re.match('.*<div class="col-md-12 queryResponseBodyKey"><pre>(.*)</pre></div>',result_text, re.DOTALL).group(1)
            return self.reply(message,whois_text)
        else:
            result_text = requests.get("http://api.whoapi.com/?apikey=3fb4ea768efd677bfbed2d705bc6f47a&r=whois&domain=" + url,
                                       headers={"User-Agent": "Mozilla/5.0"}).text
            whois_dict = json.loads(result_text)
            reply="registered: "+ whois_dict["registered"] + "date created: "+whois_dict["date_created"]
            return self.reply(message, reply)