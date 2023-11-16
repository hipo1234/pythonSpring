import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template


app = Flask(__name__,template_folder='./templates')
def get_books():
    url = "https://search.kyobobook.co.kr/search?keyword=%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8&gbCode=TOT&target=total"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books_info = []
    books = soup.find_all('div', class_='detail')

    for book in books:
        title = book.find('div', class_='title').text.strip()
        intro = book.find('div', class_='review')
        intro_text = intro.text.strip() if intro else "No introduction available"

        books_info.append({
            'title': title,
            'intro': intro_text
        })

        if len(books_info) >= 6:
            break

    return books_info



@app.route('/')
def home():
    books_info = get_books()

    # HTML 템플릿 파일과 데이터 연결
    return render_template('index.html', books=books_info)

@app.route('/aa')
def aa():
    # HTML 템플릿 파일과 데이터 연결
    return 'aaaaa'

if __name__ == '__main__':
    app.run(debug=True)

# STS에서 Spring Boot 프로젝트를 생성하고 RestTemplate를 활용해 위의 api에 접근
# import org.springframework.boot.SpringApplication;
# import org.springframework.boot.autoconfigure.SpringBootApplication;
# import org.springframework.web.client.RestTemplate;

# @SpringBootApplication
# public class Application {

# public static void main(String[] args) {
# SpringApplication.run(Application.class , args);
# RestTemplate restTemplate = new RestTemplate();
# String url="http://localhost:5000/books"; // Flask 서버 주소
# String result=restTemplate.getForObject(url, String.class );
# System.out.println(result); // 콘솔에 출력
# }
# }