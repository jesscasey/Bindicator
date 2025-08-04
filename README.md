# Bindicator

A simple command-line application that displays the next bin collection dates
for a given postcode and house name/number. The application takes these
parameters as input from the user, fetches the corresponding local authority's
website, then uses [Selenium](https://www.selenium.dev/) to retrieve the next
bin collection dates.

## Progress

| Functionality                      | Supported councils               |
| ---------------------------------- | ------------------               |
| ![](https://geps.dev/progress/100) | ![](https://geps.dev/progress/4) |

## Limitations

- For licencing reasons, Northern Ireland postcodes are not supported. Only
those in England, Scotland, and Wales are supported at this time.
- Currently, this application only retrieves household waste and recycling
collection dates. For further information, such as what time your bin should
be out by, please check your council's website.

I hope to address these limitations in the future. In the meantime, feel free
to transform this code to work around these limitations or in any other way you
see fit!

## Instructions

1. If you don't already have Selenium installed, you will need to do this. Just
run the following command in your terminal: `pip3 install selenium`
    - If you have an older version of Selenium installed, you might need to
    upgrade it: `pip3 install --upgrade selenium`
2. Install [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/)
and add to your system's PATH.
    - ChromeDriver is Chromium-based so it should work with most web browsers.
    However, for best results, Google Chrome should be installed on your
    system.
    - If you don't have a Chromium-based browser installed (or you'd prefer not
    to use one), install the relevant web driver for your browser, add to your
    system's PATH, and modify the `driver` variable accordingly.
    [Here](https://www.selenium.dev/documentation/webdriver/browsers/) is the
    list of browsers currently supported by Selenium.
3. Run the following command in your terminal: `python main.py`

## Attributions

- Contains OS data © Crown copyright and database right 2025
- Contains Royal Mail data © Royal Mail copyright and database right 2025
- Source: Office for National Statistics licensed under the
[Open Government Licence v.3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- Contains public sector information licensed under the Open Government Licence
v3.0.
- **Progress bar attribution**
    > Copyright (c) 2019 Gepser Hoil
    >
    > Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    >
    >The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    >
    >THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
