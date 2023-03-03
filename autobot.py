

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# ブラウザを起動
browser = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://www.instagram.com"

# 指定のURLにアクセスhttps://www.instagram.com/modern_inf_2022/
browser.get("https://www.instagram.com")


from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# ログイン処理
def function_login() :
    # 電話、メールまたはユーザー名のinput要素が読み込まれるまで待機（最大10秒）
    elem_user_id_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.NAME, "username")))
    # パスワードのinput要素
    elem_password_input = browser.find_element_by_name("password")

    if elem_user_id_input and elem_password_input :
        # ログインID入力
        elem_user_id_input.send_keys(LOGIN_ID)
        # パスワード入力
        elem_password_input.send_keys(PASSWORD)
        # ログインボタンクリック
        elem_login_btn = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')))

        # ボタン押下のアクション
        actions = ActionChains(browser)
        actions.move_to_element(elem_login_btn)
        actions.click(elem_login_btn)
        actions.perform()

        # ログイン処理待機（適当）
        time.sleep(5)

        # 遷移後のURLでログイン可否をチェック
        print('instagramにログインしました')
        return True
    else :
        print('ログインに失敗しました')
        False

# 実行処理
LOGIN_ID = 'sekaijyousei2022@gmail.com'
PASSWORD = 'sekaijyo-se-666'
function_login()

# 任意のタグ検索を実施/explore/tags/travelphotography/
def function_search(keyword_tag) :
    browser.get("https://www.instagram.com"+keyword_tag)
    print(keyword_tag + ' でタグ検索しました')
    time.sleep(2)


def function_niceClick() :
    # 最新の投稿を開く
    x=random.randint(0,20)
    print(x)
    elem_first_target = WebDriverWait(browser, 30).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, 'KL4Bh')))[x]
    actions = ActionChains(browser)
    actions.move_to_element(elem_first_target)
    actions.click(elem_first_target)
    actions.perform()
    time.sleep(2)


    # いいねをしてない場合のみ、いいねをクリック
    elem_target_nice_text = browser.find_elements_by_class_name('_8-yf5')
    #for e in elem_target_nice_text:
        #if (e.get_attribute('aria-label') != 'いいね！') :
            #continue
        #else :
            #browser.find_element_by_class_name('fr66n').click()
    #time.sleep(10)

# 実行処理
KEYWORD_TAG = ['/explore/tags/勉強垢/','/explore/tags/豆知識/','/explore/tags/時事問題対策/']

i=0

while i<15:
    for e in KEYWORD_TAG:
        function_search(e)
        function_niceClick()
        browser.find_element_by_class_name('fr66n').click()
        time.sleep(4)
        browser.get("https://www.instagram.com/modern_inf_2022/")

    i+=1

a=i*4
print("いいねを',a,'回実行しました")
