#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ipaddress
import re
import urllib.request
import whois



def generate_data_set(url):

    data_set = []
    #ip address
    try:
        ipaddress.ip_address(url)  #check for ipaddress in url
        data_set.append(-1) #phishing
    except:
        data_set.append(1) #legitimate

    #URL_Length
    if len(url) < 54:
        data_set.append(1) #legitimate
    elif len(url) >= 54 and len(url) <= 75:
        data_set.append(0) #suspicious
    else:
        data_set.append(-1) #phihing

    #Shortining_Service
    match = re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                      'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                      'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                      'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                      'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                      'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                      'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|tr\.im|link\.zip\.net', url)
    if match:
        data_set.append(-1) #phishing
    else:
        data_set.append(1) #legitimate

    #having_At_Symbol
    if re.findall("@", url):
        data_set.append(-1) #phishing
    else:
        data_set.append(1) #legitimate

    #double_slash_redirecting
    list = [x.start(0) for x in re.finditer('//', url)]
    if list[len(list)-1] > 6:
        data_set.append(-1)#phishing
    else:
        data_set.append(1) #legitimate

    #Prefix_Suffix
    if re.findall(r"https?://[^\-]+-[^\-]+/", url):
        data_set.append(-1) #phishing
    else:
        data_set.append(1)#legitimate

    #having_Sub_Domain
    if len(re.findall("\.", url)) == 1:
        data_set.append(1) #legitimate
    elif len(re.findall("\.", url)) == 2:
        data_set.append(0) #suspicious
    else:
        data_set.append(-1) #phishing

    #SSLfinal_State
    try:
        if response.text:
            data_set.append(1) #legitimate
    except:
        data_set.append(-1) #ohishing

    #Domain_registeration_length
    expiration_date = whois_response.expiration_date
    registration_length = 0
    try:
        expiration_date = min(expiration_date)
        today = time.strftime('%Y-%m-%d')
        today = datetime.strptime(today, '%Y-%m-%d')
        registration_length = abs((expiration_date - today).days)

        if registration_length / 365 <= 1:
            data_set.append(-1)
        else:
            data_set.append(1)
    except:
        data_set.append(-1)

    
    #port
    try:
        port = domain.split(":")[1]
        if port:
            data_set.append(-1) #phishing
        else:
            data_set.append(1) #legitimate
    except:
        data_set.append(1) #legitimate

    #HTTPS_token
    if re.findall(r"^https://", url):
        data_set.append(1) #legitimate
    else:
        data_set.append(-1) #phishing
        

    
    

    #Submitting_to_email
    if response == "":
        data_set.append(-1)
    else:
        if re.findall(r"[mail\(\)|mailto:?]", response.text):
            data_set.append(-1) #phishing
        else:
            data_set.append(1) #legitimate

    
    #Redirect
    if response == "":
        data_set.append(-1)
    else:
        if len(response.history) <= 1:
            data_set.append(-1) #phishing
        elif len(response.history) <= 4:
            data_set.append(0) #suspicious
        else:
            data_set.append(1) #legitimate

    #on_mouseover
    if response == "":
        data_set.append(-1)
    else:
        if re.findall("<script>.+onmouseover.+</script>", response.text):
            data_set.append(1)
        else:
            data_set.append(-1)

    #RightClick
    if response == "":
        data_set.append(-1)
    else:
        if re.findall(r"event.button ?== ?2", response.text):
            data_set.append(1) #legitimate
        else:
            data_set.append(-1) #pishing

    #popUpWidnow
    if response == "":
        data_set.append(-1)
    else:
        if re.findall(r"alert\(", response.text):
            data_set.append(-1) #phishing
        else:
            data_set.append(1) #legitimate

    #Iframe
    if response == "":
        data_set.append(-1)
    else:
        if re.findall(r"[<iframe>|<frameBorder>]", response.text):
            data_set.append(1)
        else:
            data_set.append(-1)

    #age_of_domain
    if response == "":
        data_set.append(-1)
    else:
        try:
            registration_date = re.findall(
                    r'Registration Date:</div><div class="df-value">([^<]+)</div>', whois_response.text)[0]
            if diff_month(date.today(), date_parse(registration_date)) >= 6:
                data_set.append(-1)
            else:
                data_set.append(1)
        except:
            data_set.append(1)

    

    #Page_Rank
    try:
        if global_rank > 0 and global_rank < 100000:
            data_set.append(-1) #phishing
        else:
            data_set.append(1) #legitimate
    except:
        data_set.append(1) #legitimate

    #Google_Index
    site = search(url, 5)
    if site:
        data_set.append(1) #legitimate
    else:
        data_set.append(-1) #phishing

    #Links_pointing_to_page
    if response == "":
        data_set.append(-1)
    else:
        number_of_links = len(re.findall(r"<a href=", response.text))
        if number_of_links == 0:
            data_set.append(1) #legitimate
        elif number_of_links <= 2:
            data_set.append(0) #suspicious
        else:
            data_set.append(-1) #phishing

   

    return data_set
 


# In[ ]:





# In[ ]:




