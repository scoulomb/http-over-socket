# Host header

## Prelim

We had seen Kubernetes ingress: https://github.com/scoulomb/myDNS/blob/master/2-advanced-bind/5-real-own-dns-application/6-use-linux-nameserver-part-f.md#sample-ingress
- Host based routing 
- with certificate

And we had seen equivalent in different technology: https://github.com/scoulomb/myDNS/blob/master/2-advanced-bind/5-real-own-dns-application/6-use-linux-nameserver-part-h.md#parallel

- Including github page which can have its DNS entry configured in a nameserver pod running in Kubernetes cluster:
https://github.com/scoulomb/myDNS/blob/master/2-advanced-bind/5-real-own-dns-application/6-use-linux-nameserver-part-i.md

<!-- after machine and minikube restart it is in error, because restart is never, do not try -->

We will start this DNS as mentioned in given link. (or use Gandi live DNS)

- Including `attestioncovid.site` in cloud run with CNAME mapping: https://github.com/scoulomb/attestation-covid19-saison2-auto#mapping-custom-domain-in-cloud-run

we will use github page and cloud run here.

## using curl

Doing 

````shell script
curl coulombel.it -v | head -n 10
curl -H "Host: coulombel.it" coulombel.it -v | head -n 10
curl -H "Host: coulombel2.it" coulombel.it -v | head -n 10
````

output is 

<!-- use hp as corp block 404-->

