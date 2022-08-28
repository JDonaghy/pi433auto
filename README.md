# Client
pushd client
npm run dev -- --host
popd

# Server
```
pushd server
FLASK_APP=srv python -m flask run
popd
```