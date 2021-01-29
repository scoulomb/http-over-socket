# README: Implement the client

## Usage 

````shell script
➤ python cli.py -h
usage: cli.py [-h] [-X {GET,POST,PUT,DELETE,PATCH}] [--path PATH] [--header HEADER [HEADER ...]] [--body BODY]

CLI for HTTP over Socket

optional arguments:
  -h, --help            show this help message and exit
  -X {GET,POST,PUT,DELETE,PATCH}
                        HTTP method
  --path PATH           url
  --header HEADER [HEADER ...]
                        url
  --body BODY           body
````


## Run from Python 

````shell script
python cli.py -X GET --path "https://attestationcovid.site:443/" --header "Accept: */*" --header "yoloheader: scoulomb"
````


## Run from Docker


### RAW Docker

````shell script
docker build . -f Dockerfile -t socket-curl
docker run socket-curl -X GET --path "https://attestationcovid.site:443/" --header "Accept: */*" --header "yoloheader: scoulomb"
````

### Compose

Edit compose file and run 

````shell script
docker-compose up --build
````

## Known limitations

- This client managed content-length only but some server returns a Transfer-Encoding with the size of the chunk
See: https://tools.ietf.org/html/rfc7230#section-3.3.2

## Example of simple usage using Kubernetes API

To play with our client, we will use kubernetes API.
For this we start `kubectl proxy`.
See how to perform this here:
- **Kubernetes doc** https://v1-16.docs.kubernetes.io/docs/tasks/access-kubernetes-api/http-proxy-access-api/
- **Basic example** https://github.com/scoulomb/myk8s/blob/6e6de11afe4fd78b761d785ecab80de021b7814e/Master-Kubectl/cheatsheet.md#using-kubectl-proxy

````shell script
sudo kubectl proxy --port=8080
````