````shell script
sylvain@sylvain-hp:~$ curl coulombel.it -v | head -n 10
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 185.199.108.153:80...
* TCP_NODELAY set
* Connected to coulombel.it (185.199.108.153) port 80 (#0)
> GET / HTTP/1.1
> Host: coulombel.it
> User-Agent: curl/7.68.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Content-Type: text/html; charset=utf-8
< Server: GitHub.com
< Last-Modified: Sat, 19 Dec 2020 21:27:31 GMT
< Access-Control-Allow-Origin: *
< ETag: "5fde7043-eefd"
< Expires: Wed, 23 Dec 2020 17:04:17 GMT
< Cache-Control: max-age=600
< X-Proxy-Cache: MISS
< X-GitHub-Request-Id: 3CCA:FEC2:1D007C3:1F1779F:5FE37638
< Content-Length: 61181
< Accept-Ranges: bytes
< Date: Wed, 23 Dec 2020 17:02:00 GMT
< Via: 1.1 varnish
< Age: 463
< Connection: keep-alive
< X-Served-By: cache-cdg20731-CDG
< X-Cache: HIT
< X-Cache-Hits: 1
< X-Timer: S1608742920.427353,VS0,VE1
< Vary: Accept-Encoding
< X-Fastly-Request-ID: 3b22017db71421eb8dd738cd2003471be24316bc
<
{ [737 bytes data]
<!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Sylvain COULOMBEL</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css"
        />
* Failed writing body (535 != 1384)
 14 61181   14  9041    0     0    98k      0 --:--:-- --:--:-- --:--:--   98k
* Closing connection 0
curl: (23) Failed writing body (535 != 1384)
sylvain@sylvain-hp:~$ curl -H "Host: coulombel.it" coulombel.it -v | head -n 10
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 185.199.108.153:80...
* TCP_NODELAY set
* Connected to coulombel.it (185.199.108.153) port 80 (#0)
> GET / HTTP/1.1
> Host: coulombel.it
> User-Agent: curl/7.68.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Content-Type: text/html; charset=utf-8
< Server: GitHub.com
< Last-Modified: Sat, 19 Dec 2020 21:27:31 GMT
< Access-Control-Allow-Origin: *
< ETag: "5fde7043-eefd"
< Expires: Wed, 23 Dec 2020 17:04:17 GMT
< Cache-Control: max-age=600
< X-Proxy-Cache: MISS
< X-GitHub-Request-Id: 3CCA:FEC2:1D007C3:1F1779F:5FE37638
< Content-Length: 61181
< Accept-Ranges: bytes
< Date: Wed, 23 Dec 2020 17:02:04 GMT
< Via: 1.1 varnish
< Age: 468
< Connection: keep-alive
< X-Served-By: cache-cdg20748-CDG
< X-Cache: HIT
< X-Cache-Hits: 1
< X-Timer: S1608742925.853166,VS0,VE1
< Vary: Accept-Encoding
< X-Fastly-Request-ID: 9e7d7bb41d9da86a0c1b649080052592f1fd1eb1
<
{ [2121 bytes data]
<!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Sylvain COULOMBEL</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css"
        />
* Failed writing body (423 != 1384)
 28 61181   28 17345    0     0  59400      0  0:00:01 --:--:--  0:00:01 59400
* Closing connection 0
curl: (23) Failed writing body (423 != 1384)
sylvain@sylvain-hp:~$ curl -H "Host: coulombel2.it" coulombel.it -v | head -n 10
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 185.199.108.153:80...
* TCP_NODELAY set
* Connected to coulombel.it (185.199.108.153) port 80 (#0)
> GET / HTTP/1.1
> Host: coulombel2.it
> User-Agent: curl/7.68.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 404 Not Found
< Content-Type: text/html; charset=utf-8
< Server: GitHub.com
< ETag: "5f7b904d-239b"
< Content-Security-Policy: default-src 'none'; style-src 'unsafe-inline'; img-src data:; connect-src 'self'
< X-GitHub-Request-Id: D62A:5BB6:58CC14:61E1EA:5FE37690
< Content-Length: 9115
< Accept-Ranges: bytes
< Date: Wed, 23 Dec 2020 17:02:08 GMT
< Via: 1.1 varnish
< Age: 384
< Connection: keep-alive
< X-Served-By: cache-cdg20729-CDG
< X-Cache: HIT
< X-Cache-Hits: 1
< X-Timer: S1608742929.847331,VS0,VE1
< Vary: Accept-Encoding
< X-Fastly-Request-ID: 8c74a3906d2b84054251b7c1474d903523da4a9f
<
{ [793 bytes data]
<!DOCTYPE html>
1<html>
0  <head>
0     <meta http-equiv="Content-type" content="text/html; charset=utf-8">
 9    <meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; img-src data:; connect-src 'self'">
11    <title>Site not found &middot; GitHub Pages</title>
5    <style type="text/css" media="screen">
       body {
         background-color: #f1f1f1;
1        margin: 0;
00  9115    0     0  44247      0 --:--:-- --:--:-- --:--:-- 44247
* Connection #0 to host coulombel.it left intact
(23) Failed writing body
sylvain@sylvain-hp:~$
````

Observations:
- It confirm github is doing host based routing.
- If we do not define `Host` header it is set to the  Hostname (until tld here) 
- If we define `Host` header, we can see it is overriden. We do not send 2 host header. And if it does not match we got a 404.

It works in HTTPS

````shell script
➤ curl https://coulombel.it | grep DevOps
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
                        <div class="card profile-card"><span class="profile-pic-container"><div class="profile-pic"><img class="media-object img-circle center-block" data-src="holder.js/100x100" alt="Sylvain COULOMBEL" src="https://s.gravatar.com/avatar/1711d3b8f78dbfdb7d539cd99aba4554?s=100&amp;r=pg&amp;d=mm" itemprop="image"/></div><div class="name-and-profession text-center"><h3 itemprop="name"><b>Sylvain COULOMBEL</b></h3><h5 class="text-muted" itemprop="jobTitle">DevOps engineer</h5></div></span>
100 61181  100 61181    0                                                 <p>I am a 30 year old software engineer with strong interest in DevOps. I
````

For attestation covid we have same conclusion

````shell script

````shell script
curl attestationcovid.site -v | head -n 10
curl -L attestationcovid.site -v | head -n 10
````

It is redirected to https (as Kubernetes ingress, see [here](https://github.com/scoulomb/myDNS/blob/master/2-advanced-bind/5-real-own-dns-application/6-use-linux-nameserver-part-h.md#extended-test)), we will query https directly.
<!-- no go more -->
Note https://www.drlinkcheck.com/blog/http-redirects-301-302-303-307-308, permanent redirect is 308 and temp redirect is 302 (Gandi redirection made same).

The address is given in `Location` header.
Similar to show curl google.com (301 document has moved)/ curl -L google.com / curl www.google.com difference

````shell script
curl https://attestationcovid.site -v | head -n 10
````

Output is 


````shell script
sylvain@sylvain-hp:~$ curl https://attestationcovid.site -v | head -n 10
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 2001:4860:4802:36::15:443...
* TCP_NODELAY set
* Connected to attestationcovid.site (2001:4860:4802:36::15) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
  CApath: /etc/ssl/certs
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [512 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [122 bytes data]
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
{ [15 bytes data]
* TLSv1.3 (IN), TLS handshake, Certificate (11):
{ [2477 bytes data]
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
{ [264 bytes data]
* TLSv1.3 (IN), TLS handshake, Finished (20):
{ [52 bytes data]
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.3 (OUT), TLS handshake, Finished (20):
} [52 bytes data]
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=attestationcovid.site
*  start date: Nov  4 00:48:59 2020 GMT
*  expire date: Feb  2 00:48:59 2021 GMT
*  subjectAltName: host "attestationcovid.site" matched cert's "attestationcovid.site"
*  issuer: C=US; O=Google Trust Services; CN=GTS CA 1D2
*  SSL certificate verify ok.
* Using HTTP2, server supports multi-use
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
} [5 bytes data]
* Using Stream ID: 1 (easy handle 0x557827422df0)
} [5 bytes data]
> GET / HTTP/2
> Host: attestationcovid.site
> user-agent: curl/7.68.0
> accept: */*
>
{ [5 bytes data]
* Connection state changed (MAX_CONCURRENT_STREAMS == 100)!
} [5 bytes data]
< HTTP/2 200
< content-disposition: inline; filename="index.html"
< accept-ranges: bytes
< etag: "b87acab742467089331e7f697046b8fd6ff81c51"
< content-type: text/html; charset=utf-8
< vary: Accept-Encoding
< x-cloud-trace-context: 0f1e25cb7185ec24c9cb3678a5059648;o=1
< date: Wed, 23 Dec 2020 17:13:06 GMT
< server: Google Frontend
< content-length: 8126
<
{ [5 bytes data]
<!DOCTYPE html><html lang="fr"><head><meta charset="UTF-8"><meta name="title" content="Générateur d'attestation COVID-19 en un click "><meta name="keywords" content="covid19, attestation"><meta name="robots" content="index, follow"><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta name="language" content="French"><title>Attestation de déplacement dérogatoire</title><script>window._mNHandle=window._mNHandle||{},window._mNHandle.queue=window._mNHandle.queue||[],medianet_versionId="3121199";</script><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous"><script src="https://contextual.media.net/dmedianet.js?cid=8CUY31688" async></script></head><body class="container"> <h1 id="Welcome mb-4"> Générateur d'attestation COVID-19 en un click ! </h1> <h2 id="why"> Service </h2> <p>Ce projet permet de générer une attestation de déplacement en &quot;1-click&quot; pour le confinement saison 2 lance en France le vendredi 30 Octobre 2020. En effet la version numérique du gouvernement (<a href="https://media.interieur.gouv.fr/deplacement-covid-19/">https://media.interieur.gouv.fr/deplacement-covid-19/</a>) nécessite</p> <ul> <li>Plus d&#39;un click pour générer une attestation</li> <li>Force a re-renter les informations a chaque utilisation sur certains navigateurs (see <a href="https://gist.github.com/niksumeiko/360164708c3b326bd1c8">autocomplete</a> set to <a href="https://github.com/LAB-MI/attestation-deplacement-derogatoire-q4-2020/blob/a2566e82555c56442dbdc6857c21f0e4c8c5dc39/src/js/form.js#L22">false</a>),</li> </ul> <h2 id="Usage"> Utilisation </h2> <p>Concu comme un lien a bookmarker sur un dispositif mobile (telephone, tablette, etc), l&#39;ouverture de ce lien declenchera le telechargement d&#39;une nouvelle attestation enrichie des informations fournies dans le lien.</p> <p>Cette exemple de lien (prealablement bookmarke) <a href="https://attestationcovid.site/?address=15%20rue%20d%27Antibes&amp;birthday=20/03/1882&amp;city=Antibes&amp;firstname=Rene&amp;minutesoffset=5&amp;lastname=Coty&amp;placeofbirth=Le%20Havre&amp;zipcode=06600&amp;reason=sport_animaux">https://attestationcovid.site/?address=15 rue d&#39;Antibes&amp;birthday=20/03/1882&amp;city=Antibes&amp;firstname=Rene&amp;minutesoffset=5&amp;lastname=Coty&amp;placeofbirth=Le Havre&amp;zipcode=06600&amp;reason=sport_animaux</a> generera une attestation avec les informations suivantes:</p> <ul> <li><strong>15 rue d&#39;Antibes</strong> <em>l&#39;addresse de votre habitation</em></li> <li><strong>20/03/1882</strong> <em>la date de votre aniversaire</em></li> <li><strong>Antibes</strong> <em>la ville d&#39;habitation</em></li> <li><strong>Rene</strong> <em>votre prenom</em></li> <li><strong>03/11/2020 a 13H18</strong> <em>la date de sortie generee a partir de l&#39;heure actuelle en ajoutant un offset (positif pour une date future ou negatif pour une date passee)</em></li> <li><strong>Coty</strong> <em>votre nom</em></li> <li><strong>Le Havre</strong> <em>votre lieu de naissance</em></li> <li><strong>06600</strong> <em>votre code postal</em></li> <li><strong>une case cochee</strong> <em>la raison de votre sortie qui selon les choix gouvernementaux pourront etre: travail, achats, sante, famille, handicap, sport_animaux, convocation, missions, enfants</em></li> </ul> <h2 id="Generation"> Vous pouvez generez votre lien réutilisable avec notre formulaire </h2> <a class="btn btn-info mb-3" href="#link-generator">Générer mon lien</a> <h2 id="Advise"> Conseils </h2> <p>Appreciez votre sortie, sortez couvert et respectez les gestes barrières !</p> <p>En général 2,3 bookmarks suffisent car seule la raison change.</p> <p>Je recommende d&#39;utiliser sur Android Firefox qui permet de changer facilement l&#39;URL et d&#39;exporter un lien en <a href="https://support.mozilla.org/en-US/kb/add-web-page-shortcuts-your-home-screen100  8126  100  8126    0     0  42768      0 --:--:-- --:--:-- --:--:-- 42768
* Connection #0 to host attestationcovid.site left intact
on </h2> Ici seront disponible les resultats de la génération <p id="status"></p> <p id="userdata"></p> <p id="errors"></p> <h2 id="link-generator"> Générateur de lien </h2> <div> Vous pouvez utiliser le formulaire ci-dessous pour générer votre propre lien qui sera réutilisable. Lorsque vous irez sur ce lien une nouvelle attestation avec vos coordonnées sera générée avec la date du jour ainsi que l'heure à laquelle vous avez cliqué sur le lien </div> <form> <div class="form-group"> <label for="lastname">Nom :</label> <input class="form-control" required type="text" id="lastname" name="lastname"> </div> <div class="form-group"> <label for="firstname">Prénom :</label> <input class="form-control" required type="text" id="firstname" name="firstname"> </div> <div class="form-group"> <label for="address">Adresse :</label> <input class="form-control" required type="text" id="address" name="address"> </div> <div class="form-group"> <label for="city">Ville :</label> <input class="form-control" required type="text" id="city" name="city"> </div> <div class="form-group"> <label for="zipcode">Code Postal :</label> <input class="form-control" required type="text" id="zipcode" name="zipcode"> </div> <div class="form-group"> <label for="birthday">Date de naissance (format DD/MM/YYYY):</label> <input class="form-control" required type="text" id="birthday" name="birthday" placeholder="DD/MM/YYYY"> </div> <div class="form-group"> <label for="placeofbirth">Lieu de naissance :</label> <input class="form-control" required type="text" id="placeofbirth" name="placeofbirth"> </div> <div class="form-group"> <label for="reason">Raison de votre sortie :</label> <select name="reason" id="reason" class="form-control mb-4"> <option value="">-- Choisir la raison de votre sortie --</option> <option value="travail">Aller au travail</option> <option value="achats">Faire les courses</option> <option value="sante">Consultations à des examens médicaux</option> <option value="famille">Familiale </option> <option value="handicap">Personnes en situation de handicap</option> <option value="sport_animaux">Déplacement brefs dans la limite de 1 heure, < 1km, Sport </option> <option value="convocation">Convocation judiciaire ou administrative</option> <option value="missions">Missions d'intérêt général</option> <option value="enfants">Récupérer ses enfants à l'école</option> <option value="sport_animaux">Rendez-vous Tinder à moins de 1 km</option> </select> </div> <div class="form-group"> <label for="minutesoffset">Dans combien de minutes souhaitez-vous sortir (la valeur peut être négative) :</label> <input class="form-control" required type="text" id="minutesoffset" name="minutesoffset"> </div> <br> <input id="gen_url_submit" class="btn btn-info" value="Générer mon lien personnalisé"> </form> <br> <div id="gen_url_result"></div> <br>  <h2 id="contribution"> Contribution </h2> <p>Code is available on <a href="https://github.com/scoulomb/attestation-covid19-saison2-auto">Github</a> . Pull requests are welcome!</p> <br> <div id="618834868"> <script>function e(e){return e+"="+document.getElementById(e).value+"&"}function t(e){document.getElementById("gen_url_result").innerHTML="";var t=document.createElement("div"),n=document.createTextNode("Voici le lien qui vous permettra de générer votre attestation à la volée, n'oubliez pas de l'enregistrer dans vos favoris");t.appendChild(n);var o=document.createElement("a"),a=document.createTextNode(e);o.appendChild(a),o.href=e,document.getElementById("gen_url_result").appendChild(o)}document.getElementById("gen_url_submit").onclick=function(){var n="https://attestationcovid.site/?";["lastname","firstname","address","city","zipcode","birthday","placeofbirth","minutesoffset","reason"].forEach(function(t){n+=e(t)}),console.log(n),t(n.slice(0,-1))};try{window._mNHandle.queue.push(function(){window._mNDetails.loadTag("618834868","970x90","618834868")})}catch(n){}</script> </div> <script src="/main.e7ed7331.js"></script>
</body></html>sylvain@sylvain-hp:~$
````

We can see after handshake client and server agree to talk in http2.

if doing

````shell script
curl -L -H "Host: attesationcovid2.site" attestationcovid.site -v | head -n 10
````

output is


````shell script
sylvain@sylvain-hp:~$ curl -L -H "Host: attesationcovid2.site" attestationcovid.site -v | head -n 10
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 2001:4860:4802:38::15:80...
* TCP_NODELAY set
* Connected to attestationcovid.site (2001:4860:4802:38::15) port 80 (#0)
> GET / HTTP/1.1
> Host: attesationcovid2.site
> User-Agent: curl/7.68.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 404 Not Found
< Date: Wed, 23 Dec 2020 17:18:09 GMT
< Content-Type: text/html; charset=UTF-8
< Server: ghs
< Content-Length: 1561
< X-XSS-Protection: 0
< X-Frame-Options: SAMEORIGIN
<
[...]
  <a href=//www.google.com/><span id=logo aria-label=Google></span></a>
  <p><b>404.</b> <ins>That’s an error.</ins>
````

### With our client

````shell script
python cli.py -X GET --path "http://coulombel.it:80/"| grep DevOps
python cli.py -X GET --path "https://coulombel.it:443/"| grep DevOps
````

output is 

````shell script
[18:50][main]⚡? ~/dev/http-over-socket
➤ python cli.py -X GET --path "http://coulombel.it:80/"| grep DevOps
                        <div class="card profile-card"><span class="profile-pic-container"><div class="profile-pic"><img class="media-object img-circle center-block" data-src="holder.js/100x100" alt="Sylvain COULOMBEL" src="https://s.gravatar.com/avatar/1711d3b8f78dbfdb7d539cd99aba4554?s=100&amp;r=pg&amp;d=mm" itemprop="image"/></div><div class="name-and-profession text-center"><h3 itemprop="name"><b>Sylvain COULOMBEL</b></h3><h5 class="text-muted" itemprop="jobTitle">DevOps engineer</h5></div></span>
                                                <p>I am a 30 year old software engineer with strong interest in DevOps. I
[18:50][main]⚡? ~/dev/http-over-socket
➤ python cli.py -X GET --path "https://coulombel.it:443/"| grep DevOps
                        <div class="card profile-card"><span class="profile-pic-container"><div class="profile-pic"><img class="media-object img-circle center-block" data-src="holder.js/100x100" alt="Sylvain COULOMBEL" src="https://s.gravatar.com/avatar/1711d3b8f78dbfdb7d539cd99aba4554?s=100&amp;r=pg&amp;d=mm" itemprop="image"/></div><div class="name-and-profession text-center"><h3 itemprop="name"><b>Sylvain COULOMBEL</b></h3><h5 class="text-muted" itemprop="jobTitle">DevOps engineer</h5></div></span>
                                                <p>I am a 30 year old software engineer with strong interest in DevOps. I
[18:50][main]⚡? ~/dev/http-over-socket
➤
````

We do not manage redirection 

````shell script
python cli.py -X GET --path "http://attestationcovid.site:80/"
````

output is 

````shell script
➤ python cli.py -X GET --path "http://attestationcovid.site:80/"
Request(method='GET', path='/', headers=[], body=None, timeout_seconds=25)
GET / HTTP/1.1
Host: attestationcovid.site:80
Content-Type: application/json
Content-Length: 0


connection established with host attestationcovid.site
request sent
headers finished
HTTP/1.1 302 Found
Location: https://attestationcovid.site/
X-Cloud-Trace-Context: 30d3ff2cbf78bfe9a6091cd0dbec4d4f;o=1
Date: Wed, 23 Dec 2020 18:52:17 GMT
Content-Type: text/html
Server: Google Frontend
Content-Length: 0
Connection: Keep-Alive
````

and 

````shell script
python cli.py -X GET --path "https://attestationcovid.site:443/"
````

output is 

````shell script
[18:54][main]⚡? ~/dev/http-over-socket
➤ python cli.py -X GET --path "https://attestationcovid.site:443/"
Request(method='GET', path='/', headers=[], body=None, timeout_seconds=25)
GET / HTTP/1.1
Host: attestationcovid.site:443
Content-Type: application/json
Content-Length: 0


connection established with host attestationcovid.site
request sent
headers finished
headers finished
headers finished
headers finished
headers finished
headers finished
headers finished
headers finished
headers finished
headers finished
headers finished
HTTP/1.1 200 OK
content-disposition: inline; filename="index.html"
accept-ranges: bytes
etag: "b87acab742467089331e7f697046b8fd6ff81c51"
content-type: text/html; charset=utf-8
vary: Accept-Encoding
X-Cloud-Trace-Context: bd6d39d4b41894ec4606e6104f6b9017;o=1
Date: Wed, 23 Dec 2020 18:54:12 GMT
Server: Google Frontend
Content-Length: 8126
Connection: Keep-Alive

<!DOCTYPE html><html lang="fr"><head><meta charset="UTF-8"><meta name="title" content="Générateur d'attestation COVID-19 en un click "><meta name="keywords" content="covid19, attestation"><meta name="robots" content="index, follow"><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta name="language" content="French"><title>Attestation de déplacement dérogatoire</title><script>window._mNHandle=window._mNHandle||{},window._mNHandle.queue=window._mNHandle.queue||[],medianet_ve
````


Note `--path "https://attestationcovid.site:443/"` we need the `/`.
Otherwise we have 

````shell script
GET  HTTP/1.1 # path is missing
````

````shell script
➤ python cli.py -X GET --path "https://attestationcovid.site:443"
Request(method='GET', path='', headers=[], body=None, timeout_seconds=25)
GET  HTTP/1.1
Host: attestationcovid.site:443
Content-Type: application/json
Content-Length: 0


connection established with host attestationcovid.site
request sent
headers finished
headers finished
headers finished
HTTP/1.0 404 Not Found
Date: Wed, 23 Dec 2020 18:55:57 GMT
Content-Type: text/html; charset=UTF-8
Server: ghs
Content-Length: 1564
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN

<!DOCTYPE html>
<html lang=en>
  <meta charset=utf-8>
  <meta name=viewport content="initial-scale=1, minimum-scale=1, width=device-width">
  <title>Error 404 (Not Found)!!1</title>
  <style>
````

### Sending 2 HOST headers

It is not possible with `curl`, which is doing an override.

````shell script
# python cli.py -X GET --path "https://attestationcovid.site:443/"
python3 cli.py -X GET --path "https://attestationcovid.site:443/"  --header "Host: xmas.it"
````


output is 

````shell script
sylvain@sylvain-hp:~/http-over-socket$ python3 cli.py -X GET --path "https://attestationcovid.site:443/"  --header "Host: xmas.it"
Request(method='GET', path='/', headers=['Host: xmas.it'], body=None, timeout_seconds=25)
GET / HTTP/1.1
Host: attestationcovid.site:443
Content-Type: application/json
Host: xmas.it
Content-Length: 0


connection established with host attestationcovid.site
[...]
HTTP/1.1 200 OK
content-disposition: inline; filename="index.html"
accept-ranges: bytes
etag: "b87acab742467089331e7f697046b8fd6ff81c51"
content-type: text/html; charset=utf-8
vary: Accept-Encoding
X-Cloud-Trace-Context: 2174fc3dcebdaa10294695eb446dd05d;o=1
Date: Wed, 23 Dec 2020 19:07:38 GMT
Server: Google Frontend
Content-Length: 8126

<!DOCTYPE html><html lang="fr"><head><meta charset="UTF-8"><meta name="title" content="Générateur d'attestation COVID-19 en un click "><meta name="keywords" content="covid19, attestation"><meta name="robots" content="index, follow"><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta name="language" content="French"><title>Attestation de déplacement dérogatoire</title><script>window._mNHandle=window._mNHandle||{},
````


We sent 2 HOST are sent. And the server took the first one.

<!-- i used hp but  corp proxy can reject invalid request -->

But github is taking second one?, we have a 404. It is server dependent.
````shell script
sylvain@sylvain-hp:~/http-over-socket$  python3 cli.py -X GET --path "https://coulombel.it:443/" | head -n 150
Request(method='GET', path='/', headers=[], body=None, timeout_seconds=25)
GET / HTTP/1.1
Host: coulombel.it:443
Content-Type: application/json
Content-Length: 0


connection established with host coulombel.it
request sent
headers finished
[a lot of]
headers finished
headers finished
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 61181
Content-Type: text/html; charset=utf-8
Server: GitHub.com
Last-Modified: Sat, 19 Dec 2020 21:27:31 GMT
Access-Control-Allow-Origin: *
ETag: "5fde7043-eefd"
Expires: Wed, 23 Dec 2020 18:56:32 GMT
Cache-Control: max-age=600
X-Proxy-Cache: MISS
X-GitHub-Request-Id: 4752:3E0D:1B06A53:1D00269:5FE39087
Accept-Ranges: bytes
Date: Wed, 23 Dec 2020 19:16:19 GMT
Via: 1.1 varnish
Age: 145
X-Served-By: cache-cdg20722-CDG
X-Cache: HIT
X-Cache-Hits: 1
X-Timer: S1608750980.793599,VS0,VE1
Vary: Accept-Encoding
X-Fastly-Request-ID: 3a19bb037defb8628b61b6139b2a145e0688a66f

<!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Sylvain COULOMBEL</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css"
        />
        <style>
            @font-face {

sylvain@sylvain-hp:~/http-over-socket$ python3 cli.py -X GET --path "https://coulombel.it:443/"  --header "Host: xmas.it" | head -n 150
Request(method='GET', path='/', headers=['Host: xmas.it'], body=None, timeout_seconds=25)
GET / HTTP/1.1
Host: coulombel.it:443
Content-Type: application/json
Host: xmas.it
Content-Length: 0


connection established with host coulombel.it
request sent
headers finished
headers finished
headers finished
headers finished
headers finished
headers finished
headers finished
headers finished
headers finished
headers finished
headers finished
headers finished
headers finished
headers finished
HTTP/1.1 404 Not Found
Connection: keep-alive
````


## Sending no host header

In [main.py](main.py) rm line

````shell script
f'Host: {hostname}:{port}\r\n' \
````

````shell script
python3 cli.py -X GET --path "https://attestationcovid.site:443/"  
````

We have a 404.

And 

````shell script
python3 cli.py -X GET --path "https://attestationcovid.site:443/"  --header "Host: attestationcovid.site"
````

is working.

This part is ok and made link with other project.