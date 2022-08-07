# URL lookup service 
######################
Pre-Requsites
######################
import cgitb
import cgi
import mysql.connector


######################
Info on URL Lookup Service
######################
URL_Lookup.py : Main backend module that parses URL from application request, looks up in mysql db for malwares
                returns the result with URL is safe or Malware.
update_db_with_malwares.py: Backend module to update service's database periodically with the info about new URLs or 
                updates on existing URLs.
URL_Lookup_WHOIS.py: Alternative URL info source WHOIS registars

URL_Lookup_App.py: Example Application using this URL Lookup service to verify it's safe to visit URL before visiting.
simple.html:    An html webform accepting URL and calls backend module with cgi field to consume the backend service.                                

######################
How to Use???
######################
1. Place the simple.html file under your webserver's config
    Example: MAMP ===>> /Applications/MAMP/htdocs
2. Checkout everything else and keep it under your webserver's cgi-bin config
    Example: MAMP ===>> /Applications/MAMP/cgi-bin