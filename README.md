# safehttpx

A small utility Python created to help developers protect their applications from Server Side Request Forgery (SSRF) attacks. It implements an **asynchronous GET method** called `safehttpx.get()`, which is a wrapper around `httpx.AsyncClient.get` while performing validation on the incoming requests. It also implements mitigation for [DNS rebinding](https://en.wikipedia.org/wiki/DNS_rebinding) attacks.

## Usage

* **Basic Usage**

```py
import safehttpx as sh

await sh.get("https://huggingface.co")
>>> <Response [200 OK]>

await sh.get("https://huggingface.co")
>>> ValueError: Hostname 127.0.0.1 failed validation
```

* d

## More info

This library was created through joint efforts of Gradio (Hugging Face) and Trail Of Bits as a result of the Trail of Bits' audit of Gradio 5

