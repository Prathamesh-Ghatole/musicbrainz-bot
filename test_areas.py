# A simple test script to add a new area to test.metabrainz.org

from editing import MusicBrainzClient
import config as cfg
import mechanize


mb = MusicBrainzClient(cfg.MB_USERNAME, cfg.MB_PASSWORD, cfg.MB_SITE)

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.set_debug_redirects(False)
browser.set_debug_http(False)

area = {
    "name": "reosarevok megacity YB",
    "type": "3",
    "ISO_3166_1": "YB",
    "ISO_3166_2": None,
    "ISO_3166_3": None,
}

area_mbid = mb.add_area(area, edit_note="boiiiiiii")
print("area MBID: " + area_mbid)
print("Link: https://test.musicbrainz.org/area/" + area_mbid)
