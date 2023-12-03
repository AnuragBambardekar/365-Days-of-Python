import httpx

r = httpx.get("https://httpbin.org/get")
r = httpx.post("https://httpbin.org/post", data={'key':'value'})
r = httpx.put("https://httpbin.org/put", data={'key':'value'})
r = httpx.delete("https://httpbin.org/delete")
r = httpx.head("https://httpbin.org/get")
r = httpx.options("https://httpbin.org/get")

# pass paramters
params = {'key1':'value1', 'key2':'value2'}
r = httpx.get('https://httpbin.org/get', params=params)

# custom headers
headers = {'user-agent':'myapp/0.0.1'}
r = httpx.get('https://httpbin.org/headers', headers=headers)

# send json encoded data
data = {'integer':123, 'boolean':True, 'list':['a','b','c']}
r = httpx.post('https://httpbin.org/post', json=data)

# cookies
r = httpx.post('https://httpbin.org/cookies/set?chocolate=chip')
print(r.cookies['chocolate'])

# Authentication
r = httpx.get('https://example.com', auth=("my_user", "password123"))

# Timeout, default = 5 seconds
httpx.get('https://github.com/', timeout=1)

