# web driver
selenium webdriver를 사용하기 위한 라이브러리

    * 의존성:
        - python 3.8.10 이상
        - selenium 4.0.0 이상
    * 브라우저:
        - Chrome
        - Firefox
        - Edge

------------------
### 사용법
```
    # install
        $  pip install git+ssh://git@github.com/bommaru-com/web_driver.git

    # chromedriver 사용 시
        from web_driver import WebDriver, WebDriverError
                :
                :
        browser = WebDriver(
            driver_path="chromedriver "./driver/chromedriver",
                :
        )
                :
        # chrome 접속
        browser.connect()
                :
        # chrome 접속 해제
        browser.disconnect() 또는 browser.quit()

    # selenium grid hub 사용 시
        from web_driver import WebDriver, WebDriverError
                :
                :
        browser = WebDriver(
            session_url="<ip-address or dns>:4444"
        )
                :
        # selenium grid hub 접속
        browser.connect()
                :
        # selenium grid 접속 해제
        browser.disconnect() 또는 browser.quit()

    # selenium web driver 요청
    driver = browser.get_driver()

    # page 요청
    browser.get(url)

    # page source 요청
    html = browser.page_source()

    [참고]
    driver = browser.get_driver()를 통해서 driver를 획득했을 경우 driver는 selenium의 webdriver의 모든 메소드를 사용할 수 있다.

```

------------------
### ARG 정의
```
    # remote_url
        - 형식: string
        - 설명: selenium grid hub의 주소를 표시한다. 예) WebDriver(remote_url='http://localhost:4444')
    # driver_path
        - 형식: string
        - 설명: chromedriver의 경로를 표시한다. 예) WebDriver(driver_path='./chromedriver')
    # version
        - 형식: string
        - 설명: chrome 버전을 입력한다.
    # visible
        - 형식: Boolean
        - 설명: 브라우저를 화면에 보이게 실행할 것인가 선택. 기본값은 False
    # implicitly_wait
        - 형식: int
        - 설명: selenium driver가 명시적으로 기다리는 시간. 단위는 초
    # __explicitly_wait
        - 형식: int
        - 설명: selenium driver가 묵시적으로 기다리는 시간. 단위는 초
    # maximize_window
        - 형식: Boolean
        - 설명: 브라우저 윈도우를 최대 사이즈로 할 것인가 선택. 기본값은 False
```

------------------
### method 정의
```
    # set_config(**kwargs)
      드라이브 설정을 다시 하고자 할 때 사용. arg는 클라스 선언 시 ARG와 동일
    # connect()
      grid hub 또는 chrome에 접속하고자 할 때 사용. 리턴값은 selenium webdriver object
    # disconnect()
      grid hub 또는 chrome으로 부터 접속을 해제할 때 사용.
    # get(url)
      페이지를 요청할 때 사용
    # get_driver()
      selenium webdriver를 요청할 때 사용
    # page_source()
      현재 드라이버가 가지고 있는 페이지의 소스를 리턴. 형식: html
```

------------------
### chromedriver 사용 시 주의점
```
    # chrome의 버전을 확인한 후 chromedriver를 사용해야 한다.
        - chrome 버전 확인 방법
            $ google-chrome --version
    # chromedriver download
        $ wget https://chromedriver.storage.googleapis.com/<chromedriver version>/chromedriver_linux64.zip
        $ unzip chromedriver_linux64.zip
    # Mac os 사용 시
        $ xattr -d com.apple.quarantine chromedriver
```