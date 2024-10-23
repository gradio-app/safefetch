import pytest

import safehttpx

FAILED_VALIDATION_ERR_MESSAGE = "failed validation"

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "url",
    [
        "https://localhost",
        "http://127.0.0.1/file/a/b/c",
        "http://[::1]",
        "https://192.168.0.1",
        "http://10.0.0.1?q=a",
        "http://192.168.1.250.nip.io",
    ],
)
async def test_local_urls_fail(url):
    with pytest.raises(ValueError, match=FAILED_VALIDATION_ERR_MESSAGE):
        await safehttpx.get(url)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "url",
    [
        "https://google.com",
        "https://8.8.8.8/",
        "http://93.184.215.14.nip.io/",
        "https://huggingface.co/datasets/dylanebert/3dgs/resolve/main/luigi/luigi.ply",
    ],
)
async def test_public_urls_pass(url):
    await safehttpx.get(url)


@pytest.mark.asyncio
async def test_domain_whitelist():
    try:
        await safehttpx.get("http://192.168.1.250.nip.io", domain_whitelist=["192.168.1.250.nip.io"])
    except ValueError as e:
        assert FAILED_VALIDATION_ERR_MESSAGE not in str(e)
    except Exception:
        pass # Other exeptions (e.g. connection timeouts) are fine

    with pytest.raises(ValueError, match=FAILED_VALIDATION_ERR_MESSAGE):
        await safehttpx.get("http://192.168.1.250.nip.io", domain_whitelist=["huggingface.co"])

@pytest.mark.asyncio
async def test_transport_false():
    try:
        await safehttpx.get("http://192.168.1.250.nip.io", _transport=False)
    except ValueError as e:
        assert FAILED_VALIDATION_ERR_MESSAGE not in str(e)
    except Exception:
        pass # Other exeptions (e.g. connection timeouts) are fine