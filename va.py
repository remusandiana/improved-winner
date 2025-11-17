from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

import requests
geo_data = requests.get("http://ip-api.com/json/").json()

latitude = geo_data["lat"]
longitude = geo_data["lon"]
timezone_id = geo_data["timezone"]
language_code = geo_data["countryCode"].lower()  # e.g., 'us' -> 'en-US'
with SB(uc=True, test=True,locale=f"{language_code.upper()}") as yt2yweydr:
    yt2yweydr.execute_cdp_cmd(
        "Emulation.setGeolocationOverride",
        {
            "latitude": latitude,
            "longitude": longitude,
            "accuracy": 100
        }
    )
    yt2yweydr.execute_cdp_cmd(
        "Emulation.setTimezoneOverride",
        {"timezoneId": timezone_id}
    )
    #yt2yweydr.set_window_size(resolution.width, resolution.height)
    #"#live-channel-stream-information"
    url = "https://kick.com/brutalles"
    yt2yweydr.uc_open_with_reconnect(url, 4)
    yt2yweydr.sleep(4)
    yt2yweydr.uc_gui_click_captcha()
    yt2yweydr.sleep(1)
    yt2yweydr.uc_gui_handle_captcha()
    yt2yweydr.sleep(4)
    if yt2yweydr.is_element_present('button:contains("Accept")'):
        yt2yweydr.uc_click('button:contains("Accept")', reconnect_time=4)
    if yt2yweydr.is_element_visible('#injected-channel-player'):
        yt2yweydr.uc_open_with_reconnect("https://www.twitch.tv/brutalles", 4)
        yt2yweydr.sleep(4)
        yt2yweydr2 = yt2yweydr.get_new_driver(undetectable=True)
        yt2yweydr2.uc_open_with_reconnect(url, 5)
        yt2yweydr2.uc_gui_click_captcha()
        yt2yweydr2.uc_gui_handle_captcha()
        yt2yweydr.sleep(5)
        if yt2yweydr2.is_element_present('button:contains("Accept")'):
            yt2yweydr2.uc_click('button:contains("Accept")', reconnect_time=4)
        while yt2yweydr2.is_element_visible('#injected-channel-player'):
            yt2yweydr2.sleep(1)
        yt2yweydr.quit_extra_driver()
    yt2yweydr.sleep(1)
    url = "https://www.twitch.tv/streamerhouse"
    yt2yweydr.uc_open_with_reconnect(url, 5)
    yt2yweydr.sleep(14)
    if yt2yweydr.is_element_present("#live-channel-stream-information"):

        if yt2yweydr.is_element_present('button:contains("Accept")'):
            yt2yweydr.uc_click('button:contains("Accept")', reconnect_time=4)
        if True:
            yt2yweydr.uc_open_with_reconnect("https://kick.com/brutalles", 5)
            yt2yweydr2 = yt2yweydr.get_new_driver(undetectable=True)
            yt2yweydr2.uc_open_with_reconnect(url, 5)
            yt2yweydr.sleep(10)
            if yt2yweydr2.is_element_present('button:contains("Accept")'):
                yt2yweydr2.uc_click('button:contains("Accept")', reconnect_time=4)
            while yt2yweydr2.is_element_present("#live-channel-stream-information"):
                yt2yweydr2.sleep(1)
            yt2yweydr.quit_extra_driver()
    yt2yweydr.sleep(1)
