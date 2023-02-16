import dev.api_sample as api_sample


def test_get_forces():
    r = api_sample.get_forces()
    assert r.status_code == 200


def test_get_neighbourhoods():
    r = api_sample.get_neighbourhoods('avon-and-somerset')
    assert r.status_code == 200


def test_negative_get_neighbourhoods():
    r = api_sample.get_neighbourhoods('niggavile')
    assert r.status_code == 404
