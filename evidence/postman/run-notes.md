# Run notes

Date: 2026-04-28  
Environment: demo-3 local  
Base URL: http://localhost:8080  

## What I tested
- GET /
- GET /health
- GET /no-such-route

## Expected result
- / returns 200 and JSON body with status = ok
- /health returns 200 and JSON body with status = ok
- Response Content-Type includes application/json
- /no-such-route returns 404

## Actual result
- GET / : pass
- GET /health : pass
- GET /no-such-route : pass

## Notes
- Used Postman collection export in evidence/postman/
- Used local port forwarding from Ubuntu VM to Windows host