<!-- window for `vagrant rsync-auto, proxy, and client -->

**Warning**: start as sudo otherwise authentication error.
````shell script
# List pods
python cli.py -X GET --path http://localhost:8080/api/v1/namespaces/default/pods
# Create pods
python cli.py -X POST --path "http://localhost:8080/api/v1/namespaces/default/pods" --body '{"apiVersion":"v1","kind":"Pod","metadata":{"name":"nginx1"},"spec":{"containers":[{"name":"nginx","image":"nginx:1.7.9","ports":[{"containerPort":80}]}]}}'
# List pods
python cli.py -X GET --path http://localhost:8080/api/v1/namespaces/default/pods
# delete pods 404
python cli.py -X DELETE --path http://localhost:8080/api/v1/namespaces/default/pods/nginx
# delete pods 200
python cli.py -X DELETE --path http://localhost:8080/api/v1/namespaces/default/pods/nginx1
# List pods
python cli.py -X GET --path http://localhost:8080/api/v1/namespaces/default/pods
````

<details>
  <summary>Click to expand output!</summary>
  
````shell script
[21:13][main]⚡? ~/dev/http-over-socket
➤ python cli.py -X GET --path http://localhost:8080/api/v1/namespaces/default/pods
Request(method='GET', path='/api/v1/namespaces/default/pods', headers=[], body=None, timeout_seconds=25)
GET /api/v1/namespaces/default/pods HTTP/1.1
Host: localhost:8080
Content-Type: application/json
Content-Length: 0


connection established with host localhost
request sent
headers finished
HTTP/1.1 200 OK
Cache-Control: no-cache, private
Content-Length: 131
Content-Type: application/json
Date: Mon, 07 Dec 2020 21:13:41 GMT

{"kind":"PodList","apiVersion":"v1","metadata":{"selfLink":"/api/v1/namespaces/default/pods","resourceVersion":"6857"},"items":[]}

[21:13][main]⚡? ~/dev/http-over-socket
➤ python cli.py -X POST --path "http://localhost:8080/api/v1/namespaces/default/pods" --body '{"apiVersion":"v1","kind":"Pod","metadata":{"name":"nginx1"},"spec":{"containers":[{"name":"nginx","image":"nginx:1.7.9","ports":[{"containerPort":80}]}]}}'

Request(method='POST', path='/api/v1/namespaces/default/pods', headers=[], body='{"apiVersion":"v1","kind":"Pod","metadata":{"name":"nginx1"},"spec":{"containers":[{"name":"nginx","image":"nginx:1.7.9","ports":[{"containerPort":80}]}]}}', timeout_seconds=25)
POST /api/v1/namespaces/default/pods HTTP/1.1
Host: localhost:8080
Content-Type: application/json
Content-Length: 155

{"apiVersion":"v1","kind":"Pod","metadata":{"name":"nginx1"},"spec":{"containers":[{"name":"nginx","image":"nginx:1.7.9","ports":[{"containerPort":80}]}]}}
connection established with host localhost
request sent
headers finished
headers finished
HTTP/1.1 201 Created
Cache-Control: no-cache, private
Content-Length: 1876
Content-Type: application/json
Date: Mon, 07 Dec 2020 21:13:49 GMT

{"kind":"Pod","apiVersion":"v1","metadata":{"name":"nginx1","namespace":"default","selfLink":"/api/v1/namespaces/default/pods/nginx1","uid":"627c0ece-dcd6-41f0-ac6e-32e2a75620bd","resourceVersion":"6864","creationTimestamp":"2020-12-07T21:13:49Z","managedFields":[{"manager":"kubectl","operation":"Update","apiVersion":"v1","time":"2020-12-07T21:13:49Z","fieldsType":"FieldsV1","fieldsV1":{"f:spec":{"f:containers":{"k:{\"name\":\"nginx\"}":{".":{},"f:image":{},"f:imagePullPolicy":{},"f:name":{},"f:ports":{".":{},"k:{\"containerPort\":80,\"protocol\":\"TCP\"}":{".":{},"f:containerPort":{},"f:protocol":{}}},"f:resources":{},"f:terminationMessagePath":{},"f:terminationMessagePolicy":{}}},"f:dnsPolicy":{},"f:enableServiceLinks":{},"f:restartPolicy":{},"f:schedulerName":{},"f:securityContext":{},"f:terminationGracePeriodSeconds":{}}}}]},"spec":{"volumes":[{"name":"default-token-bmclp","secret":{"secretName":"default-token-bmclp","defaultMode":420}}],"containers":[{"name":"nginx","image":"nginx:1.7.9","ports":[{"containerPort":80,"protocol":"TCP"}],"resources":{},"volumeMounts":[{"name":"default-token-bmclp","readOnly":true,"mountPath":"/var/run/secrets/kubernetes.io/serviceaccount"}],"terminationMessagePath":"/dev/termination-log","terminationMessagePolicy":"File","imagePullPolicy":"IfNotPresent"}],"restartPolicy":"Always","terminationGracePeriodSeconds":30,"dnsPolicy":"ClusterFirst","serviceAccountName":"default","serviceAccount":"default","securityContext":{},"schedulerName":"default-scheduler","tolerations":[{"key":"node.kubernetes.io/not-ready","operator":"Exists","effect":"NoExecute","tolerationSeconds":300},{"key":"node.kubernetes.io/unreachable","operator":"Exists","effect":"NoExecute","tolerationSeconds":300}],"priority":0,"enableServiceLinks":true,"preemptionPolicy":"PreemptLowerPriority"},"status":{"phase":"Pending","qosClass":"BestEffort"}}

[21:13][main]⚡? ~/dev/http-over-socket
➤ python cli.py -X GET --path http://localhost:8080/api/v1/namespaces/default/pods
Request(method='GET', path='/api/v1/namespaces/default/pods', headers=[], body=None, timeout_seconds=25)
GET /api/v1/namespaces/default/pods HTTP/1.1
Host: localhost:8080
Content-Type: application/json
Content-Length: 0


connection established with host localhost
request sent
headers finished
headers finished
headers finished
headers finished
HTTP/1.1 200 OK
Cache-Control: no-cache, private
Content-Length: 3556
Content-Type: application/json
Date: Mon, 07 Dec 2020 21:13:54 GMT

{"kind":"PodList","apiVersion":"v1","metadata":{"selfLink":"/api/v1/namespaces/default/pods","resourceVersion":"6875"},"items":[{"metadata":{"name":"nginx1","namespace":"default","selfLink":"/api/v1/namespaces/default/pods/nginx1","uid":"627c0ece-dcd6-41f0-ac6e-32e2a75620bd","resourceVersion":"6872","creationTimestamp":"2020-12-07T21:13:49Z","managedFields":[{"manager":"kubectl","operation":"Update","apiVersion":"v1","time":"2020-12-07T21:13:49Z","fieldsType":"FieldsV1","fieldsV1":{"f:spec":{"f:containers":{"k:{\"name\":\"nginx\"}":{".":{},"f:image":{},"f:imagePullPolicy":{},"f:name":{},"f:ports":{".":{},"k:{\"containerPort\":80,\"protocol\":\"TCP\"}":{".":{},"f:containerPort":{},"f:protocol":{}}},"f:resources":{},"f:terminationMessagePath":{},"f:terminationMessagePolicy":{}}},"f:dnsPolicy":{},"f:enableServiceLinks":{},"f:restartPolicy":{},"f:schedulerName":{},"f:securityContext":{},"f:terminationGracePeriodSeconds":{}}}},{"manager":"kubelet","operation":"Update","apiVersion":"v1","time":"2020-12-07T21:13:50Z","fieldsType":"FieldsV1","fieldsV1":{"f:status":{"f:conditions":{"k:{\"type\":\"ContainersReady\"}":{".":{},"f:lastProbeTime":{},"f:lastTransitionTime":{},"f:status":{},"f:type":{}},"k:{\"type\":\"Initialized\"}":{".":{},"f:lastProbeTime":{},"f:lastTransitionTime":{},"f:status":{},"f:type":{}},"k:{\"type\":\"Ready\"}":{".":{},"f:lastProbeTime":{},"f:lastTransitionTime":{},"f:status":{},"f:type":{}}},"f:containerStatuses":{},"f:hostIP":{},"f:phase":{},"f:podIP":{},"f:podIPs":{".":{},"k:{\"ip\":\"172.17.0.3\"}":{".":{},"f:ip":{}}},"f:startTime":{}}}}]},"spec":{"volumes":[{"name":"default-token-bmclp","secret":{"secretName":"default-token-bmclp","defaultMode":420}}],"containers":[{"name":"nginx","image":"nginx:1.7.9","ports":[{"containerPort":80,"protocol":"TCP"}],"resources":{},"volumeMounts":[{"name":"default-token-bmclp","readOnly":true,"mountPath":"/var/run/secrets/kubernetes.io/serviceaccount"}],"terminationMessagePath":"/dev/termination-log","terminationMessagePolicy":"File","imagePullPolicy":"IfNotPresent"}],"restartPolicy":"Always","terminationGracePeriodSeconds":30,"dnsPolicy":"ClusterFirst","serviceAccountName":"default","serviceAccount":"default","nodeName":"archlinux","securityContext":{},"schedulerName":"default-scheduler","tolerations":[{"key":"node.kubernetes.io/not-ready","operator":"Exists","effect":"NoExecute","tolerationSeconds":300},{"key":"node.kubernetes.io/unreachable","operator":"Exists","effect":"NoExecute","tolerationSeconds":300}],"priority":0,"enableServiceLinks":true,"preemptionPolicy":"PreemptLowerPriority"},"status":{"phase":"Running","conditions":[{"type":"Initialized","status":"True","lastProbeTime":null,"lastTransitionTime":"2020-12-07T21:13:49Z"},{"type":"Ready","status":"True","lastProbeTime":null,"lastTransitionTime":"2020-12-07T21:13:50Z"},{"type":"ContainersReady","status":"True","lastProbeTime":null,"lastTransitionTime":"2020-12-07T21:13:50Z"},{"type":"PodScheduled","status":"True","lastProbeTime":null,"lastTransitionTime":"2020-12-07T21:13:49Z"}],"hostIP":"10.0.2.15","podIP":"172.17.0.3","podIPs":[{"ip":"172.17.0.3"}],"startTime":"2020-12-07T21:13:49Z","containerStatuses":[{"name":"nginx","state":{"running":{"startedAt":"2020-12-07T21:13:50Z"}},"lastState":{},"ready":true,"restartCount":0,"image":"nginx:1.7.9","imageID":"docker-pullable://nginx@sha256:e3456c851a152494c3e4ff5fcc26f240206abac0c9d794affb40e0714846c451","containerID":"docker://84f9c938b5112ec8cfc8419659a44171089efc718008ceaf01dbb22baa90910d","started":true}],"qosClass":"BestEffort"}}]}

[21:13][main]⚡? ~/dev/http-over-socket
➤ python cli.py -X DELETE --path http://localhost:8080/api/v1/namespaces/default/pods/nginx
Request(method='DELETE', path='/api/v1/namespaces/default/pods/nginx', headers=[], body=None, timeout_seconds=25)
DELETE /api/v1/namespaces/default/pods/nginx HTTP/1.1
Host: localhost:8080
Content-Type: application/json
Content-Length: 0


connection established with host localhost
request sent
headers finished
HTTP/1.1 404 Not Found
Cache-Control: no-cache, private
Content-Length: 178
Content-Type: application/json
Date: Mon, 07 Dec 2020 21:13:59 GMT

{"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"pods \"nginx\" not found","reason":"NotFound","details":{"name":"nginx","kind":"pods"},"code":404}

[21:13][main]⚡? ~/dev/http-over-socket
➤ python cli.py -X DELETE --path http://localhost:8080/api/v1/namespaces/default/pods/nginx1
Request(method='DELETE', path='/api/v1/namespaces/default/pods/nginx1', headers=[], body=None, timeout_seconds=25)
DELETE /api/v1/namespaces/default/pods/nginx1 HTTP/1.1
Host: localhost:8080
Content-Type: application/json
Content-Length: 0


connection established with host localhost
request sent
headers finished
headers finished
headers finished
headers finished
HTTP/1.1 200 OK
Cache-Control: no-cache, private
Content-Length: 3532
Content-Type: application/json
Date: Mon, 07 Dec 2020 21:14:20 GMT

{"kind":"Pod","apiVersion":"v1","metadata":{"name":"nginx1","namespace":"default","selfLink":"/api/v1/namespaces/default/pods/nginx1","uid":"627c0ece-dcd6-41f0-ac6e-32e2a75620bd","resourceVersion":"6895","creationTimestamp":"2020-12-07T21:13:49Z","deletionTimestamp":"2020-12-07T21:14:50Z","deletionGracePeriodSeconds":30,"managedFields":[{"manager":"kubectl","operation":"Update","apiVersion":"v1","time":"2020-12-07T21:13:49Z","fieldsType":"FieldsV1","fieldsV1":{"f:spec":{"f:containers":{"k:{\"name\":\"nginx\"}":{".":{},"f:image":{},"f:imagePullPolicy":{},"f:name":{},"f:ports":{".":{},"k:{\"containerPort\":80,\"protocol\":\"TCP\"}":{".":{},"f:containerPort":{},"f:protocol":{}}},"f:resources":{},"f:terminationMessagePath":{},"f:terminationMessagePolicy":{}}},"f:dnsPolicy":{},"f:enableServiceLinks":{},"f:restartPolicy":{},"f:schedulerName":{},"f:securityContext":{},"f:terminationGracePeriodSeconds":{}}}},{"manager":"kubelet","operation":"Update","apiVersion":"v1","time":"2020-12-07T21:13:50Z","fieldsType":"FieldsV1","fieldsV1":{"f:status":{"f:conditions":{"k:{\"type\":\"ContainersReady\"}":{".":{},"f:lastProbeTime":{},"f:lastTransitionTime":{},"f:status":{},"f:type":{}},"k:{\"type\":\"Initialized\"}":{".":{},"f:lastProbeTime":{},"f:lastTransitionTime":{},"f:status":{},"f:type":{}},"k:{\"type\":\"Ready\"}":{".":{},"f:lastProbeTime":{},"f:lastTransitionTime":{},"f:status":{},"f:type":{}}},"f:containerStatuses":{},"f:hostIP":{},"f:phase":{},"f:podIP":{},"f:podIPs":{".":{},"k:{\"ip\":\"172.17.0.3\"}":{".":{},"f:ip":{}}},"f:startTime":{}}}}]},"spec":{"volumes":[{"name":"default-token-bmclp","secret":{"secretName":"default-token-bmclp","defaultMode":420}}],"containers":[{"name":"nginx","image":"nginx:1.7.9","ports":[{"containerPort":80,"protocol":"TCP"}],"resources":{},"volumeMounts":[{"name":"default-token-bmclp","readOnly":true,"mountPath":"/var/run/secrets/kubernetes.io/serviceaccount"}],"terminationMessagePath":"/dev/termination-log","terminationMessagePolicy":"File","imagePullPolicy":"IfNotPresent"}],"restartPolicy":"Always","terminationGracePeriodSeconds":30,"dnsPolicy":"ClusterFirst","serviceAccountName":"default","serviceAccount":"default","nodeName":"archlinux","securityContext":{},"schedulerName":"default-scheduler","tolerations":[{"key":"node.kubernetes.io/not-ready","operator":"Exists","effect":"NoExecute","tolerationSeconds":300},{"key":"node.kubernetes.io/unreachable","operator":"Exists","effect":"NoExecute","tolerationSeconds":300}],"priority":0,"enableServiceLinks":true,"preemptionPolicy":"PreemptLowerPriority"},"status":{"phase":"Running","conditions":[{"type":"Initialized","status":"True","lastProbeTime":null,"lastTransitionTime":"2020-12-07T21:13:49Z"},{"type":"Ready","status":"True","lastProbeTime":null,"lastTransitionTime":"2020-12-07T21:13:50Z"},{"type":"ContainersReady","status":"True","lastProbeTime":null,"lastTransitionTime":"2020-12-07T21:13:50Z"},{"type":"PodScheduled","status":"True","lastProbeTime":null,"lastTransitionTime":"2020-12-07T21:13:49Z"}],"hostIP":"10.0.2.15","podIP":"172.17.0.3","podIPs":[{"ip":"172.17.0.3"}],"startTime":"2020-12-07T21:13:49Z","containerStatuses":[{"name":"nginx","state":{"running":{"startedAt":"2020-12-07T21:13:50Z"}},"lastState":{},"ready":true,"restartCount":0,"image":"nginx:1.7.9","imageID":"docker-pullable://nginx@sha256:e3456c851a152494c3e4ff5fcc26f240206abac0c9d794affb40e0714846c451","containerID":"docker://84f9c938b5112ec8cfc8419659a44171089efc718008ceaf01dbb22baa90910d","started":true}],"qosClass":"BestEffort"}}

[21:14][main]⚡? ~/dev/http-over-socket
➤ python cli.py -X GET --path http://localhost:8080/api/v1/namespaces/default/pods
Request(method='GET', path='/api/v1/namespaces/default/pods', headers=[], body=None, timeout_seconds=25)
GET /api/v1/namespaces/default/pods HTTP/1.1
Host: localhost:8080
Content-Type: application/json
Content-Length: 0


connection established with host localhost
request sent
headers finished
HTTP/1.1 200 OK
Cache-Control: no-cache, private
Content-Length: 131
Content-Type: application/json
Date: Mon, 07 Dec 2020 21:14:33 GMT

{"kind":"PodList","apiVersion":"v1","metadata":{"selfLink":"/api/v1/namespaces/default/pods","resourceVersion":"6907"},"items":[]}
````

</details>

<!-- Infoblox had some issue:
python cli.py -X POST --path "https://<DNS VIP>:443/wapi/v2.5/record:a" --header="Authorization: Basic YWRtaW46aW5mb2Jsb3g=" --body='{"name":"test1.test.loc","ipv4addr":"10.10.10.2"}'
-->

## Resources

See:
- https://docs.python.org/3/howto/sockets.html
- https://en.wikipedia.org/wiki/Network_socket
- https://en.wikipedia.org/wiki/Internet_protocol_suite
- https://medium.com/swlh/looking-under-the-hood-http-over-tcp-sockets-952a944c99da

**See [Analysis and comments](README_SUITE.md).**

