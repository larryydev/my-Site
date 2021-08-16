import requests

r = requests.delete('https://38vaq8.deta.dev/blog/Test ', 
    headers= {
        'Content-Type': 'application/json',
        'X-API-Key': 'h8mWXY88.bBEC8CWmjJmhnRmSdkMuZB-t4W48phcxu'

    }
    )

print(r)