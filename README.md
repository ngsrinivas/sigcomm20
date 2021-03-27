# sigcomm20
Software and content for sigcomm 2020 web pages.

## Dependencies

You need `jinja2` and `python` (2.7+). The command `jinja2` must work on the terminal.

You can install the jinja2 command line tool by running `pip install jinja2 jinja2-cli`.

## Quick start

(in the sigcomm20 clone folder)

```
python gen.py
cd staging
python -m SimpleHTTPServer &
```

Go to http://localhost:8000/sigcomm/2020/ on the browser.

