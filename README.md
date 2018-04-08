# What

A demonstration of why https://twistedmatrix.com/trac/ticket/5406#comment:10 is necessary.

# How

Install Django and the Twisted branch to test.

Run the demo application with

```
python -m twisted web --port=unix:sock --wsgi=demo.wsgi.application
```

Then try

```
curl -v -H "Host:" --http1.0 --unix-socket sock http://example.invalid/
```

To see why there must be a value for `SERVER_NAME`, and

```
curl -v --unix-socket sock http://example.invalid/
```

To see why there must be a value for `SERVER_PORT`.
