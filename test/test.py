import pytest

import safehttpx

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
    with pytest.raises(ValueError, match="failed validation"):
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
