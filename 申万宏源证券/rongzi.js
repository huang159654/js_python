const crypto = require('crypto-js')

// t='K0FWJlJJ7hojwG3yOTA/NshaO9jUNRiTzZsxTWdFMAY/ZG/OkUckgKlcCVSiPWYBmA2miiO237Y+tacxOH1++M1MzrCIP/+G4UiTrXXn+jL6X42J+bwQL6jmdW/g8n04vn9Rr6l/kNqP2zIhheok8z+5Pg/xFZCNFkDMSU0gVNnmLvo+QyKgXVx9pnjbCaUh3OOfVWVP8vnQ6ZRN2MwMvckxjFYNasogX+SlAKodoMr8M+WdSvLqU7UfD9OEiM1KuB/tjEiHc2iVFZPnuxjIV+yAlIpJGh2lqO2XezxTlGNN1wAZ2tqFq4j3Rd3n4iRBbp4UQ1P6lUTSgTHXfj1Rz6KkdcBjxQSOKiVcEtVw5g/pox8C76y0bMXPDwoFtiroxjA4utS64hAT0HFl9dRqbUn1Lunn7m3pqwdchpIMoRvb8GfvwIBEEB6ixJHhfVGcB/NwXHZyCCJ/aKXDy69/x1EVmyU0Z+2/fFkc3k8OEUcbueBJInqMw+JVHbJHP2JAWcFmgXu6rP5Zb5uyP5UXkLytd9HzZKNRz7TvF39JAp/GMDi61LriEBPQcWX11GptkQof9QazFZLUOdnWNbNjftvwZ+/AgEQQHqLEkeF9UZwH83BcdnIIIn9opcPLr3/H0/PZ8sSsiF2f8K0I5DyGAhu54EkieozD4lUdskc/YkCq4whZCDzriuf9aCLYf+bR7wEK5dCLiPxQTuQaMexSXcYwOLrUuuIQE9BxZfXUam2RCh/1BrMVktQ52dY1s2N+2/Bn78CARBAeosSR4X1RnAfzcFx2cggif2ilw8uvf8fjfqOLsREmAmfqO0JW2+rBG7ngSSJ6jMPiVR2yRz9iQHC5W0xvZUQWiQX5KjA4NHSOKH04DwJcsIxOjh5G4AFjxjA4utS64hAT0HFl9dRqbXMIejZJADevYMXF2fjqJ9zb8GfvwIBEEB6ixJHhfVGcB/NwXHZyCCJ/aKXDy69/x9Pz2fLErIhdn/CtCOQ8hgIbueBJInqMw+JVHbJHP2JAKF+4OLSzWFwgvGwmirBmQU9FY7FKRvzIel85MWmoRKrGMDi61LriEBPQcWX11GptkQof9QazFZLUOdnWNbNjftvwZ+/AgEQQHqLEkeF9UZwH83BcdnIIIn9opcPLr3/H436ji7ERJgJn6jtCVtvqwRu54EkieozD4lUdskc/YkDSyvxAf76QmgTYxosXWWl+eaakKVgFJOmMLIhTn61ZQ6glnOXNZXWVnpf2y6xjuy/tJmXrffiMAHK+ZeO/TYAaRDbRqMNnpOI7hwJKikOKHnbcJYXYAflgq8pbidrLz3HnJ3u3Ou4ygHGdGBijV7GdYvA+lgl5FgZG6euMWouGOZtawA4CAYDf44aoPN54yiEQOf4+OKsl3eNvkXNynyd6fJnWvoSyRocXj7rFpbpqoJy1LvZTJ5ouwKB2oGXOARd87bxQ9W0MHOeyIwN8gsLutr7z+BQpBYPS2aC8qbHHubfs51K+vgVqyDvxSdFW1/zTlzQkZWiYhmoWJ7e98MDQPl8KC3RbyO9vfUoLY7wnUh7Wc+eTU73f8hiuav0DFA98mda+hLJGhxePusWlumqgnLUu9lMnmi7AoHagZc4BF3ztvFD1bQwc57IjA3yCwu62vvP4FCkFg9LZoLypsce5t+znUr6+BWrIO/FJ0VbX/DLkvyCTMkbZX76WjvSTB9NcbL9yUlmJw+h4L2/2CCmgz+sTN3CIS9EvlwOAUpvNs3yZ1r6EskaHF4+6xaW6aqCctS72UyeaLsCgdqBlzgEXfO28UPVtDBznsiMDfILC7ra+8/gUKQWD0tmgvKmxx7lVEnm9kDLtq8Wo9D8nObgePD1tVXVN3ydcJZ5oqAvFtT/kVLw0H6N+gDqMre/EeIQ='

function Decrypt(t) {
    var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : ""
        , r = void 0 !== n ? 'rewin-swhysc1234' + n : e.aesKey
        , i = crypto.enc.Utf8.parse(r)
        , o =crypto.AES.decrypt(t, i, {
        mode: crypto.mode.ECB,
        padding: crypto.pad.Pkcs7
    });
    return crypto.enc.Utf8.stringify(o).toString()
}
// console.log(Decrypt(t))