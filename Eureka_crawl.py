import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service


# Tạo tiêu đề cho ứng dụng
st.title("Ứng dụng Nhập URL Facebook Post và Hiển thị Profile")

# Tạo ô input cho người dùng nhập vào
user_input = st.text_input("Nhập URL bài viết trên Facebook:")

# Kiểm tra nếu người dùng đã nhập dữ liệu
if user_input:
    st.write("Đang tải thông tin từ trang web...")
    
    # Cài đặt Selenium WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # Điều hướng đến trang Facebook bài viết
    driver.get("https://www.facebook.com")
    
    # Task 1.2: Nhập username và password (Thay thế bằng của bạn)
    phone_field = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input')
    phone_field.send_keys('0398569572')
    password_field = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input')
    password_field.send_keys('Dophilong5678')
    password_field.send_keys(Keys.ENTER)

    # Điều hướng đến URL bài viết từ người dùng nhập vào
    link_post = user_input
    driver.get("https://www.facebook.com/Theanh28/posts/pfbid02gmcocnekVGQGHkBRTCkRy5rzi3EazrCtdHdo7wh37UpCNySiJMRZwpo516UY1hmLl?__cft__[0]=AZWi45RVhgUT3eIk_g6iY8Nxqx2Im58rEDQ_qUHjbLi2IgvDpoeITHpe20KA1dLWgLHZMEh2uwAIl7f4bHaIf-i7qCqdvW3ERW6on7nMY1baES3K1bQbO9gmz00qioLiTOhQexNtyNzjzWYwncCo4C-RxY1hMmI2BhdDKFUqSK8nwXSUNqq74GnEWgVmZqYCjIqI7zmUiM-wCO_Pwzp6kWiA1ZiocGyO1cDeSriTxTDNlg&__tn__=%2CO%2CP-R")
    
    # Sử dụng BeautifulSoup để lấy source của trang
    page_source = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Tìm thông tin Profile từ bài viết
    profile = page_source.find('div', class_='xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a').get_text().strip()
    
    # Hiển thị thông tin profile trên giao diện Streamlit
    st.write("Thông tin profile từ bài viết:")
    st.write(profile)


    # Đóng trình duyệt sau khi lấy thông tin
    driver.quit()
else:
    st.write("Vui lòng nhập URL vào ô bên trên.")
